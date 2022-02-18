import queue

from dice import Dice
from gameboard import GameBoard
from player_controller import PlayerController


class GameManager:
    def __init__(self, snakes_positions, ladders_positions, players):
        self.game_board = GameBoard(snakes_positions, ladders_positions)
        self.player_controller = PlayerController()
        self.player_turns = queue.Queue()
        self.dice = Dice()
        for player in players:
            self.player_controller.add_player(player)
            self.player_turns.put(self.player_controller.name_to_player_mapping[player])

    def run(self):
        while True:
            player = self.get_player_turn()
            player.move_current_position_by_dice(self.dice, self.game_board)
            if self.player_won(player):
                print(f'{player.get_name()} wins the game.')
                break
            self.add_player_to_end(player)

    def get_player_turn(self):
        player = self.player_turns.get()
        return player

    def player_won(self, player):
        return player.get_current_position() == self.game_board.board_size

    def add_player_to_end(self, player):
        self.player_turns.put(player)
