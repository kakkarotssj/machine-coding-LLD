from ladder import Ladder


class LadderController:
    def __init__(self):
        self.start_to_ladder_mapping = {}

    def add_ladder(self, start, end):
        self.start_to_ladder_mapping[start] = Ladder(start, end)

    def get_ladder(self, start):
        return self.start_to_ladder_mapping.get(start)
