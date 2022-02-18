from ladder_controller import LadderController
from snake_controller import SnakeController


class GameBoard:
    def __init__(self, snakes, ladders, board_size=10):
        self.board_size = board_size*board_size
        self.snake_controller = SnakeController()
        self.ladder_controller = LadderController()
        for head, tail in snakes:
            self.snake_controller.add_snake(head, tail)
        for start, end in ladders:
            self.ladder_controller.add_ladder(start, end)

    def add_snake(self, head, tail):
        self.snake_controller.add_snake(head, tail)

    def get_snake_for_position(self, position):
        return self.snake_controller.head_to_snake_mapping.get(position)

    def add_ladder(self, start, end):
        self.ladder_controller.add_ladder(start, end)

    def get_ladder_for_position(self, position):
        return self.ladder_controller.start_to_ladder_mapping.get(position)
