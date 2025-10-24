from datetime import *
from src.score import Score
import src.parse_input as parse_input
import src.calculate_ranks as calculate_ranks

scores_folder = "data"

print("Elo OiM!")
scores = parse_input.load_all(scores_folder)

ranking = {}
calculate_ranks.calculate_ranks(scores, ranking)

sorted_ranking = sorted(ranking.items(), key=lambda kv: kv[1], reverse=True)
for i, p in enumerate(sorted_ranking, start=1):
    print(f"{i}. {p[0]}: {p[1]:.2f}")
