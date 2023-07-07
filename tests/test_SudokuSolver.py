import sys
sys.path.append('..')

from SudokuSolver import SudokuSolver

def test_solve_sudoku():
    # Test a valid Sudoku grid
    grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    assert SudokuSolver.solve(grid)
    assert is_valid_solution(grid)

    # Test an invalid Sudoku grid
    grid = [
        [6, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 0, 9]
    ]
    assert not SudokuSolver.solve(grid)

def is_valid_solution(grid):
    # Check if each row, column, and 3x3 box contains all numbers from 1 to 9
    for i in range(9):
        row_nums = set(grid[i])
        col_nums = set(grid[j][i] for j in range(9))
        box_nums = set(grid[i//3*3+j//3][i%3*3+j%3] for j in range(9))
        if row_nums != set(range(1, 10)) or col_nums != set(range(1, 10)) or box_nums != set(range(1, 10)):
            return False
    return True

