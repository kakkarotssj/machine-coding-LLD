"""
input :
1). integer (s) --> number of snakes
s lines with (head, tail)

2). integer(t) --> number of ladders
l lines with (start, end)

3). integer(p) --> number of players
p lines with (name)


9
62 5
33 6
49 9
88 16
41 20
56 53
98 64
93 73
95 75
8
2 37
27 46
10 32
51 68
61 79
65 84
71 91
81 100
2
Gaurav
Sagar



Output: <player-name> rolled a <dice-value> and moved from <initial-position> to <final-position>

When someone wins the game, print
<player-name> wins the game


Entities:
Snake:
head, tail --> integer

SnakeAggregatedData:
This entity will hold the map, key will be head and against this an object of snake

Ladder:
start, end --> integer

LadderAggregatedData:
This entity will hold the map, key will start and against this an object of ladder

Dice:
get_random_number() --> this will give me a random number between 1 and 6

Player:
name --> string
current_position --> integer
get_name() --> returns name
get_current_position() --> returns current position
move_current_position_by_dice(value) --> this will change the current position of the player
perform_snake_and_ladder_movements():
    while True loop
        if call_check_snake_position():
            move_current_position_by_snake_or_ladder()
        if call_check_ladder_position():
            move_current_position_by_snake_or_ladder()


class PlayerAggregatedData:
This entity will hold the map, name is key and against this a object of player

GameBoard:
matrix: {} 10 x 10
snakes_positions: snake_aggregated_data
ladder_positions: ladder_aggregated_data.py


GameManager:
Init phase:
1). Initiates ladder and snakes data
2). Initiates a gameboard
3). Initiates a dice
4). Initiates player aggregated data
5). make a queue to get which player has the current chance

6). call run method
"""

from game_manager import GameManager


def driver():
    snakes_count = int(input())
    snakes = []
    for count in range(snakes_count):
        head, tail = map(int, input().split(' '))
        snakes.append((head, tail))

    ladders_count = int(input())
    ladders = []
    for count in range(ladders_count):
        start, end = map(int, input().split(' '))
        ladders.append((start, end))

    players_count = int(input())
    players = []
    for count in range(players_count):
        players.append(input())

    game_manager = GameManager(snakes, ladders, players)
    game_manager.run()


driver()
