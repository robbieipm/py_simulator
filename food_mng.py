from food import *

class FoodMng:

    def __init__(self):
        self.food = []

    def Add(self, position):
        self.food.append(Food(position))

    def FoodPositions(self):
        return self.food
