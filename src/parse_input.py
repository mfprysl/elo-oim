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

    scoreFactory = score.ScoreFactory()
    
    try:
        with scores_file.open("r", encoding=encoding, newline="") as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            for row_number, row in enumerate(reader, start=1):

                s = scoreFactory.getScore(row)
                scores.append(s)

    except UnicodeDecodeError:
        logging.error(f"Error: could not decode file using encoding '{encoding}'.")
        sys.exit(2)
    except csv.Error as e:
        logging.error(f"CSV parsing error: {e}")
        sys.exit(3)

    return scores

