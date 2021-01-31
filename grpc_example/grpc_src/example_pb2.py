# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='example',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rexample.proto\x12\x07\x65xample\"(\n\x05Param\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\t\n\x01z\x18\x03 \x01(\x05\"\x14\n\x03Res\x12\r\n\x05value\x18\x01 \x01(\x05\x32\xbf\x01\n\x04\x46unc\x12(\n\x06Simple\x12\x0e.example.Param\x1a\x0c.example.Res\"\x00\x12.\n\nStreamResp\x12\x0e.example.Param\x1a\x0c.example.Res\"\x00\x30\x01\x12-\n\tStreamReq\x12\x0e.example.Param\x1a\x0c.example.Res\"\x00(\x01\x12.\n\x08\x42iStream\x12\x0e.example.Param\x1a\x0c.example.Res\"\x00(\x01\x30\x01\x62\x06proto3'
)




_PARAM = _descriptor.Descriptor(
  name='Param',
  full_name='example.Param',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='example.Param.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='example.Param.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='example.Param.z', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=26,
  serialized_end=66,
)


_RES = _descriptor.Descriptor(
  name='Res',
  full_name='example.Res',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='example.Res.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=68,
  serialized_end=88,
)

DESCRIPTOR.message_types_by_name['Param'] = _PARAM
DESCRIPTOR.message_types_by_name['Res'] = _RES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Param = _reflection.GeneratedProtocolMessageType('Param', (_message.Message,), {
  'DESCRIPTOR' : _PARAM,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.Param)
  })
_sym_db.RegisterMessage(Param)

Res = _reflection.GeneratedProtocolMessageType('Res', (_message.Message,), {
  'DESCRIPTOR' : _RES,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.Res)
  })
_sym_db.RegisterMessage(Res)



_FUNC = _descriptor.ServiceDescriptor(
  name='Func',
  full_name='example.Func',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=91,
  serialized_end=282,
  methods=[
  _descriptor.MethodDescriptor(
    name='Simple',
    full_name='example.Func.Simple',
    index=0,
    containing_service=None,
    input_type=_PARAM,
    output_type=_RES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamResp',
    full_name='example.Func.StreamResp',
    index=1,
    containing_service=None,
    input_type=_PARAM,
    output_type=_RES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamReq',
    full_name='example.Func.StreamReq',
    index=2,
    containing_service=None,
    input_type=_PARAM,
    output_type=_RES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='BiStream',
    full_name='example.Func.BiStream',
    index=3,
    containing_service=None,
    input_type=_PARAM,
    output_type=_RES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FUNC)

DESCRIPTOR.services_by_name['Func'] = _FUNC

# @@protoc_insertion_point(module_scope)
