# ss command

Display socket statistics, providing information about network connections.

## Overview

The `ss` command is a utility for investigating sockets, showing information about network connections, routing tables, and network interfaces. It's a more powerful and faster alternative to the older `netstat` command, offering detailed insights into TCP, UDP, and other socket connections on a system.

## Options

### **-a, --all**

Show both listening and non-listening sockets

```console
$ ss -a
Netid  State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port  Process
u_str  ESTAB   0       0       * 19350               * 19351
u_str  ESTAB   0       0       * 18935               * 18936
tcp    LISTEN  0       4096    127.0.0.1:5432       0.0.0.0:*
tcp    ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
udp    UNCONN  0       0       0.0.0.0:68           0.0.0.0:*
```

### **-l, --listening**

Display only listening sockets

```console
$ ss -l
Netid  State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port  Process
tcp    LISTEN  0       4096    127.0.0.1:5432       0.0.0.0:*
tcp    LISTEN  0       128     0.0.0.0:22           0.0.0.0:*
tcp    LISTEN  0       511     0.0.0.0:80           0.0.0.0:*
```

### **-t, --tcp**

Display only TCP sockets

```console
$ ss -t
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
ESTAB   0       0       192.168.1.5:49834    151.101.65.69:443
```

### **-u, --udp**

Display only UDP sockets

```console
$ ss -u
State    Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
UNCONN   0       0       0.0.0.0:68           0.0.0.0:*
UNCONN   0       0       0.0.0.0:5353         0.0.0.0:*
```

### **-p, --processes**

Show process using socket

```console
$ ss -tp
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port   Process
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721  users:(("sshd",pid=1234,fd=3))
```

### **-n, --numeric**

Don't resolve service names (show port numbers instead)

```console
$ ss -tn
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
LISTEN  0       128     0.0.0.0:22           0.0.0.0:*
```

### **-i, --info**

Show internal TCP information

```console
$ ss -ti
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
         cubic wscale:7,7 rto:204 rtt:0.98/0.49 ato:40 mss:1448 cwnd:10 bytes_acked:1448 segs_out:2 segs_in:1
```

## Usage Examples

### Showing all TCP connections

```console
$ ss -ta
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
LISTEN  0       128     0.0.0.0:22           0.0.0.0:*
LISTEN  0       511     0.0.0.0:80           0.0.0.0:*
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
```

### Filtering connections by port

```console
$ ss -t '( dport = :ssh or sport = :ssh )'
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
```

### Showing socket summary statistics

```console
$ ss -s
Total: 187
TCP:   12 (estab 3, closed 0, orphaned 0, timewait 0)
Transport Total     IP        IPv6
RAW       0         0         0
UDP       8         5         3
TCP       12        9         3
INET      20        14        6
FRAG      0         0         0
```

## Tips:

### Combine Options for Detailed Output

Combine options like `ss -tuln` to show TCP and UDP listening sockets with numeric ports, which is useful for quickly checking what services are running on your system.

### Use with grep for Filtering

Pipe `ss` output to `grep` to filter for specific connections: `ss -ta | grep ESTABLISHED` to see only active connections.

### Monitor Connections in Real-time

Use `watch ss -ta` to monitor connections in real-time with updates every 2 seconds, helpful for troubleshooting network issues.

### Check for Connection Issues

Use `ss -tan state time-wait` or `ss -tan state close-wait` to identify potentially problematic connections that aren't closing properly.

## Frequently Asked Questions

#### Q1. What's the difference between `ss` and `netstat`?
A. `ss` is faster and provides more detailed information than `netstat`. It reads information directly from the kernel rather than from `/proc` files, making it more efficient, especially on systems with many connections.

#### Q2. How can I see which process is using a specific port?
A. Use `ss -tlp` to see listening TCP sockets with their associated processes. You may need to run this as root to see all process information.

#### Q3. How do I filter connections by IP address?
A. Use `ss` with filter expressions: `ss -t dst 192.168.1.10` to show TCP connections to that IP address.

#### Q4. Can I see connection timing information?
A. Yes, use `ss -ti` to display detailed TCP metrics including round-trip time (RTT) and retransmission timeout (RTO).

## References

https://man7.org/linux/man-pages/man8/ss.8.html

## Revisions

- 2025/05/04 First revision