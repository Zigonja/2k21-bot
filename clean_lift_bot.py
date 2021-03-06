from pyautogui import *
from datetime import datetime
import pygetwindow as gw
import pyautogui
import time
import random
import keyboard
import win32api, win32con
import win32gui
import threading

# Controller button maper, change to fit yours
A = "space"
X = "k"
LB = "u"
RB = "i"

def get_time_stamp_ms():
    dateTimeObj = datetime.now()
    
    return dateTimeObj.strftime("(%H:%M:%S:%f)")

def get_time_stamp():
    dateTimeObj = datetime.now()
    
    return dateTimeObj.strftime("(%H:%M:%S)")

def press_button(button):
    keyboard.press(button)
    time.sleep(0.1)
    keyboard.release(button)

def button_thread(button, button_rgb, pixel_coordinates, end_time):
    while time.time() <= end_time:
        find_and_press_btn(button, button_rgb, pixel_coordinates)
    print("Button thread finished")


hwnd = win32gui.FindWindow(None, "NBA 2K21")
win32gui.SetForegroundWindow(hwnd)

print(get_time_stamp(), "Starting bot in 3 seconds. Make sure you are next to the clean lift machine.")
time.sleep(1)

print(get_time_stamp(), "Starting clean lift bot in 2 seconds.")
time.sleep(1)

print(get_time_stamp(), "Starting clean lift bot in 1 second.")
time.sleep(1)

print(get_time_stamp(), "Starting bot.")

win = gw.getWindowsWithTitle('NBA 2K21')

if len(win) > 0:
    win[0].activate()
else:
    print(get_time_stamp(), "NBA 2K21 is not running. Exiting.")
    exit()

press_button(A)
time.sleep(5) # wait for instrucition popup,           5s should be enough
press_button(A) # change to X button for practice, so you test it before going for real

time.sleep(10.5)

for i in range (20):
    keyboard.press(RB)
    keyboard.press(LB)
    time.sleep(0.465)
    keyboard.release(RB)
    keyboard.release(LB)
    sleep(1.8)

print(get_time_stamp(), "Bot finished. Goodbye!")
