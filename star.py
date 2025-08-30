import random

STAR_SIZE = (1, 2, 3) # Turn into enum
START_SPEED = (1, 2, 3) # Turn into enum

class Star:

    def __init__(self, center, size, speed, color):
        self.x = center[0]
        self.y = center[1]
        self.size = size
        self.speed = speed
        self.color = color

    @staticmethod
    def create_random_star(x_max, y_max, color):
        x = random.randint(0, x_max)
        y = random.randint(0, y_max)
        size = random.choice(STAR_SIZE)
        speed = random.choice(START_SPEED)
        return Star((x, y), size, speed, color)

    def draw(self, drawer):
        drawer.circle(
            (self.x, self.y),
            self.size,
            self.color,
        )

    def move(self, bound_x, bound_y):
        self.y += self.speed
        if self.y > bound_y:
            self.y = 0
            self.x = random.randint(0, bound_x)