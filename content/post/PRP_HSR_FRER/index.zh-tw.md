+++
date = '2024-11-08T16:14:38+08:00'
title = 'PRP、HSR 與 FRER'
image = "pawel-czerwinski-fnLi5j7kPU4-unsplash.jpg"
categories = [
    "Protocol"
]
+++

# 深入淺出：PRP、HSR 與 FRER —— 高可靠性網路技術全面解析

**這篇文章由 AI 自動產生，尚在整理當中**

在現代工業自動化、交通運輸、能源管理和其他關鍵任務系統中，高可靠性網路是實現穩定運行的基石。針對這些需求，**平行冗餘協議(PRP)**、**高可用性無縫冗餘(HSR)** 和 **幀複製與消除技術(FRER)** 成為不可或缺的技術工具。

這篇文章將探討這三種技術的核心機制、優勢、挑戰及應用場景。

---

## PRP：Parallel Redundancy Protocol

**PRP(Parallel Redundancy Protocol)** 是專為容錯而設計的高可靠性協議，定義在 **IEC 62439-3 標準**當中。主要特點是在 Layer 2 的節點當中進行**雙網平行資料傳輸** ，確保在任意網路故障的情況下通訊不會中斷。

### PRP 的基本概念

1. **雙網路冗餘**：封包在兩個獨立網路(LAN A 和 LAN B)上同步發送。
2. **自動故障隔離**：接收端會選擇最先到達的封包並丟棄重複資料。
3. **即時切換**：在任何單網故障的情況下，通訊不需等待恢復或切換時間。

### PRP 的架構

