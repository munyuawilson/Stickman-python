import pyautogui
import time
import keyboard
import numpy as np
import cv2
from PIL import ImageGrab


time.sleep(5)

def start_game():
    
    x=700
    y=444

    pyautogui.click(x=x,y=y)
    
def choose_chapter():
    x=427
    y=460
    
    pyautogui.click(x=x,y=y)
    print(pyautogui.position())

def start_chapter_one():
    x=387
    y=299
    pyautogui.click(x=x,y=y)
    
def detect_object():
    screenshot = ImageGrab.grab()

    # Convert the screenshot to OpenCV format
    screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Preprocessing (example: converting to grayscale)
    gray_screenshot = cv2.cvtColor(screenshot_cv, cv2.COLOR_BGR2GRAY)

    # Object Detection (example: template matching)
    template = cv2.imread('templat.png', 0)  # Replace with the path to your template image
    result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8  # Adjust the threshold as per your requirement
    locations = np.where(result >= threshold)
    object_coordinates = list(zip(*locations[::-1]))
    return object_coordinates
    
def play_game():
    
   
    time.sleep(2)
    
    
    pyautogui.keyUp('right') 
    time.sleep(3)
    pyautogui.keyDown('right') 
    object_coordinates=detect_object()
    print(object_coordinates)
    

    
    if object_coordinates:
        keyboard.press("x")
        time.sleep(1)
        keyboard.release("x")
        keyboard.press("y")
        time.sleep(1)
        keyboard.release("y")
        
    
    
    
    



        
          

start_game()
time.sleep(5)
choose_chapter()
time.sleep(5)
start_chapter_one()
time.sleep(5)
play_game()
    
    