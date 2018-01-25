import six
import random
import copy

# a 3 by 3 board for playing tic tac toe
class Board(object):
    ''' Board is initialized with blank strings '''
    def __init__(self, board=[' ']*9):
        self.board = board
        self.unoccupied_places = list(range(9))
        self.game_state = 'In progress'

    def __str__(self):
        return (' {0} | {1} | {2} \n===+===+===\n'
              + ' {3} | {4} | {5} \n===+===+===\n'
              + ' {6} | {7} | {8} \n').format(self._board[0], self._board[1], self._board[2],
                                              self._board[3], self._board[4], self._board[5],
                                              self._board[6], self._board[7], self._board[8])

    @property
    def board(self):
        return self._board

    ''' A list can assigned to the board. This works in program and is not visible to the user '''
    @board.setter
    def board(self, value):
        if not type(value) == list:
            raise Exception('Argument passed in is not a list.')
        if not len(value) == 9:
            raise Exception('The size of the input board must be equal to 9.')
        if not all([i in ['X', 'O', ' '] for i in value]):
            print('value is', value)
            raise Exception('Some of the arguments entered are not numeric or not in the range 0-8 for the position field')
        self.unoccupied_places = []
        for i in range(len(value)):
            if value[i] == ' ' and not i not in self.unoccupied_places:
                self.unoccupied_places.append(i)
        self._board = value

    def __getitem__(self, position):
        if not type(position) == int:
            raise Exception('Position passed is not a numeric value.')
        if position < 0 or position > 8:
            raise Exception('Position has to be a value between 0 to 8. Please choose a new position : ')
        return self._board[position]

    def __setitem__(self, position, marker):
        if not type(position) == int:
            raise Exception('Position passed is not a numeric value.')
        if position < 0 or position > 8:
            raise Exception('Position has to be a value between 0 to 8. Please choose a new position : ')
        # dont need to specify validation for marker as it is already taken care of
        self._board[position] = marker

    def __iter__(self):
        for i in self._board:
            yield i

    def insert_move(self, player_move, player_marker):
        if self._board[player_move] != ' ': 
            print('Currently occupied by ' + self._board[player_move])
            print('Position is already occupied. Please choose a new position : ')
            return False
        else:
            self._board[player_move] = player_marker
            del self.unoccupied_places[self.unoccupied_places.index(player_move)]
        return True

    def check_three_in_a_row(self):
        for marker in ['X', 'O']:  # this is necessary because you don't want to check 3 empty spaces in a row
            # Horizontal line checks
            if ((self._board[0] == self._board[1] == self._board[2] == marker) or
                (self._board[3] == self._board[4] == self._board[5] == marker) or
                (self._board[6] == self._board[7] == self._board[8] == marker)):
                return True
            # Vertical line checks
            elif ((self._board[0] == self._board[3] == self._board[6] == marker) or
                  (self._board[1] == self._board[4] == self._board[7] == marker) or
                  (self._board[2] == self._board[5] == self._board[8] == marker)):
                return True
            # Diagonal line checks
            elif ((self._board[0] == self._board[4] == self._board[8] == marker) or
                  (self._board[2] == self._board[4] == self._board[6] == marker)):
                return True
        return False

    def check_tie(self):
        return len(self.unoccupied_places) == 0