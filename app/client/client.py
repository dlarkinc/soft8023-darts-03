import logging

import grpc

import app.darts_match_pb2 as darts_match_pb2
import app.darts_match_pb2_grpc as darts_match_pb2_grpc
from datatype.enums import DartMultiplier


def run():
    channel = grpc.insecure_channel('127.0.0.1:50055')
    stub = darts_match_pb2_grpc.DartsMatchStub(channel)

    player1 = stub.RegisterPlayer(darts_match_pb2.RegisterRequest(name='Alice')).playerIndex
    player2 = stub.RegisterPlayer(darts_match_pb2.RegisterRequest(name='Jamal')).playerIndex
    # player3 = stub.RegisterPlayer(darts_match_pb2.RegisterRequest(name='Eddie')).playerIndex

    stub.FinalizeMatch(darts_match_pb2.FinalizeRequest())

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player1, visit=my_visit))
    print(response.message)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player2, visit=my_visit))
    print(response.message)

    # my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
    #             darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
    #             darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    # response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player3, visit=my_visit))
    # print(response.message)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player1, visit=my_visit))
    print(response.message)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player2, visit=my_visit))
    print(response.message)

    # my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=10),
    #             darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
    #             darts_match_pb2.Dart(multiplier=DartMultiplier.MISS, segment=0)]
    # response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player3, visit=my_visit))
    # print(response.message)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=19),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player1, visit=my_visit))
    print(response.message)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=1),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player2, visit=my_visit))
    print(response.message)

    # my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
    #             darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
    #             darts_match_pb2.Dart(multiplier=DartMultiplier.MISS, segment=0)]
    # response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player3, visit=my_visit))
    # print(response.message)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=7),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player1, visit=my_visit))
    print(response.message)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player2, visit=my_visit))
    print(response.message)

    # my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=2),
    #             darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
    #             darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=11)]
    # response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player3, visit=my_visit))
    # print(response.message)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=19),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=7),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=19)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player1, visit=my_visit))
    print(response.message)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=3),
                darts_match_pb2.Dart(multiplier=DartMultiplier.MISS, segment=0),
                darts_match_pb2.Dart(multiplier=DartMultiplier.DOUBLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player2, visit=my_visit))
    print(response.message)

    # my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20),
    #             darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=15),
    #             darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=1)]
    # response = stub.ProcessVisit(darts_match_pb2.VisitRequest(index=player3, visit=my_visit))
    # print(response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
