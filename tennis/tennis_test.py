import unittest
from tennis import Tennis


class TennisTestCase(unittest.TestCase):
    def test_love_all(self) -> None:
        tennis = Tennis()
        self.assertEqual("love all", tennis.get_result(0, 0))

    def test_player1_scores_1(self) -> None:
        tennis = Tennis()
        self.assertEqual("fifteen love", tennis.get_result(1, 0))


if __name__ == "__main__":
    unittest.main()
