import logging

import grpc

import app.visit_pb2 as visit_pb2
import app.visit_pb2_grpc as visit_pb2_grpc
from datatype.enums import DartMultiplier


def run():
    channel = grpc.insecure_channel('127.0.0.1:50055')
    stub = visit_pb2_grpc.VisitStub(channel)

    my_visit = [visit_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
                visit_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                visit_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(visit_pb2.VisitRequest(index=1, visit=my_visit))
    print("Client received: " + response.message)

    my_visit = [visit_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                visit_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                visit_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20)]
    response = stub.ProcessVisit(visit_pb2.VisitRequest(index=2, visit=my_visit))
    print("Client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
