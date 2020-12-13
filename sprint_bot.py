from pyautogui import *
from datetime import datetime
import pygetwindow as gw
import pyautogui
import time
import random
import keyboard
import win32api, win32con

A = "space"
X = "k"
LT = "left shift"
RT = "right shift"

def get_time_stamp():
    dateTimeObj = datetime.now()
    
    return dateTimeObj.strftime("(%H:%M:%S)")

def press_button(button):
    keyboard.press(button)
    time.sleep(0.2)
    keyboard.release(button)

print(get_time_stamp(), "Starting sprint bot in 3 seconds. Make sure you are next to the treadmill.")
time.sleep(1)

print(get_time_stamp(), "Starting sprint bot in 2 seconds.")
time.sleep(1)

print(get_time_stamp(), "Starting sprint bot in 1 second.")
time.sleep(1)

print(get_time_stamp(), "Starting bot.")

win = gw.getWindowsWithTitle('NBA 2K21')

if len(win) > 0:
    win[0].activate();
else:
    print(get_time_stamp(), "NBA 2K21 is not running. Exiting.");
    exit()

press_button(A)
time.sleep(5) # wait for instrucition popup, 5s should be enough
press_button(A) # change to  X for practice

for i in range(125):
    press_button(RT)
    press_button(LT)

print(get_time_stamp(), "The bot finished! Goodbye")