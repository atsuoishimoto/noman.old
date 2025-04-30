# ss command

Display socket statistics, providing information about network connections.

## Overview

The `ss` command is a modern replacement for the older `netstat` utility. It displays detailed information about network sockets, showing how your system is connected to other systems or how processes are communicating over the network. It's faster and provides more information than `netstat`, making it valuable for network troubleshooting and monitoring.

## Options

### **-t (--tcp)**

Show only TCP sockets

```console
$ ss -t
State    Recv-Q   Send-Q     Local Address:Port      Peer Address:Port   Process
ESTAB    0        0          192.168.1.5:22          192.168.1.10:52414
ESTAB    0        0          192.168.1.5:22          192.168.1.15:39658
```

### **-u (--udp)**

Show only UDP sockets

```console
$ ss -u
State    Recv-Q   Send-Q     Local Address:Port      Peer Address:Port   Process
UNCONN   0        0          0.0.0.0:68              0.0.0.0:*
UNCONN   0        0          0.0.0.0:5353            0.0.0.0:*
```

### **-l (--listening)**

Display only listening sockets

```console
$ ss -l
Netid    State     Recv-Q    Send-Q       Local Address:Port        Peer Address:Port    Process
tcp      LISTEN    0         128          0.0.0.0:ssh               0.0.0.0:*
tcp      LISTEN    0         5            127.0.0.1:ipp             0.0.0.0:*
```

### **-p (--processes)**

Show process using socket

```console
$ ss -p
State    Recv-Q   Send-Q     Local Address:Port      Peer Address:Port   Process
ESTAB    0        0          192.168.1.5:22          192.168.1.10:52414  users:(("sshd",pid=1234,fd=3))
```

### **-n (--numeric)**

Don't resolve service names (show port numbers instead)

```console
$ ss -tn
State    Recv-Q   Send-Q     Local Address:Port      Peer Address:Port
ESTAB    0        0          192.168.1.5:22          192.168.1.10:52414
```

## Usage Examples

### Viewing all established TCP connections

```console
$ ss -t state established
State    Recv-Q   Send-Q     Local Address:Port      Peer Address:Port   Process
ESTAB    0        0          192.168.1.5:22          192.168.1.10:52414
ESTAB    0        0          192.168.1.5:443         192.168.1.20:60123
```

### Finding which process is using a specific port

```console
$ ss -tlp | grep 80
tcp   LISTEN  0   128   *:80   *:*   users:(("nginx",pid=1234,fd=6))
```

### Displaying socket statistics

```console
$ ss -s
Total: 268
TCP:   16 (estab 2, closed 8, orphaned 0, timewait 0)
Transport Total     IP        IPv6
RAW       0         0         0
UDP       9         6         3
TCP       8         6         2
INET      17        12        5
FRAG      0         0         0
```

## Tips:

### Combine Options for More Specific Output

Combine options like `ss -tuln` to show TCP and UDP listening sockets with numeric ports, which is useful for quick security audits.

### Filter by State

Use `ss state established` to see only active connections, or `ss state time-wait` to see connections in the TIME-WAIT state, helping with connection troubleshooting.

### Filter by Port

Use `ss sport = :22` to see connections to a specific source port, or `ss dport = :80` for destination port, which helps when troubleshooting specific services.

### Memory Usage

The `ss` command uses less memory than `netstat` when displaying the same information, making it more efficient for systems with many connections.

## Frequently Asked Questions

#### Q1. What's the difference between ss and netstat?
A. `ss` is faster, uses less resources, and shows more information than `netstat`. It's designed as a modern replacement with better performance on systems with many connections.

#### Q2. How do I see which process is using a specific port?
A. Use `ss -tlp | grep PORT_NUMBER` to see the process using a specific listening port.

#### Q3. Can I filter connections by IP address?
A. Yes, use `ss dst ADDRESS` to filter by destination IP or `ss src ADDRESS` for source IP.

#### Q4. How do I see only IPv4 or IPv6 connections?
A. Use `ss -4` for IPv4 connections only or `ss -6` for IPv6 connections only.

## References

https://man7.org/linux/man-pages/man8/ss.8.html

## Revisions

- 2025/04/30 First revision