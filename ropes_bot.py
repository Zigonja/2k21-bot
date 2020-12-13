from pyautogui import *
from datetime import datetime
import pygetwindow as gw
import pyautogui
import time
import random
import keyboard
import win32api, win32con

# Controller button maper, change to fit yours
A = "space"
X = "k"
L_UP = "w"
L_DOWN = "s"
R_UP = "t"
R_DOWN = "g"

def get_time_stamp():
    dateTimeObj = datetime.now()
    
    return dateTimeObj.strftime("(%H:%M:%S)")

def press_button(button):
    keyboard.press(button)
    time.sleep(0.2)
    keyboard.release(button)

def press_buttons(button1, button2):
    keyboard.press(button1)
    keyboard.press(button2)
    time.sleep(0.1)
    keyboard.release(button1)
    keyboard.release(button2)

print(get_time_stamp(), "Starting battle ropes bot in 3 seconds. Make sure you are next to the battle ropes.")
time.sleep(1)

print(get_time_stamp(), "Starting battle ropes bot in 2 seconds.")
time.sleep(1)

print(get_time_stamp(), "Starting battle ropes bot in 1 second.")
time.sleep(1)

print(get_time_stamp(), "Starting bot.")

win = gw.getWindowsWithTitle('NBA 2K21')

if len(win) > 0:
    win[0].activate();
else:
    print(get_time_stamp(), "NBA 2K21 is not running. Exiting.");
    exit()

press_button(A)
time.sleep(5) 
press_button(A) # change to X for debug

for i in range(150):
    press_buttons(L_UP, R_DOWN)
    time.sleep(0.08)
    press_buttons(R_UP, L_DOWN)
    time.sleep(0.1)

print(get_time_stamp(), "The bot finished! Goodbye");
