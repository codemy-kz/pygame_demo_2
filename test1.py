import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
    
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

# pygame-ді инициализациялау және терезені құру
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyGame Template")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

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