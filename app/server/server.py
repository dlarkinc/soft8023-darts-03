import logging
from concurrent import futures

import grpc
import uuid

from app.gameimpl import x01_match
from app.darts_match_pb2 import VisitResponse, RegisterResponse, FinalizeResponse, MatchResponse
from app.darts_match_pb2_grpc import DartsMatchServicer, add_DartsMatchServicer_to_server
from app.server.match_registry import MatchRegistry
from domain import darts_match, visit
from pattern import object_factory


class DartServer(DartsMatchServicer):

    def __init__(self):
        # temp / test values for just 1 match initially
        self.match_type = "X01"
        self.factory = object_factory.ObjectFactory()
        self.factory.register_builder('X01', x01_match.X01MatchBuilder())
        self.registry = MatchRegistry.get_instance()

    def ProcessVisit(self, request, context):
        print("in 'visit' for: " + str(request.matchId))
        my_visit = visit.Visit(request.visit)
        match = self.registry.get_match(request.matchId)
        result, response = match.process_visit(request.playerIndex, my_visit)
        return VisitResponse(result=result, message=response)

    def RegisterPlayer(self, request, context):
        print("in register player")
        match = self.registry.get_match(request.matchId)
        player_index = match.match.register_player(request.userName)
        print(match.match.players)
        return RegisterResponse(playerIndex=player_index)

    def FinalizeMatch(self, request, context):
        print("in finalize")
        self.registry.get_match(request.matchId).finalize_setup()
        return FinalizeResponse()

    def CreateMatch(self, request, context):
        """
        This is stateless, i.e. no dedicated session for the match; must return the unique id of the match and this
        must be sent as a parameter with all requests. Like sessions on a multi-threaded webserver.
        :param request:
        :param context:
        :return: match_id
        """
        print("in create match")
        new_match = self.factory.create(request.matchType)
        match = darts_match.DartsMatch()
        match.register_player(request.userName)
        new_match.set_match(match)
        match_id = self.registry.add_match(new_match)
        return MatchResponse(matchId=match_id.bytes)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_DartsMatchServicer_to_server(DartServer(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
