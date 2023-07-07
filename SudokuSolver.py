class SudokuSolver:
    @staticmethod
    def solve(puzzle):
        row, col = SudokuSolver.find_empty_cell(puzzle)
        if row == -1 and col == -1:
            return True

        for num in range(1, 10):
            if SudokuSolver.is_valid_number(puzzle, row, col, num):
                puzzle[row][col] = num

                if SudokuSolver.solve(puzzle):
                    return True

                puzzle[row][col] = 0

        return False

    @staticmethod
    def find_empty_cell(grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return i, j
        return -1, -1

    @staticmethod
    def is_valid_number(grid, row, col, num):
        for i in range(9):
            if grid[row][i] == num:
                return False

        for i in range(9):
            if grid[i][col] == num:
                return False

        box_row = row - row % 3
        box_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[box_row + i][box_col + j] == num:
                    return False

        return True