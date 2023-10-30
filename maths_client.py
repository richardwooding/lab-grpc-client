"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc

import maths_pb2
import maths_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to fibonacci ...")
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = maths_pb2_grpc.MathsStub(channel)
        response = stub.Fibonacci(maths_pb2.FibonacciRequest(number=20))
        print("Maths client fibonacci received: ", response.number)
        stub = maths_pb2_grpc.MathsStub(channel)
        response = stub.Factorial(maths_pb2.FactorialRequest(number=20))
        print("Maths client factorial received: ", response.number)
        for response in stub.Count(maths_pb2.Counter(initialValue=0, comparison=maths_pb2.lessThan, increment=1, value=10)):
            print("Response: ", response.number)


if __name__ == "__main__":
    logging.basicConfig()
    run()
