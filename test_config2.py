import unittest
from game import TicTacToe

class Test2(unittest.TestCase):
    def setUp(self):
        print('Starting a new test ...')
        self.game1 = TicTacToe(configparam=('C', 'C', "X", "O",0,1, 'ComputerVComputer'))
        self.game1.start_game()

    def test_game_0_1(self):
        self.assertTrue(self.game1.board.game_state in ["win", "tie"])

if __name__ == '__main__':
    unittest.main()
