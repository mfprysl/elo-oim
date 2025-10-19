from datetime import *
from src.score import Score
from typing import List, Dict

def sort_scores(scores: List[Score]) -> List[Score]:
    scores.sort(key=lambda s: s.Datetime)
    return scores

def adjust_rank_by_score(s: Score, ranking:Dict[str,float]):
    ranking['P1'] = 1000

def calculate_ranks(scores: List[Score],ranking:Dict[str,float]) -> Dict[str,float]:
    sort_scores(scores)
    for s in scores:
        adjust_rank_by_score(s, ranking)
    return ranking
