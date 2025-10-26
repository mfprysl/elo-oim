from datetime import *
import logging
from src.score import Score
import src.parse_input as parse_input
import src.calculate_ranks as calculate_ranks
import src.master_data as mdm

logging.basicConfig(level=logging.INFO, format='\t%(message)s')

scores_folder = "data/Facts"
player_master_data_file = "data/MasterData/player.csv"

print("Elo OiM!")

scores = parse_input.load_all_scores(scores_folder)

playerMDM = mdm.MasterDataDict()
parse_input.load_master_data(playerMDM, player_master_data_file)

for s in scores:
    s.harmonizePlayers(playerMDM)

ranking = {}
calculate_ranks.calculate_ranks(scores, ranking)

sorted_ranking = sorted(ranking.items(), key=lambda kv: kv[1], reverse=True)
for i, p in enumerate(sorted_ranking, start=1):
    print(f"{i}. {p[0]}: {p[1]:.2f}")
