[English](README.md) | 繁體中文
# dark and darker 吟遊詩人腳本
一個協助自動演奏的腳本。

# 需要的庫
* ```pip install PyAutoGUI```
* ```pip install opencv-python```

# image you need
Because it will need right resolution. So it may need to cut the right image by your self.

And image should be named ```image.png```.

# principle
This script is made for detect the image that the bar moving in yellow area. And it will auto right click. So you sould replace the ```image.png``` by yourself.

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
