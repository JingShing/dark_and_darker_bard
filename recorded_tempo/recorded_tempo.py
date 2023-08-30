from time import sleep
from pyautogui import click, locateOnScreen
setting = dict()
set_file_name = "set.txt"
def read_setting():
    now_key = None
    line_list = read_text_file_to_list(set_file_name)
    for line in line_list:
        if not "Delay" in line and not "Right" in line:
            now_key = line
            setting[now_key] = list()
        else:
            setting[now_key].append(line)
    print(setting.keys())
    print(setting)
    return

def detect_song_name():
    for i in setting.keys():
        print(i+".png")
        location = locateOnScreen(i+".png")
        if location is not None:
            play_script(setting[i])
            return

def play_script(list):
    for i in list:
        print(i)
        if "Delay" in i:
            sleep(int(i.split(" ")[-1]))
        elif "Right" in i:
            click(button="right")

# Read a text file into a list
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

# Write a list to a text file
def write_list_to_text_file(file_path, data_list):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(item + '\n')
        print(f"Data has been written to the file '{file_path}'.")
    except Exception as e:
        print(f"An error occurred while writing the file: {str(e)}")

def normalize_script(list):
    to_remove = "MoveTo"
    new_list = [item for item in list if not to_remove in item]
    for i in range(len(new_list)):
        new_list[i] = new_list[i].replace("Click", "").replace("Down", "")
    return new_list

# Example usage
def process_script(input_file_path, output_file_path):
    my_list = read_text_file_to_list(input_file_path)
    write_list_to_text_file(output_file_path, normalize_script(my_list))

if __name__ == "__main__":
    # process_script("or.txt", "set.txt")
    read_setting()
    while 1:
        detect_song_name()