from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Comparison(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    equalTo: _ClassVar[Comparison]
    notEqualTo: _ClassVar[Comparison]
    lessThan: _ClassVar[Comparison]
    lessThanOrEqualTo: _ClassVar[Comparison]
    greaterThan: _ClassVar[Comparison]
    greaterThanOrEqualTo: _ClassVar[Comparison]
equalTo: Comparison
notEqualTo: Comparison
lessThan: Comparison
lessThanOrEqualTo: Comparison
greaterThan: Comparison
greaterThanOrEqualTo: Comparison

class FibonacciRequest(_message.Message):
    __slots__ = ["number"]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: int
    def __init__(self, number: _Optional[int] = ...) -> None: ...

class FibonacciResponse(_message.Message):
    __slots__ = ["number"]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: int
    def __init__(self, number: _Optional[int] = ...) -> None: ...

class FactorialRequest(_message.Message):
    __slots__ = ["number"]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: int
    def __init__(self, number: _Optional[int] = ...) -> None: ...

class FactorialResponse(_message.Message):
    __slots__ = ["number"]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: int
    def __init__(self, number: _Optional[int] = ...) -> None: ...

class Counter(_message.Message):
    __slots__ = ["initialValue", "comparison", "increment", "value"]
    INITIALVALUE_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_FIELD_NUMBER: _ClassVar[int]
    INCREMENT_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    initialValue: int
    comparison: Comparison
    increment: int
    value: int
    def __init__(self, initialValue: _Optional[int] = ..., comparison: _Optional[_Union[Comparison, str]] = ..., increment: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...

class CounterResult(_message.Message):
    __slots__ = ["number"]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    number: int
    def __init__(self, number: _Optional[int] = ...) -> None: ...
