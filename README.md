# Protobuf

Importantly, the protocol buffer format supports the idea of extending the format over time in such a way that the code can still read data encoded with the old format.

## Installation

1. Install a pre-built binary protocol **compiler** `protoc` [link](https://github.com/protocolbuffers/protobuf/blob/main/README.md#protocol-compiler-installation) to compile `addressbook.proto` to `python`.

2. Install the protobuf python **runtime** [link](https://github.com/protocolbuffers/protobuf/tree/main/examples#python).
```bash
$ pip install protobuf
```

## Example

1. Compile `addressbook.proto` to `python`, which will generate `addressbook_pb2.py`:
```bash
$  protoc addressbook.proto --python_out=/Users/zhaoshu/Documents/workspace/protobuf
```

2. Add a person:
```bash
$ python add_person.py registry.db
```

3. List all the people:
```bash
$ python list_people.py registry.db

Person ID: 1
  Name: shu
  E-mail address: shu@google.com
  Mobile phone #: 123
  Home phone #: 456
```

4. Delete the first person:
```bash
$ python delete_person.py registry.db 
```

## References

* https://docs.feast.dev/getting-started/architecture-and-components/registry
* https://github.com/feast-dev/feast/tree/master/protos/feast/core
* https://developers.google.com/protocol-buffers/docs/pythontutorial
* https://github.com/protocolbuffers/protobuf/tree/main/examples
* https://github.com/protocolbuffers/protobuf/releases  
* https://databricks.com/blog/2019/09/24/diving-into-delta-lake-schema-enforcement-evolution.html
* https://github.com/confluentinc/schema-registry
