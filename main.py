from SudokuSolver import SudokuSolver
from rich.console import Console
import time

def create_sudoku_table():
    table = [[0] * 9 for _ in range(9)]
    console = Console()

    console.print("[bold green]Enter the Sudoku table row by row:[/bold green]")
    console.print("[bold green]For blank slot, [bold yellow]Type 0 or Press Enter[/bold yellow][/bold green]")
    for i in range(9):
        console.print(f"\n[bold yellow]Enter row {i+1}:[/bold yellow]")
        for j in range(9):
            while True:
                value = console.input(f"Enter value for column {j+1}: ")
                if value == "":
                    value = 0
                if int(value) != 0:
                    if not value.isdigit() or int(value) < 0 or int(value) > 9:
                        console.print("[bold red]Invalid input. Please enter a number between 1 and 9.[/bold red]")
                        continue
                    if (not check_sudoku_rule(table, i, j, int(value))):
                        console.print("[bold red]Sudoku rule violation. Please enter a valid number.[/bold red]")
                        continue
                table[i][j] = int(value)
                print_sudoku_table(table, console)
                break

    return table

def print_sudoku_table(table, console, clear=True):
    if clear:
        console.clear()
        console.print("[bold cyan]Sudoku Table:[/bold cyan]")
        for row in table:
            console.print(" | ".join(str(cell) for cell in row))
    else:
        console.print("[bold green]Sudoku Table:[/bold green]")
        for row in table:
            console.print(" | ".join(str(cell) for cell in row))

def check_sudoku_rule(table, row, col, value):
    for i in range(9):
        if table[row][i] == value or table[i][col] == value:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if table[i][j] == value:
                return False

    return True

sudoku_table = create_sudoku_table()

try:
    console = Console()
    console.print("\n[bold yellow]Solving Sudoku...[/bold yellow]")
    start = time.process_time()
    solved_puzzle = SudokuSolver.solve(sudoku_table)
    in_time = time.process_time() - start
    console.print(f"\n[bold green]Finish! in {in_time} [/bold green]")
    print_sudoku_table(solved_puzzle, console, clear=False)
except Exception:
    console.print("\n[bold red]Failed to solve![/bold red]")
