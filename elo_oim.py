from datetime import *
import logging
from src.score import Score
import src.parse_input as parse_input
import src.calculate_ranks as calculate_ranks
import src.master_data as mdm
import csv

logging.basicConfig(level=logging.INFO, format='\t%(message)s')

scores_folder = "data/Facts/Score"
player_master_data_file = "data/MasterData/player.csv"

print("Elo OiM!")

scores = parse_input.load_all_scores(scores_folder)

playerMDM = mdm.MasterDataDict()
parse_input.load_master_data(playerMDM, player_master_data_file)

for s in scores:
    s.harmonizePlayers(playerMDM)

ranking = {}
last_game = calculate_ranks.calculate_ranks(scores, ranking)

print(f"\nLast game started: {last_game}\n")
sorted_ranking = sorted(ranking.items(), key=lambda kv: kv[1], reverse=True)

e_file = f"data/Facts/Elo/Elo_{last_game.year}_{last_game.month}_{last_game.day}.csv"
with open(e_file, 'w', newline='') as csvfile:
    logging.info('Writing ' + e_file + ' ...')
    fieldnames = ['Player','Rank']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')

    writer.writeheader()
    for r in sorted_ranking:
        writer.writerow({'Player':r[0],'Rank':r[1]})

for i, p in enumerate(sorted_ranking, start=1):
    print(f"{i}. {p[0]}: {p[1]:.2f}")
