import unittest
from game import TicTacToe

class Test4(unittest.TestCase):
    def setUp(self):
        print('Starting a new test ...')
        self.game1 = TicTacToe(configparam=('C', 'C', "X", "O",1,1, 'ComputerVComputer'))
        self.game1.start_game()

    def test_game_1_1(self):
        self.assertTrue(self.game1.board.game_state in ["win", "tie"])

if __name__ == '__main__':
    unittest.main()
