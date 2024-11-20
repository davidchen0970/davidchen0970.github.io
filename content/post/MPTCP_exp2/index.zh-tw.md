+++
date = '2024-11-20T17:38:06+08:00'
draft = true
title = 'MPTCP_exp2'
image = "pawel-czerwinski-V10CV7MBdhc-unsplash.jpg"
categories = [
    "MPTCP","Protocol"
]
description = "修改原本的 router ，改成相同網域的 switch"
+++

# MPTCP - 實驗記錄 2

## 1. 實驗名稱

MPTCP 三路徑實驗 - 相同網域使用 switch 


## 2. 實驗目標

利用 MPTCP 做出在兩個 host 中利用一個 switch 實作出具有三條連線的拓樸。

## 3. 實驗方法

1. 利用 script 建立拓樸

   ![圖1: 實驗拓樸](/topo.png)

    ```cpp
    #!/usr/bin/python

    from mininet.net import Mininet
    from mininet.node import Host,  OVSKernelSwitch
    from mininet.cli import CLI
    from mininet.link import TCLink, Intf
    from mininet.log import setLogLevel, info
    from subprocess import call


    def myNetwork():

        net = Mininet(topo=None,
                        build=False,
                        ipBase='10.0.0.0/8')

        info( '*** Adding controller\n' )
        info( '*** Add switches/APs\n')
        s1  = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')

        info( '*** Add hosts/stations\n')
        h1 = net.addHost('h1', cls=Host)
        h2 = net.addHost('h2', cls=Host)

        info( '*** Add links\n')
        linkopt = {'bw': 10}

        net.addLink(s1, h1, cls=TCLink, **linkopt)
        net.addLink(s1, h1, cls=TCLink, **linkopt)
        net.addLink(s1, h1, cls=TCLink, **linkopt)
        net.addLink(s1, h2, cls=TCLink, **linkopt)
        net.addLink(s1, h2, cls=TCLink, **linkopt)
        net.addLink(s1, h2, cls=TCLink, **linkopt)

        info( '*** Starting network\n')
        net.build()
        info( '*** Starting controllers\n')
        for controller in net.controllers:
            controller.start()

        info( '*** Starting switches/APs\n')
        net.get('s1').start([])

        info( '*** Post configure nodes\n')
        s1.cmd("ifconfig s1-eth1 0")
        s1.cmd("ifconfig s1-eth2 0")
        s1.cmd("ifconfig s1-eth3 0")
        s1.cmd("ifconfig s1-eth4 0")
        s1.cmd("ifconfig s1-eth5 0")
        s1.cmd("ifconfig s1-eth6 0")

        h1.cmd("ifconfig h1-eth0 0")
        h1.cmd("ifconfig h1-eth1 0")
        h1.cmd("ifconfig h1-eth2 0")

        h2.cmd("ifconfig h2-eth0 0")
        h2.cmd("ifconfig h2-eth1 0")
        h2.cmd("ifconfig h2-eth2 0")

        h1.cmd("ifconfig h1-eth0 10.0.0.1 netmask 255.255.255.0")
        h1.cmd("ifconfig h1-eth1 10.0.0.2 netmask 255.255.255.0")
        h1.cmd("ifconfig h1-eth2 10.0.0.3 netmask 255.255.255.0")

        h2.cmd("ifconfig h2-eth0 10.0.0.4 netmask 255.255.255.0")
        h2.cmd("ifconfig h2-eth1 10.0.0.5 netmask 255.255.255.0")
        h2.cmd("ifconfig h2-eth2 10.0.0.6 netmask 255.255.255.0")

        # Add MPTCP configurations

        h1.cmd("ip rule add from 10.0.0.1 table 1")
        h1.cmd("ip rule add from 10.0.0.2 table 2")
        h1.cmd("ip rule add from 10.0.0.3 table 3")
        h1.cmd("ip route add 10.0.0.0/24 dev h1-eth0 scope link table 1")
        h1.cmd("ip route add 10.0.0.0/24 dev h1-eth1 scope link table 2")
        h1.cmd("ip route add 10.0.0.0/24 dev h1-eth2 scope link table 3")
        h1.cmd("ip route add default via 10.0.0.1 dev h1-eth0 table 1")
        h1.cmd("ip route add default via 10.0.0.1 dev h1-eth1 table 2")
        h1.cmd("ip route add default via 10.0.0.1 dev h1-eth2 table 3")

        h2.cmd("ip rule add from 10.0.0.4 table 1")
        h2.cmd("ip rule add from 10.0.0.5 table 2")
        h2.cmd("ip rule add from 10.0.0.6 table 3")
        h2.cmd("ip route add 10.0.0.0/24 dev h2-eth0 scope link table 1")
        h2.cmd("ip route add 10.0.0.0/24 dev h2-eth1 scope link table 2")
        h2.cmd("ip route add 10.0.0.0/24 dev h2-eth2 scope link table 3")
        h2.cmd("ip route add default via 10.0.0.4 dev h2-eth0 table 1")
        h2.cmd("ip route add default via 10.0.0.4 dev h2-eth1 table 2")
        h2.cmd("ip route add default via 10.0.0.4 dev h2-eth2 table 3")


        CLI(net)
        net.stop()


    if __name__ == '__main__':
        setLogLevel( 'info' )
        myNetwork()
    ```
2. 執行實驗

## 4. 實驗結果、分析

1. 沒開 MPTCP

   ![圖2: 沒有開啟 MPTCP 的實驗結果](/result_without_MPTCP.png)

2. 有開 MPTCP

   ![圖3: 開啟 MPTCP 之後的實驗結果](/result_with_MPTCP.png)

## 5. 結論

MPTCP 可以在相同 LAN 當中進行多路徑傳輸，提升網路傳輸效率。

## 6. 參考資料

1. [mptcp 协议参数解析](https://blog.csdn.net/asddasads/article/details/110678627)
2. [MPTCP 协议在 mininet 中的性能测试](https://blog.csdn.net/asddasads/article/details/110678705)
