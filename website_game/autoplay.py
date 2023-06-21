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
    x=420
    y=460
    
    pyautogui.click(x=x,y=y)
    

def start_chapter_one():
    x=387
    y=299
    pyautogui.click(x=x,y=y)
def position():
    time.sleep(5)
    print(pyautogui.position())

   
def detect_object():
    if pyautogui.locateOnScreen("black_guy.png"):
        return True
    elif pyautogui.locateOnScreen("redguy.png"):
        return True
    elif pyautogui.locateOnScreen("pink_guy.png"):
        return True
    
    else:
        return False
    
def play_game():
    pyautogui.keyDown('right')
    time.sleep(2)
    pyautogui.keyUp('right')
    

    
    while True:
        
        
        if keyboard.is_pressed('e'):
            exit()
        else:
            pyautogui.keyDown('z')
            pyautogui.keyUp('z')
            pyautogui.keyDown('x')
            pyautogui.keyUp('x')
            
        
        
        
start_game()
time.sleep(5)
choose_chapter()
time.sleep(5)
start_chapter_one()
time.sleep(5)
play_game()


    
    
