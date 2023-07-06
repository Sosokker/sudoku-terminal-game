from rich.console import Console

def create_sudoku_table():
    table = []
    console = Console()

    console.print("[bold green]Enter the Sudoku table row by row:[/bold green]")
    for i in range(9):
        row = []
        console.print(f"\n[bold yellow]Enter row {i+1}:[/bold yellow]")
        for j in range(9):
            value = console.input(f"Enter value for column {j+1}: ")
            row.append(value)
        table.append(row)

    return table

sudoku_table = create_sudoku_table()

console = Console()
console.print("\n[bold cyan]Sudoku Table:[/bold cyan]")
for row in sudoku_table:
    console.print(" | ".join(row))
