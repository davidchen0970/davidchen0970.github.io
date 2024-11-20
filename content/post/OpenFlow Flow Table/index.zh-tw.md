+++
date = '2024-11-16T14:00:21+08:00'
title = 'OpenFlow Flow Table'
categories = [
    "SDN"
]
+++


# 軟體定義網路 - OpenFlow 中 Flow Table 介紹

reference:

1. [OpenFlow Switch: What Is It and How Does it Work?](https://www.cables-solutions.com/whats-openflow-switch-how-it-works.html)
2. [圖 : Flow Table Packet Processing Pipeline](https://www.researchgate.net/figure/Flow-Table-Packet-Processing-Pipeline-2_fig1_318652506)
3. [2-2 FlowTables](https://www.youtube.com/watch?v=aaPwiyjwrQM&t)
4. [OpenFlow Switch Specification](https://opennetworking.org/wp-content/uploads/2014/10/openflow-switch-v1.3.5.pdf)
5. [圖 : 各版本openflow 的 header 長相](https://download.huawei.com/mdl/image/download?uuid=12ee231f981047fabd03378e1442168f)
6. [OpenFlow 交換器規範 1.3.0 (1)](https://www.jianshu.com/p/acfeae1771b3)
7. [Ryubook 1.0 說明文件](https://book.ryu-sdn.org/zh_tw/html/)

----

目錄:

1. [Open Flow 的架構](#1-Open-Flow-的架構)
2. [Flow Table 和 Flow Entry](#2-Flow-Table-和-Flow-Entry)
3. [Flow Table 欄位](#3-Flow-Table-的欄位)
4. [Action Set 中 Action 的執行順序](#4-Action-Set-中-Action-的執行順序)
---

### 1. Open Flow 的架構
![圖1 : OpenFlow 架構示意圖](https://www.cables-solutions.com/wp-content/uploads/2018/07/what-is-openflow-switch.png)  

<ul style='list-style-position:outside;'><li>在 OpenFlow 的交換器中，最主要的結構就是 Flow Table。<li>Flow Table 彼此具有順序性，封包也被規定不能由後往前傳遞。</ul> 

#### 1.1 Flow Table 的 Pipeline
![圖2: OpenFlow Pipeline 簡易流程圖](https://www.researchgate.net/publication/318652506/figure/fig1/AS:519482711998464@1500865738587/Flow-Table-Packet-Processing-Pipeline-2.png) 

![圖3: OpenFlow Pipeline 詳細流程圖](https://i.imgur.com/MC05Xma.jpg) 

### 2. Flow Table 和 Flow Entry

※此 Flow Table為 OpenFlow 1.3 的樣式，1.0~1.2 版本可以參考 [1](https://support.huawei.com/enterprise/en/doc/EDOC1100196737) [2](https://download.huawei.com/mdl/image/download?uuid=12ee231f981047fabd03378e1442168f) [3](https://davidleitw.github.io/posts/sdn2/#flow-table)

| Match Fields | Priority | Counter | Instructions | Timeouts | Cookie | Flags |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| ... | ... | ... | ... | ... | ... | ... | ... | 

* 整個表會稱為 Flow Table，裡面的每個 row 稱為 Flow Entry。

### 3 Flow Table 的欄位

#### 3.1 各個欄位的作用:

|     名稱     | 解釋|
|:------------:| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Match Fields](https://book.ryu-sdn.org/zh_tw/html/openflow_protocol.html#match) | 要去比對 packet 有沒有符合 flow entry，比對的內容至少有以下: <ul style='list-style-position:outside;'><li>ingress port</li><li>packet header</li> <li>optional metadate from previous table</li></ul>                 |
|   Priority   | flow entry 的優先程度，**數字越高越優先**，最小為零。 |
| Counter | 紀錄以下資訊(當封包mtach時就更新): <ul style='list-style-position:outside;'><li>Received Packet</li><li>Received Data</li><li>Duration(秒數，**一定要紀錄**，指的是 flow entry 存在多久)</li><li>Duration(奈秒)</li></ul> |
|[Instruction](https://book.ryu-sdn.org/zh_tw/html/openflow_protocol.html#instruction)|當封包符合 flow entry 的條件時，所要做的動作，包括以下:<ul style='list-style-position:outside;'><li>Meter : 要去看符合此 Flow Table 的封包量是否已經太多。</li><li>Apply Actions : 馬上對封包進行動作。例如把封包的header改掉，**但不改變 Action set 的內容。** </li><li>Clear/Write Actions (必須):修改封包中 Action set 的內容。</li><li>Write Metadata : 加入一些 metadata 給後面的 flow table 比對用。</li><li>Goto_Table(必須):指示封包之後要往哪一個 flow table 前進。</li><li>flood : 將接收到的封包廣播(除了輸入的 port 以外)</li></ul>|
|Timeouts|標記此 flow entry 甚麼時候要被消除，包含以下兩種形式:<ul style='list-style-position:outside;'><li>idle-timeout : 在閒置多久之後要被消除。</li> <li>hard-timeout : 在經過多少時間之後，不管有沒有閒置都要被消除。</li></ul>|
|Cookie|<ul style='list-style-position:outside;'><li> 在處理封包的時候不會使用到此欄位。</li> <li>opaque data value chosen by the controller. May be used by the controller to filter flow entries affected by flow statistics, flow modification and flow deletion requests.  </li></ul>|
|Flags| 用來改變 flow entry 的管理方式，例如 OFPFF_SEND_FLOW_REM 會觸發到刪除此 flow entry 的 message。 |

#### 3.2 Flow Table 管線處理流程

![圖4: Flow Table 管線處理流程](https://i.imgur.com/JnHJVhP.jpg)

- 封包一定要從 table 0 開始比對。
- **由 priority 高的開始比對**。

#### 3.3 Table Miss Entry

以下是某個 Flow Table :

| Match Fields | Priority | Counter | Instructions | Timeouts | Cookie | Flags |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| ... | ... | ... | ... | ... | ... | ... | ... | 
| ANY | 0 | ... | ... | ... | ... | ... | ... | 
| ... | ... | ... | ... | ... | ... | ... | ... | 

由上表可以看到，Table Miss Entry 所使用的 Match Feild 是 ANY，且因為是最後比的，因此 Priority 是最低的 0 。

### 4. Action Set 中 [Action](https://book.ryu-sdn.org/zh_tw/html/openflow_protocol.html#action) 的執行順序



| 順位 | 名稱 | 功能 |
| -------- | -------- | -------- |
|1.|copy [TTL]() inwards|
|2.|pop|
|3.|push-[MPLS](https://www.google.com/search?q=MPLS&sourceid=chrome&ie=UTF-8)| 
|4.|push-PBB|
|5.|push-VLAN|
|6.|copy TTL|
|7.|decrement TTL| TTL-=1|
|8.|set (set-field) | 修改封包內的某些欄位 |
|9.|qos (set-queue) | 寫入一個 queue id 進到指定封包內 |
|10.|group|如果有指定 group action ，就依照 group table 內的指令做 |
|11.|output| 如果沒有指定 group action，則在 output action 指定的 port 轉發 packet。|

- <span id="TTL"> TTL </span> : Time To Live 
指一個封包在經過一個路由器時，可傳遞的最長距離（躍點數）。目的是防止封包因不正確的路由表等原因造成的無限循環而無法送達及耗盡網路資源。

###### tags: `SDN`
