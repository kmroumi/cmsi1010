import math
import random
import pygame
from dataclasses import dataclass

WIDTH, HEIGHT = 1024, 600
GRASS_HEIGHT = 100
GROUND_LEVEL = HEIGHT - GRASS_HEIGHT // 2
TREE_SPACING = 173
MAX_SPEED = 23
MIN_SPEED = 5
PITCH_LIMIT = 0.3
CRASH_ANGLE_THRESHOLD = 0.26
CRASH_SPEED_THRESHOLD = 13
CRUISING_ALTITUDE = 50

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plane Simulator - No Windows")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
big_font = pygame.font.SysFont(None, 100)
small_font = pygame.font.SysFont(None, 40)

SKY_TOP = (135, 206, 235)
SKY_BOTTOM = (176, 226, 255)
GRASS_COLOR = (124, 252, 0)
RUNWAY_RECT = pygame.Rect(WIDTH // 2 - 200, GROUND_LEVEL - 10, 400, 20)


@dataclass
class Cloud:
    x: int
    y: int
    size: int

    def move(self):
        self.x -= 1
        if self.x < -self.size * 2:
            self.x = WIDTH + random.randint(50, 200)
            self.y = random.randint(40, 180)

    def draw(self):
        for offset in [(-20, 0), (0, -10), (20, 0)]:
            pygame.draw.ellipse(screen, (255, 255, 255),
                                (self.x + offset[0], self.y + offset[1],
                                 self.size, self.size // 2))


@dataclass
class Plane:
    x: int
    y: int
    speed: float = 15
    rotation: float = 0
    state: str = "flying"
    color: tuple = (80, 80, 200)

    def draw(self):
        body = [(-24, 0), (-10, 8), (20, 4), (28, 0), (20, -4), (-10, -8)]
        tail = [(-20, 0), (-30, 8), (-26, 0), (-30, -8)]
        wing = [(-2, -2), (12, -2), (5, -16)]

        def rotate(shape):
            return [(x * math.cos(self.rotation) - y * math.sin(self.rotation),
                     x * math.sin(self.rotation) + y * math.cos(self.rotation)) for x, y in shape]

        def offset(coords):
            return [(WIDTH // 2 + 4 * x, self.y - 4 * y) for x, y in coords]

        pygame.draw.polygon(screen, self.color, offset(rotate(body)))
        pygame.draw.polygon(screen, (160, 160, 255), offset(rotate(tail)))
        pygame.draw.polygon(screen, (160, 160, 255), offset(rotate(wing)))

    def move(self):
        if self.state == "flying":
            self.x += self.speed
            self.y -= math.sin(self.rotation) * self.speed * 0.5
            if self.y >= GROUND_LEVEL:
                self.y = GROUND_LEVEL
                too_fast = self.speed > CRASH_SPEED_THRESHOLD
                bad_angle = abs(self.rotation) > CRASH_ANGLE_THRESHOLD
                off_runway = not (RUNWAY_RECT.left <= WIDTH //
                                  2 <= RUNWAY_RECT.right)

                if too_fast or bad_angle or off_runway:
                    self.state = "crashed"
                    self.color = (255, 0, 0)
                else:
                    self.state = "landed"
                    self.speed = 0


plane = Plane(x=0, y=CRUISING_ALTITUDE)
clouds = [Cloud(x, random.randint(40, 180), random.randint(60, 100))
          for x in range(0, WIDTH, 250)]


def draw_background():
    for i in range(HEIGHT - GRASS_HEIGHT):
        color = [SKY_TOP[j] + (SKY_BOTTOM[j] - SKY_TOP[j])
                 * i // (HEIGHT - GRASS_HEIGHT) for j in range(3)]
        pygame.draw.line(screen, color, (0, i), (WIDTH, i))
    for cloud in clouds:
        cloud.move()
        cloud.draw()
    pygame.draw.rect(screen, GRASS_COLOR, (0, HEIGHT -
                     GRASS_HEIGHT, WIDTH, GRASS_HEIGHT))
    pygame.draw.rect(screen, (60, 60, 60), RUNWAY_RECT)


def draw_scene():
    draw_background()
    x = -plane.x
    while x < WIDTH:
        pygame.draw.rect(screen, (139, 69, 19),
                         (x - 5, GROUND_LEVEL - 20, 10, 20))
        pygame.draw.polygon(screen, (0, 128, 0), [(
            x - 30, GROUND_LEVEL - 20), (x + 30, GROUND_LEVEL - 20), (x, GROUND_LEVEL - 100)])
        x += TREE_SPACING

    plane.draw()
    screen.blit(font.render(
        f"Speed: {round(plane.speed, 1)}", True, (0, 0, 0)), (10, 10))
    screen.blit(font.render(
        f"Pitch: {round(math.degrees(plane.rotation), 1)}°", True, (0, 0, 0)), (10, 45))

    if plane.state == "crashed":
        game_over = big_font.render("GAME OVER", True, (255, 0, 0))
        restart_msg = small_font.render(
            "Press R to restart", True, (255, 100, 100))
        screen.blit(
            game_over, (WIDTH//2 - game_over.get_width()//2, HEIGHT//2 - 60))
        screen.blit(restart_msg, (WIDTH//2 -
                    restart_msg.get_width()//2, HEIGHT//2 + 20))

    pygame.display.flip()
    clock.tick(60)


while True:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and plane.state in ["crashed", "landed"]:
                plane = Plane(x=0, y=CRUISING_ALTITUDE)

    if keys[pygame.K_RIGHT]:
        plane.speed = min(plane.speed + 0.1, MAX_SPEED)
    if keys[pygame.K_LEFT]:
        plane.speed = max(plane.speed - 0.1, MIN_SPEED)

    if keys[pygame.K_UP]:
        plane.rotation = min(plane.rotation + 0.01, PITCH_LIMIT)
    if keys[pygame.K_DOWN]:
        plane.rotation = max(plane.rotation - 0.01, -PITCH_LIMIT)

    if plane.state == "flying":
        plane.move()

    draw_scene()
