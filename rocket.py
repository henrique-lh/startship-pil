from ship import Spaceship


class Rocket(Spaceship):

    def __init__(self, x, y, width, height, speed, acceleration):
        super().__init__(x=x, y=y, width=width, height=height, speed=speed)
        self.acceleration = acceleration