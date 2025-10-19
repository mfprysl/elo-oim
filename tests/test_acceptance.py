import unittest
from src.score import Score
import src.calculate_ranks
import src.parse_input

class Test_Acceptance(unittest.TestCase):

    def test_AcceptanceSampleScores(self):

        scores = src.parse_input.load_scores('tests/test_scores.csv')
        ranking = {}
        src.calculate_ranks.calculate_ranks(scores, ranking)

        sorted_ranking = sorted(ranking.items(), key=lambda kv: kv[1], reverse=True)

        self.assertEqual(f"{sorted_ranking[0][0]}: {sorted_ranking[0][1]:.2f}",'Zenon Kuśmider: 1048.20')
        self.assertEqual(f"{sorted_ranking[1][0]}: {sorted_ranking[1][1]:.2f}",'Hans Gonschorek: 1039.80')
        self.assertEqual(f"{sorted_ranking[2][0]}: {sorted_ranking[2][1]:.2f}",'Krashan Bhamaradżanga: 960.15')
        self.assertEqual(f"{sorted_ranking[3][0]}: {sorted_ranking[3][1]:.2f}",'Stanisław Krokodyl: 951.85')
