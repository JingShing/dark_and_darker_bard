English | [繁體中文](README_TCH.md)
# dark_and_darker_bard
a script help you to auto play bard music.

In the [latest version](https://github.com/JingShing-Python/dark_and_darker_bard/releases/tag/ver1.4) it can worked in most song.

# How to use?
In the best case I highly suggest you to use the python to run this script. 

Since there are some problem to packed it as exe file. So let me help you to run this script for dark and darker bard auto play.
* ## Install Python3.10
  * You can get [python here](https://www.python.org/downloads/release/python-3106/).
  * My script is write in 3.10.6, so I recommend to install this version.
* ## Install modules
  * Using command in ```modules you need``` part
  * Or using the bat file I provide name as ```install_modules.bat```
* ## Editing Setting and Finding your perfect set
  * I cannot help you in this step. As I don't know your screen resolution and pc detail.
  * So you can see the detailed setting in ```Setting``` part. And you can cut the perfect image by yourself.
* ## Final
  * Enjoy your perfect auto song machine.
  * And if you think this repo helped you can leave a comment or star.
  * Genuinely Thank you for reading ```README```.

# module you need
* ```pip install PyAutoGUI```
* ```pip install opencv-python```

Or you can use ```install_modules.bat```:
```bat
@echo off
pip install PyAutoGUI
pip install opencv-python
```

# image you need
Because it will need right resolution. So it may need to cut the right image by your self.

~~And image should be named ```image.png```.~~
* In the latest version. It will take two image: ```image_left.png``` and ```image_right.png```.
> In the future version. It will take more image to increase accuracy.

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
* region=763,859,390,30
  * This is for detect area. It can be edit by your self. 4 value is for x, y, width, height.
  * Default 1920X1080 should be 0, 0, 1920, 1080.
  * region=763,859,390,30 is also for the 1920X1080 resolution.
* interval=0.01
 * time interval between right click. I suggest value between 0.01 ~ 0.05.

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

<details>
<summary>Update Log</summary>

## Ver 1.0
* Release first version
  * Still disorder. And it is worked like a disastar.
  * It just a code junk.
  * Started to suspect to the image detect.
## Ver 1.1
* Give up using image detect and recording song script.
  * It still worked awful.
  * It is not easy to record all the song.
## Ver 1.2
* Figure out that we can give image detect some confidence.
  * Ya. The confidence made the image detect worked.
  * It fill my determination.
  * Nooooo. Confidence broke exe package.
  * Sorry guys. We need to dircetly using script.
## Ver 1.3
* I find out that we cannot just using ```click()``` function to simulate right click.
  * Write new click function. And it worked!
  * So in this version. We finally can run.
  * I add some setting in this script: confidence, grayscale, interval and region.
## Ver 1.4
* Actually it worked. But it kinda broke? So I spend some time to make it better.
  * I cut the region to make it faster.
  * I adjust some confidence. To make it more wisely.
  * I consider to using grey scale. It make detect more faster.
  * I adjust the interval between right click to avoid double clicking.
  * And I made two bat to help you to install module and run python more easily.
## Ver 1.5
* I was frustrated. That sometimes script work not well. So I started to get more image to detect.
  * In my case. In the elder version that I only detect one side of pointer. So it is easy to miss tempo.
  * I add two side detect. So it can be more accurate.
  * It worked better than usual.
  * I decide to cut more image to make it run better.
</details>
