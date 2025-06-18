import pygame

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


def draw_scene():
    screen.fill(SKY_COLOR)
    pygame.draw.circle(screen, SUN_COLOR, SUN_POSITION, SUN_RADIUS)
    pygame.draw.rect(screen, GRASS_COLOR, GRASS_RECTANGLE)
    pygame.display.flip()


draw_scene()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            raise SystemExit
