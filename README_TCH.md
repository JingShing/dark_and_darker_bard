[English](README.md) | 繁體中文
# dark and darker 吟遊詩人腳本
一個協助自動演奏的腳本。

# 需要的庫
* ```pip install PyAutoGUI```
* ```pip install opencv-python```

# 需要的圖片
因為需要正確的解析度，我是使用 1920X1080 作為範例。如果效果不佳，請自行擷取。

圖片名需為 ```image.png```。

# 原理
原理是採用圖形偵測，來偵測指標到達黃色的節奏點時，可以自動撥放。如果想要調整更好的效果，可以更改 ```setting.txt``` 的參數 和自行擷取更好的 ```image.png```。

# 不同版本
## 偵測節奏版本(預設的 script)
我更建議直接使用 [此腳本](script/auto_play_bard.py)。當然也可以使用 [打包好的版本](https://github.com/JingShing-Python/dark_and_darker_bard/releases) 不過打包好的效果並沒代碼好。

因為 confidence 的參數我無法打包進 exe 中。所以準確度很差。

目前的版本可以正常演奏部分節奏較長的樂曲。但短節奏的樂曲會在偵測上有些問題。

* 建議解析度為 1920X1080。 否則需要自行替換 ```image.png``` 和調整 ```setting.txt```
* 電腦需要安裝 opencv-python ，可以使用這個指令安裝： ```pip install opencv-python```
## 錄製節奏版本 (recorded tempo version)
我當時想嘗試看看其他方法來自動演奏，所以採用了錄製好節奏的方法。

這個方法可以演奏大部分歌曲，但是很麻煩，所以我放棄了這個方法。
