import unittest
from src.score import Score
import src.calculate_ranks

class Test_CalculateRanks(unittest.TestCase):

    def test_SortScores(self):

        scores = []
        s1 = Score()
        s1.setArmy1('a1').setArmy2('a2').setPlayer1('p1').setPlayer2('p2')
        s1.setDatetime('2009-10-08 11:00').setTournament('t')
        s1.setVictoryPoints1(4).setVictoryPoints2(2).setTournamentPoints1(3).setTournamentPoints2(1)
        scores.append(s1)

        s2 = Score()
        s2.setArmy1('b1').setArmy2('b2').setPlayer1('pl1').setPlayer2('pl2')
        s2.setDatetime('1974-07-07 12:00').setTournament('tt')
        s2.setVictoryPoints1(4).setVictoryPoints2(2).setTournamentPoints1(3).setTournamentPoints2(1)
        scores.append(s2)

        src.calculate_ranks.sort_scores(scores)

        self.assertEqual(scores[0].Army1,'b1')
        self.assertEqual(scores[1].Army1,'a1')
        
