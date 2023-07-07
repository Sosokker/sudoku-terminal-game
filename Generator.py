import random
from SudokuSolver import SudokuSolver

def generate_sudoku():
    puzzle = [[0] * 9 for _ in range(9)]

    SudokuSolver.solve(puzzle)

    remove_numbers(puzzle)

    return puzzle

def remove_numbers(grid):
    num_holes = random.randint(40, 55)
    for _ in range(num_holes):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if grid[row][col] != 0:
            grid[row][col] = 0

def display_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(grid[i][j])
            else:
                print(grid[i][j], end=" ")
                
print(generate_sudoku())