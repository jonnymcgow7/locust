# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: parse.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import git_pb2 as git__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='parse.proto',
  package='locust.parse',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bparse.proto\x12\x0clocust.parse\x1a\tgit.proto\".\n\x10\x44\x65\x66initionParent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04line\x18\x02 \x01(\x05\"\xa6\x01\n\rRawDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x63hange_type\x18\x02 \x01(\t\x12\x0c\n\x04line\x18\x03 \x01(\x05\x12\x0e\n\x06offset\x18\x04 \x01(\x05\x12\x10\n\x08\x65nd_line\x18\x05 \x01(\x05\x12\x12\n\nend_offset\x18\x06 \x01(\x05\x12.\n\x06parent\x18\x07 \x01(\x0b\x32\x1e.locust.parse.DefinitionParent\"\xbf\x01\n\x0cLocustChange\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x63hange_type\x18\x02 \x01(\t\x12\x10\n\x08\x66ilepath\x18\x03 \x01(\t\x12\x10\n\x08revision\x18\x04 \x01(\t\x12\x0c\n\x04line\x18\x05 \x01(\x05\x12\x15\n\rchanged_lines\x18\x06 \x01(\x05\x12\x13\n\x0btotal_lines\x18\x07 \x01(\x05\x12.\n\x06parent\x18\x08 \x01(\x0b\x32\x1e.locust.parse.DefinitionParent\"\x9b\x01\n\x0bParseResult\x12\x0c\n\x04repo\x18\x01 \x01(\t\x12\x13\n\x0binitial_ref\x18\x02 \x01(\t\x12\x14\n\x0cterminal_ref\x18\x03 \x01(\t\x12&\n\x07patches\x18\x04 \x03(\x0b\x32\x15.locust.git.PatchInfo\x12+\n\x07\x63hanges\x18\x05 \x03(\x0b\x32\x1a.locust.parse.LocustChangeb\x06proto3'
  ,
  dependencies=[git__pb2.DESCRIPTOR,])




_DEFINITIONPARENT = _descriptor.Descriptor(
  name='DefinitionParent',
  full_name='locust.parse.DefinitionParent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='locust.parse.DefinitionParent.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line', full_name='locust.parse.DefinitionParent.line', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=40,
  serialized_end=86,
)


_RAWDEFINITION = _descriptor.Descriptor(
  name='RawDefinition',
  full_name='locust.parse.RawDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='locust.parse.RawDefinition.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='change_type', full_name='locust.parse.RawDefinition.change_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line', full_name='locust.parse.RawDefinition.line', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='locust.parse.RawDefinition.offset', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_line', full_name='locust.parse.RawDefinition.end_line', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_offset', full_name='locust.parse.RawDefinition.end_offset', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent', full_name='locust.parse.RawDefinition.parent', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=89,
  serialized_end=255,
)


_LOCUSTCHANGE = _descriptor.Descriptor(
  name='LocustChange',
  full_name='locust.parse.LocustChange',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='locust.parse.LocustChange.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='change_type', full_name='locust.parse.LocustChange.change_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filepath', full_name='locust.parse.LocustChange.filepath', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='revision', full_name='locust.parse.LocustChange.revision', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line', full_name='locust.parse.LocustChange.line', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='changed_lines', full_name='locust.parse.LocustChange.changed_lines', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='total_lines', full_name='locust.parse.LocustChange.total_lines', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parent', full_name='locust.parse.LocustChange.parent', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=258,
  serialized_end=449,
)


_PARSERESULT = _descriptor.Descriptor(
  name='ParseResult',
  full_name='locust.parse.ParseResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='repo', full_name='locust.parse.ParseResult.repo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='initial_ref', full_name='locust.parse.ParseResult.initial_ref', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='terminal_ref', full_name='locust.parse.ParseResult.terminal_ref', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='patches', full_name='locust.parse.ParseResult.patches', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='changes', full_name='locust.parse.ParseResult.changes', index=4,
      number=5, type=11, cpp_type=10, label=3,
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
  serialized_start=452,
  serialized_end=607,
)

_RAWDEFINITION.fields_by_name['parent'].message_type = _DEFINITIONPARENT
_LOCUSTCHANGE.fields_by_name['parent'].message_type = _DEFINITIONPARENT
_PARSERESULT.fields_by_name['patches'].message_type = git__pb2._PATCHINFO
_PARSERESULT.fields_by_name['changes'].message_type = _LOCUSTCHANGE
DESCRIPTOR.message_types_by_name['DefinitionParent'] = _DEFINITIONPARENT
DESCRIPTOR.message_types_by_name['RawDefinition'] = _RAWDEFINITION
DESCRIPTOR.message_types_by_name['LocustChange'] = _LOCUSTCHANGE
DESCRIPTOR.message_types_by_name['ParseResult'] = _PARSERESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DefinitionParent = _reflection.GeneratedProtocolMessageType('DefinitionParent', (_message.Message,), {
  'DESCRIPTOR' : _DEFINITIONPARENT,
  '__module__' : 'parse_pb2'
  # @@protoc_insertion_point(class_scope:locust.parse.DefinitionParent)
  })
_sym_db.RegisterMessage(DefinitionParent)

RawDefinition = _reflection.GeneratedProtocolMessageType('RawDefinition', (_message.Message,), {
  'DESCRIPTOR' : _RAWDEFINITION,
  '__module__' : 'parse_pb2'
  # @@protoc_insertion_point(class_scope:locust.parse.RawDefinition)
  })
_sym_db.RegisterMessage(RawDefinition)

LocustChange = _reflection.GeneratedProtocolMessageType('LocustChange', (_message.Message,), {
  'DESCRIPTOR' : _LOCUSTCHANGE,
  '__module__' : 'parse_pb2'
  # @@protoc_insertion_point(class_scope:locust.parse.LocustChange)
  })
_sym_db.RegisterMessage(LocustChange)

ParseResult = _reflection.GeneratedProtocolMessageType('ParseResult', (_message.Message,), {
  'DESCRIPTOR' : _PARSERESULT,
  '__module__' : 'parse_pb2'
  # @@protoc_insertion_point(class_scope:locust.parse.ParseResult)
  })
_sym_db.RegisterMessage(ParseResult)


# @@protoc_insertion_point(module_scope)
