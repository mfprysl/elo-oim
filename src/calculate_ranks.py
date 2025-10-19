from datetime import *
from src.score import Score
from typing import List, Dict

def sort_scores(scores: List[Score]) -> List[Score]:
    scores.sort(key=lambda s: s.Datetime)
    return scores

def adjust_rank_by_score(s: Score, ranking:Dict[str,float]):
    P1_previous_rank = 1000 if not s.Player1 in ranking else ranking[s.Player1]
    P2_previous_rank = 1000 if not s.Player2 in ranking else ranking[s.Player2]

    P1_new_rank = 1030
    P2_new_rank = 970

    ranking[s.Player1] = P1_new_rank
    ranking[s.Player2] = P2_new_rank

def calculate_ranks(scores: List[Score],ranking:Dict[str,float]) -> Dict[str,float]:
    sort_scores(scores)
    for s in scores:
        adjust_rank_by_score(s, ranking)
    return ranking
