import unittest
from game import TicTacToe

class Test5(unittest.TestCase):
    def setUp(self):
        print('Starting a new test ...')
        self.game = TicTacToe(configparam=('C', 'C', "X", "O", 2, 1, 'ComputerVComputer'))
        self.game.start_game()

    def test_game_1_2(self):
        self.assertTrue(self.game.board.game_state in ["win", "tie"])

if __name__ == '__main__':
    unittest.main()
