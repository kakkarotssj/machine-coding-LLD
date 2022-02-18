"""
Player
name | string --> done
shape | Shape --> done
get_name() --> returns string --> done
make_turn(board) --> returns none

Shape(Enum) --> done
CROSS = 'X'
CIRCLE = 'O'

GameBoard:
size | integer | default value 3
matrix of sizeXsize
validate_input(cell) --> returns true/false
mark_cell(shape) -> returns none
check_win_condition(cell) --> returns true/false

GameManager:
board | GameBoard
player1 and player2
give CROSS to player1 and CIRCLE to player2
player_turn | 1 indicates player 1 and  2 indicates player 2
run()
"""


from game_manager import GameManager


def driver():
    game_manager = GameManager(size=3)
    game_manager.run()


driver()
