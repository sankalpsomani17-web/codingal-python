import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Sprites Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Define the Sprite class
class RectSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5

    def update(self, keys):
        # Movement controls for the player sprite
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

# Create sprite instances
player_sprite = RectSprite(BLUE, 50, 50, 100, 100)  # Controllable
static_sprite = RectSprite(RED, 50, 50, 400, 300)   # Stationary

# Group the sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player_sprite)
all_sprites.add(static_sprite)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys and update movement
    keys = pygame.key.get_pressed()
    player_sprite.update(keys)

    # Fill screen background
    screen.fill(WHITE)

    # Draw all sprites
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

pygame.quit()
