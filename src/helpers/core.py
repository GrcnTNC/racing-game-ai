class Car:
    # Car class is representing common values of all cars in the game
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # width is originating from car image width
        self.width = 40
        # height is originating from car image width
        self.height = 80


class MyCar(Car):
    # MyCar class specifies distinct features of player's car
    # move method allows to move the car to the left or right
    def move(self, direction):
        # 40 is the distance form the left wall to the center of the 1st road line
        if direction == "left" and self.x > 40:
            # 80 is the distance between the road lines
            self.x = self.x - 80
        elif direction == "right" and self.x < width - 40:
            self.x = self.x + 80


class EnemyCar(Car):
    # active bool will help to remove the car from the state
    self.active = True

    # move method descends a car by its height ( 80px )
    def move(self):
        self.y = self.y + self.height

    # deactivate method changes car's state to be removed later
    def deactivate(self):
        self.active = False
