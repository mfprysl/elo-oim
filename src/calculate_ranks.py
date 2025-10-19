from datetime import *
from src.score import Score
from typing import List, Dict

class Rank:
    Rank = 1000

def sort_scores(scores: List[Score]) -> List[Score]:
    scores.sort(key=lambda s: s.Datetime)
    return scores

def calculate_ranks(scores: List[Score],ranking:Dict[str,Rank]) -> Dict[str,Rank]:
    ranking = []
    sort_scores(scores)
    return ranking
