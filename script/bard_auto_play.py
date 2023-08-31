# code written by: JingShing
# This script is for dark and darker bard autoplay song
from pyautogui import mouseDown, mouseUp, locateOnScreen
import time
import os

# pip install pyautogui
setting = dict()
image_list = list()
folder_name = "image"
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
            for i in image_list:
                file_name = folder_name+"/"+i
                location = locateOnScreen(file_name, confidence=setting["confidence"], grayscale=setting["grayscale"], region=setting["region"])
                if location is not None:
                    print("find: "+i)
                    break

            if location is not None:
                mouseDown(button='right')
                time.sleep(setting["interval"])
                mouseUp(button='right')

        except Exception as e:
            print(f"error: {str(e)}")


def find_folder_file(folder_path=folder_name)->list():
    if os.path.exists(folder_path):
        file_list = os.listdir(folder_path)
        return file_list
    else:
        print("folder not exist")
        return []

if __name__ == "__main__":
    image_list = find_folder_file(folder_path=folder_name)
    print("image list loaded: "+str(image_list))
    default_set()
    load_set(read_text_file_to_list("setting.txt"))
    detect_tempo()
