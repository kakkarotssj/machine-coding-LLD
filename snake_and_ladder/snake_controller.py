from snake import Snake


class SnakeController:
    def __init__(self):
        self.head_to_snake_mapping = {}

    def add_snake(self, head, tail):
        self.head_to_snake_mapping[head] = Snake(head, tail)

    def get_snake(self, head):
        return self.head_to_snake_mapping.get(head)
