+++
date = '2024-11-16T12:39:48+08:00'
title = 'SDN concept'
categories = [
    "SDN"
]
+++



# 軟體定義網路 - SDN 主要概念與分層架構 (1-2)

reference:
1. [SDN架構](https://youtu.be/a1tnptPFH0s)
2. [SDN - 大叔筆記](https://sites.google.com/a/cnsrl.cycu.edu.tw/da-shu-bi-ji/sdn)
3. [北向、南向，都在講些什麼 "東西"?](https://showipprotocols-tw.blogspot.com/2014/06/northbound-southbound-east-west-bound.html)
4. [計算機網路筆記-ch4](https://hackmd.io/@UULi/SyqrpEntt)
5. [Software-defined networking - wiki](https://en.wikipedia.org/wiki/Software-defined_networking)
6. [What is software-defined networking?](https://www.techtarget.com/searchnetworking/definition/software-defined-networking-SDN)
---

1. SDN主要概念
2. SDN分層架構


---
### 0. 網路術語
<img src="https://i.imgur.com/Nv98Zic.png" alt="drawing" width="400"/>

在控制器的角度上 :
    1. 往下傳達控制物理網路元件指令的API，習慣上稱為南向(Southbound API)
    2. 往上接受服務請求的API，習慣上稱為北向(Northbound API)。


### 1. 傳統路由器架構
* 維基百科 : 
    1. 路由（routing） : 就是通過互聯的網路把資訊從源位址傳輸到目的位址的活動。路由發生在OSI網路參考模型中的第三層即網路層。
    2. 轉送 : 將路由器輸入端的封包移送至適當的路由器輸出端。

    所以，路由器（英語：Router，又稱路徑器）是一種電訊網路裝置，提供路由與轉送兩種重要機制。



### 2. OpenFlow 路由器架構
<img src="https://i.imgur.com/LzlzwJD.png" alt="drawing" width="400"/>

1. SDN在這裡會把路由分成 control plane 和 forwarding plane。
2. 在control plane 和 forwarding plane之間新增一個 OpenFlow protocol 以做到分離效果。

### 3. 從傳統路由器轉化成 SDN 路由器的步驟

1. 把原先都是合併在一起的 control plane 和 forwarding plane 分離。
2. 定義此兩層之間的標準介面 (API)
3. 在把分離後的 control plane 集中管理，交給 controller，再透過 Openflow 協定控制其行為。


### 4. SDN 網路架構
![](https://i.imgur.com/XvYtqdz.png)

控制器可以透過openflow的管道與交換器溝通，也可以使用既有的網管協定與交換器溝通。

### 5. SDN的三層架構
<!-- ![](https://i.imgur.com/mgG2ss7.png) -->
<!-- ![](https://i.imgur.com/PRKDyPM.png) -->
<img src="https://cdn.ttgtmedia.com/rms/onlineimages/sdn-sdn_architecture.png" alt="drawing" width="300"/>

1. Application layer
    包含普通網絡應用程式或功能，例如防火牆、附載平衡器等。
    
2. Control layer
    代表集中式 SDN 控制器軟體，可以稱為SDN中的大腦，管理整個網路的流向和流量。
    
3. Infrastructure layer
    就是由所有的交換器所組成。負責傳輸網路流量。

<!-- 
### 6. 電腦系統的演進趨勢
![](https://i.imgur.com/pdsdN42.png)
![](https://i.imgur.com/qpxQWHU.png)
 -->
 
### 6. SDN的三個特色
1. 平台標準化
每一個switch 都只要懂 openflow的協定就好，不用細分成很多層的switch

2. 軟體平台化
軟體不用對硬體開發，是對平台開發

3. 資訊中心化
軟體可以看到網路的全貌，可以做到全體的最佳化


###### tags: `SDN`