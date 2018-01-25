from human_player import HumanPlayer
from computer_player import ComputerPlayer

class Player(object):
    ''' Create a player with a given marker and player type (Human or Computer).'''
    def __init__(self):
        pass

    # need not pass self to a static method
    def create_player(player_str, player_marker, game_difficulty):
        if player_str == 'H':
            return HumanPlayer(player_marker)
        elif player_str == 'C':
            return ComputerPlayer(player_marker, game_difficulty)

    create_player = staticmethod(create_player)