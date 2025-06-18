import pygame
from dataclasses import dataclass


WIDTH, HEIGHT = 800, 600
SKY_COLOR = (0, 255, 255)
SUN_COLOR = (255, 200, 0)
SUN_POSITION = (WIDTH - 100, 100)
SUN_RADIUS = 150
GRASS_COLOR = (0, 128, 0)
GRASS_HEIGHT = 100
GRASS_TOP = HEIGHT - GRASS_HEIGHT
GRASS_RECTANGLE = (0, GRASS_TOP, WIDTH, GRASS_HEIGHT)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invasion")
clock = pygame.time.Clock()


@dataclass
class UFO:
    x: int
    y: int
    width: int = 100
    height: int = 30
    color: tuple = (128, 128, 128)
    speed: int = 1

    def draw(self):
        pygame.draw.ellipse(
            screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.ellipse(
            screen, self.color,
            (self.x + self.width//4, self.y-self.height//3, self.width//2, self.height))

    def move(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.x = -self.width


ufos = [
    UFO(x=0, y=50, speed=30),
    UFO(x=200, y=100, speed=20, width=80, color=(255, 255, 255)),
    UFO(x=400, y=150, color=(160, 160, 160), width=120, speed=40),
    UFO(x=600, y=200, speed=60, color=(32, 168, 219))]


def draw_scene():
    screen.fill(SKY_COLOR)
    pygame.draw.circle(screen, SUN_COLOR, SUN_POSITION, SUN_RADIUS)
    pygame.draw.rect(screen, GRASS_COLOR, GRASS_RECTANGLE)
    for ufo in ufos:
        ufo.draw()
        ufo.move()
    pygame.display.flip()
    clock.tick(60)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            raise SystemExit
    draw_scene()
