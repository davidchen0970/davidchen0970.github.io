+++
date = '2024-12-04T01:03:11+08:00'
title = 'NachOS Install Note'
image = "pawel-czerwinski-muvgkVuKPDo-unsplash.jpg"
description = "紀錄如何安裝 NachOS，以及一些坑..."
+++

# 安裝 NachOS 筆記

在這篇筆記中，將會在 Ubuntu 20.04.5 虛擬機上安裝和設定 NachOS。

## 安裝步驟

### 開啟虛擬機 Ubuntu 20.04.5
首先，啟動你的虛擬機並進入 Ubuntu 20.04.5 環境。



###  安裝基本建構工具
在終端機中執行以下指令安裝 `build-essential`：

```bash
sudo apt-get install build-essential
```



###  檢查系統是否為 64 位元核心
確認你的系統架構為 `amd64` 才可繼續：

```bash
dpkg --print-architecture
```



###  檢查系統是否支援 32 位元架構
執行以下命令查看支援狀態，顯示 i386 表示系統支援：

```bash
dpkg --print-foreign-architectures 
```



### 啟用 32 位元支援功能
若尚未啟用 32 位元架構，請執行：

```bash
sudo dpkg --add-architecture i386
```


### 安裝 C shell、gcc 和 g++
接著，安裝必要的工具：

```bash
sudo apt-get install csh
sudo apt-get install gcc
sudo apt-get install g++

sudo apt-get update
sudo apt-get upgrade
```



###  安裝 C 與 C++ 多平台 lib
執行以下命令安裝多平台支援：

```bash
sudo apt-get install gcc-multilib g++-multilib
```



### 8: 安裝 32 位元 kernel 環境
為了支援 32 位元應用程式，執行以下指令：

```bash
sudo apt-get install lib32ncurses5 lib32z1
# Ubuntu 20.04 改為：
sudo apt-get install lib32ncurses5-dev lib32z1

sudo apt-get install zlib1g:i386 libstdc++6:i386
sudo apt-get install libc6:i386 libncurses5:i386
sudo apt-get install libgcc1:i386 libstdc++5:i386
```



###  下載 NachOS 4.0 和 mips-x86.linux-xgcc
執行以下命令下載並解壓縮檔案：

```bash
wget -d http://cc.ee.ntu.edu.tw/~farn/courses/OS/OS2015/projects/project.1/mips-x86.linux-xgcc.tar.gz
wget -d http://cc.ee.ntu.edu.tw/~farn/courses/OS/OS2015/projects/project.1/nachos-4.0.tar.gz

tar -zxvf nachos-4.0.tar.gz

sudo mv mips-x86.linux-xgcc.tar.gz /
tar -zxvf /mips-x86.linux-xgcc.tar.gz
```

- 注意: [有坑](https://stackoverflow.com/questions/36937560/unable-to-run-tar-command-invalid-option)
    主要就是 `tar -zxvf` 當中的`-` 有問題，如果用複製的話會有這個問題產生，要刪掉再用手打一次



###  解壓縮 NachOS 檔案
將解壓縮的檔案放到指定資料夾。



### 修改 Makefile 以支援 32 位元編譯

1. 修改 `/nachos-4.0/code/Makefile.common`：
```bash
CPP=/lib/cpp
CC = g++ -m32 -Wno-deprecated
LD = g++ -m32 -Wno-deprecated
AS = as --32                  

PROGRAM = nachos
```

2. 修改 `/nachos-4.0/code/bin/Makefile`：
```bash
CC=gcc -m32                    
CFLAGS=-I../lib -I../threads $(HOST)
LD=gcc -m32

all: coff2noff 
```

3. 修改 `/nachos-4.0/code/TEST/MAKEFILE`：
```bash

...
GCCDIR = /mips-x86.linux-xgcc/
...
CPP = /mips-x86.linux-xgcc/cpp0
...
CFLAGS = -G 0 -c $(INCDIR) -B/mips-x86.linux-xgcc/

```



### 執行 Make 指令
進入 NachOS 的 `code` 目錄並執行編譯：

```bash
cd nachos-4.0/code
make
```



### 測試 NachOS 環境
最後，進入 `userprog` 目錄並測試：

```bash
cd userprog
./nachos -e ../test/test1
```

測試成功的話，結果如下圖:


![圖1: 測試成功結果圖](/2024-12-04_011131.png)



## 參考資料：
1. [HackMD 筆記](https://hackmd.io/@r83V7BYGQYqK6_RFjL0vbA/B1Et9W_8w)
2. [Sean Peng 的 HackMD 筆記](https://hackmd.io/@seanpeng12/HkrEHYsu5)
3. [JeffProgrammer 部落格](https://jeffprogrammer.wordpress.com/2016/10/31/%E4%BD%9C%E6%A5%AD%E7%B3%BB%E7%B5%B1-nachos-%E7%B0%A1%E4%BB%8B/)