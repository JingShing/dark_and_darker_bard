# code written by: JingShing
from pyautogui import mouseDown, mouseUp, locateOnScreen
import time

# pip install pyautogui
setting = dict()
image_left = 'image_left.png'
image_right = 'image_right.png'
def read_text_file_to_list(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Remove newline characters at the end of each line
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"File '{file_path}' does not exist.")
        return []

def default_set():    
    setting["confidence"] = 0.8
    setting["grayscale"] = True
    setting["interval"] = 0.02
    # left, top, width, height
    setting["region"]=(0, 0, 1920, 1080)

def load_set(list):
    for i in list:
        if "confidence" in i:
            print("confidence loaded: "+i)
            setting["confidence"] = float(i.split("=")[-1])
        elif "grayscale" in i:
            print("grayscale loaded: "+i)
            setting["grayscale"] = bool(i.split("=")[-1])
        elif "region" in i:
            scale_set = tuple([int(item) for item in i.split("=")[-1].split(",")])
            print("region set loaded: "+str(scale_set))
            setting["region"] = scale_set
        elif "interval" in i :
            print("interval loaded: "+i)
            setting["interval"] = float(i.split("=")[-1])

def detect_tempo():
    print("start play!")
    while True:
        try:
            location = locateOnScreen(image_left, confidence=setting["confidence"], grayscale=setting["grayscale"], region=setting["region"])
            if location is None:
                location = locateOnScreen(image_right, confidence=setting["confidence"], grayscale=setting["grayscale"], region=setting["region"])
            if location is not None:
                mouseDown(button='right')
                time.sleep(setting["interval"])
                mouseUp(button='right')
                print("hit")

        except Exception as e:
            print(f"error: {str(e)}")

if __name__ == "__main__":
    default_set()
    load_set(read_text_file_to_list("setting.txt"))
    detect_tempo()