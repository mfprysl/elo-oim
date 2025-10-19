from datetime import *
from src.score import Score
import src.parse_input as parse_input
import src.calculate_ranks as calculate_ranks

scores_filename = "tests/test_scores.csv"

print("Elo OiM!")
scores = parse_input.load_scores(scores_filename)
for s in scores:
    print(s)
ranking = {}
calculate_ranks.calculate_ranks(scores, ranking)
for p in ranking:
    print(f"{p} : {ranking[p]}")
