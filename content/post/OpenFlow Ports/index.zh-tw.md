# 軟體定義網路 - OpenFlow Ports 介紹  (2-1)

reference:

1. [OpenFlow - wiki - en](https://en.wikipedia.org/wiki/OpenFlow)
2. [OpenFlow](https://zh.wikipedia.org/zh-tw/OpenFlow)
3. [2-1 OpenFlow概述｜OpenFlow Overview](https://www.youtube.com/watch?v=6ZEqeWEAnL4)
4. [區分OpenFlow定義各Port 弄懂軟體定義網路交換器](https://www.netadmin.com.tw/netadmin/zh-tw/technology/FA061FD873454FB2934151DB0A6C89D1?page=2)

----

目錄:
1. OpenFlow 的特性
2. OpenFlow ports
3. 各種保留埠的特性
4. Multiple Controller
5. Controller Connection Faliure
---

### 1. OpenFlow 的特性

1. OpenFlow 是一個在**資料連接層**的通訊協定。
2. 可以控制、定義網路交換器的 forwarding plane 來改變封包所走的網路路徑。
3. OpenFlow 位於 TCP 之上，在TCP port 6653 (舊版:6633)監聽要建立連接的交換器。
4. 轉發規則以 Flow 為單位 (一個flow被定義為:兩台電腦所連接的一個 port)。


#### 1.1 OpenFlow 交換器的基本架構
| 圖片                                 | 說明                                                      |
| :------------------------------------: | --------------------------------------------------------- |
| ![](https://i.imgur.com/kPEyRcA.png) | 主要動作:<br><ul style='list-style-position:outside;'><li>欄位匹配<li>匹配後動作<li>訪問控制器(packet in / out)</ul> |

###### switch processing

* match : 封包進交換器之後會去跟flow table做比對，當比對到時，比對的 flow entry 會寫下要如何進行下一個動作。
* action : 當比對到之後，就會執行之後要做的事情。
* packet in : 當 switch 不知道要如何處理封包的時候，就會執行此動作，詢問 controller 要如何處理此封包。
* packet out : controll 回應 packet in 的相對動作，用來回應 switch 要如何動作。 此地方會有不同方式:
     1. 第一種會請 controller 直接丟封包到某一個 port 就結束。
     2. 第二種會請 controller 再比對此封包一次，比對完之後再根據 flow table 的內容再傳送出去





#### 1.2 controller 和 switch 之間的連線方式

| 圖片 | 連線方式 | 
| :--------: | -------- | 
| ![](https://i.imgur.com/6hzuv5N.png) |  <ul style='list-style-position:outside;'><li>In-Band<li> Out-of-Band</li></ul>    |

* In-Band : 指的是 controller 和 switch 的控制封包走的路徑是和一般封包一樣，因此控制封包會使用 TLS 加密。會使用的port : **LOCAL port**。
* Out-of-Band : 代表有特殊路徑 (port) 來傳送控制封包。會使用的 port : **CONTROLLER port**。


### 2. OpenFlow Ports

#### 2.1 OpenFlow Ports

1. 實體埠 (physical port) : 在乙太網路的交換器上，會直接對應到實際的port。另外可以指定 Queue ID 來區隔 QoS。
2. 邏輯埠 (logical port) : 保留給設備商，讓設備商可以自行定義。這種邏輯性的埠指的是與硬體上無關，而是由軟體定義並且管理的埠，這些埠不見得都是由OpenFlow協定所建立，也可能是其他方式所產生的。 可以指定 Tunnel ID。
3. 保留埠 (reversed port) ： 也是一種 Logical port ，由 OpenFlow 先定義好。(LOCAL、NORMAL、FLOOD可以不支援。)
![](https://i.imgur.com/Hn3jPde.png)

#### 2.2 Port Queues
指的是在某一個 physical port 裡面，設計很多個 queue 來做 QoS ，而不同的 Queue 會有不同的優先權。

### 3. 各種保留埠的特性

#### 3.1 ALL (Required)
| 圖片 | 說明 |
| :--------: | -------- | 
|![](https://i.imgur.com/jlF1GOy.png)|  主要特點:<br><ul style='list-style-position:outside;'><li>對所有的port傳送封包，除了 ingress port(也就是輸入封包的port)</li> </ul> | 



#### 3.2 CONTROLLER (Required)
| 圖片 | 說明 |
| :--------: | -------- | 
|![](https://i.imgur.com/Y9b9zmn.png)|  主要特點:<br><ul style='list-style-position:outside;'><li>是 Out-of-Band 的傳輸模式，由特殊的 port 互相傳輸。</li> </ul> | 

#### 3.3 TABLE (Reqiured)
| 圖片 | 說明 |
| :--------: | -------- | 
|![](https://i.imgur.com/UbRVrID.png)|  主要特點:<br><ul style='list-style-position:outside;'><li>主要用於 packet out，即如果 controller 對 switch 的指令是要 switch [再次比對封包時](#switch-processing)，就會使用到此封包。</li> </ul> | 



#### 3.4 IN_PORT (Required)

| 圖片 | 說明 |
| :--------: | -------- | 
|![](https://i.imgur.com/2SfxJuB.png) |  主要特點:<br><ul style='list-style-position:outside;'><li>會將封包回傳給原本輸入進封包的 port 。</li> </ul> | 


#### 3.6 LOCAL (Optional)
| 圖片 | 說明 |
| :--------: | -------- | 
| ![](https://i.imgur.com/BwyW79a.png) | 主要特點:<br><ul style='list-style-position:outside;'><li>是 In-Band 的傳輸模式，因此會使用 TLS 加密。</li> </ul> | 


#### 3.7 NORMAL (Optional)
| 圖片 | 說明 |
| :--------: | -------- | 
| ![](https://i.imgur.com/T0zRi3S.png) | 主要特點:<br><ul style='list-style-position:outside;'><li>當此port 所傳送的封包所要使用的協定不是OpenFlow時，就會傳送此訊號。</li> </ul> | 

#### 3.7 FLOOD (Optional)
| 圖片 | 說明 |
| :--------: | -------- | 
| ![](https://i.imgur.com/hai16CV.png) | 主要特點:<br><ul style='list-style-position:outside;'><li>當廣播的動作要由其他協定而不是 OpenFlow 做時會使用到此功能。 </li> </ul> | 

### 4. Multiple Controller

#### 4.1 控制器對交換器的三種模式
1. master : 控制器具有完全的控制權 (且唯一)
2. slave : 控制器只會向交換器詢問資料 
3. equal : 控制器具有完全的控制權 (可不唯一) 

### 5. Controller Connection Faliure

#### 5.1 交換器失去與控制器的連線的兩種方式
1. fail secure : 交換器依照失去連接前的flow table 正常運作，但不對控制器再發送任何訊號。
2. fail standalone : 交換器回到 legacy (non-OpenFlow) 模式運作。


###### tags: `SDN`
