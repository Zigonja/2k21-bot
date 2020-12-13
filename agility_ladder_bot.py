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
B = "l"
Y = "j"

def get_time_stamp_ms():
    dateTimeObj = datetime.now()
    
    return dateTimeObj.strftime("(%H:%M:%S:%f)")

def get_time_stamp():
    dateTimeObj = datetime.now()
    
    return dateTimeObj.strftime("(%H:%M:%S)")

def press_button(button):
    keyboard.press(button)
    time.sleep(0.01)
    keyboard.release(button)
    time.sleep(0.01)

def get_button_coords():
    hwnd = win32gui.FindWindow(None, "NBA 2K21")
    win32gui.SetForegroundWindow(hwnd)
    x, y, x1, y1 = win32gui.GetWindowRect(hwnd)

    return (x+407,y+223)     

def find_and_press_btn(button, button_rgb, pixel_coordinates):
    if (pyautogui.pixelMatchesColor(pixel_coordinates[0], pixel_coordinates[1], button_rgb, tolerance=40)):
        press_button(button)  


def button_thread(button, button_rgb, pixel_coordinates, end_time):
    while time.time() <= end_time:
        find_and_press_btn(button, button_rgb, pixel_coordinates)
    print("Button thread finished")

print(get_time_stamp(), "Starting bot in 3 seconds. Make sure you are next to the agility ladder.")
time.sleep(1)

print(get_time_stamp(), "Starting agility ladder bot in 2 seconds.")
time.sleep(1)

print(get_time_stamp(), "Starting agility ladder bot in 1 second.")
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

btn_coords = get_button_coords()

t_end = time.time() + 55 # now + 50 seconds
      
threadA = threading.Thread(target=button_thread, args=(A,(78, 160, 43),btn_coords,t_end))
threadB = threading.Thread(target=button_thread, args=(B,(214, 16, 26),btn_coords,t_end))
threadX = threading.Thread(target=button_thread, args=(X,(16, 175, 246),btn_coords,t_end))
threadY = threading.Thread(target=button_thread, args=(Y,(241, 210, 15),btn_coords,t_end))

threadB.start()
threadX.start()
threadY.start()
threadA.start()