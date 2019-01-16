# ************************************************************************************************

# Resources
# https://pypi.org/project/PyAutoGUI/
# https://stackoverflow.com/questions/44324377/python-3-tkinter-keyboard-shortcuts-call-a-function

# ************************************************************************************************

# Instructions
# 1. Install the most up-to-date version of Python (PyAutoGUI is automatically installed)
# 2. Install TKinter and any dependencies (comes with Python on Windows OS)
# 3. Ensure that Python is runnable from the command prompt and run the autoDialer.py script
# 4. Help with running python scripts: https://www.quora.com/How-can-I-run-a-py-notepad-file-using-Windows-10-command-prompt

# ************************************************************************************************

# Imported packages
from tkinter import *
import pyautogui

# Functions to Start, End, and Mute the call
def startCall(self):
    
    # Find the center of the home text area
    locatedText = pyautogui.locateCenterOnScreen("leadImage.png")

    # Move the cursor to the home text
    pyautogui.moveTo(locatedText)

    # Move the cursor to the phone number
    pyautogui.moveRel(0, 115, duration=0.5)

    # Click again to properly highlight the phone number
    pyautogui.click(clicks=3, button='left')

    # Right click to bring up selections.
    pyautogui.rightClick()

    # Move down to "send to web dialer" and click.
    pyautogui.click(x=787, y=616, clicks=1, button='left')
        
    # Click to select Enabled IE page.
    pyautogui.click(x=787, y=500, interval=1, clicks=1, button='left')

    # Scroll down to the bottom of the page, the parameter is a "number of clicks". Negative values scroll down.
    pyautogui.scroll(-2000) # parameter "amount_to_scroll" 

    # Another click function to take the mouse back to the window TK window
    pyautogui.click(x=39, y=718, clicks=1, button='left')

    print("Call started.")

def endCall(self):

    # Click twice on the end call button (for good measure).
    pyautogui.click(x=199, y=302, clicks=1, interval=0.025, button='left')

    # Another click function to take the mouse back to the window TK window
    pyautogui.click(x=39, y=718, clicks=1, button='left')

    print("Call ended.")

def muteCall(self):

    # Click the mute button
    pyautogui.click(x=129, y=300, clicks=1, interval=0.025, button='left')

    # Another click function to take the mouse back to the window TK window
    pyautogui.click(x=39, y=718, clicks=1, button='left')
    print("Call muted.")

# Initializing functions & tkinter window
if __name__ == "__main__":
    root = Tk()

    # Bind all functions to their respective keys.
    root.bind('<F9>', startCall)
    root.bind('<F10>', endCall)
    root.bind('<F8>', muteCall)

    root.mainloop()
