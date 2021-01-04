# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: render.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import parse_pb2 as parse__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='render.proto',
  package='locust.parse',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0crender.proto\x12\x0clocust.parse\x1a\x0bparse.proto\"J\n\x08IndexKey\x12\x10\n\x08\x66ilepath\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04line\x18\x03 \x01(\x05\x12\x10\n\x08revision\x18\x04 \x01(\t\"\x8d\x01\n\x0cNestedChange\x12#\n\x03key\x18\x01 \x01(\x0b\x32\x16.locust.parse.IndexKey\x12*\n\x06\x63hange\x18\x02 \x01(\x0b\x32\x1a.locust.parse.LocustChange\x12,\n\x08\x63hildren\x18\x03 \x03(\x0b\x32\x1a.locust.parse.NestedChangeb\x06proto3'
  ,
  dependencies=[parse__pb2.DESCRIPTOR,])




_INDEXKEY = _descriptor.Descriptor(
  name='IndexKey',
  full_name='locust.parse.IndexKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filepath', full_name='locust.parse.IndexKey.filepath', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='locust.parse.IndexKey.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line', full_name='locust.parse.IndexKey.line', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision', full_name='locust.parse.IndexKey.revision', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=117,
)


_NESTEDCHANGE = _descriptor.Descriptor(
  name='NestedChange',
  full_name='locust.parse.NestedChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='locust.parse.NestedChange.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='change', full_name='locust.parse.NestedChange.change', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='children', full_name='locust.parse.NestedChange.children', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=120,
  serialized_end=261,
)

_NESTEDCHANGE.fields_by_name['key'].message_type = _INDEXKEY
_NESTEDCHANGE.fields_by_name['change'].message_type = parse__pb2._LOCUSTCHANGE
_NESTEDCHANGE.fields_by_name['children'].message_type = _NESTEDCHANGE
DESCRIPTOR.message_types_by_name['IndexKey'] = _INDEXKEY
DESCRIPTOR.message_types_by_name['NestedChange'] = _NESTEDCHANGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IndexKey = _reflection.GeneratedProtocolMessageType('IndexKey', (_message.Message,), {
  'DESCRIPTOR' : _INDEXKEY,
  '__module__' : 'render_pb2'
  # @@protoc_insertion_point(class_scope:locust.parse.IndexKey)
  })
_sym_db.RegisterMessage(IndexKey)

NestedChange = _reflection.GeneratedProtocolMessageType('NestedChange', (_message.Message,), {
  'DESCRIPTOR' : _NESTEDCHANGE,
  '__module__' : 'render_pb2'
  # @@protoc_insertion_point(class_scope:locust.parse.NestedChange)
  })
_sym_db.RegisterMessage(NestedChange)


# @@protoc_insertion_point(module_scope)
