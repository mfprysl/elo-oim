import unittest
import src.score as score

class Test_Score(unittest.TestCase):

    def test_ScoreFactory(self):

        f = score.ScoreFactory()

        sampleData = { "Datetime": "2009-10-08 11:00",
            "Tournament": "Balatonfűzfő 2004",
            "TournamentRank": 30,
            "Player1": "Dżordż Łazienkowski",
            "Army1": "A1",
            "VictoryPoints1": 6,
            "TournamentPoints1": 0,
            "Player2": "Zygmund Snæfellsjökull",
            "Army2": "A2",
            "VictoryPoints2": 7,
            "TournamentPoints2": 3
        }

        s = f.getScore(sampleData)
        self.assertEqual(s.__str__(),'2009-10-08 11:00:00 Balatonfűzfő 2004 (30) | Dżordż Łazienkowski (A1) : Zygmund Snæfellsjökull (A2) | 0 (6) : 3 (7), standard scoring')

        sampleData["ScoringType"]="7LEVELS_BIG"
        s = f.getScore(sampleData)
        self.assertEqual(s.__str__(),'2009-10-08 11:00:00 Balatonfűzfő 2004 (30) | Dżordż Łazienkowski (A1) : Zygmund Snæfellsjökull (A2) | 0 (6) : 3 (7), scoring 7LEVELS_BIG')

        sampleData["ScoringType"]="7LEVELS_SMALL"
        s = f.getScore(sampleData)
        self.assertEqual(s.__str__(),'2009-10-08 11:00:00 Balatonfűzfő 2004 (30) | Dżordż Łazienkowski (A1) : Zygmund Snæfellsjökull (A2) | 0 (6) : 3 (7), scoring 7LEVELS_SMALL')

        sampleData["ScoringType"]="5LEVELS_SMALL"
        s = f.getScore(sampleData)
        self.assertEqual(s.__str__(),'2009-10-08 11:00:00 Balatonfűzfő 2004 (30) | Dżordż Łazienkowski (A1) : Zygmund Snæfellsjökull (A2) | 0 (6) : 3 (7), scoring 5LEVELS_SMALL')

    def test_SetUpScore(self):

        s = score.Score()
        self.assertEqual(s.__str__(),
                         '1974-07-07 12:00:00 T (20) | P1 : P2 | 0 (0) : 0 (0), standard scoring')
        s.setArmy1('a1').setArmy2('a2').setPlayer1('p1').setPlayer2('p2')
        s.setDatetime('2009-10-08 11:00').setTournament('t').setTournamentRank('30')
        s.setVictoryPoints1(4).setVictoryPoints2(2).setTournamentPoints1(3).setTournamentPoints2(1)
        self.assertEqual(s.__str__(),
            '2009-10-08 11:00:00 t (30) | p1 (a1) : p2 (a2) | 3 (4) : 1 (2), standard scoring')

    def test_SetUpScore7LevelsBig(self):

        s = score.Score7LevelsBig()
        self.assertEqual(s.__str__(),
            '1974-07-07 12:00:00 T (20) | P1 : P2 | 0 (0) : 0 (0), scoring 7LEVELS_BIG')

    def test_SetUpScore7LevelsSmall(self):

        s = score.Score7LevelsSmall()
        self.assertEqual(s.__str__(),
            '1974-07-07 12:00:00 T (20) | P1 : P2 | 0 (0) : 0 (0), scoring 7LEVELS_SMALL')

    def test_SetUpScore5LevelsSmall(self):

        s = score.Score5LevelsSmall()
        self.assertEqual(s.__str__(),
            '1974-07-07 12:00:00 T (20) | P1 : P2 | 0 (0) : 0 (0), scoring 5LEVELS_SMALL')
