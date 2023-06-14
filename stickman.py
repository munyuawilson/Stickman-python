import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Stickman Game")

# Load the background image
background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

# Set up the stickman
stickman_img = pygame.image.load("stickman.png")
stickman_width = 50
stickman_height = 60
stickman_img = pygame.transform.scale(stickman_img, (stickman_width, stickman_height))
stickman_x = screen_width // 2 - stickman_width // 2
stickman_y = screen_height - stickman_height - 10
stickman_speed = 5

# Set up the obstacle
obstacle_img = pygame.image.load("obstacle.png")
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = random.randint(screen_height // 2, screen_height - obstacle_height)
obstacle_speed = 3

obstacle_img = pygame.transform.scale(obstacle_img, (obstacle_width, obstacle_height))

# Set up the font for failure message, restart button, and score counter
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

running = True
game_over = False
restart = False
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and game_over and restart:
            # Restart the game
            game_over = False
            restart = False
            score = 0
            obstacle_x = random.randint(0, screen_width - obstacle_width)
            obstacle_y = random.randint(screen_height // 2, screen_height - obstacle_height)

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            stickman_x -= stickman_speed
            # Check if the stickman goes out of the window
            if stickman_x < 0:
                stickman_x = 0
        if keys[pygame.K_RIGHT]:
            stickman_x += stickman_speed
            # Check if the stickman goes out of the window
            if stickman_x > screen_width - stickman_width:
                stickman_x = screen_width - stickman_width
        if keys[pygame.K_UP]:
            stickman_y -= stickman_speed
            # Check if the stickman goes out of the window
            if stickman_y < 0:
                stickman_y = 0
        if keys[pygame.K_DOWN]:
            stickman_y += stickman_speed
            # Check if the stickman goes out of the window
            if stickman_y > screen_height - stickman_height:
                stickman_y = screen_height - stickman_height

        # Update obstacle position
        obstacle_x -= obstacle_speed

        # Check for collision
        if (
            stickman_x < obstacle_x + obstacle_width
            and stickman_x + stickman_width > obstacle_x
            and stickman_y < obstacle_y + obstacle_height
            and stickman_y + stickman_height > obstacle_y
        ):
            game_over = True
            restart = True

        # Generate new obstacle when the current obstacle goes off-screen
        if obstacle_x + obstacle_width < 0:
            obstacle_x = screen_width
            obstacle_y = random.randint(screen_height // 2, screen_height - obstacle_height)
            score += 1

    # Clear the screen
    screen.blit(background_img, (0, 0))

    if not game_over:
        # Draw stickman
        screen.blit(stickman_img, (stickman_x, stickman_y))
        # Draw obstacle
        screen.blit(obstacle_img, (obstacle_x, obstacle_y))
    else:
        # Display failure message
        text = font.render("You failed!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

        # Display restart button
        restart_text = font.render("Click to Restart", True, (0, 255, 0))
        restart_text_rect = restart_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(restart_text, restart_text_rect)

    # Display score counter
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect(topright=(screen_width - 10, 10))
    screen.blit(score_text, score_rect)

    pygame.display.flip()
    clock.tick(60)

# Clean up and exit
pygame.quit()
