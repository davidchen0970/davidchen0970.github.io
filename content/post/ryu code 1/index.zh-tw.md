+++
date = '2024-11-18T02:14:38+08:00'
title = '軟體定義網路 - ryu 的第一個程式'
image = "pawel-czerwinski-fnLi5j7kPU4-unsplash.jpg"
categories = [
    "Protocol"
]
+++

# 軟體定義網路 - ryu 的第一個程式  (3-2-1)

reference:

1. [Getting Started - ryu](https://ryu.readthedocs.io/en/latest/getting_started.html)
2. [【SDN 筆記】 Mininet 介紹與 RYU 相關安裝](https://joechang0113.github.io/2020/02/18/mininet-ryu-install.html)
3. [實驗環境安裝教學](https://courses.openedu.tw/courses/course-v1:5GMB+QA+20016/pdfbook/0/)
4. [研究型 Controller ： Ryu](https://ithelp.ithome.com.tw/articles/10240163)
5. [撰寫 Ryu 簡易入門](https://github.com/YanHaoChen/Learning-SDN/tree/master/Controller/Ryu/FirstRyuApplication)
6. [[Day33] python的super繼承](https://ithelp.ithome.com.tw/articles/10222948)
----

目錄:

0. 執行環境
1. 安裝 ryu
2. 測試 ryu
3. 編寫第一個 ryu程式
---

### 0. 執行環境
    
| 環境名稱 | 版本號      | 查詢指令         |
| -------- | ----------- | ---------------- |
| Ubuntu   | 20.04.5 LTS | lsb_release -a   |
| python   | 3.8.10      | python3 --version |


### 1. 安裝 ryu
安裝前先確定是否有已經有以下檔案:



| 環境名稱 | 套件名稱                                                                 |
| -------- | ------------------------------------------------------------------------ |
| Linux    | gcc python-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev zlib1g-dev mininet |
| Python   | pip                                                                      |


輸入以下指令以下載檔案
```bash
python3 -m pip install ryu
sudo apt install ryu-bin
```
(所下載版本 : ryu-4.34)


### 2. 測試 ryu

在終端機輸入以下指令:
```
sudo ryu-manager ryu.app.simple_switch_13
```
![圖1: 測試結果](https://i.imgur.com/6HAQZmI.png)

如果有上述結果代表正常執行。


### 3. 編寫第一個 ryu程式

在terminal中寫下 `nano simpleApplication.py` 開啟編輯器。
複製以下程式碼，作為第一個最基本的ryu程式。

```python
from ryu.base import app_manager

class SimpleSwitch(app_manager.RyuApp):
    
    # 選擇支援的openFlow版本，可不只一個版本
    OFP_VERSION = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        
        # super().__init__會去呼叫父類別的initializer__init__
        super(SimpleSwitch, self).__init__(*args, **kwargs)

```

儲存並離開。
這裡寫完就可以執行了XD

在 terminal 中打下 `sudo ryu-manager simpleApplication.py` 執行剛剛所儲存的程式碼。

確定之後會馬上結束，並跑出以下結果:

![](https://i.imgur.com/rO60w5t.png)


這樣就可以確定我們已經寫完第一支屬於自己的第一個 ryu 程式啦。



###### tags: `SDN`