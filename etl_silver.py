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

files_to_process = [
    '2023_06_18_Warszawa',
    '2023_07_22_M1_Krakow',
    '2023_09_23_PolaChwaly',
    '2023_11_18_Poznan',
    '2024_01_28_Poznan',
    '2024_02_10_M2_Krakow',
    '2024_05_11_M3_Krakow',
    '2024_06_15_BoW1',
    '2024_06_15_Pyra1',
    '2024_07_28_Pyra2',
    '2024_08_17_Maraton_Warszawa',
    '2024_09_07_Kapitularz',
    '2024_09_28_PolaChwaly',
    '2024_10_19_Sucha',
    '2024_11_09_BoW2',
    '2025_02_01_Wroclaw',
    '2025_02_22_Pulawy_P',
    '2025_02_22_Pulawy_Z',
    '2025_03_22_Wroclaw',
    '2025_03_29_M4_Krakow',
    '2025_04_27_Bydgoszcz',
    '2025_05_10_Lublin',
    '2025_05_24_Poznan',
    '2025_06_14_BoW3',
    '2025_06_29_Bydgoszcz',
    '2025_07_26_Wroclaw',
    '2025_08_09_Lublin',
    '2025_08_17_Poznan',
    '2025_08_24_Wroclaw',
    '2025_08_30_Lodz',
    '2025_09_27_Gdansk',
    '2025_09_27_PolaChwaly',
    '2025_10_11_OiM_MHP',
    '2025_10_18_Sucha'
] # data/Raw/Scores/

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

playerMDM = mdm.MasterDataDict()
parse_input.load_master_data(playerMDM, player_master_data_file)

tournaments = {}

for f in files_to_process:
    event_date = f[0:10].replace('_','-')
    logging.info(f"Event date: {event_date}")

    scores = parse_input.load_scores('data/Raw/Scores/' + f + '.csv')
    raw_player_facts = load_player_facts('data/Raw/Players/' + f + '_Players.csv')
    player_facts = {}
    positions = []

    for rpf in raw_player_facts:
        new_pf = {'City': rpf['City'], 'Army': rpf['Army']}
        new_pos = {'Date': event_date, 'Tournament': rpf['Tournament'], 'Position': rpf['D0'],
                          'Player':rpf['Player'], 'Army': rpf['Army']}

        player_facts[rpf['Player']] = new_pf
        positions.append(new_pos)

        if rpf['Tournament'] != '': 
            if rpf['Tournament'] not in tournaments:
                n_rounds = 0
                if rpf['D4'] != '':
                    n_rounds = 1
                if rpf['D7'] != '':
                    n_rounds = 2
                if rpf['D10'] != '':
                    n_rounds = 3
                if rpf['D13'] != '':
                    n_rounds = 4
                if rpf['D16'] != '':
                    n_rounds = 5
                tournaments[rpf['Tournament']] = {'Tournament':rpf['Tournament'], 
                    'Date': event_date, 'nRounds':n_rounds, 'nPlayers': 1, 'Rank': 15}
            else:
                tournaments[rpf['Tournament']]['nPlayers'] = tournaments[rpf['Tournament']]['nPlayers'] + 1

    for s in scores:
        s.harmonizePlayers(playerMDM)
        if s.Player1 in player_facts:
            s.setArmy1(player_facts[s.Player1]['Army'])
        if s.Player2 in player_facts:
            s.setArmy2(player_facts[s.Player2]['Army'])
        tournaments[s.Tournament]['Rank'] = s.TournamentRank

    for s in scores:
        if s.Army1 == '':
            logging.error(s.__str__())
        if s.Army2 == '':
            logging.error(s.__str__())

    pos_file = 'data/Facts/Position/' + f + '_Position.csv'
    with open(pos_file, 'w', newline='') as csvfile:
        logging.info('Writing ' + pos_file + ' ...')
        fieldnames = ['Date', 'Tournament', 'Position', 'Player', 'Army']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

        writer.writeheader()
        for p in positions:
            writer.writerow(p)
    
    out_file = 'data/Facts/Score/' + f + '.csv'
    with open(out_file, 'w', newline='') as csvfile:
        logging.info('Writing ' + out_file + ' ...')
        fieldnames = ['Datetime','Tournament','TournamentRank','Player1','VictoryPoints1',
                    'TournamentPoints1','TournamentPoints2','VictoryPoints2','Player2',
                    'Army1','Army2','ScoringType']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

        writer.writeheader()
        for s in scores:
            writer.writerow(s.getAsDict(playerNaturalKey=True))

t_file = 'data/Facts/Tournament.csv'
with open(t_file, 'w', newline='') as csvfile:
    logging.info('Writing ' + t_file + ' ...')
    fieldnames = ['Date','Tournament','Rank','nRounds','nPlayers']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')

    writer.writeheader()
    for t in list(tournaments.values()):
        writer.writerow(t)

