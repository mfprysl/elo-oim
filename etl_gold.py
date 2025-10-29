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

player_master_data_file = "data/MasterData/player.csv"
army_master_data_file = "data/MasterData/army.csv"
tournaments_file = 'data/Facts/Tournament.csv'
scores_folder = 'data/Facts/Score'
positions_folder = 'data/Facts/Position'

def load_positions(file: Path) -> List:

    encoding = 'utf-8-sig';
    delimiter = ';';

    positions = []

    if not isinstance(file, Path):
        file = Path(file)

    logging.info('Reading ' + str(file.resolve()) + ' ...')

    if not file.exists():
        logging.error(f"File not found: {file}")
        sys.exit(1)

    try:
        with file.open("r", encoding=encoding, newline="") as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            for row_number, row in enumerate(reader, start=1):
                positions.append(row)

    except UnicodeDecodeError:
        logging.error(f"Could not decode file using encoding '{encoding}'.")
        sys.exit(2)
    except csv.Error as e:
        logging.error(f"CSV parsing error: {e}")
        sys.exit(3)

    return positions

def load_tournaments(file: Path) -> List[Dict]:

    encoding = 'utf-8-sig';
    delimiter = ';';

    tournaments = []

    if not isinstance(file, Path):
        file = Path(file)

    logging.info('Reading ' + str(file.resolve()) + ' ...')

    if not file.exists():
        logging.error(f"File not found: {file}")
        sys.exit(1)
  
    try:
        with file.open("r", encoding=encoding, newline="") as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            for row_number, row in enumerate(reader, start=1):
                tournaments.append(row)

    except UnicodeDecodeError:
        logging.error(f"Could not decode file using encoding '{encoding}'.")
        sys.exit(2)
    except csv.Error as e:
        logging.error(f"CSV parsing error: {e}")
        sys.exit(3)

    return tournaments

positions = []
scores = []
tournaments = []

playerMDM = mdm.MasterDataDict()
parse_input.load_master_data(playerMDM, player_master_data_file)

armyMDM = mdm.MasterDataDict()
parse_input.load_master_data(armyMDM, army_master_data_file)

scores = parse_input.load_all_scores(scores_folder)
for s in scores:
    s.harmonizePlayers(playerMDM)
    s.harmonizeArmies(armyMDM)

if not isinstance(positions_folder, Path):
    positions_folder = Path(positions_folder)
logging.info('Opening folder ' + str(positions_folder.resolve()) + ' ...')
for file in sorted(positions_folder.glob('*.csv')):
    if not file.is_file():
        continue
    positions += load_positions(file)

for p in positions:
    p['Army'] = armyMDM.getGoldenKey(p['Tournament'],p['Army'],anyDataProvider=True)

tournaments = load_tournaments(tournaments_file)

t_file = 'data/Gold/Tournament.csv'
with open(t_file, 'w', newline='') as csvfile:
    logging.info('Writing ' + t_file + ' ...')
    fieldnames = ['Date','Tournament','Rank','nRounds','nPlayers']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')

    writer.writeheader()
    for t in tournaments:
        writer.writerow(t)

s_file = 'data/Gold/Score.csv'
with open(s_file, 'w', newline='') as csvfile:
    logging.info('Writing ' + s_file + ' ...')
    fieldnames = ['Datetime','Tournament','TournamentRank','Player1','VictoryPoints1',
                'TournamentPoints1','TournamentPoints2','VictoryPoints2','Player2',
                'Army1','Army2','ScoringType']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')

    writer.writeheader()
    for s in scores:
        writer.writerow(s.getAsDict())

pos_file = 'data/Gold/Position.csv'
with open(pos_file, 'w', newline='') as csvfile:
    logging.info('Writing ' + pos_file + ' ...')
    fieldnames = ['Date', 'Tournament', 'Position', 'Player', 'Army']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',')

    writer.writeheader()
    for p in positions:
        writer.writerow(p)
