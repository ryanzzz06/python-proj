import random

def display_grid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)

def check_victory(grid, symbol):
    for row in grid:
        if row[0] == row[1] == row[2] == symbol:
            return True
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] == symbol:
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] == symbol:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == symbol:
        return True
    return False

def master_move(grid, symbol):
    opponent = 'X'
    for row in range(3):
        for col in range(3):
            if grid[row][col] == " ":
                grid[row][col] = symbol
                if check_victory(grid, symbol):
                    return row, col
                grid[row][col] = " "
    for row in range(3):
        for col in range(3):
            if grid[row][col] == " ":
                grid[row][col] = opponent
                if check_victory(grid, opponent):
                    grid[row][col] = symbol
                    return row, col
                grid[row][col] = " "
    for r in range(3):
        for c in range(3):
            if grid[r][c] == " ":
                return r, c

def player_turn(grid):
    while True:
        row, col = map(int, input("Player X, it's your turn where do you want to place your symbol? ").split())
        if grid[row][col] == " ":
            grid[row][col] = 'X'
            break
        else:
            print("Cell already occupied. Choose another one.")

def master_turn(grid):
    print("Game master's turn (O)...")
    row, col = master_move(grid, 'O')
    grid[row][col] = 'O'

def full_grid(grid):
    return all(cell != " " for row in grid for cell in row)

def check_result(grid):
    if check_victory(grid, 'X'):
        print("Player 'X' wins!")
        return True
    elif check_victory(grid, 'O'):
        print("Game Master 'O' wins!")
        return True
    elif full_grid(grid):
        print("It's a draw!")
        return True
    return False

def tictactoe_game():
    print("Welcome to Tic-Tac-Toe game against the master")
    print("To play, enter your move coordinates in the form row(space)column, e.g: 1 2")
    grid = [[" " for i in range(3)] for j in range(3)]
    display_grid(grid)
    while True:
        player_turn(grid)
        display_grid(grid)
        if check_result(grid):
            return True
        master_turn(grid)
        display_grid(grid)
        if check_result(grid):
            return False

tictactoe_game()