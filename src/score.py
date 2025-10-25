from datetime import *

SCORE_STANDARD = 0
SCORE_3LEVELS = 0 # win/draw/loss
SCORE_7LEVELS = 1 # grand win/big win/small win/draw/loss/big loss/grand loss

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
    ScoreType = SCORE_3LEVELS

    def __str__(self):

        strScoreType = '3 levels'
        if self.ScoreType == SCORE_7LEVELS: 
            strScoreType = '7 levels'

        strArmy1 = '' if self.Army1 == '' else f" ({self.Army1})"
        strArmy2 = '' if self.Army2 == '' else f" ({self.Army2})"

        return (f"{self.Datetime} {self.Tournament} ({self.TournamentRank})"
                f" | {self.Player1}{strArmy1} : {self.Player2}{strArmy2}"
                f" | {self.TournamentPoints1} ({self.VictoryPoints1})"
                f" : {self.TournamentPoints2} ({self.VictoryPoints2})"
                f", {strScoreType}"
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

    def setScoreType(self, value):
        self.ScoreType = int(value)
        return self
