import six
import random
import copy

class ComputerPlayer(object):
    ''' Initialize player with marker (X or O) '''
    def __init__(self, marker, game_difficulty):
        self.marker = marker
        self.other_player_marker = 'X' if marker != 'X' else 'O'
        self.game_difficulty = game_difficulty

    def __str__(self):
        return 'Computer player with marker : ' + self.marker

    def game_over(self, board):
        if not board.check_three_in_a_row() and not board.check_tie():  # take advantage of python shortcircuiting
            return False
        return True

    def check_one_move_win(self, board):
        # first we need to check if we can win in the next move
        print('checking one move win')
        for position in board.unoccupied_places:
            board[position] = self.marker
            if self.game_over(board):
                print('Computer chose position {}'.format(position))
                #six.moves.input('Press enter to continue ...')
                return position
            board[position] = ' '
        return -1

    def check_one_move_lose(self, board):
        # block the player since we cant win in one move
        print('checking one move lose')
        for position in board.unoccupied_places:
            board[position] = self.other_player_marker
            if self.game_over(board):
                print('Computer chose position {}'.format(position))
                #six.moves.input('Press enter to continue ...')
                return position  # we need to block this position
            board[position] = ' '
        return -1

    def check_corner_edges(self, board):
        # check if the player is scheming against us by doing a double edge move
        print('checking corner edges ')
        if (board[1] == board[3] == self.other_player_marker) and (0 in board.unoccupied_places):
            return 0
        elif (board[1] == board[5] == self.other_player_marker) and (2 in board.unoccupied_places):
            return 2
        elif (board[3] == board[7] == self.other_player_marker) and (6 in board.unoccupied_places):
            return 6
        elif (board[5] == board[7] == self.other_player_marker) and (8 in board.unoccupied_places):
            return 8
        return -1

    def take_center(self, board):
        # if its the first move, or if we have nothing to do, take the center
        print('checking take center')
        if 4 in board.unoccupied_places:
            print('Computer chose position 4')
            #six.moves.input('Press enter to continue ...')
            return 4
        return -1

    def take_edge(self, board):
        # if we cant take the center, we can take an edge instead
        print('checking take edge')
        for position in board.unoccupied_places:
            if position in [1, 3, 5, 7]:
                print('Computer chose position {}'.format(position))
                #six.moves.input('Press enter to continue ...')
                return position
        return -1

    def take_corner(self, board):
        # if we cant do either, we can take a corner instead
        print('checking take corner')
        for position in board.unoccupied_places:
            if position in [0, 2, 6, 8]:
                print('Computer chose position {}'.format(position))
                #six.moves.input('Press enter to continue ...')
                return position
        return -1

    # this object is a copy of the original object
    def get_next_move(self, board):
        print('Computer is choosing a move ...')
        if self.game_difficulty == 0:   # easy difficulty
            current_move = random.choice(board.unoccupied_places)
            print('Computer chose position {}'.format(current_move))
            #six.moves.input('Press enter to continue ...')
            return current_move
        # the medium strategy
        elif self.game_difficulty == 1:
            # do a smart move 50% of the times and stupid move the other times
            if random.random() < 0.5:
                current_move = random.choice(board.unoccupied_places)
                print('Computer chose position {}'.format(current_move))
                #six.moves.input('Press enter to continue ...')
                return current_move
        # the impossible win strategy -> should guarantee a draw if not a win
        strategies = [self.check_one_move_win, self.check_one_move_lose, self.check_corner_edges,
                      self.take_center, self.take_edge, self.take_corner]
        for strategy in strategies:
            position = strategy(board)
            if position != -1:
                return position
        # don't need to send any move, as we must have exhausted all moves
        print('Done with all moves')
        return self.board.unoccupied_places[0]
