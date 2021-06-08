import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# pygame-ді инициализациялау және терезені құру
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame Template")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

# Game loop
flRunning = True
while flRunning:
    clock.tick(FPS)
    
    # Process inputs(events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flRunning = False
            pygame.quit()
    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    # draw -дан кейін
    pygame.display.update()