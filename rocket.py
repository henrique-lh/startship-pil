from ship import Spaceship, PINK_COLOR


class Rocket(Spaceship):

    def __init__(self, name, x, y, width, height, speed, acceleration=0.0, color=PINK_COLOR):
        super().__init__(name=name, x=x, y=y, width=width, height=height, speed=speed, color=color)
        self.acceleration = acceleration

    def draw(self, drawer):
        body_tl_x = self.x - self.width // 3
        body_tl_y = self.y - self.height // 2
        body_br_x = self.x + self.width // 3
        body_br_y = self.y + self.height // 2

        cone_p1 = (self.x, self.y - self.height * 0.7)
        cone_p2 = (body_tl_x, body_tl_y)
        cone_p3 = (body_br_x, body_br_y)

        win_radius = self.width // 4
        win_tl_x = self.x - win_radius
        win_tl_y = self.y - self.height * 0.2
        win_br_x = self.x + win_radius
        win_br_y = self.y

        drawer.polygon([cone_p1, cone_p2, cone_p3], fill='red')
        drawer.rectangle([(body_tl_x, body_tl_y), (body_br_x, body_br_y)], fill=(200, 200, 200))
        drawer.ellipse([(win_tl_x, win_tl_y), (win_br_x, win_br_y)], fill=(100, 200, 255))

    def update_outro(self):
        super().update_outro()
        self.speed += self.acceleration
