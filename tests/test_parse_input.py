import unittest
from src.score import Score
import src.parse_input as parse_input
import src.calculate_ranks

class Test_ParseInput(unittest.TestCase):

    def test_LoadScores(self):
        scores = parse_input.load_scores('tests/test_scores.csv')
        self.assertEqual(scores[0].__str__(),'2025-08-01 09:00:00 Bitka o Jabłko 2025 (20) | Hans Gonschorek (Tatarzy) : Stanisław Krokodyl (Korona) | 3 (18) : 0 (0), standard scoring')
        self.assertEqual(scores[1].__str__(),'2025-07-07 09:00:00 Pola Chabrów 2025 (30) | Zenon Kuśmider (Korona) : Krashan Bhamaradżanga (Kozacy) | 3 (13) : 0 (3), standard scoring')
        self.assertEqual(scores[2].__str__(),'2025-07-07 09:00:00 Pola Chabrów 2025 (30) | Hans Gonschorek (Tatarzy) : Stanisław Krokodyl (Korona) | 1 (7) : 1 (7), standard scoring')
        self.assertEqual(scores[3].__str__(),'2025-07-07 13:00:00 Pola Chabrów 2025 (30) | Krashan Bhamaradżanga (Kozacy) : Hans Gonschorek (Tatarzy) | 0 (7) : 3 (8), standard scoring')
        self.assertEqual(scores[4].__str__(),'2025-07-07 13:00:00 Pola Chabrów 2025 (30) | Zenon Kuśmider (Korona) : Stanisław Krokodyl (Korona) | 3 (14) : 0 (4), standard scoring')

    def test_LoadAll(self):
        scores = parse_input.load_all('tests')
        src.calculate_ranks.sort_scores(scores)
        self.assertEqual(scores[0].__str__(),'2025-07-07 09:00:00 Pola Chabrów 2025 (30) | Zenon Kuśmider (Korona) : Krashan Bhamaradżanga (Kozacy) | 3 (13) : 0 (3), standard scoring')
        self.assertEqual(scores[1].__str__(),'2025-07-07 09:00:00 Pola Chabrów 2025 (30) | Hans Gonschorek (Tatarzy) : Stanisław Krokodyl (Korona) | 1 (7) : 1 (7), standard scoring')
        self.assertEqual(scores[2].__str__(),'2025-07-07 13:00:00 Pola Chabrów 2025 (30) | Krashan Bhamaradżanga (Kozacy) : Hans Gonschorek (Tatarzy) | 0 (7) : 3 (8), standard scoring')
        self.assertEqual(scores[3].__str__(),'2025-07-07 13:00:00 Pola Chabrów 2025 (30) | Zenon Kuśmider (Korona) : Stanisław Krokodyl (Korona) | 3 (14) : 0 (4), standard scoring')
        self.assertEqual(scores[4].__str__(),'2025-08-01 09:00:00 Bitka o Jabłko 2025 (20) | Hans Gonschorek (Tatarzy) : Stanisław Krokodyl (Korona) | 3 (18) : 0 (0), standard scoring')
        self.assertEqual(scores[5].__str__(),'2025-09-01 09:00:00 Jesienne Harce 2025 (20) | Zdzisław Mroczkowski (Litwa) : Marian Ceglarek (Kozacy) | 2 (3) : 6 (4), scoring 7LEVELS_BIG')
