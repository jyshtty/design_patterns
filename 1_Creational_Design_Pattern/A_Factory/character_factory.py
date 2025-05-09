from A_Factory.player.knight import Knight
from A_Factory.player.archer import Archer

class CharacterFactory:

    @staticmethod
    def create_player(player_type):
        if player_type == 'Knight':
            return Knight()

        if player_type == 'Archer':
            return Archer()
