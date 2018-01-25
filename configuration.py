import six

class Configuration(object):
    def __init__(self, configparam=None):
        if configparam:
            # example config : ('H', 'C', "X", "O", 0, 0, 'HC')
            (self.p1_type, self.p2_type, self.p1_marker, self.p2_marker,
             self.game_difficulty, self.starting_player, self.game_type) = configparam
        else:
            self.p1_type = self.init_player_type(player_num=1)
            self.p2_type = self.init_player_type(player_num=2)
            self.p1_marker = self.init_player_marker(player_num=1)
            self.p2_marker = self.init_player_marker(player_num=2)
            self.game_difficulty = self.init_game_difficulty()
            self.starting_player = self.init_starting_player()
            self.game_type = self.init_game_type()

    def init_player_type(self, player_num):
        print('Enter the player type for Player{} (Enter H for Human or C for computer): '.format(player_num))
        type_player = six.moves.input()
        while True:
            if not type_player:
                print('The player field cannot be empty! Please enter a valid type : ')
                type_player = six.moves.input()
            elif type_player != 'H' and type_player != 'C':
                print('The player has to be of type H (human) or C (computer). Please enter a valid type (H or C) : ')
                type_player = six.moves.input()
            else:
                break
        return type_player

    def init_player_marker(self, player_num):
        if player_num == 1:
            print('Choose a marker for Player{} (Enter X or O): '.format(player_num))
            marker = six.moves.input()
            while True:
                if not marker:
                    print('The marker field cannot be empty! Please enter a valid marker : ')
                    marker = six.moves.input()
                elif marker != 'X' and marker != 'O':
                    print('The marker is not an X or an O. Please enter an X or an O : ')
                    marker = six.moves.input()
                else:
                    break
            return marker
        elif self.p1_marker == 'X':  # if player_1 has already choosen a marker
            print('Choosing a default marker O for Player{}'.format(player_num))
            return 'O'
        print('Choosing a default marker X for Player{}'.format(player_num))
        return 'X'

    def init_game_difficulty(self):
        if (self.p1_type == self.p2_type == 'C') or (self.p1_type != self.p2_type):  # wont work if both are human players
            print('Choose a difficulty level (0 for Easy, 1 for Medium, 2 for Impossible) : ')
            while True:
                game_difficulty = six.moves.input()
                if not game_difficulty.isdigit():
                    print('The number entered must be numeric. Please enter 0 for Easy, 1 for Medium, 2 for Impossible: ')
                elif not game_difficulty in ['0', '1', '2']:
                    print('The number entered must be one of 0, 1 or 2.')
                    print('Please enter 0 for Easy, 1 for Medium or 2 for Impossible difficulty: ')
                else:
                    return int(game_difficulty)
        return None

    def init_starting_player(self):
        print('Which player wants to start the game? (Enter 0 for Player1 or 1 for Player2) : ')
        while True:
            starting_player = six.moves.input()
            if not starting_player.isdigit():
                print('The number entered must be numeric. Please enter 0 for Player1 or 1 for Player2 : ')
            elif starting_player != '1' and starting_player != '0':
                print('The starting player has to be 0 or 1! Please enter 0 for Player1 or 1 for Player2 : ')
            else:
                return int(starting_player)


    def init_game_type(self):
        if self.p1_type == self.p2_type == 'H':
            game_type = 'HumanVHuman'   # human vs human
        elif self.p1_type == self.p2_type == 'C':
            game_type = 'ComputerVComputer'
        else:
            game_type = 'HumanVComputer'
        return game_type
