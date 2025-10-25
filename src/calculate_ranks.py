from datetime import *
import logging
from src.score import Score
import src.score as score
from typing import List, Dict

def sort_scores(scores: List[Score]) -> List[Score]:
    scores.sort(key=lambda s: s.Datetime)
    return scores

def adjust_rank_by_score(s: Score, ranking:Dict[str,float]):
    P1_previous_rank = 1000 if not s.Player1 in ranking else ranking[s.Player1]
    P2_previous_rank = 1000 if not s.Player2 in ranking else ranking[s.Player2]

    if s.ScoreType == score.SCORE_7LEVELS:
        diff = s.TournamentPoints1 - s.TournamentPoints2

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
    else:
        if s.TournamentPoints1 > s.TournamentPoints2:
            P1_score = 1.0
            P2_score = 0.0
        elif s.TournamentPoints1 < s.TournamentPoints2:
            P1_score = 0.0
            P2_score = 1.0
        else:
            P1_score = 0.5
            P2_score = 0.5

    result_rank = s.TournamentRank + 2.0 * abs(s.VictoryPoints1 - s.VictoryPoints2)

    P1_win_chance = 1.0/(1.0 + pow(10,(P2_previous_rank - P1_previous_rank)/400))
    P2_win_chance = 1.0 - P1_win_chance

    P1_new_rank = P1_previous_rank + result_rank * (P1_score - P1_win_chance)
    P2_new_rank = P2_previous_rank + result_rank * (P2_score - P2_win_chance)

    ranking[s.Player1] = P1_new_rank
    ranking[s.Player2] = P2_new_rank

def calculate_ranks(scores: List[Score],ranking:Dict[str,float]) -> Dict[str,float]:
    sort_scores(scores)
    for s in scores:
        adjust_rank_by_score(s, ranking)
    return ranking
