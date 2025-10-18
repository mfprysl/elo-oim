from datetime import *
from src.score import Score
import src.parse_input as parse_input

def calculate_rank(scores):
    return True

scores_filename = "scores.csv"

print("Elo OiM!")
scores = parse_input.load_scores(scores_filename)
for s in scores:
    print(s)
ranking = calculate_rank(scores)
print(ranking)