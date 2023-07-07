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
    
    @staticmethod
    def is_valid_solution(grid):
    # Check if each row, column, and 3x3 box contains all numbers from 1 to 9
        for i in range(9):
            row_nums = set(grid[i])
            col_nums = set(grid[j][i] for j in range(9))
            box_nums = set(grid[i//3*3+j//3][i%3*3+j%3] for j in range(9))
            if row_nums != set(range(1, 10)) or col_nums != set(range(1, 10)) or box_nums != set(range(1, 10)):
                return False
        return True