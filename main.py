import os

from PIL import Image, ImageDraw

from ship import Spaceship
from star import Star

BLACK = (0, 0, 0)
WIDTH = 1280
HEIGHT = 1280
NUM_STARS = 50
MAX_FRAMES = 300

def save_gif(frames_dir, output_dir, gif_name, fps=30, exclude=False):

    file_list = sorted(
        [f for f in os.listdir(frames_dir) if f.endswith(('.png', '.jpg'))],
        key=lambda f: int(f.split('.')[0])
    )
    frames = [Image.open(os.path.join(frames_dir, name)) for name in file_list]
    frames[0].save(
        os.path.join(output_dir, gif_name),
        save_all=True,
        append_images=frames[1:],
        duration=1/fps,
        loop=0,
    )
    if exclude:
        for filename in file_list:
            os.remove(os.path.join(frames_dir, filename))


def is_visible(ship):
    left = ship.x - ship.width // 2
    right = ship.x + ship.width // 2
    top = ship.y - ship.height // 2
    bottom = ship.y + ship.height // 2

    horizontal = right > 0 and left < WIDTH
    vertical = bottom > 0 and top < HEIGHT

    return horizontal and vertical

def generate_animation(ship, stars, idle_duration_frames=90):
    frames = []

    animation = 'intro'
    n_idle_frames = 0

    while animation != 'done' and len(frames) < MAX_FRAMES:

        img = Image.new("RGB", (WIDTH, HEIGHT), BLACK)
        drawer = ImageDraw.Draw(img)

        for star in stars:
            star.draw(drawer)
            star.move(bound_x=WIDTH, bound_y=HEIGHT)

        if animation == 'intro':
            ship.update_intro(bounds=(WIDTH, HEIGHT))
            if ship.y - ship.idle_target(bounds=(WIDTH, HEIGHT))[1] < ship.idle_range:
                animation = 'idle'
        elif animation == 'idle':
            ship.idle_animation(bounds=(WIDTH, HEIGHT))
            n_idle_frames += 1
            if n_idle_frames >= idle_duration_frames:
                animation = 'outro'
        elif animation == 'outro':
            ship.update_outro()
            if not is_visible(ship):
                animation = 'done'

        ship.draw(drawer)
        ship.idle_animation(bounds=(WIDTH, HEIGHT))

        frames.append(img)
    return frames


def main(OUTPUT_DIR):

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR, exist_ok=True)

    stars = [Star.create_random_star(x_max=WIDTH, y_max=HEIGHT, color="white") for _ in range(NUM_STARS)]
    ship = Spaceship(WIDTH//2, HEIGHT, 40, 60, 7)

    frames = generate_animation(ship, stars)

    [img.save(os.path.join(OUTPUT_DIR, f"{idx}.png")) for idx, img in enumerate(frames)]

    save_gif(OUTPUT_DIR, "runs/gifs", "universe_with_ship.gif", exclude=True)


if __name__ == "__main__":
    main("runs/frames")