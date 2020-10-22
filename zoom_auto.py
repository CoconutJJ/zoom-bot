# Author: u/CoconutJJ

import pyautogui
import subprocess
import time
import sys

def locateAndClick(imgUrl, delay=0):

    loc = pyautogui.locateCenterOnScreen(imgUrl)

    if delay > 0:
        time.sleep(delay)

    pyautogui.click(loc)

def record():
    # subprocess.Popen(["/usr/bin/obs", "--startrecording", "--minimize-to-tray"])
    return

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("usage: " + sys.argv[0] + " [Zoom Meeting Id] [Zoom Meeting Password]")
        exit(1)

    sub = subprocess.Popen("zoom")
    
    time.sleep(4)

    locateAndClick("icons/meeting_join.png", 1)
    pyautogui.click()

    locateAndClick("icons/meeting_id_input.png", 1)
    pyautogui.write(sys.argv[1])

    locateAndClick("icons/meeting_id_join.png")

    locateAndClick("icons/meeting_password_input.png", 1)
    pyautogui.write(sys.argv[2])

    locateAndClick("icons/meeting_password_join.png")

    record()