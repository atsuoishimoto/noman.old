# ip command

Display and manipulate network interfaces, routing, and tunnels on Linux systems.

## Overview

The `ip` command is a powerful utility for configuring network interfaces, routing tables, and tunnels in Linux. It's part of the iproute2 package and provides more functionality than older networking commands like `ifconfig` and `route`. The command uses a hierarchical structure where objects (like link, address, route) are followed by commands and options.

## Options

### **-s, --stats, --statistics**

Display more information or statistics

```console
$ ip -s link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    RX: bytes  packets  errors  dropped overrun mcast   
    3500       35       0       0       0       0      
    TX: bytes  packets  errors  dropped carrier collsns 
    3500       35       0       0       0       0      
```

### **-c, --color**

Use color output for better readability

```console
$ ip -c addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
```

### **-br, --brief**

Display brief output (one line per object)

```console
$ ip -br addr show
lo               UNKNOWN        127.0.0.1/8 ::1/128 
eth0             UP             192.168.1.10/24 fe80::1234:5678:abcd:ef01/64
```

### **-d, --details**

Show detailed information

```console
$ ip -d link show dev eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff promiscuity 0 
    altname enp0s3
    vlan protocol 802.1Q
    vlan id 1 <REORDER_HDR> 
```

## Usage Examples

### Displaying network interfaces

```console
$ ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
```

### Showing IP addresses

```console
$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.10/24 brd 192.168.1.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::1234:5678:abcd:ef01/64 scope link 
       valid_lft forever preferred_lft forever
```

### Configuring an IP address

```console
$ sudo ip addr add 192.168.1.100/24 dev eth0
```

### Bringing an interface up or down

```console
$ sudo ip link set eth0 up
$ sudo ip link set eth0 down
```

### Displaying routing table

```console
$ ip route show
default via 192.168.1.1 dev eth0 proto static 
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.10
```

### Adding a static route

```console
$ sudo ip route add 10.0.0.0/24 via 192.168.1.254
```

## Tips

### Use Shortcuts for Common Commands

The `ip` command allows shortened versions of its subcommands:
- `ip a` instead of `ip addr show`
- `ip l` instead of `ip link show`
- `ip r` instead of `ip route show`

### Save and Restore Configuration

You can save your current IP configuration and restore it later:

```console
$ ip addr save > ip-config.txt
$ ip addr restore < ip-config.txt
```

### Temporary vs. Permanent Changes

Changes made with the `ip` command are not persistent across reboots. To make permanent changes, modify your distribution's network configuration files.

### Use Namespaces for Network Isolation

Network namespaces allow you to create isolated network environments:

```console
$ sudo ip netns add mynetwork
$ sudo ip netns exec mynetwork ip addr
```

## Frequently Asked Questions

#### Q1. How is `ip` different from `ifconfig`?
A. `ip` is newer, more powerful, and provides more functionality than `ifconfig`. It can manage routing, tunneling, and policy-based routing, while `ifconfig` is limited to basic interface configuration.

#### Q2. How do I check my IP address?
A. Use `ip addr show` or the shorter `ip a` to display all IP addresses on your system.

#### Q3. How do I add a temporary IP address?
A. Use `sudo ip addr add IP_ADDRESS/NETMASK dev INTERFACE`, for example: `sudo ip addr add 192.168.1.100/24 dev eth0`.

#### Q4. How do I check my routing table?
A. Use `ip route show` or the shorter `ip r` to display your routing table.

#### Q5. How do I flush an IP address from an interface?
A. Use `sudo ip addr flush dev INTERFACE`, for example: `sudo ip addr flush dev eth0`.

## References

https://man7.org/linux/man-pages/man8/ip.8.html

## Revisions

2025/05/04 First revision