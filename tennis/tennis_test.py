import unittest
from player_score import PlayerScore
from tennis import Tennis


class TennisTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.tennis = Tennis(PlayerScore())
        return super().setUp()

    def test_love_all(self) -> None:
        self.assertEqual("love all", self.tennis.get_result())

    def test_player1_scores_1(self) -> None:
        self.tennis.player1_scores()
        self.assertEqual("fifteen love", self.tennis.get_result())


if __name__ == "__main__":
    unittest.main()
