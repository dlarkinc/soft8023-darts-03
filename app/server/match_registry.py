import threading
import uuid


class MatchRegistry:
    """ Simple in-memory implementation for now; thread-safe

    """
    __instance = None

    def __init__(self):
        if MatchRegistry.__instance is not None:
            raise Exception("This is a singleton!")
        else:
            MatchRegistry.__instance = self
        self.lock = threading.Lock()
        self.matches = {}
        self.instance = None

    @staticmethod
    def get_instance():
        if MatchRegistry.__instance is None:
            with threading.Lock():
                if MatchRegistry.__instance is None:  # Double locking mechanism
                    MatchRegistry()
        return MatchRegistry.__instance

    def add_match(self, match):
        self.lock.acquire()
        match_id = uuid.uuid4()  # generate what will almost certainly be a unique id (may need to investigate SafeUUID)
        self.matches[match_id] = match
        self.lock.release()
        return match_id

    def get_match(self, match_id):
        return self.matches[uuid.UUID(bytes=match_id)]
