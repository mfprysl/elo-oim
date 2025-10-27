from typing import List
import csv
import sys
from pathlib import Path
import logging
import src.score as score
import src.master_data as mdm

def load_all_scores(scores_folder: Path) -> List[score.Score]:
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
        logging.error(f"File not found: {scores_file}")
        sys.exit(1)

    scoreFactory = score.ScoreFactory()
    
    try:
        with scores_file.open("r", encoding=encoding, newline="") as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            for row_number, row in enumerate(reader, start=1):

                if 'Datetime' in row and 'Tournament' in row and 'Player1' in row and 'Player2' in row and row['Datetime'] != '' and row['Player1'] != '' and row['Player2'] != '':
                    try:
                        s = scoreFactory.getScore(row)
                    except ValueError:
                        logging.warning(f"Malformed data in: {scores_file}")
                    else:
                        scores.append(s)
                else:
                    logging.info('Skipping rows in ' + str(scores_file.resolve()) + ', no relevant data found ...')
                    break 

    except UnicodeDecodeError:
        logging.error(f"Could not decode file using encoding '{encoding}'.")
        sys.exit(2)
    except csv.Error as e:
        logging.error(f"CSV parsing error: {e}")
        sys.exit(3)

    return scores

def load_master_data(mdmDict: mdm.MasterDataDict, mdm_file: Path):
    encoding = 'utf-8-sig';
    delimiter = ';';

    if not isinstance(mdm_file, Path):
        mdm_file = Path(mdm_file)

    logging.info('Reading ' + str(mdm_file.resolve()) + ' ...')

    if not mdm_file.exists():
        logging.error(f"Error: file not found: {mdm_file}")
        sys.exit(1)
    
    try:
        with mdm_file.open("r", encoding=encoding, newline="") as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            for row_number, row in enumerate(reader, start=1):
                mdmDict.addKey(row['DataProvider'],row['NaturalKey'],row['GoldenKey'])

    except UnicodeDecodeError:
        logging.error(f"Error: could not decode file using encoding '{encoding}'.")
        sys.exit(2)
    except csv.Error as e:
        logging.error(f"CSV parsing error: {e}")
        sys.exit(3)
