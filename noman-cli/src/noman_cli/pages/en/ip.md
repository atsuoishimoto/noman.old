# ip command

Display and manipulate network interfaces, routing, and tunnels on Linux systems.

## Overview

The `ip` command is a powerful utility for configuring network interfaces, routing tables, and tunnels on Linux systems. It's part of the iproute2 package and provides more functionality than older networking commands like `ifconfig` and `route`. The command follows a structured syntax where you specify an object (like link, address, route) followed by an action (like show, add, delete).

## Options

### **ip addr** - Manage IP addresses

Shows or modifies IP addresses assigned to network interfaces.

```console
$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:b6:43:c5 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0
       valid_lft forever preferred_lft forever
```

### **ip link** - Manage network interfaces

Shows or modifies network interface attributes.

```console
$ ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:b6:43:c5 brd ff:ff:ff:ff:ff:ff
```

### **ip route** - Manage routing table

Shows or modifies the routing table entries.

```console
$ ip route show
default via 192.168.1.1 dev eth0 
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```

### **ip neigh** - Manage ARP table

Shows or modifies the neighbor/ARP table entries.

```console
$ ip neigh show
192.168.1.1 dev eth0 lladdr 00:11:22:33:44:55 REACHABLE
192.168.1.5 dev eth0 lladdr aa:bb:cc:dd:ee:ff STALE
```

## Usage Examples

### Adding an IP address to an interface

```console
$ sudo ip addr add 192.168.1.200/24 dev eth0
```

### Bringing an interface up or down

```console
$ sudo ip link set eth0 up
$ sudo ip link set eth0 down
```

### Adding a static route

```console
$ sudo ip route add 10.0.0.0/24 via 192.168.1.1
```

### Flushing all addresses on an interface

```console
$ sudo ip addr flush dev eth0
```

## Tips

### Use -c for Colorized Output

The `-c` option provides colorized output, making it easier to read:

```console
$ ip -c addr show
```

### Brief Output Format

Use `-br` for brief output that's easier to parse:

```console
$ ip -br addr show
lo               UNKNOWN        127.0.0.1/8
eth0             UP             192.168.1.100/24
```

### Save and Restore Configuration

You can save your IP configuration and restore it later:

```console
$ ip addr save > ip-config.txt
$ ip addr restore < ip-config.txt
```

### Temporary Configuration

Changes made with the `ip` command are not persistent across reboots. To make permanent changes, modify your distribution's network configuration files.

## Frequently Asked Questions

#### Q1. How is `ip` different from `ifconfig`?
A. `ip` is newer, more powerful, and provides more functionality than `ifconfig`. It can manage routing tables, ARP tables, tunnels, and more, all in one command.

#### Q2. How do I see my IP address?
A. Use `ip addr show` to see all IP addresses, or `ip -br addr` for a more concise view.

#### Q3. How do I add a temporary IP address?
A. Use `sudo ip addr add 192.168.1.200/24 dev eth0` to add an IP address to interface eth0.

#### Q4. How do I change my default gateway?
A. First delete the current default route with `sudo ip route del default`, then add a new one with `sudo ip route add default via 192.168.1.1`.

#### Q5. Are changes made with `ip` permanent?
A. No, changes made with the `ip` command are lost after a reboot. To make permanent changes, modify your distribution's network configuration files.

## References

https://man7.org/linux/man-pages/man8/ip.8.html

## Revisions

- 2025/04/30 First revision