import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (135, 206, 235)
PLAYER_COLOR = (255, 0, 0)
PLATFORM_COLOR = (0, 0, 0)

# Player settings
player_width, player_height = 50, 50
player_x, player_y = 50, HEIGHT - player_height
player_speed = 5
jump_height = 10
gravity = 1
is_jumping = False
jump_count = 0

# Platform settings
platform_width, platform_height = 100, 20
platforms = [(100, HEIGHT - 100), (300, HEIGHT - 200), (500, HEIGHT - 300)]

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Scrolling Platformer")

# Game loop
clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, PLAYER_COLOR, (x, y, player_width, player_height))

def draw_platforms(platform_list):
    for platform in platform_list:
        pygame.draw.rect(screen, PLATFORM_COLOR, (platform[0], platform[1], platform_width, platform_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Apply gravity
    if not is_jumping:
        player_y += gravity
    else:
        player_y -= jump_count
        jump_count -= 1

    # Jumping logic
    if not is_jumping:
        if keys[pygame.K_SPACE]:
            is_jumping = True
            jump_count = jump_height

    # Update game logic here

    # Keep player within the screen bounds
    player_x = max(0, min(player_x, WIDTH - player_width))
    player_y = max(0, min(player_y, HEIGHT - player_height))

    # Scroll the screen when player reaches the right edge
    if player_x > WIDTH - player_width:
        for i in range(len(platforms)):
            platforms[i] = (platforms[i][0] - player_speed, platforms[i][1])

    # Clear the screen
    screen.fill(BACKGROUND_COLOR)

    # Draw platforms
    draw_platforms(platforms)

    # Draw player
    draw_player(player_x, player_y)

    # Check for collisions with platforms
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for platform in platforms:
        platform_rect = pygame.Rect(platform[0], platform[1], platform_width, platform_height)
        if player_rect.colliderect(platform_rect):
            if gravity > 0:
                player_y = platform_rect.top - player_height
                is_jumping = False
            else:
                player_y = platform_rect.bottom
                jump_count = 0

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)
