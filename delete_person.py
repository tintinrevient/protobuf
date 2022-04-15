#! /usr/bin/env python
import addressbook_pb2
import sys


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "ADDRESS_BOOK_FILE")
        sys.exit(-1)

    address_book = addressbook_pb2.AddressBook()

    # Read the existing address book.
    try:
        with open(sys.argv[1], "rb") as f:
            address_book.ParseFromString(f.read())
    except IOError:
        print(sys.argv[1] + ": File not found.  Creating a new file.")

    # Delete the first person from people
    del address_book.people[0]

    # Write the new address book back to disk.
    with open(sys.argv[1], "wb") as f:
        f.write(address_book.SerializeToString())