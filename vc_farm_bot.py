from pyautogui import *
from datetime import datetime
import pygetwindow as gw
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def get_time_stamp():
    dateTimeObj = datetime.now()
    
    return dateTimeObj.strftime("(%H:%M:%S)")

def start_game_are_u_sure(game_count):
    print(get_time_stamp(), "Starting the game.")
    print(get_time_stamp(), "Botting started. Game number", game_count)
    keyboard.press("s")
    time.sleep(0.2)
    keyboard.release("s")

    keyboard.press("space")
    time.sleep(0.2)
    keyboard.release("space")

def ens_season_are_u_sure():
    print(get_time_stamp(), "Ending the season.")
    keyboard.press("s")
    time.sleep(0.2)
    keyboard.release("s")

    keyboard.press("space")
    time.sleep(0.2)
    keyboard.release("space")

def go_to_next_game():
    print(get_time_stamp(), "Navigating to next game.")
    keyboard.press("d")
    time.sleep(0.2)
    keyboard.release("d")

def skip_all_star():
    print(get_time_stamp(), "Skipping all star games.")

    while pyautogui.locateOnScreen('assets/allstar.png', grayscale=True, confidence=0.8) is not None:
        keyboard.press("d")
        time.sleep(0.2)
        keyboard.release("d")

def skip_to_sub_in():
    print(get_time_stamp(), "Skipping to next appearance.")
    keyboard.press("space")
    time.sleep(5)
    keyboard.release("space")

print(get_time_stamp(), "Welcome to 2K22 VC MyCareer Bot, to quit it press Q on the keyboard.")
game_count = 0

while keyboard.is_pressed('q') == False:
    win = gw.getWindowsWithTitle('NBA 2K22')

    if len(win) > 0:
        win[0].activate()
    else:
        print(get_time_stamp(), "NBA 2K22 is not running. Exiting.")
        break;    

    if keyboard.is_pressed('p') == True:
        print(get_time_stamp(), "Sleeping for 10 seconds.")
        time.sleep(10)

    next_game_pos = pyautogui.locateOnScreen('assets/playnextgame.png', grayscale=True, confidence=0.8)
    next_game_selected = pyautogui.locateOnScreen('assets/nextgameselected.png', grayscale=True, confidence=0.9)

    if next_game_pos is not None and next_game_selected is None:
        next_game_x, next_game_y = pyautogui.center(next_game_pos)
        pyautogui.moveTo(x=next_game_x, y=next_game_y)
        pyautogui.mouseDown()
        time.sleep(0.2)
        pyautogui.mouseUp()
    if pyautogui.locateOnScreen('assets/playgame.png', grayscale=True, confidence=0.8) is not None:
        start_game_are_u_sure(game_count + 1)
        game_count += 1
    elif pyautogui.locateOnScreen('assets/endseason.png', grayscale=True, confidence=0.8) is not None:
        ens_season_are_u_sure()    
    elif pyautogui.locateOnScreen('assets/allstar.png', grayscale=True, confidence=0.8) is not None:
        skip_all_star()
    elif pyautogui.locateOnScreen('assets/teampractice.png', grayscale=True, confidence=0.8) is not None:
        go_to_next_game()
    elif pyautogui.locateOnScreen('assets/onthecourt.png', grayscale=True, confidence=0.8) is not None:
        skip_to_sub_in()    
    elif pyautogui.locateOnScreen('assets/seasons.png', grayscale=True, confidence=0.8) is not None:
        keyboard.press("esc")
        time.sleep(0.2)
        keyboard.release("esc")
    else:
        keyboard.press("space")
        time.sleep(2)
        keyboard.release("space")

print(get_time_stamp(), "The bot completed", game_count, " games. Goodybe!  ");
