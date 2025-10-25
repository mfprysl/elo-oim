import unittest
from src.score import Score
import src.score as score
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

    def test_AdjustRankByScore(self):

        r = {'Krashan Bhamaradżanga': 975}

        s = Score()
        s.setArmy1('Kozacy').setArmy2('Tatarzy').setPlayer1('Krashan Bhamaradżanga').setPlayer2('Hans Gonschorek')
        s.setDatetime('2025-07-07 13:00').setTournament('Pola Chabrów 2025').setTournamentRank(30)
        s.setVictoryPoints1(7).setVictoryPoints2(8).setTournamentPoints1(0).setTournamentPoints2(3)

        src.calculate_ranks.adjust_rank_by_score(s,r)

        self.assertEqual(round(r['Krashan Bhamaradżanga'],2),960.15)
        self.assertEqual(round(r['Hans Gonschorek'],2),1014.85)

    def test_7levels(self):

        r = {}
        scores = []
        s1 = Score()
        s1.setArmy1('a1').setArmy2('a2').setPlayer1('p1').setPlayer2('p2')
        s1.setDatetime('2009-10-08 11:00').setTournament('t')
        s1.setVictoryPoints1(6).setVictoryPoints2(3).setTournamentPoints1(4).setTournamentPoints2(2)
        s1.setScoreType(score.SCORE_7LEVELS)
        scores.append(s1)
        src.calculate_ranks.calculate_ranks(scores, r)
        self.assertEqual(round(r['p1'],2),1007.80)
        self.assertEqual(round(r['p2'],2),992.20)


