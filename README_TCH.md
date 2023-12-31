[English](README.md) | 繁體中文
# dark and darker 吟遊詩人腳本
一個協助自動演奏的腳本。

在 [最新的版本中](https://github.com/JingShing-Python/dark_and_darker_bard/releases/tag/ver1.4)。我們已經能演奏大部分的樂器和樂曲！

## [預覽影片](https://youtu.be/2QAdS9OccjA)
點擊下方圖片或 [此連結](https://youtu.be/2QAdS9OccjA) 觀看腳本預覽影片。

<a href="http://www.youtube.com/watch?feature=player_embedded&v=2QAdS9OccjA" target="_blank">
 <img src="http://img.youtube.com/vi/2QAdS9OccjA/mqdefault.jpg" alt="Watch the video"/>
</a>

# 如何使用？
在最佳的條件下，我推薦您使用 python 來直接運行腳本。

* 在最新的版本中可以使用打包好的 exe 檔。

~~因為打包成 exe 檔有些技術上的障礙，所以接下來將由我來幫助您安裝所需的環境和配件。~~
* ## 安裝 Python3.10
  * 可以在 [這裡](https://www.python.org/downloads/release/python-3106/) 下載 python 的安裝包。
  * 此腳本使用 3.10.6 版本測試，所以我推薦使用此版本。
* ## 安裝模塊
  * 可以使用指令安裝，詳情在底下 ```需要的庫``` 的部分。
  * 或是使用我打包好的指令檔 ```install_modules.bat``` 來安裝模塊。
* ## 修改設定並找到適合的設定
  * 我無法在這個步驟幫助您，因為我並不知道您電腦詳細的配置和螢幕的解析度。
  * 所以推薦您閱覽 ```設定``` 的篇章。還有圖片無法適用時，請自行裁切適合的圖檔來匹配。
* ## 最後
  * 享受您的自動撥放點唱機(無情的唱歌機器、沒有靈魂的吟遊詩人)。
  * 如果這個腳本有幫助到您，歡迎留下星星和評論。
  * 真摯地感謝您閱讀了此篇 ```README```
# 如何打包
* python 3.9.10
* ```pip install opencv-python==4.5.3.56```
> 在最新的版本中 opencv 和 pyinstaller 相容性很糟。
* 使用 pyinstaller 打包 exe

# 需要的庫
* ```pip install PyAutoGUI```
* ```pip install opencv-python```

或者你可以使用 ```install_modules.bat``` 來安裝:
```bat
@echo off
pip install PyAutoGUI
pip install opencv-python
```

# 需要的圖片
因為需要正確的解析度，我是使用 1920X1080 作為範例。如果效果不佳，請自行擷取。

~~圖片名需為 ```image.png```。~~
~~* 在最新的版本中。需要兩張圖片： ```image_left.png``` 和 ```image_right.png```。~~
> 未來的版本可能會需要更多的圖片，以增加準確率。
* 在 1.6 的版本中，我們可以直接將圖片放入 ```image``` 資料夾中。程式會自動的讀入圖檔。

# 原理
原理是採用圖形偵測，來偵測指標到達黃色的節奏點時，可以自動撥放。如果想要調整更好的效果，可以更改 ```setting.txt``` 的參數 和自行擷取更好的 ```image.png```。

# Bat
Script 中的 bat 檔可以幫助你快速的啟動 python 腳本。

這是一個比較方便的方法來開啟 python 腳本(因為這個腳本打包時，有些問題)

bat 代碼:
```bat
@echo off
REM 這個 bat 會跑兩個指令
REM 切換到 bat 在的資料夾
cd /d "%~dp0"

REM 跑 python 腳本
python bard_auto_play.py
```

# 設置檔
可以透過修改 ```setting.txt``` 來讓腳本的效果更好:
* confidence=0.88
  * 圖片的容忍度，建議值： 0.85 ~ 1.0
* grayscale=True
  * 這個數值為 True 或 False。這個數值為 True 時會使用灰階來判定，可以增快找到圖片的效率。
* region=763,859,390,30
  * 這個數值為偵測的螢幕範圍。 可以自己來更改： 4 個數值： x, y, 寬度, 高度。
  * 預設 1920X1080 應該為 0, 0, 1920, 1080。
  * 上面的 763,859,390,30 數值，對應到的是 1920X1080 解析度。
* interval=0.01
 * 右鍵按下的時間間隔。 建議數值： 0.01 ~ 0.05。

## 有關判定區域的設定
這裡有 [腳本可以幫助你取得座標](https://github.com/JingShing/dark_and_darker_bard/blob/main/helping_script/get_position.py)。

* 判定區域有 4 個數值: x, y, 寬度, 高度.
* 可以透過拿到左上座標(x1, y1) 和右下座標(x2, y2).
* 數值應該為： x1,y1,(x2-x1),(y2-y1)

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

<details>
<summary>更新日誌</summary>

## 版本 1.0
* 發布首個版本
  * 仍然很糟。
  * 這只是一堆無用的代碼。
  * 開始懷疑圖像檢測。
## 版本 1.1
* 放棄使用圖像檢測，開始使用錄製腳本。
  * 跑的很糟。
  * 錄製所有歌曲並不容易。
## 版本 1.2
* 發現我們可以給圖像檢測一些信心(confidece，容錯率)。
  * 耶！信心(confidence)讓圖像檢測有用了。
  * 這使我充滿了我的決心。
  * 不，信心(confidence)搞爛了打包版本，無法嵌入 opencv 到 exe 檔。
  * 對不起。我們需要直接用 python 跑腳本。
## 版本 1.3
* 我發現我們不能僅使用 `click()` 函數來模擬右鍵單擊。
  * 編寫新的 點擊(click) 函數。它有效了！
  * 所以在這個版本中，我們終於可以運行了。
  * 我在腳本中添加了一些設置：信心(confidence)、灰度、間隔和區域。
## 版本 1.4
* 實際上腳本有效。但它不太有效？所以我花了一些時間最佳化腳本。
  * 縮小檢測區域以提高速度。
  * 我調整了一些 信心(confidence) 數值，讓腳本不要太自信，也不要太小心。
  * 我考慮使用灰度。可以更快地檢測。
  * 我調整了右鍵單擊之間的間隔時間，以避免雙擊。
  * 我製作了兩個 bat 檔，以幫助您更輕鬆地安裝模塊和運行 Python。
## 版本 1.5
* 感到沮喪。有時腳本運行不穩定。所以我開始採用更多圖像來檢測。
  * 在我的情況下，在早期版本中，我只檢測了指針的一側。所以很容易錯過節奏。
  * 添加了兩側的檢測。更加準確。
  * 比之前效果好。
  * 未來版本中，將採用更多圖像，讓精準度提高。
## 版本 1.6
* 新增了自動添加圖片的腳本。直接把想偵測的圖片丟入 ```image``` 資料夾。腳本會自動偵測資料夾中所有的圖片。
  * 我們終於可以不用使用 ```image.png``` 來命名圖檔了。
  * 可以使用英文字母和 ascii 的符號來命名。(中文命名可能會有問題)
  * 圖片數量可以自由地增加或減少了。
## 版本 1.7
* 找到不能打包 exe 檔的原因了
  * 原因很簡單，而這浪費了我大量的時間
  * 詳細原因可以參見 ```如何打包 exe```。
  * Opencv 和 pyinstaller 在 python 的 3.10 版本後有些衝突。可以安裝 3.9 以前的版本來避免。
  * 建議安裝此版本的 opencv： ``` pip install opencv-python==4.5.3.56```
  * 具體套件可以參考此： [requirement.txt](requirement.txt).
</details>
