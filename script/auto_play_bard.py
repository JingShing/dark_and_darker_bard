import pyautogui
# pip install pyautogui
target_image_path = 'image.png'
global confidence_value
confidence_value = 0.8
def read_first_line_as_float(file_path):
    try:
        with open(file_path, 'r') as file:
            first_line = file.readline().strip()
            first_line_as_float = float(first_line)
            return first_line_as_float
    except:
        return 1
def detect_tempo():
    global confidence_value
    while True:
        try:
            location = pyautogui.locateOnScreen(target_image_path)
            if location is not None:
                pyautogui.click(button='right', confidence=confidence_value)
                print("play")

        except Exception as e:
            print(f"error: {str(e)}")

if __name__ == "__main__":
    confidence_value = read_first_line_as_float("confidence.txt")
    detect_tempo()