PRP 在 end nodes 中進行冗餘功能。每個 [DAN](./#dan) 會利用兩個 LAN 進行傳輸，而且這兩個 LAN 不相交且並行運作。當單一介面節點必須連接到兩個網路 (LAN) 時，需使用冗餘盒 (RedBox) 進行資料交換。而 SAN (singly attached node) 則不需連接到兩個 LAN ，只需連接其中一個即可。

由於 RedBox 後面的節點會出現在其他節點(如 DAN)中，因此稱為虛擬 DAN (VDAN)。 RedBox 本身是一個 DAN，代表其 VDAN 的代理。

![PRP](/image002.jpg)

#### DAN

![DAN 的放大圖及 LRE 在 node 當中的位置](/image004.jpg)

每個 PRP Node 都有 2 個乙太網路的介面，稱為 DAN (doubly attached node)，其功能是將 [LRE](./#lre) 一分為二後進行傳輸，以及接收資料後向上將資料回傳給 [LRE](./#lre) 當中。

#### SAN

SAN (singly attached node) 則是只會連接兩個 LAN 當中的其中一個的節點。

#### LRE

LRE (link redundancy entity) 負責管理底下連接埠的資料傳輸功能。當上層協定發送幀時，LRE 複製此幀並同時透過其兩個連接埠發送；接收時節點的 LRE 會將第一個接收到的訊框轉發到其上層，並丟棄重複(比較後到達)的幀。

#### SAN 和 DAN 之間的通訊

SAN 可以連接到任何 LAN。連接到一個 LAN 的 SAN 無法直接與連接到另一個 LAN 的 SAN 通訊。

### PRP 的優勢與限制

**優勢**：

- 零恢復時間，確保通信不中斷。
- 協議無關性，適用於多種高層協議(如 TCP/IP、Profinet)。
- 適合雙網結構的簡單拓撲。

**限制**：

- 硬體成本：需要雙網路接口和額外的網路基礎設施。
- 頻寬消耗：同時傳輸兩份封包增加了網路負載。

### 應用場景

- **工業自動化**：實時控制和 PLC 系統。
- **能源系統**：變電站的 SCADA 通信。
- **醫療設備**：患者監控和生命支持系統。

---

## HSR：高可用性無縫冗餘

**HSR(High-Availability Seamless Redundancy)** 與 PRP 一樣，定義於 **IEC 62439-3 標準**，但它採用**環形網路拓撲**，為節點提供更強的容錯能力。

### HSR 的核心機制

1. **環網資料轉發**：封包在環網中雙向傳輸，每個節點接收資料後再轉發。
2. **冗餘資料處理**：接收端會消除重複資料，確保通信可靠。
3. **即時恢復**：環網結構使得單一節點故障時，資料仍能通過另一方向繼續傳輸。

### 優勢與挑戰

**優勢**：

- 零恢復時間，無需等待故障修復。
- 每個節點既是通信設備也是轉發設備，增加靈活性。

**挑戰**：

- **拓撲限制**：僅適用於環網結構。
- **複雜性增加**：節點數量增多時，管理和排障更加困難。

### 應用場景

- **交通運輸**：鐵路信號、航空管制。
- **智慧城市**：智能路燈和監控系統。
- **能源管理**：電網和可再生能源系統。

---

## FRER：幀複製與消除技術

**FRER(Frame Replication and Elimination for Reliability)** 是由 **IEEE 802.1CB 標準**定義的技術，專注於資料的多路徑冗餘傳輸。與 PRP 和 HSR 不同，FRER 的設計更靈活，適用於複雜的網路拓撲。

### FRER 的核心機制

1. **資料複製與消除**：在傳輸層上複製封包，通過多條路徑發送，接收端根據序列號消除重複資料。
2. **與 TSN 集成**：FRER 可與時間敏感網路(TSN)技術配合，實現更精確的延遲控制和可靠性。

### 優勢與挑戰

**優勢**：

- **靈活性**：不依賴於特定拓撲，適用於多種網路架構。
- **可擴展性**：可與其他 TSN 技術(如優先級調度)結合。
- **低延遲**：針對實時應用進行優化。

**挑戰**：

- **實施門檻**：需支持 IEEE 802.1 標準的硬件。
- **封包管理複雜性**：多路徑設計可能導致封包處理負擔增加。

### 應用場景

- **車載通信**：自動駕駛中的傳感器融合。
- **智慧工廠**：工業 4.0 的實時控制網路。
- **音視頻同步**：專業音頻和視頻傳輸系統。

---

## PRP、HSR 與 FRER 的對比

| 特性         | **PRP**          | **HSR**              | **FRER**                       |
| ------------ | ---------------- | -------------------- | ------------------------------ |
| **標準**     | IEC 62439-3      | IEC 62439-3          | IEEE 802.1CB                   |
| **運作模式** | 雙網平行冗餘     | 環網冗餘             | 多路徑冗餘                     |
| **拓撲要求** | 雙網路           | 環網                 | 支持任意拓撲                   |
| **恢復時間** | 零恢復時間       | 零恢復時間           | 零恢復時間                     |
| **適用場景** | 工業、能源、醫療 | 交通、能源、城市基建 | 車載通信、智慧工廠、音視頻傳輸 |
| **可擴展性** | 中等             | 中等                 | 高                             |

---

## 如何選擇適合的技術？

1. **雙網冗餘場景**：選擇 PRP，適用於簡單雙網結構的應用。
2. **環網拓撲場景**：選擇 HSR，適用於需要節點轉發的場景。
3. **靈活多拓撲場景**：選擇 FRER，特別是在與 TSN 集成的應用中。

---

## 總結

**PRP、HSR 和 FRER** 各有其適用範圍與特點，適合不同的高可靠性需求。PRP 和 HSR 在傳統工業和能源領域中具有穩定的應用，而 FRER 作為現代網路的代表，將在自動駕駛、智慧工廠和音視頻領域發揮越來越重要的作用。

隨著技術的進步，這些解決方案將繼續演進，為我們構建更安全、可靠的未來網路奠定基礎。

## reference

1. [什麼是 HSR/PRP?](https://www.oringnet.com/zh/knowledge-base/what-is-hsr-prp-3)
2. [甚麼是 HSR&PRP?FPGA 實現直通交換與存儲轉發的切換延遲](https://hongtronics.com/hsr-prp-cut-through-switching-store-and-forward/)
3. [Parallel Redundancy Protocol (PRP)](https://www.flexibilis.com/technology/parallel-redundancy-protocol-prp/)
4. [Parallel Redundancy Protocol (PRP) - wireshark](https://wiki.wireshark.org/PRP)
5. [Chapter: High-Availability Seamless Redundancy (HSR)](https://www.cisco.com/c/en/us/td/docs/switches/lan/cisco_ie3X00/software/17_4/b_redundancy_17-4_iot_switch_cg/m_hsr_iosxe_iotswitch.html)
6. Borgohain, R., Roy, M. J., Choudhury, P. P., & Das, R. (2018, October). A brief introduction to high availability seamless redundancy (HSR) and some of its drawbacks: An insight into the functioning of HSR protocol. In 2018 3rd International Conference on Communication and Electronics Systems (ICCES) (pp. 523-527). IEEE.
