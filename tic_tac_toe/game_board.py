class GameBoard:
    def __init__(self, size):
        self.size = size
        self.matrix = [['-' for _ in range(size)] for _ in range(size)]
        self.empty_cells_count = 9

    def get_size(self):
        return self.size

    def get_empty_cells_count(self):
        return self.empty_cells_count

    def reduce_empty_cells_count(self):
        self.empty_cells_count -= 1

    def print_matrix(self):
        for row in range(self.size):
            for col in range(self.size):
                print(self.matrix[row][col], end=' ')
            print()

    def validate_input(self, cell_x, cell_y):
        if not 0 <= cell_x < self.get_size() or not 0 <= cell_y < self.get_size():
            return False

        return self.matrix[cell_x][cell_y] == '-'

    def mark_cell(self, cell_x, cell_y, shape):
        self.matrix[cell_x][cell_y] = shape
        self.reduce_empty_cells_count()

    def check_win_condition(self, cell_x, cell_y):
        if self.row_win_condition(cell_x, cell_y):
            return True
        if self.col_win_condition(cell_x, cell_y):
            return True
        if self.top_to_bottom_diagonal_win_condition(cell_x, cell_y):
            return True
        if self.bottom_to_top_diagonal_win_condition(cell_x, cell_y):
            return True

        return False

    def row_win_condition(self, cell_x, cell_y):
        shape = self.matrix[cell_x][cell_y]
        for col in range(self.get_size()):
            if shape != self.matrix[cell_x][col]:
                return False

        return True

    def col_win_condition(self, cell_x, cell_y):
        shape = self.matrix[cell_x][cell_y]
        for row in range(self.get_size()):
            if shape != self.matrix[row][cell_y]:
                return False

        return True

    def top_to_bottom_diagonal_win_condition(self, cell_x, cell_y):
        shape = self.matrix[cell_x][cell_y]
        for row_col in range(self.get_size()):
            if shape != self.matrix[row_col][row_col]:
                return False

        return True

    def bottom_to_top_diagonal_win_condition(self, cell_x, cell_y):
        shape = self.matrix[cell_x][cell_y]
        for row in range(self.get_size() - 1, -1, -1):
            if shape != self.matrix[row][self.get_size() - 1 - row]:
                return False

        return True
