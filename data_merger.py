from datetime import *
import logging
from src.score import Score
import src.parse_input as parse_input
import src.master_data as mdm
from typing import List, Dict
import csv
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='\t%(message)s')

results_file = 'data/Facts/2023_06_18_Warszawa.csv'
players_file = 'data/Raw/2023_06_18_Warszawa_Players.csv'
player_master_data_file = "data/MasterData/player.csv"

def load_player_facts(players_file: Path) -> List[Dict]:

    encoding = 'utf-8-sig';
    delimiter = ';';

    player_facts = []

    if not isinstance(players_file, Path):
        players_file = Path(players_file)

    logging.info('Reading ' + str(players_file.resolve()) + ' ...')

    if not players_file.exists():
        logging.error(f"File not found: {players_file}")
        sys.exit(1)
  
    try:
        with players_file.open("r", encoding=encoding, newline="") as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            for row_number, row in enumerate(reader, start=1):
                player_facts.append(row)

    except UnicodeDecodeError:
        logging.error(f"Could not decode file using encoding '{encoding}'.")
        sys.exit(2)
    except csv.Error as e:
        logging.error(f"CSV parsing error: {e}")
        sys.exit(3)

    return player_facts


print("Combining data for Elo OiM from several files!")

scores = parse_input.load_scores(results_file)
raw_player_facts = load_player_facts(players_file)
player_facts = {}
for rpf in raw_player_facts:
    player_facts[rpf['Player']]={'City': rpf['City'], 'Army': rpf['Army']}

playerMDM = mdm.MasterDataDict()
parse_input.load_master_data(playerMDM, player_master_data_file)

for s in scores:
    s.harmonizePlayers(playerMDM)
    if s.Player1 in player_facts:
        s.setArmy1(player_facts[s.Player1]['Army'])
    if s.Player2 in player_facts:
        s.setArmy2(player_facts[s.Player2]['Army'])

with open('out.csv', 'w', newline='') as csvfile:
    fieldnames = ['Datetime','Tournament','TournamentRank','Player1','VictoryPoints1',
                  'TournamentPoints1','TournamentPoints2','VictoryPoints2','Player2',
                  'Army1','Army2','ScoringType']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

    writer.writeheader()
    for s in scores:
        writer.writerow(s.getAsDict(playerNaturalKey=True))
