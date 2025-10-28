import unittest
import src.score as score
import src.master_data as mdm

class Test_Score(unittest.TestCase):

    def test_ScoreFactory(self):

        f = score.ScoreFactory()

        sampleData = { "Datetime": "2009-10-08 11:00",
            "Tournament": "Balatonfűzfő 2004",
            "TournamentRank": 30,
            "Player1": "Dżordż Łazienkowski",
            "Army1": "A1",
            "VictoryPoints1": 6,
            "TournamentPoints1": "you're a failure",
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

        with self.assertRaises(ValueError):
            s = f.getScore({'': ''})

    def test_SetUpScore(self):

        s = score.Score()
        self.assertEqual(s.__str__(),
                         '1974-07-07 12:00:00 T (20) | P1 : P2 | 0 (0) : 0 (0), standard scoring')
        s.setArmy1('a1').setArmy2('a2').setPlayer1('p1').setPlayer2('p2')
        s.setDatetime('2009-10-08 11:00').setTournament('t').setTournamentRank('30')
        s.setVictoryPoints1(4).setVictoryPoints2(2).setTournamentPoints1(3).setTournamentPoints2(1)
        self.assertEqual(s.__str__(),
            '2009-10-08 11:00:00 t (30) | p1 (a1) : p2 (a2) | 3 (4) : 1 (2), standard scoring')
        self.assertEqual(s.Player1NaturalKey,'p1')
        self.assertEqual(s.Player2NaturalKey,'p2')
        
    def test_ScoreHarmonization(self):
        s = score.Score()
        myMDM = mdm.MasterDataDict()
        myMDM.addKey('T','P1','Player1')
        myMDM.addKey('T','P2','Player2')
        s.harmonizePlayers(myMDM)
        self.assertEqual(s.Player1,'Player1')
        self.assertEqual(s.Player2,'Player2')
        self.assertEqual(s.Player1NaturalKey,'P1')
        self.assertEqual(s.Player2NaturalKey,'P2')

    def test_ScoreInferTP(self):
        s = score.Score()

        s.setVictoryPoints1(4).setVictoryPoints2(2)
        s.inferTournamentPoints()
        self.assertEqual(s.TournamentPoints1,3)
        self.assertEqual(s.TournamentPoints2,0)

        s.setVictoryPoints1(1).setVictoryPoints2(8)
        s.inferTournamentPoints()
        self.assertEqual(s.TournamentPoints1,0)
        self.assertEqual(s.TournamentPoints2,3)

        s.setVictoryPoints1(0).setVictoryPoints2(0)
        s.inferTournamentPoints()
        self.assertEqual(s.TournamentPoints1,1)
        self.assertEqual(s.TournamentPoints2,1)

    def test_ScoreExportDict(self):
        s = score.Score()
        myMDM = mdm.MasterDataDict()
        myMDM.addKey('T','P1','Player1')
        myMDM.addKey('T','P2','Player2')
        s.harmonizePlayers(myMDM)
        sDict = s.getAsDict()
        self.assertEqual(sDict['Player1'],'Player1')
        self.assertEqual(sDict['Player2'],'Player2')
        sDict = s.getAsDict(playerNaturalKey=True)
        self.assertEqual(sDict['Player1'],'P1')
        self.assertEqual(sDict['Player2'],'P2')

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
