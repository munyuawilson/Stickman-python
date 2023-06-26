import pyautogui
import time
import keyboard
import numpy as np


print("Starting..")
print("Press 'e' to stop the stickman on the game window")
time.sleep(5)

# Define the Q-learning table
q_table = np.zeros((3, 2))  # Assuming 3 states and 2 actions (z and x)


def move_right():
    if pyautogui.locateOnScreen("arrow.png", confidence=0.5):
        pyautogui.keyDown("right")
        time.sleep(2)
        pyautogui.keyUp("right")
        detect_object(state)
    elif pyautogui.locateOnScreen("no_opponents.png", confidence=0.5):
        pyautogui.keyDown("right")
        time.sleep(2)
        pyautogui.keyUp("right")
        detect_object(state)   
        
def game_over():
    gameOver=True
    if pyautogui.locateOnScreen("gameover.png", confidence=0.5):
        gameOver=True
        
    else:
        gameOver=False
        
    return gameOver

def detect_object(state):
    if pyautogui.locateOnScreen("health_bar.png", confidence=0.8,region=(661,164,400,211)):
        while True:
            state, _ = play_game(state)
            move_right()
            game_over()
            detect_object(state)
           
            
        
    elif pyautogui.locateOnScreen("health_bar_2.png", confidence=0.8,region=(741,164,311,211)):
        while True:
            state, _ = play_game(state)
            move_right()
            game_over()
            detect_object(state)
            
            
    elif pyautogui.locateOnScreen("health_bar_3.png", confidence=0.8,region=(661,164,400,211)):
        while True:
            state, _ = play_game(state)
            move_right()
            game_over()
            detect_object(state)
            
            
    elif pyautogui.locateOnScreen("health_bar_4.png", confidence=0.8,region=(661,164,400,211)):
        while True:
            state, _ = play_game(state)
            move_right()
            game_over()
            detect_object(state)
            
    elif pyautogui.locateOnScreen("health_bar_5.png", confidence=0.8,region=(661,164,400,211)):
        while True:
            state, _ = play_game(state)
            move_right()
            game_over()
            detect_object(state)
            
    elif pyautogui.locateOnScreen("health_bar_6.png", confidence=0.8,region=(661,164,400,211)):
        while True:
            state, _ = play_game(state)
            move_right()
            game_over()
            detect_object(state)
            
    elif pyautogui.locateOnScreen("health_bar_7.png", confidence=0.8,region=(661,164,400,211)):
        while True:
            state, _ = play_game(state)
            move_right()
            game_over()
            detect_object(state)
            
    elif pyautogui.locateOnScreen("health_bar_8.png", confidence=0.8,region=(661,164,400,211)):
        while True:
            state, _ = play_game(state)
            move_right()
            game_over()
            detect_object(state)
            
    elif pyautogui.locateOnScreen("health_bar_9.png", confidence=0.8,region=(661,164,400,211)):
        while True:
            state, _ = play_game(state)
            move_right()
            game_over()
            detect_object(state)
            
    
        
    else:
        print("nothing")
        pyautogui.keyDown('right')
        time.sleep(2)
        pyautogui.keyUp('right')
    
def play_game(state):
    if keyboard.is_pressed('e'):
        exit()
    else:
        # Select action based on epsilon-greedy policy
        epsilon = 0.2
        if np.random.uniform(0, 1) < epsilon:
            action = np.random.randint(0, 2)  # Random action
        else:
            action = np.argmax(q_table[state])  # Greedy action

        if action == 0:
            pyautogui.keyDown('z')
            pyautogui.keyUp('z')
        else:
            pyautogui.keyDown('x')
            pyautogui.keyUp('x')

        # Observe the new state
        new_state = state  # Placeholder for now

        # Calculate reward based on game outcome
        reward = calculate_reward(new_state)  # Implement your own reward function

        # Update Q-value of previous state-action pair
        learning_rate = 0.1
        discount_factor = 0.9
        q_table[state, action] += learning_rate * (reward + discount_factor * np.max(q_table[new_state]) - q_table[state, action])
        return new_state, reward

def calculate_reward(state):
    # Implement your own reward function based on the game outcome and states
    reward = state
    if game_over():
        # Assign a negative reward if the game is lost
        reward = -1
    else:
        # Assign a positive reward if the agent achieves the goal
        reward += 1
    

    return reward
    


state = 0  # Initial state
detect_object(state)
