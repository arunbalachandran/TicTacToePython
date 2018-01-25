import six
import random
import copy

class HumanPlayer(object):
    ''' Initialize player with marker (X or O) '''
    def __init__(self, marker=None):
        self.marker = marker

    def __str__(self):
        return 'Human player with marker : ' + self.marker

    def get_next_move(self, unoccuppied_places):
        print('Enter a position between 0 to 8 to add your marker to : ')
        while True:
            marker_position = six.moves.input()
            if not marker_position.isdigit():
                print('Position has to be a number. Enter a position between 0 to 8 : ')
                continue
            elif not int(marker_position) >= 0 and int(marker_position) <= 8:
                print('Position has to be in the range 0 to 8. Please enter a position between 0 to 8 : ')
                continue
            return int(marker_position)