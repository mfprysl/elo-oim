from datetime import *
from typing import Tuple, Dict

SCORE_STANDARD = 0 # no levels, just exponent
SCORE_7LEVELS_BIG = 1 # 1/0.9/0.8/0.5/0.2/0.1/0
SCORE_7LEVELS_SMALL = 2 # 1/0.65/0.6/0.5/0.4/0.35/0

class Score:
    Datetime = datetime.fromisoformat('1974-07-07 12:00')
    Tournament = 'T'
    TournamentRank = 20
    Player1 = 'P1'
    Army1 = ''
    VictoryPoints1 = 0
    TournamentPoints1 = 0
    Player2 = 'P2'
    Army2 = ''
    VictoryPoints2 = 0
    TournamentPoints2 = 0
    ScoringType = SCORE_STANDARD
    ScoringTypeStr = 'standard scoring'

    def __str__(self):

        strArmy1 = '' if self.Army1 == '' else f" ({self.Army1})"
        strArmy2 = '' if self.Army2 == '' else f" ({self.Army2})"

        return (f"{self.Datetime} {self.Tournament} ({self.TournamentRank})"
                f" | {self.Player1}{strArmy1} : {self.Player2}{strArmy2}"
                f" | {self.TournamentPoints1} ({self.VictoryPoints1})"
                f" : {self.TournamentPoints2} ({self.VictoryPoints2})"
                f", {self.ScoringTypeStr}"
                )

    def setDatetime(self, value):
        if isinstance(value, datetime):
            self.Datetime = value
        else:
            self.Datetime = datetime.fromisoformat(value)
        return self
    
    def setTournament(self, value):
        self.Tournament = value
        return self
    
    def setTournamentRank(self, value):
        self.TournamentRank = int(value)
        return self
    
    def setPlayer1(self, value):
        self.Player1 = value
        return self
    
    def setArmy1(self, value):
        self.Army1 = value
        return self
    
    def setVictoryPoints1(self, value):
        self.VictoryPoints1 = int(value)
        return self
    
    def setTournamentPoints1(self, value):
        self.TournamentPoints1 = int(value)
        return self
        
    def setPlayer2(self, value):
        self.Player2 = value
        return self
    
    def setArmy2(self, value):
        self.Army2 = value
        return self
    
    def setVictoryPoints2(self, value):
        self.VictoryPoints2 = int(value)
        return self
    
    def setTournamentPoints2(self, value):
        self.TournamentPoints2 = int(value)
        return self

    def getScore(self) -> Tuple[int, int]:
        if self.TournamentPoints1 > self.TournamentPoints2:
            P1_score = 1.0
            P2_score = 0.0
        elif self.TournamentPoints1 < self.TournamentPoints2:
            P1_score = 0.0
            P2_score = 1.0
        else:
            P1_score = 0.5
            P2_score = 0.5

        return [P1_score, P2_score]

class Score7LevelsBig(Score):
    ScoringType = SCORE_7LEVELS_BIG
    ScoringTypeStr = 'scoring 7LEVELS_BIG'

    def getScore(self) -> Tuple[int, int]:
        diff = self.VictoryPoints1 - self.VictoryPoints2

        if diff >= 11:
            P1_score = 1.0
            P2_score = 0.0
        elif diff >= 6:
            P1_score = 0.9
            P2_score = 0.1
        elif diff >= 2:
            P1_score = 0.8
            P2_score = 0.2
        elif diff >= -1:
            P1_score = 0.5
            P2_score = 0.5
        elif diff >= -5:
            P1_score = 0.2
            P2_score = 0.8
        elif diff >= -10:
            P1_score = 0.1
            P2_score = 0.9
        else:
            P1_score = 0.0
            P2_score = 1.0

        return [P1_score, P2_score]

class Score7LevelsBig(Score):
    ScoringType = SCORE_7LEVELS_BIG
    ScoringTypeStr = 'scoring 7LEVELS_BIG'

    def getScore(self) -> Tuple[int, int]:
        diff = self.VictoryPoints1 - self.VictoryPoints2

        if diff >= 11:
            P1_score = 1.0
            P2_score = 0.0
        elif diff >= 6:
            P1_score = 0.9
            P2_score = 0.1
        elif diff >= 2:
            P1_score = 0.8
            P2_score = 0.2
        elif diff >= -1:
            P1_score = 0.5
            P2_score = 0.5
        elif diff >= -5:
            P1_score = 0.2
            P2_score = 0.8
        elif diff >= -10:
            P1_score = 0.1
            P2_score = 0.9
        else:
            P1_score = 0.0
            P2_score = 1.0

        return [P1_score, P2_score]

class Score7LevelsSmall(Score):
    ScoringType = SCORE_7LEVELS_SMALL
    ScoringTypeStr = 'scoring 7LEVELS_SMALL'

    def getScore(self) -> Tuple[int, int]:
        diff = self.VictoryPoints1 - self.VictoryPoints2

        if diff >= 3:
            P1_score = 1.0
            P2_score = 0.0
        elif diff >= 2:
            P1_score = 0.65
            P2_score = 0.35
        elif diff >= 1:
            P1_score = 0.6
            P2_score = 0.4
        elif diff > -1:
            P1_score = 0.5
            P2_score = 0.5
        elif diff > -2:
            P1_score = 0.4
            P2_score = 0.6
        elif diff > -3:
            P1_score = 0.35
            P2_score = 0.65
        else:
            P1_score = 0.0
            P2_score = 1.0

        return [P1_score, P2_score]

class ScoreFactory:
    def getScore(self,row: Dict) -> Score:
        if 'ScoringType' in row and row['ScoringType'] == '7LEVELS_BIG':
            s = Score7LevelsBig()
        elif 'ScoringType' in row and row['ScoringType'] == '7LEVELS_SMALL':
            s = Score7LevelsSmall()
        else:
            s = Score()

        s.setDatetime(row['Datetime'])
        s.setTournament(row['Tournament'])
        s.setTournamentRank(row['TournamentRank'])
        s.setPlayer1(row['Player1'])

        if 'Army1' in row:
            s.setArmy1(row['Army1'])
        
        s.setVictoryPoints1(row['VictoryPoints1'])
        s.setTournamentPoints1(row['TournamentPoints1'])
        s.setPlayer2(row['Player2'])
        
        if 'Army2' in row:
            s.setArmy2(row['Army2'])
        
        s.setVictoryPoints2(row['VictoryPoints2'])
        s.setTournamentPoints2(row['TournamentPoints2'])

        return s