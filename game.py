# Arun Balchandran
import six
import copy
from configuration import Configuration
from board import Board
from player import Player

class TicTacToe(object):
    ''' Player we get from the config is either a HumanPlayer or a ComputerPlayer object. '''
    def __init__(self, configparam=None):
        if configparam:
            config = Configuration(configparam)
        else:
            self.game_helper()
            config = Configuration()
        self.game_difficulty = config.game_difficulty
        self.p1 = Player.create_player(config.p1_type, config.p1_marker, config.game_difficulty)
        self.p2 = Player.create_player(config.p2_type, config.p2_marker, config.game_difficulty)
        self.starting_player = config.starting_player
        self.game_type = config.game_type
        self.board = Board()

    def game_helper(self):
        print(('Welcome to TicTacToe\n'
             + 'This is how a board looks like :\n'
             + ' {0} | {1} | {2} \n===+===+===\n'
             + ' {3} | {4} | {5} \n===+===+===\n'
             + ' {6} | {7} | {8} \n').format(*([' ']*9)))
        print(('\nThe elements of the board are accessed using numbers from 0 - 8.\n'
             + 'Here is a representation of the board elements and the numbers they can be accessed by :\n'
             + ' {0} | {1} | {2} \n===+===+===\n'
             + ' {3} | {4} | {5} \n===+===+===\n'
             + ' {6} | {7} | {8} \n').format(*(range(9))))

    def game_over(self):
        if self.board.check_three_in_a_row():
            self.board.game_state = 'win'
            return True
        elif self.board.check_tie():
            self.board.game_state = 'tie'
            return True
        else:
            return False

    def start_game(self):
        # start by printing the board
        print(('\nOur initial board setup is :\n{}'
             + '\nThe game is of type : {} vs {}').format(str(self.board), *self.game_type.split('V')))
        current_player = self.starting_player
        while not self.game_over():
            print('Current player is : Player{}'.format(str(current_player + 1)))    # current_player is either 0 or 1
            while True:
                if current_player == 0:
                    current_move = self.p1.get_next_move(copy.deepcopy(self.board))   # if successful insertion of move
                    current_marker = self.p1.marker
                elif current_player == 1:
                    current_move = self.p2.get_next_move(copy.deepcopy(self.board))
                    current_marker = self.p2.marker
                if self.board.insert_move(current_move, current_marker):  # if you can insert into board
                    break
            print('\n' + str(self.board))
            current_player = (current_player + 1) % 2
        if self.board.game_state == 'win':
            print('Game over. The winner is Player{}'.format(str(((current_player + 1) % 2) + 1)))
        else:    # game_state == 'tie'
            print('Game over. The game is a tie.')


if __name__ == '__main__':
    game = TicTacToe()
    print('\nThe game starts now ...\n')
    game.start_game()
