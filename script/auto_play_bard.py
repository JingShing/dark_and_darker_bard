import pyautogui
# pip install pyautogui
target_image_path = 'image.png'
confidence_value = 0.8
while True:
    try:
        location = pyautogui.locateOnScreen(target_image_path)
        if location is not None:
            pyautogui.click(button='right', confidence=confidence_value)
            print("play")

    except Exception as e:
        print(f"error: {str(e)}")
