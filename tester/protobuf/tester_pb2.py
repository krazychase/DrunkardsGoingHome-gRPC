# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/tester.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15protobuf/tester.proto\x12\x06tester\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\")\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x08\x32\x39\n\x06Tester\x12/\n\x08GetHello\x12\x0f.tester.Message\x1a\x10.tester.Response\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protobuf.tester_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGE._serialized_start=33
  _MESSAGE._serialized_end=59
  _RESPONSE._serialized_start=61
  _RESPONSE._serialized_end=102
  _TESTER._serialized_start=104
  _TESTER._serialized_end=161
# @@protoc_insertion_point(module_scope)