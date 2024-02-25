from grid import *
import sys
import time

def move_cursor_up(lines):
    sys.stdout.write(f'\033[{lines}A')  # Move cursor up by `lines` lines

def move_cursor_down(lines):
    sys.stdout.write(f'\033[{lines}B')  # Move cursor down by `lines` lines

def clear_current_line():
    sys.stdout.write('\033[K')  # Clear current line

def pop_elements_conditionally(lst, condition):
    for i in range(len(lst)):  # Iterate over the list in reverse order
        if condition(lst[i]):  # Check if the condition is True for the element
            lst.pop(i)  # If True, pop the element from the list

#create simulation grid
gridHeight = 10
gridWidth = 10
creatures = []
foods = []
grid = Grid(gridHeight, gridWidth)
grid.PrintGrid()
FOOD_SPAWN = 3

# spawn creatures and food
spawnedCreature = grid.Spawn(Tile.CREATURE_TYPE)
if spawnedCreature == None:
    print("ERROR: failed to spawn creature!")
creatures.append(spawnedCreature)

for _ in range(FOOD_SPAWN):
    spawnedFood = grid.Spawn(Tile.FOOD_TYPE)
    if spawnedFood == None:
        print("ERROR: failed to spawn food!")
    foods.append(spawnedFood)

move_cursor_up(gridHeight)
for _ in range(gridWidth):
    clear_current_line()
grid.PrintGrid()

creatures[0].FindClosestInList(foods)
foodCount = creatures[0].foodCount
while grid.MoveCreature(creatures[0]) or creatures[0].Position() != creatures[0].home:
    if creatures[0].foodCount > foodCount:
        foodCount = creatures[0].foodCount
        pop_elements_conditionally(foods, x: x.Position() == creatures[0].Position())
    creatures[0].FindClosestInList(foods)
    print(f"position: {creatures[0].Position()} home: {creatures[0].home} path: {creatures[0].path}")
    time.sleep(0.5)
    #move_cursor_up(gridHeight)
    #for _ in range(gridWidth):
    #    clear_current_line()
    grid.PrintGrid()

input("\nPress any key to end")
