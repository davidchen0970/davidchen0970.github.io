+++
date = '2024-11-16T13:51:21+08:00'
title = 'mininet commands and parameters'
categories = [
    "SDN"
]
+++


# 軟體定義網路 - Mininet 基本指令與參數介紹 (1-4)

reference:

1. [Day10 菜鳥的Mininet紀錄-Mininet指令](https://ithelp.ithome.com.tw/articles/10243780)
2. [Mininet基本演練
](https://www.kshuang.xyz/doku.php/ccis_lab:sdn:mininet:mininet_basic)
3. [【Mininet指令介紹】](https://tingkuan.wordpress.com/2017/11/09/%E3%80%90mininet%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9%E3%80%91/)
4. [USING GNOME-TERMINAL INSTEAD OF XTERM ON MININET](https://airtoncs.wordpress.com/2014/07/30/using-gnome-terminal-instead-of-xterm-on-mininet/)


----

目錄:

0. Mininet 是甚麼
1. Mininet 的特性
2. 基本 Mininet 指令
<!-- 3. Mininet 參數 -->
---

### 0. Mininet 是甚麼
Mininet是一個網路拓樸模擬器(network emulation orchestration system)，它可以模擬出一整個有路由器、交換器、主機的叢集。 ([reference](https://ithelp.ithome.com.tw/articles/10243028))



### 1. Mininet 的特性

1. 支援OpenFlow
2. 可以自行定義複雜的拓樸
3. 因為是基於Linux開發的，所以具有高硬體移植性。
4. 具有高拓展性
5. 提供Python API，所以可以方必多人協同開發。


### 2. 基本 Mininet 指令

####  1. net



| 圖片                                 | 說明                                                      |
| :------------------------------------: | --------------------------------------------------------- |
| ![](https://i.imgur.com/geqpnSh.png) |列出現在所有節點的資訊。<br> 在此可以看到: <br> <ul style='list-style-position:outside;'><li>有兩台虛擬機h1和h2<li>h1接上的是**eth0**的網路卡，並對接到交換器 s0 的 eth1上。<li>h2接上的也是自己的**eth0**的網路卡，並對接到交換器 s0 的 eth2上。</ul> |


#### 2. nodes

| 圖片                                 | 說明                                                      |
| :------------------------------------: | --------------------------------------------------------- |
| ![](https://i.imgur.com/Xw9LPrK.png) |顯示可用的所有節點。 |

#### 3. links
| 圖片                                 | 說明                                                      |
| :------------------------------------: | --------------------------------------------------------- |
| ![](https://i.imgur.com/RBn9O0s.png) |列出目前的節點連接狀態。 後面的OK代表之間的連線正常。 |


#### 4. ports
| 圖片                                 | 說明                                                      |
| :------------------------------------: | --------------------------------------------------------- |
| ![](https://i.imgur.com/zVQNZvR.png) |查看交換機連接的port |


#### 5. dump
| 圖片                                 | 說明                                                      |
| :------------------------------------: | --------------------------------------------------------- |
| ![](https://i.imgur.com/WuzcpLo.png) |顯示各節點資訊 <br> pid -> process id|


#### 6. intfs
| 圖片                                 | 說明                                                      |
| :------------------------------------: | --------------------------------------------------------- |
| ![](https://i.imgur.com/qsbP3pb.png) |列出各個設備所有的網路介面。|

#### 7. iperf
| 圖片                                 | 說明                                                      |
| :------------------------------------: | --------------------------------------------------------- |
| ![](https://i.imgur.com/j6e1RR1.png) |在兩個節點之間進行 iperf 的測試。|

#### 8. pingall
| 圖片                                 | 說明                                                      |
| :------------------------------------: | --------------------------------------------------------- |
| ![](https://i.imgur.com/EkVaeO5.png) |ping 所有的相連的裝置。|


#### 9. pingallfull
| 圖片                                 | 說明                                                      |
| :------------------------------------: | --------------------------------------------------------- |
| ![](https://i.imgur.com/1L57NVb.png) |顯示詳細資訊的pingall。|



#### 10. exit
| 圖片                                 | 說明                                                      |
| :------------------------------------: | --------------------------------------------------------- |
| ![](https://i.imgur.com/OvN8Jad.png) |離開mininet。|


#### 11. xterm / gterm
使用 xterm {host/switch} 可以打開虛擬的終端，模擬該 switch 或 host 並對他輸入指令。
![](https://i.imgur.com/O4lEsOD.png)

![](https://i.imgur.com/NEkxkFy.png)

<!-- ### 3. Mininet 參數

#### 1. 總覽
`mn [–topo] [–controller] [–link] [–switch] [–mac] [–nat] [–ipbase]`

#### 2. topo -->


###### tags: `SDN` `mininet`
