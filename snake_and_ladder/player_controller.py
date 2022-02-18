from player import Player


class PlayerController:
    def __init__(self):
        self.name_to_player_mapping = {}

    def add_player(self, name):
        self.name_to_player_mapping[name] = Player(name)

    def get_player(self, name):
        return self.name_to_player_mapping.get(name)
