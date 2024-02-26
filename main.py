from turn_logic import *
# import time

# creatures[0].FindClosestInList(foods)
# foodCount = creatures[0].foodCount
# while grid.MoveCreature(creatures[0]) or creatures[0].Position() != creatures[0].home:
#     if creatures[0].foodCount > foodCount:
#         foodCount = creatures[0].foodCount
#         pop_elements_conditionally(foods, x: x.Position() == creatures[0].Position())
#     creatures[0].FindClosestInList(foods)
#     print(f"position: {creatures[0].Position()} home: {creatures[0].home} path: {creatures[0].path}")
#     time.sleep(0.5)
#     #move_cursor_up(GRID_HEIGHT)
#     #for _ in range(GRID_WIDTH):
#     #    clear_current_line()
#     grid.PrintGrid()

# input("\nPress any key to end")




# app definitions
GRID_HEIGHT = 10
GRID_WIDTH = 10
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

