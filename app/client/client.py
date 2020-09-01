import logging

import grpc

import app.darts_match_pb2 as darts_match_pb2
import app.darts_match_pb2_grpc as darts_match_pb2_grpc
from datatype.enums import DartMultiplier


def run():
    channel = grpc.insecure_channel('127.0.0.1:50055')
    stub = darts_match_pb2_grpc.DartsMatchStub(channel)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=0, visit=my_visit))
    print("Client received: " + response.message)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=1, visit=my_visit))
    print("Client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
