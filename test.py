import pygame
import random
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the game window
# ... (existing code)
# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Stickman Game")

# Load the background image
background_img = pygame.image.load("background.jpg")
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))
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

x_range = int(screen_width * 0.4)
min_x = int(screen_width * 0.3)  # Adjust the percentage as needed
max_x = int(screen_width * 0.7)  # Adjust the percentage as needed



obstacle_x = random.randint(min_x, max_x)
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

# Set up the Q-table
num_states = 4  # Number of possible states
num_actions = 4  # Number of possible actions
q_table = np.random.rand(num_states, num_actions)

# Define the rewards and learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 1  # Exploration rate
epsilon_decay = 0.99
# Define the states and actions
states = {
    "LEFT": 0,
    "RIGHT": 1,
    "UP": 2,
    "DOWN": 3
}

actions = [
    pygame.K_LEFT,
    pygame.K_RIGHT,
    pygame.K_UP,
    pygame.K_DOWN
]
# Save the Q-table
np.save("q_table.npy", q_table)
# Helper function to get the current state
def get_state():
    return (int(stickman_x < obstacle_x), int(stickman_x > obstacle_x), int(stickman_y < obstacle_y), int(stickman_y > obstacle_y))

# Helper function to choose an action based on the epsilon-greedy policy
# Helper function to choose an action based on the epsilon-greedy policy
def choose_action(state):
    state_index = np.ravel(state, order='C')[0]
    if random.uniform(0, 1) < epsilon:
        action = random.choice(range(num_actions))
    else:
        action = np.argmax(q_table[state_index])
    return action



# Helper function to update the Q-values
# Helper function to update the Q-values
def update_q_value(state, action, reward, next_state):
    state_index = np.ravel(state, order='C')[0]
    next_state_index = np.ravel(next_state, order='C')[0]
    max_q_value = np.max(q_table[next_state_index])
    q_table[state_index, action] = (1 - alpha) * q_table[state_index, action] + alpha * (reward + gamma * max_q_value)


running = True
while running:
    screen.blit(background_img, (0, 0))  # Draw the background image

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
        state = get_state()
        action = choose_action(state)

        # Perform the selected action automatically
        if actions[action] == pygame.K_LEFT:
            if stickman_x - stickman_speed >= min_x:  # Check left boundary
                stickman_x -= stickman_speed
        elif actions[action] == pygame.K_RIGHT:
            if stickman_x + stickman_speed + stickman_width <= max_x:  # Check right boundary
                stickman_x += stickman_speed

        elif actions[action] == pygame.K_UP:
            stickman_y -= stickman_speed
        elif actions[action] == pygame.K_DOWN:
            stickman_y += stickman_speed

        # Check if the stickman goes out of the window
        if stickman_x < 0:
            stickman_x = 0
        elif stickman_x > screen_width - stickman_width:
            stickman_x = screen_width - stickman_width
        elif stickman_y < 0:
            stickman_y = 0
        elif stickman_y > screen_height - stickman_height:
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
            reward = -1  # Negative reward for collision
            game_over = True
            restart = True
        else:
            reward = 1  # Positive reward for moving without collision

        next_state = get_state()
        update_q_value(state, action, reward, next_state)

        # Generate new obstacle when the current obstacle goes off-screen
        if obstacle_x + obstacle_width < 0:
            obstacle_x = screen_width
            obstacle_y = random.randint(screen_height // 2, screen_height - obstacle_height)
            score += 1
        
    else:
        # Display failure message
        text = font.render("You failed!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

        # Display restart button
        restart_text = font.render("Click to Restart", True, (0, 255, 0))
        restart_text_rect = restart_text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(restart_text, restart_text_rect)

    # Draw the stickman
    screen.blit(stickman_img, (stickman_x, stickman_y))

    # Draw the obstacle
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))

    # Display score counter
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect(topright=(screen_width - 10, 10))
    screen.blit(score_text, score_rect)

    pygame.display.flip()
    clock.tick(60)

# Clean up and exit
pygame.quit()

q_table = np.load("q_table.npy")