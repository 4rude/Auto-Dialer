# Auto-Dialer
This is a script written in python using the pyautogui and tkinter modules. The script, when ran, loads up a tkinter window named tk. When the window is selected, the F8, F9, and F10 keys are bound to three functions that are written in this script.

Before starting this application, Python 3 must be downloaded. The required modules (pyautogui and tkinter) should come with the installation. If they don't, look in the AutoDialer.py source code for notes on how to accomplish this task. 

This auto dialer is written with a specific application layout in mind. Internet Explorer and the software phone dialer web-applications must be specificly placed on the screen in order for pyautogui to correctly dial phone numbers. Look in the downloaded folder for an example layout. Notice where the software dialer, the Internet explorer page, and the tk (AutoDialer.py) applications are placed.

To use:
1. Double click the AutoDialer.py application and it should load up a small window title tk and a command prompt window. 
2. Shrink the command prompt window and move the tk window to the position recommended in the Layout Example picture (found in the Auto Dialer folder).
3. Use the F8 hotkey to mute calls. Use the F9 key to dail out. Use the F10 key to end the phone call.

Troubleshooting:
1. If the tk window is not showing up when the AutoDialer.py file is double clicked, make sure the pyautogui module is downloaded.
2. If the application is loaded and the command prompt window is saying that the "leadImage.png" cannot be located, try zooming in and out of the Internet Explorer window to see if the PNG file can then be located on the screen. The reason for this is that the actual pixels of the PNG file leadImage.png (found in the Auto Dialer folder) must match the same pixel resolution on screen. 
