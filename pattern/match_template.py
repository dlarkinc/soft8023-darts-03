import pattern.object_factory as object_factory


class MatchFactory(object_factory.ObjectFactory):
    def get(self, match_type, **kwargs):
        return self.create(match_type, **kwargs)


