import logging
from concurrent import futures

import grpc

from app.gameimpl import x01_match
from app.visit_pb2 import VisitResponse
from app.visit_pb2_grpc import VisitServicer, add_VisitServicer_to_server
from datatype.enums import DartMultiplier
from domain import darts_match, visit
from pattern import object_factory


class DartServer(VisitServicer):

    def __init__(self):
        print("here")
        # temp / test values for just 1 match initially
        self.match_type = "X01"
        factory = object_factory.ObjectFactory()
        factory.register_builder('X01', x01_match.X01MatchBuilder())

        x01 = factory.create('X01')
        match = darts_match.DartsMatch()

        match.register_player('Alice')  # player_index = 1
        match.register_player('Kalifa')  # player_index = 2
        x01.set_match(match)

        self.match = x01

    def ProcessVisit(self, request, context):
        print("here")
        my_visit = visit.Visit(request.visit)
        result, response = self.match.process_visit(request.index, my_visit)
        return VisitResponse(result=result, message=response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_VisitServicer_to_server(DartServer(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
