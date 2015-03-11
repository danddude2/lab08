from tennis_game import TennisGame
import unittest

class TestTennisGame(unittest.TestCase):

    def testScore_ZeroToZero(self):
        '''simple example to start you off'''
        match = TennisGame()
        self.assertEqual("love - love", match.score())
	match.playerOneScored()
        self.assertEqual("15 - love", match.score())


if __name__ == '__main__':
    unittest.main()
