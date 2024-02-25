import sys
from grid import *

def move_cursor_up(lines):
    sys.stdout.write(f'\033[{lines}A')  # Move cursor up by `lines` lines

def move_cursor_down(lines):
    sys.stdout.write(f'\033[{lines}B')  # Move cursor down by `lines` lines

def clear_current_line():
    sys.stdout.write('\033[K')  # Clear current line

class Printer:
    def __init__(self, grid):
        self.grid = grid

    def clearGrid(self):
        move_cursor_up(self.grid.height)
        for _ in range(self.grid.width):
            clear_current_line()

    def RewriteGrid(self):
        self.clearGrid()
        self.grid.PrintGrid()

    def PrintError(self, error):
        self.clearGrid()
        print(f'ERR: {error}')
        self.grid.PrintGrid()
