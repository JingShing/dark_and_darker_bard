import pyautogui
target_image_path = 'image.png'

while True:
    try:
        location = pyautogui.locateOnScreen(target_image_path)

        if location is not None:
            x, y, _, _ = location
            pyautogui.click(x + 10, y + 10, button='right')
            print("play")

    except Exception as e:
        print(f"error: {str(e)}")
