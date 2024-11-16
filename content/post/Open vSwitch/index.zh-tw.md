+++
date = '2024-11-16T12:51:21+08:00'
title = 'Open vSwitch'
categories = [
    "SDn"
]
+++


# 軟體定義網路 - Open vSwitch (1-3)

reference:
1. [在 OpenWRT 上架設 Open vSwitch (OVS)](https://openwrt-nctu.gitbook.io/project/experiment-sdn/ovs-on-openwrt)
2. [Open vSwitch](https://www.youtube.com/watch?v=-jX4ce_WaOM)

---

目錄:
1. Open vSwitch


---

### 1. Open vSwitch
1. 是一種虛擬交換器，目的是實現網路的虛擬化
2. 可以用來作為 L2 Switch，或其他層的 Switch
3. 支援 OpenFlow 協定
4. 針對 Linux 核心開發

### 2. Open vSwitch 的特性
![](https://i.imgur.com/gjlrCqx.png)
    1. 成本低
    2. 工作效率高
    3. 占用資源小
    4. 配置靈活性高

### 3. Open vSwitch 架構
<!--     ![](https://i.imgur.com/tO5EZvx.png) -->
![](https://i.imgur.com/bCnpF6C.png)

ovs-vswitchd ${\to}$ switch 的邏輯運作 、 control plane 的抽象化，提供像 OpenFlow 的介面，可以跟外部的控制器連接。
ovsdb-server ${\to}$ 管理輕量級的資料庫:ovsdb，存放資料轉發的規則表(flow-table)，裡面的規則稱作 : flow-role
openvswitch.ko ${\to}$ep su3 負責資料轉發層的 data plane 的工作，




###### tags: `SDN`