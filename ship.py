PINK_COLOR = (246, 71, 255)


class Spaceship:

    def __init__(self, name, x, y, width, height, speed, color=PINK_COLOR):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color

        self.idle_direction = 1
        self.idle_factor = 0.5
        self.idle_range = 7

    def draw(self, drawer):
        top_left_x = self.x - self.width // 2
        top_left_y = self.y - self.height // 2

        bottom_right_x = self.x + self.width // 2
        bottom_right_y = self.y + self.height // 2
        drawer.rectangle(
            (top_left_x, top_left_y, bottom_right_x, bottom_right_y),
            fill=self.color
        )

    @staticmethod
    def idle_target(bounds):
        return bounds[0] // 2, bounds[1] // 2

    def idle_animation(self, bounds):
        self.y += (self.speed * self.idle_factor) * self.idle_direction

        if abs(self.y - self.idle_target(bounds)[1]) > self.idle_range:
            self.idle_direction = -self.idle_direction

    def update_intro(self, bounds):
        target_y = bounds[1] // 2

        if self.y > target_y:
            self.y -= self.speed

    def update_outro(self):
        if self.y + self.height // 2 > 0:
            self.y -= self.speed