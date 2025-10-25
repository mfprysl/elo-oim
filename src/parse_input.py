from typing import List
import csv
import sys
from pathlib import Path
import logging
import src.score as score

def load_all(scores_folder: Path) -> List[score.Score]:
    scores = []

    if not isinstance(scores_folder, Path):
        scores_folder = Path(scores_folder)

    logging.info('Opening folder ' + str(scores_folder.resolve()) + ' ...')

    for file in sorted(scores_folder.glob('*.csv')):

        if not file.is_file():
            continue
    
        scores += load_scores(file)

    return scores

def load_scores(scores_file: Path) -> List[score.Score]:

    encoding = 'utf-8-sig';
    delimiter = ';';

    scores = []

    if not isinstance(scores_file, Path):
        scores_file = Path(scores_file)

    logging.info('Reading ' + str(scores_file.resolve()) + ' ...')

    if not scores_file.exists():
        logging.error(f"Error: file not found: {scores_file}")
        sys.exit(1)

    try:
        with scores_file.open("r", encoding=encoding, newline="") as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            for row_number, row in enumerate(reader, start=1):
                if 'ScoringType' in row and row['ScoringType'] == '7LEVELS_BIG':
                    s = score.Score7LevelsBig()
                else:
                    s = score.Score()
                s.setDatetime(row['Datetime'])
                s.setTournament(row['Tournament'])
                s.setTournamentRank(row['TournamentRank'])
                s.setPlayer1(row['Player1'])

                if 'Army1' in row:
                    s.setArmy1(row['Army1'])
                
                s.setVictoryPoints1(row['VictoryPoints1'])
                s.setTournamentPoints1(row['TournamentPoints1'])
                s.setPlayer2(row['Player2'])
                
                if 'Army2' in row:
                    s.setArmy2(row['Army2'])
                
                s.setVictoryPoints2(row['VictoryPoints2'])
                s.setTournamentPoints2(row['TournamentPoints2'])
                                
                scores.append(s)

    except UnicodeDecodeError:
        logging.error(f"Error: could not decode file using encoding '{encoding}'.")
        sys.exit(2)
    except csv.Error as e:
        logging.error(f"CSV parsing error: {e}")
        sys.exit(3)

    return scores

