import pattern.object_factory as object_factory
import app.gameimpl.x01_match as x01_match
import domain.darts_match as darts_match
from datatype.enums import DartMultiplier
from domain import visit

factory = object_factory.ObjectFactory()
factory.register_builder('X01', x01_match.X01MatchBuilder())

x01 = factory.create('X01')
match = darts_match.DartsMatch()

player1_index = match.register_player('Alice')
player2_index = match.register_player('Kalifa')
x01.set_match(match)

my_visit = visit.Visit([(DartMultiplier.SINGLE, 20), (DartMultiplier.TREBLE, 20), (DartMultiplier.SINGLE, 5)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.SINGLE, 1), (DartMultiplier.SINGLE, 5), (DartMultiplier.SINGLE, 20)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.TREBLE, 20), (DartMultiplier.TREBLE, 20), (DartMultiplier.TREBLE, 20)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.TREBLE, 5), (DartMultiplier.SINGLE, 20), (DartMultiplier.SINGLE, 20)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.SINGLE, 20), (DartMultiplier.TREBLE, 20), (DartMultiplier.SINGLE, 20)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.SINGLE, 20), (DartMultiplier.TREBLE, 20), (DartMultiplier.SINGLE, 20)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.SINGLE, 20), (DartMultiplier.SINGLE, 20), (DartMultiplier.TREBLE, 20)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.SINGLE, 20), (DartMultiplier.SINGLE, 20), (DartMultiplier.SINGLE, 1)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.SINGLE, 0), (DartMultiplier.DOUBLE, 18), (DartMultiplier.SINGLE, 0)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

# This should trigger an error message and the visit ignored
my_visit = visit.Visit([(DartMultiplier.SINGLE, 10), (DartMultiplier.DOUBLE, 18), (DartMultiplier.SINGLE, 20)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)
