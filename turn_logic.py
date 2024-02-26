from grid import *
from creature_mng import *
from food_mng import *
from terminal_printer import *
import time

MOVEMENT_PAUSE = 0.3
FOOD_MULTIPLIER_SPAWN = 3

class TurnLogic:

    def __init__(self, grid, foodMng, creatureMng, printer):
        # definitions
        self.CREATURE_INIT_SPAWN = 8
        # initializing
        self.grid = grid
        self.creatureMng = creatureMng
        self.foodMng = foodMng
        self.printer = printer
        self.grid.PrintGrid()
        self.Init()
        self.printer.RewriteGrid()

    def Init(self):
        for _ in range(self.CREATURE_INIT_SPAWN):
            self.SpawnCreature()
        for _ in range(self.CREATURE_INIT_SPAWN):
            emptyTile = self.grid.GetEmptyTile()
            if emptyTile.Type() == Tile.INVALID_TYPE:
                self.printer.PrintError("was unable to spawn creature")
            emptyTile.ChangeType(Tile.CREATURE_TYPE)
            self.creatureMng.Add(emptyTile.Position())

        self.printer.RewriteGrid()
        # TODO: record turn 0

    def SpawnCreature(self, sourceSpawnPositions = []):
        if len(sourceSpawnPositions) == 0:
            emptyTile = self.grid.GetEmptyTile()
            if emptyTile.Type() == Tile.INVALID_TYPE:
                self.printer.PrintError("was unable to spawn creature")
            emptyTile.ChangeType(Tile.CREATURE_TYPE)
            self.creatureMng.Add(emptyTile.Position())
            return
        for spawnSourcePos in sourceSpawnPositions:
            emptyTile = self.grid.GetEmptyTileAround(spawnSourcePos)
            if emptyTile.Type() == Tile.INVALID_TYPE:
                continue
            emptyTile.ChangeType(Tile.CREATURE_TYPE)
            self.creatureMng.Add(emptyTile.Position())

    def SpawnFood(self, creatureAmount):
        for _ in range(creatureAmount * FOOD_MULTIPLIER_SPAWN):
            emptyTile = self.grid.GetEmptyTile()
            if emptyTile.Type() == Tile.INVALID_TYPE:
                self.printer.PrintError("was unable to spawn food")
            emptyTile.ChangeType(Tile.FOOD_TYPE)
            self.foodMng.Add(emptyTile.Position())

    def Start(self, turnNumber):
        self.SpawnFood(self.creatureMng.Size())
        self.movementStage()
        self.grid.ResetTiles(self.foodMng.FoodPositions())
        self.foodMng.Reset()
        creatureResult = self.creatureMng.EndTurnResult()
        self.grid.ResetTiles(creatureResult[0])
        self.SpawnCreature(creatureResult[1])
        # spawn born creatures
        time.sleep(1)
        self.printer.RewriteGrid()

    def movementStage(self):
        self.creatureMng.PrepareToMove(self.foodMng.FoodPositions())
        while self.creatureMng.AreCreaturesStillMoving():
            navigationPossibilities = self.creatureMng.GetOptionalMovements()
            movementsMade = self.grid.ExecuteMovements(navigationPossibilities)
            consumedFood = self.creatureMng.MoveCreatures(movementsMade)
            self.foodMng.Consume(consumedFood)
            time.sleep(MOVEMENT_PAUSE)
            self.printer.RewriteGrid()
            self.creatureMng.UpdatePaths(self.foodMng.FoodPositions())