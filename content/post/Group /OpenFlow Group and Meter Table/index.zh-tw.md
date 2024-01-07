# 軟體定義網路 - OpenFlow 中 Group / Meter Table (2-3)

reference:

1. [2-3 GroupTable and MeterTable](https://www.youtube.com/watch?v=kHdym8hVeFs)
2. [OpenFlow Switch Specification](https://opennetworking.org/wp-content/uploads/2014/10/openflow-switch-v1.3.5.pdf)

----

目錄:

1. [Group Table](#1-Group-Table) 
2. [Meter Table](#2-Meter-Table)

---

### 1. Group Table

以下是 Group Table 的長相 :

| Group Idantifier | Group Type | Counter | Action Buckets|
| -------- | -------- | -------- | -------- |
| ... |... |... |... |
| ... |... |... |... |

* Group Identifier : 是一個 32 bit 的非負整數，用來識別用。
* [Group Type](#11-Group-Type) : 用來決定此 Group 的 semantic。 共有四種。
* Counter : 用來計算此 Group 被使用幾次。
* Action Buckets : 內含一堆 action bucket ，而每個 action bucket 都內含著一系列的 [action](https://hackmd.io/@91UWhfTFSYS7v0K-bURk6A/rylyjGUni#switch-processing) 。

#### 1.1 Group Type
用來決定此 Group 的 semantic。 以下共有四種。



| 名稱 | switch 支援程度 | 解釋 |
| -------- | -------- | -------- |
|  Indirect    |  必須支援   |   <ul style='list-style-position:outside;'><li>去執行 action bucket 裡面的動作。</li><li>此組的 action bucket 只會有一個。</li> </ul>|
|All|  必須支援   |<ul style='list-style-position:outside;'> <li>去執行 action bucket 內**所有的**動作。</li> <li>此組的 action bucket 可以有很多個。</li> </ul>|
|Select|  不一定支援   ||
|fast failover|  不一定支援   ||

#### 1.2 小例子

| Group Idantifier | Group Type | Counter | Action Buckets| 動作解釋 |
| -------- | -------- | -------- | -------- | -------- |
| 7 |Indirect |... |{output 3} | 從 output 3 丟出去 | 
| 8 |All |... |{output 1}, {output 3} | all 會複製封包， 分別在 port 1/3 各傳送一份。|
| 9 |Select |... |{output 1}, {output 3} | 封包會選擇 port 1/3 的其中一個送出去。 |
| 10 |fast failover |... |{output 1}, {output 3} | 預設會先傳送某一個 port ，若發現預設 port 的有問題時，會在不經過 controller 的情況下，直接使用 action bucket 另外一個 port 傳送。|

※ failover : 故障排除


### 2. Meter Table

以下是 Meter Table 的長相 : 

| Meter Identifier | Meter Band | Counter |
| -------- | -------- | -------- |
| ... |{...},{...} |... |
| ... |{...} |... |

#### 2.1 Meter Table -- Meter Band

其中 Meter Band 可以再放大成底下的樣子 : 

| Band Type| Rate     | Burst    | Counters | Type specific arguments |
| -------- | -------- | -------- | -------- | -------- |
| 指定封包要做怎麼樣的處理 | 指定的速率 | 自己設定的單位 | 計數器 |  其他參數|

Meter Band 在 Meter Table 代表的是當此類的封包達到一定的速率後要如何處理，因此會記錄一些重要資訊。

Band Type 在此有兩種處理方式 :

1. drop : 在封包超過一定流量時，直接將封包丟棄。
2. dscp_remark : 當封包超過一定流量時，將封包的優先度降低。




###### tags: `SDN`