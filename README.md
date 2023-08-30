English | [繁體中文](README_TCH.md)
# dark_and_darker_bard
a script help you to auto play bard music.

# module you need
* ```pip install PyAutoGUI```
* ```pip install opencv-python```

# image you need
Because it will need right resolution. So it may need to cut the right image by your self.

And image should be named ```image.png```.

# principle
This script is made for detect the image that the bar moving in yellow area. And it will auto right click. So you sould replace the ```image.png``` by yourself.

# Bat
You can use bat to automatically using python to run it.

It is a convenient way to run script(Since I have trouble to packed script into exe).

bat code:
```bat
@echo off
REM it will run two command
REM switch to the bat folder
cd /d "%~dp0"

REM run python script
python bard_auto_play.py
```

# Setting
You can edit ```setting.txt``` to make this script more suitable for your purpose:
* confidence=0.88
  * This value is for the tolerance for the image. I suggest value between 0.85 ~ 1.0
* grayscale=True
  * This value is True or False. This value is for using grey image to detect or not. If using this script can be faster.
* region=768,860,500,100
  * This is for detect area. It can be edit by your self. 4 value is for x, y, width, height.
  * Default 1920X1080 should be 0, 0, 1920, 1080.
  * 768,860,500,100 is also for the 1920X1080 resolution.

# different version
## detect tempo version
I highly suggest to directly to use [This Script](script/auto_play_bard.py). Or you can use these [packed exe](https://github.com/JingShing-Python/dark_and_darker_bard/releases) in release.

Since I cannot deal with the confidence parameter in packed exe. So I highly suggest to use code directly.

Now this version is kindly worked? It can play long tempo song. But sometimes it failed to detect.

* Suggested resolution is 1920X1080. OR you should cut your own ```image.png``` and change ```setting.txt```
* And your pc should installed opencv-python using ```pip install opencv-python```
## recorded tempo version
I want to tried another method to play song.

This method is to record all the song play. But this method is totally waste time.
