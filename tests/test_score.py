import unittest
from src.score import Score

class Test_Score(unittest.TestCase):

    def test_SetUpScore(self):

        s = Score()
        self.assertEqual(s.__str__(),'1974-07-07 12:00:00 T (20) | P1 (A1) : P2 (A2) | 0 (0) : 0 (0)')
        s.setArmy1('a1').setArmy2('a2').setPlayer1('p1').setPlayer2('p2')
        s.setDatetime('2009-10-08 11:00').setTournament('t').setTournamentRank('30')
        s.setVictoryPoints1(4).setVictoryPoints2(2).setTournamentPoints1(3).setTournamentPoints2(1)
        self.assertEqual(s.__str__(),'2009-10-08 11:00:00 t (30) | p1 (a1) : p2 (a2) | 3 (4) : 1 (2)')
