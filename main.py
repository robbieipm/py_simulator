from turn_logic import *

# app definitions
GRID_HEIGHT = 30
GRID_WIDTH = 30
FOOD_SPAWN = 3
MAX_TURN = 10

# app objects
creatureMng = CreatureMng()
foodMng = FoodMng()
grid = Grid(GRID_HEIGHT, GRID_WIDTH)
printer = Printer(grid)
turnProcessor = TurnLogic(grid, foodMng, creatureMng, printer)

# start simulator
for i in range(MAX_TURN):
    turnProcessor.Start(i)

