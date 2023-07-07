import sys
import pytest
sys.path.append('..')

from SudokuSolver import SudokuSolver
from Generator import generate_sudoku

@pytest.mark.parametrize("test_num", range(20))
def test_generate_sudoku(test_num):
    # Test if generate_sudoku generates a valid Sudoku puzzle.
    puzzle = generate_sudoku()
    assert SudokuSolver.solve(puzzle)
    assert SudokuSolver.is_valid_solution(puzzle)

