from typing import List
import csv
import sys
from pathlib import Path

from src.score import Score

def load_scores(scores_file: Path) -> List[Score]:

    encoding = 'utf-8-sig';
    delimiter = ';';

    scores = []

    if not isinstance(scores_file, Path):
        scores_file = Path(scores_file)

    print('Reading ' + str(scores_file.resolve()) + ' ...')

    if not scores_file.exists():
        print(f"Error: file not found: {scores_file}")
        sys.exit(1)

    try:
        with scores_file.open("r", encoding=encoding, newline="") as f:
            reader = csv.DictReader(f, delimiter=delimiter)
            for row_number, row in enumerate(reader, start=1):
                s = Score()
                s.setDatetime(row['Datetime'])
                s.setTournament(row['Tournament'])
                s.setTournamentRank(row['TournamentRank'])
                s.setPlayer1(row['Player1'])
                s.setArmy1(row['Army1'])
                s.setVictoryPoints1(row['VictoryPoints1'])
                s.setTournamentPoints1(row['TournamentPoints1'])
                s.setPlayer2(row['Player2'])
                s.setArmy2(row['Army2'])
                s.setVictoryPoints2(row['VictoryPoints2'])
                s.setTournamentPoints2(row['TournamentPoints2'])
                scores.append(s)

    except UnicodeDecodeError:
        print(f"Error: could not decode file using encoding '{encoding}'.")
        sys.exit(2)
    except csv.Error as e:
        print(f"CSV parsing error: {e}")
        sys.exit(3)

    return scores

