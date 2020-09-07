from __future__ import print_function
import logging

import grpc

import app.darts_match_pb2 as darts_match_pb2
import app.darts_match_pb2_grpc as darts_match_pb2_grpc

from domain.visit import Visit


def run():
    """ What would be ideal is a list of live matches to choose from. Instead, this just sends and empty request for
    a match to watch. It gets the first match in the registry, so use this script with the first match while it is in
    progress. This script could be improved a lot to provide more stats, more choice, etc.

    It does demonstrate streaming gRPC. The server streams to the client which maintains an open connection. The server
    is using up a thread to maintain this connection, so it may not be the most efficient approach. A more traditional
    client-server approach might be more appropriate, perhaps using a polling mechanism. But this is a good demo of
    what is possible in terms of data streaming for real-time data and analytics.
    :return:
    """
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('127.0.0.1:50055') as channel:
        stub = darts_match_pb2_grpc.DartsMatchStub(channel)
        for response in stub.WatchMatch(
                darts_match_pb2.WatchRequest()):
            print("Player: " + response.player.userName)
            print("Visit: " + Visit(response.darts).to_string())


if __name__ == '__main__':
    logging.basicConfig()
    run()