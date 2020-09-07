from datatype.enums import DartMultiplier

from datetime import datetime

class Dart:
    def __init__(self, multiplier, segment):
        self.multiplier = multiplier    # see datatype.enums.DartType; optionally create this as a property and validate
        self.segment = segment   # 1 to 20 or 25, 0 for miss / double-bull / single-bull

    def get_score(self):
        return self.multiplier * self.segment
    
    def to_string(self):
        segment = None
        if self.segment is 25:
            segment = "BULL"
        if self.segment is 0:
            return "MISS"
        return DartMultiplier(self.multiplier).name + "-" + str(self.segment) if segment is None else segment


class Visit:
    def __init__(self):
        self.darts = []   # Limited to 3 Dart elements for most games
        self.timestamp = datetime.now()

    def __init__(self, darts):
        self.darts = []  # Limited to 3 Dart elements for most games
        self.add_darts(darts)
        self.timestamp = datetime.now()

    def add_dart(self, dart):
        self.darts.append(Dart(dart.multiplier, dart.segment))

    def add_darts(self, darts):
        for dart in darts:
            self.add_dart(dart)

    def remove_trailing_darts(self, index):
        del self.darts[index:]

    # For many dart games, the total score from 3 darts will be relevant, though there is an argument for placing this
    # in each specific type of dart game where it is most relevant
    def get_total(self):
        total = 0
        for dart in self.darts:
            total += dart.get_score()
        return total

    def to_string(self):
        output = ""
        for dart in self.darts:
            output += dart.to_string() + " "
        return output