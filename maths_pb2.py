# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: maths.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bmaths.proto\"\"\n\x10\x46ibonacciRequest\x12\x0e\n\x06number\x18\x01 \x01(\x04\"#\n\x11\x46ibonacciResponse\x12\x0e\n\x06number\x18\x01 \x01(\x04\"\"\n\x10\x46\x61\x63torialRequest\x12\x0e\n\x06number\x18\x01 \x01(\x04\"#\n\x11\x46\x61\x63torialResponse\x12\x0e\n\x06number\x18\x01 \x01(\x04\"b\n\x07\x43ounter\x12\x14\n\x0cinitialValue\x18\x01 \x01(\x12\x12\x1f\n\ncomparison\x18\x02 \x01(\x0e\x32\x0b.Comparison\x12\x11\n\tincrement\x18\x05 \x01(\x12\x12\r\n\x05value\x18\x06 \x01(\x12\"\x1f\n\rCounterResult\x12\x0e\n\x06number\x18\x01 \x01(\x12*y\n\nComparison\x12\x0b\n\x07\x65qualTo\x10\x00\x12\x0e\n\nnotEqualTo\x10\x01\x12\x0c\n\x08lessThan\x10\x02\x12\x15\n\x11lessThanOrEqualTo\x10\x03\x12\x0f\n\x0bgreaterThan\x10\x04\x12\x18\n\x14greaterThanOrEqualTo\x10\x05\x32\x9a\x01\n\x05Maths\x12\x34\n\tFibonacci\x12\x11.FibonacciRequest\x1a\x12.FibonacciResponse\"\x00\x12\x34\n\tFactorial\x12\x11.FactorialRequest\x1a\x12.FactorialResponse\"\x00\x12%\n\x05\x43ount\x12\x08.Counter\x1a\x0e.CounterResult\"\x00\x30\x01\x42.Z,github.com/spandigital/lab-grpc-server/mathsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'maths_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z,github.com/spandigital/lab-grpc-server/maths'
  _globals['_COMPARISON']._serialized_start=294
  _globals['_COMPARISON']._serialized_end=415
  _globals['_FIBONACCIREQUEST']._serialized_start=15
  _globals['_FIBONACCIREQUEST']._serialized_end=49
  _globals['_FIBONACCIRESPONSE']._serialized_start=51
  _globals['_FIBONACCIRESPONSE']._serialized_end=86
  _globals['_FACTORIALREQUEST']._serialized_start=88
  _globals['_FACTORIALREQUEST']._serialized_end=122
  _globals['_FACTORIALRESPONSE']._serialized_start=124
  _globals['_FACTORIALRESPONSE']._serialized_end=159
  _globals['_COUNTER']._serialized_start=161
  _globals['_COUNTER']._serialized_end=259
  _globals['_COUNTERRESULT']._serialized_start=261
  _globals['_COUNTERRESULT']._serialized_end=292
  _globals['_MATHS']._serialized_start=418
  _globals['_MATHS']._serialized_end=572
# @@protoc_insertion_point(module_scope)
