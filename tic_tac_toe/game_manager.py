from game_board import GameBoard
from player import Player
from shape import Shape


class GameManager:
    def __init__(self, size=3):
        self.player1 = Player('player1', Shape.CROSS)
        self.player2 = Player('player2', Shape.CIRCLE)
        self.game_board = GameBoard(size)
        self.player_turn = self.player1

    def run(self):
        while True:
            if self.game_board.get_empty_cells_count() == 0:
                print(f'Draw! Nobody wins the game')
                break
            self.game_board.print_matrix()
            print(f'{self.player_turn.name} turn')
            cell_x, cell_y = map(int, input().split(' '))
            cell_x, cell_y = cell_x-1, cell_y-1
            if not self.game_board.validate_input(cell_x, cell_y):
                print('Invalid move')
                continue

            self.game_board.mark_cell(cell_x, cell_y, self.player_turn.shape.value)
            if self.game_board.check_win_condition(cell_x, cell_y):
                print(f'{self.player_turn.name} wins the game')
                break

            self.change_player_turn()

    def change_player_turn(self):
        if self.player_turn == self.player1:
            self.player_turn = self.player2
        else:
            self.player_turn = self.player1
