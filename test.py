from dao import darts_match_dao
from domain import darts_match
from service import match_service

dao = darts_match_dao.DartsMatchDao()

match = darts_match.DartsMatch('Dupe', 'Dup1')

dao.add(match)

