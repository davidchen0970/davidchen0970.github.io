# 軟體定義網路 - OpenFlow Protocol (2-4)

reference:

1. [OpenFlow Switch Specification](https://opennetworking.org/wp-content/uploads/2014/10/openflow-switch-v1.3.5.pdf)
2. [2-4 OpenFlow Switch Protocol](https://www.youtube.com/watch?v=dYE_AVoXtgA)

----

目錄:

1. OpenFlow Header
2. OpenFlow 交換器協定的三種分群
---

### 1. OpenFlow Header

| 其他 protocol 的 header | Version  |   Type   |  Length  | Transaction ID |
| ---------- | -------- | -------- | -------- | -------- |
|    ....    |   ....   |    ..    |   ...    |   ....   |

以下分別介紹 : 

| 欄位 | 長度 (bit) | 說明 |
| -------- | -------- | -------- |
|Version|8| OpenFlow Protocol 的[版本](#OpenFlow-版本及版本代碼對照表) |
|Type|8||
|Length|16|用來標記 OpenFlow 信令實際內容長度 |
|Transaction ID|32|標記溝通的順序，幫助controller 和 switch 知道溝通的訊息|

### 2. OpenFlow 交換器協定的三種分群

分群的意義就是把 controller 與 switch 的訊息方向。

1. 對稱 (Symmetric)
2. 控制器到交換器 (Controller-to-switch)
3. 非同步 (Asynchronous)

#### 2.1 對稱 (Symmetric)
代表 Controller 與 Switch 之間的溝通是雙向的。**兩者都可以直接發起信令**，無須任何請求。裡面含有三種信令:

1. Hello 
2. Echo
3. Experimenter

#### 2.2 控制器到交換器 (Controller-to-switch)
信令由 **controller** 發起，通常用於管理或檢查 switch 的狀態。

#### 2.3 非同步 (Asynchronous)
信令由 **Switch** 發起，通常用於更新 controller 的狀態及更新與 controller 有關的網路事件。

#### OpenFlow 版本及版本代碼對照表

| OpenFlow 版本 | 版本代碼 |
| ------------- | -------- |
| 1.0.0         | 0X01     |
| 1.1.0         | 0X02     |
| 1.2.0         | 0X03     |
| 1.3.0         | 0X04     |
| 1.4.0         | 0X05     |
| 1.5.0         | 0X06     |


###### tags: `SDN`