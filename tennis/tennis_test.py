import unittest
from tennis import Tennis

class TennisTestCase(unittest.TestCase):
    def test_love_all(self) -> None:
        tennis = Tennis()
        self.assertEqual('love all', tennis.get_result())


if __name__ == "__main__":
    unittest.main()