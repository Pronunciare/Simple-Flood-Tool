import time
import pyperclip
import pyautogui

time.sleep(5)
f = open("spam","r")

for char in f:
    pyperclip.copy(char)
    pyautogui.hotkey('ctrl', 'v', interval=-0000.0000)
    pyautogui.typewrite("\n")
