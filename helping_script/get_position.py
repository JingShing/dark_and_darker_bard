import pyautogui
import time

while True:
    time.sleep(1)
    x, y = pyautogui.position()
    print(f"Current mouse position: x={x}, y={y}")
