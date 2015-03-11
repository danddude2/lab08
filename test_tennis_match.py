from tennis_game import TennisGame
import unittest

class TestTennisGame(unittest.TestCase):

	def testScore_ZeroToZero(self):
		'''Testing zero to zero'''
		match = TennisGame()
		self.assertEqual("love - love", match.score())

	def testScore_OneToZero(self):
		'''Testing one to zero'''
		match = TennisGame()
		match.playerOneScored()
		self.assertEqual("15 - love", match.score())


if __name__ == '__main__':
    unittest.main()
