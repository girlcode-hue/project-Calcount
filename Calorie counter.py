class weight():
    def __init__(self, weight):
        self.weight = weight


class Height():
    def __init__(self, height):
        self.height = height


class Calories():
    def __init__(self, calories):
        self.calories = calories

class about():
    def username(self, username: object) -> object:
        self.username = username
    def info(self):
        print("Hi,I'm, my weight is", weight.weight, "kg and I'm ", Height.height, "cm amd my total calorie for the day is",Calories.calories, "Kcal")


weight.weight(80)
Height.height(180)
Calories.calories(2400)
about.info()