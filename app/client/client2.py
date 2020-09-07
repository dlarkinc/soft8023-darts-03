import logging

import grpc

import time

import app.darts_match_pb2 as darts_match_pb2
import app.darts_match_pb2_grpc as darts_match_pb2_grpc
from datatype.enums import DartMultiplier


def run():
    channel = grpc.insecure_channel('127.0.0.1:50055')
    stub = darts_match_pb2_grpc.DartsMatchStub(channel)

    # Let's create 2 501 darts matches

    match1 = stub.CreateMatch(darts_match_pb2.MatchRequest(userName='Bobbie', matchType='X01')).matchId
    m1_player1 = 0   # owning player always 0
    m1_player2 = stub.RegisterPlayer(darts_match_pb2.RegisterRequest(matchId=match1, userName='Eddie')).playerIndex
    # player3 = stub.RegisterPlayer(darts_match_pb2.RegisterRequest(matchId=match1, userName='Eddie')).playerIndex
    stub.FinalizeMatch(darts_match_pb2.FinalizeRequest(matchId=match1))

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player1, visit=my_visit))
    print(response.message)

    time.sleep(8)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=2)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player2, visit=my_visit))
    print(response.message)

    time.sleep(6)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=10),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=15),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player1, visit=my_visit))
    print(response.message)

    time.sleep(2)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=2)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player2, visit=my_visit))
    print(response.message)

    time.sleep(9)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=10),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player1, visit=my_visit))
    print(response.message)

    time.sleep(6)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=1),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player2, visit=my_visit))
    print(response.message)

    time.sleep(6)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=2)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player1, visit=my_visit))
    print(response.message)

    time.sleep(7)

    my_visit = [darts_match_pb2.Dart(multiplier=DartMultiplier.SINGLE, segment=5),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20),
                darts_match_pb2.Dart(multiplier=DartMultiplier.TREBLE, segment=20)]
    response = stub.ProcessVisit(darts_match_pb2.VisitRequest(matchId=match1, playerIndex=m1_player2, visit=my_visit))
    print(response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
