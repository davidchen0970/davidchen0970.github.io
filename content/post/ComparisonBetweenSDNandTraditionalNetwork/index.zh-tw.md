+++  
date = '2024-11-11T22:11:02+08:00'  
title = 'Comparison Between SDN and Traditional Network'  
categories = [
"SDN"
]
+++

# 軟體定義網路（SDN）與傳統網路架構的比較

原始連結: [Link](https://hackmd.io/@91UWhfTFSYS7v0K-bURk6A/r1WWxc8Ko)

**Reference**:

1. [1-1 傳統網路的演進與 SDN 的崛起｜ Architecture of Traditional Network and Emergence of SDN](https://youtu.be/pIU-3gzlu9I)
2. [TCP/IP，網際網路的基礎通訊架構](https://ithelp.ithome.com.tw/articles/10267704)

### 目錄

1. 傳統網路架構概述
2. SDN 嘗試解決的問題(傳統 Internet 的既有限制)

## 傳統網路架構

在早期網際網路的發展中，為了讓多台電腦能夠彼此溝通，建立在**TCP/IP 協議**基礎上的傳統網路架構誕生了。這種架構具備以下特徵：

1. **通訊協議的重要性**  
   兩台電腦或多台電腦需要可以共同溝通時，必須要有相同的 protocol。

2. **網路架構形式**  
   網路中的設備可以採用以下兩種架構之一：

   - **主從式架構（Client-Server）**：由伺服器提供服務，客戶端發起請求。
   - **對等式架構（Peer-to-Peer）**：所有節點平等，彼此直接傳遞資料。

3. **基礎設備需求**  
   傳輸資料需要依賴網路設備，例如：
   - **交換器（Switch）**：用於內部網路中的資料交換。
   - **路由器（Router）**：管理網路間的資料流動。
   - **集線器**

這些設備通常由網路供應商（ISP）部署於其資料中心內，構成整體的網路基礎設施。

![圖1: 傳統網路架構示意圖](https://ithelp.ithome.com.tw/upload/images/20210919/20128159lPmUQe3GJx.jpg)

## SDN 想解決網路設備的甚麼問題

隨著網路需求不斷增長，傳統網路架構的侷限逐漸明顯。**軟體定義網路（SDN）**作為新一代網路架構，針對以下問題提供了解決方法：

### 1. 缺乏彈性（Inflexibility）

傳統網路的硬體設備安裝後，通常很少進行調整或變更，原因在於：

- 設備配置複雜且靜態。
- 網路拓撲固定，難以快速響應變化的需求。

**SDN 的解決方式**：  
通過將 Control Plane 與 Data Plane 分離，SDN 可以更動態地控制網路流量。

---

### 2. 供應商鎖定（Vendor Lock-In）

傳統網路設備通常由單一供應商提供，擴展時可能面臨以下問題：

- 與其他供應商設備的相容性低。
- 原供應商的解決方案最適合原始架構，導致難以更換供應商。

**SDN 的解決方式**：  
SDN 採用開放式標準，允許不同品牌的設備共同運作，減少對單一供應商的依賴。
