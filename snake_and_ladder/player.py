class Player:
    def __init__(self, name):
        self.name = name
        self.current_position = 0

    def get_name(self):
        return self.name

    def get_current_position(self):
        return self.current_position

    def set_current_position(self, position):
        self.current_position = position

    def move_current_position_by_dice(self, dice, board):
        dice_value = dice.roll_dice()
        if dice_value+self.get_current_position() > board.board_size:
            return
        initial_pos = self.get_current_position()
        self.set_current_position(self.get_current_position()+dice_value)
        self.perform_snake_and_ladder_movements(board)
        print(f'{self.get_name()} rolled a {dice_value} and moved from {initial_pos} to {self.get_current_position()}')

    def perform_snake_and_ladder_movements(self, board):
        while True:
            is_moved = False
            snake = board.get_snake_for_position(self.get_current_position())
            if snake:
                tail_position = snake.get_tail()
                self.set_current_position(tail_position)
                is_moved = True
                pass

            ladder = board.get_ladder_for_position(self.get_current_position())
            if ladder:
                end_position = ladder.get_end()
                self.set_current_position(end_position)
                is_moved = True
                pass

            if not is_moved:
                break
