+++
date = '2024-11-11T16:37:14+08:00'
title = 'MPTCP Experiment 1'
image = "pawel-czerwinski-V10CV7MBdhc-unsplash.jpg"
categories = [
    "MPTCP","Protocol"
]
description = "Using MPTCP to create a topology with three connections between two hosts over a single route."
+++

# MPTCP - Experiment Record

## 1. Experiment Name

MPTCP Three-Path Experiment

## 2. Experiment Objective

Using MPTCP to create a topology with three connections between two hosts over a single route.

## 3. Experiment Methodology

1. Create topology using a script

   ![Figure 1: Experiment Topology](/topo.png)

   ```cpp
   #!/usr/bin/python

   import argparse
   from mininet.net import Mininet
   from mininet.node import RemoteController, OVSKernelSwitch, Host
   from mininet.cli import CLI
   from mininet.link import TCLink, Intf
   from mininet.log import setLogLevel, info
   from subprocess import call, check_call


   def configure_local_mptcp(enable_mptcp):
       """
       Configure MPTCP on the local machine.
       :param enable_mptcp: True to enable MPTCP, False to skip.
       """
       if enable_mptcp:
           try:
               info("Configuring local MPTCP (mptcp_enabled=1)...\n")
               check_call(["sudo", "sysctl", "net.mptcp.mptcp_enabled=1"])
           except Exception as e:
               info(f"Failed to configure local MPTCP: {e}\n")
       else:
           try:
               info("Configuring local MPTCP (mptcp_enabled=0)...\n")
               check_call(["sudo", "sysctl", "net.mptcp.mptcp_enabled=0"])
           except Exception as e:
               info(f"Failed to configure local MPTCP: {e}\n")


   def myNetwork(enable_mptcp):
       # Configure MPTCP on the local machine if enabled
       configure_local_mptcp(enable_mptcp)

       # Create Mininet
       net = Mininet(topo=None, build=False, ipBase='10.0.0.0/8')

       info('*** Adding controller\n')

       # Add hosts and router
       h1 = net.addHost('h1')
       h2 = net.addHost('h2')
       r1 = net.addHost('r1')

       # Set bandwidth to 10Mbps
       linkopt = {'bw': 10}

       # Add multiple links between h1, h2, and r1
       net.addLink(r1, h1, cls=TCLink, **linkopt)
       net.addLink(r1, h1, cls=TCLink, **linkopt)
       net.addLink(r1, h1, cls=TCLink, **linkopt)
       net.addLink(r1, h2, cls=TCLink, **linkopt)
       net.addLink(r1, h2, cls=TCLink, **linkopt)
       net.addLink(r1, h2, cls=TCLink, **linkopt)

       net.build()

       # Set all interfaces' IPs to 0 in preparation for manual IP allocation
       r1.cmd("ifconfig r1-eth0 0")
       r1.cmd("ifconfig r1-eth1 0")
       r1.cmd("ifconfig r1-eth2 0")
       r1.cmd("ifconfig r1-eth3 0")
       r1.cmd("ifconfig r1-eth4 0")
       r1.cmd("ifconfig r1-eth5 0")

       h1.cmd("ifconfig h1-eth0 0")
       h1.cmd("ifconfig h1-eth1 0")
       h1.cmd("ifconfig h1-eth2 0")

       h2.cmd("ifconfig h2-eth0 0")
       h2.cmd("ifconfig h2-eth1 0")
       h2.cmd("ifconfig h2-eth2 0")

       # Enable IP forwarding to allow r1 to route packets
       r1.cmd("echo 1 > /proc/sys/net/ipv4/ip_forward")

       info('*** Configuring MPTCP for Mininet hosts...\n')
       if enable_mptcp:
           for host in [h1, h2]:
               host.cmd("sysctl -w net.mptcp.mptcp_enabled=1")
               host.cmd("sysctl -w net.mptcp.mptcp_debug=0")
               host.cmd("sysctl -w net.mptcp.mptcp_path_manager=fullmesh")
       else:
           for host in [h1, h2]:
               host.cmd("sysctl -w net.mptcp.mptcp_enabled=0")
               host.cmd("sysctl -w net.mptcp.mptcp_debug=0")

       # Assign IP addresses to r1, h1, and h2
       r1.cmd("ifconfig r1-eth0 10.0.0.1 netmask 255.255.255.0")
       r1.cmd("ifconfig r1-eth1 10.0.1.1 netmask 255.255.255.0")
       r1.cmd("ifconfig r1-eth2 10.0.2.1 netmask 255.255.255.0")
       r1.cmd("ifconfig r1-eth3 10.0.3.1 netmask 255.255.255.0")
       r1.cmd("ifconfig r1-eth4 10.0.4.1 netmask 255.255.255.0")
       r1.cmd("ifconfig r1-eth5 10.0.5.1 netmask 255.255.255.0")

       h1.cmd("ifconfig h1-eth0 10.0.0.2 netmask 255.255.255.0")
       h1.cmd("ifconfig h1-eth1 10.0.1.2 netmask 255.255.255.0")
       h1.cmd("ifconfig h1-eth2 10.0.2.2 netmask 255.255.255.0")

       h2.cmd("ifconfig h2-eth0 10.0.3.2 netmask 255.255.255.0")
       h2.cmd("ifconfig h2-eth1 10.0.4.2 netmask 255.255.255.0")
       h2.cmd("ifconfig h2-eth2 10.0.5.2 netmask 255.255.255.0")

       # Set up multi-path routing for h1
       h1.cmd("ip rule add from 10.0.0.2 table 1")
       h1.cmd("ip rule add from 10.0.1.2 table 2")
       h1.cmd("ip rule add from 10.0.2.2 table 3")
       h1.cmd("ip route add 10.0.0.0/24 dev h1-eth0 scope link table 1")
       h1.cmd("ip route add 10.0.1.0/24 dev h1-eth1 scope link table 2")
       h1.cmd("ip route add 10.0.2.0/24 dev h1-eth2 scope link table 3")
       h1.cmd("ip route add default via 10.0.0.1 dev h1-eth0 table 1")
       h1.cmd("ip route add default via 10.0.1.1 dev h1-eth1 table 2")
       h1.cmd("ip route add default via 10.0.2.1 dev h1-eth2 table 3")
       h1.cmd("ip route add default scope global nexthop via 10.0.0.1 dev h1-eth0")

       # Set up multi-path routing for h2
       h2.cmd("ip rule add from 10.0.3.2 table 1")
       h2.cmd("ip rule add from 10.0.4.2 table 2")
       h2.cmd("ip rule add from 10.0.5.2 table 3")
       h2.cmd("ip route add 10.0.3.0/24 dev h2-eth0 scope link table 1")
       h2.cmd("ip route add 10.0.4.0/24 dev h2-eth1 scope link table 2")
       h2.cmd("ip route add 10.0.5.0/24 dev h2-eth2 scope link table 3")
       h2.cmd("ip route add default via 10.0.3.1 dev h2-eth0 table 1")
       h2.cmd("ip route add default via 10.0.4.1 dev h2-eth1 table 2")
       h2.cmd("ip route add default via 10.0.5.1 dev h2-eth2 table 3")
       h2.cmd("ip route add default scope global nexthop via 10.0.3.1 dev h2-eth0")

       info('*** Post configure nodes\n')
       CLI(net)
       net.stop()


    if __name__ == '__main__':
       parser = argparse.ArgumentParser(description="Mininet MPTCP Setup Script")
       parser.add_argument('-m', '--mptcp', action='store', default='0', choices=['0', '1'],
                           help="Enable MPTCP if set to 1. Default is 0 (disabled).")
       args = parser.parse_args()
       setLogLevel('info')
       myNetwork(enable_mptcp=(args.mptcp == '1'))
   ```

2. Conduct the experiment

## 4. Results and Analysis

1. Without MPTCP

   ![Figure 2: Results without MPTCP](/result_without_MPTCP.png)

2. With MPTCP

   ![Figure 3: Results with MPTCP](/result_with_MPTCP.png)

## 5. Conclusion

## 6. References

1. [MPTCP Protocol Parameter Analysis](https://blog.csdn.net/asddasads/article/details/110678627)
2. [MPTCP Performance Testing in Mininet](https://blog.csdn.net/asddasads/article/details/110678705)

```

```
