# ping command

Send ICMP ECHO_REQUEST packets to network hosts to verify connectivity.

## Overview

The `ping` command is a network diagnostic tool that tests the reachability of a host on an IP network. It measures the round-trip time for messages sent from the originating host to a destination computer and back. Ping works by sending Internet Control Message Protocol (ICMP) Echo Request packets to the target host and waiting for an ICMP Echo Reply.

## Options

### **-c count** / **--count=count**

Stop after sending (and receiving) count ECHO_REQUEST packets.

```console
$ ping -c 4 google.com
PING google.com (142.250.190.78) 56(84) bytes of data.
64 bytes from lga25s74-in-f14.1e100.net (142.250.190.78): icmp_seq=1 ttl=116 time=15.2 ms
64 bytes from lga25s74-in-f14.1e100.net (142.250.190.78): icmp_seq=2 ttl=116 time=14.8 ms
64 bytes from lga25s74-in-f14.1e100.net (142.250.190.78): icmp_seq=3 ttl=116 time=15.0 ms
64 bytes from lga25s74-in-f14.1e100.net (142.250.190.78): icmp_seq=4 ttl=116 time=14.9 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 14.816/14.979/15.201/0.158 ms
```

### **-i interval** / **--interval=interval**

Wait interval seconds between sending each packet. The default is to wait for one second between each packet.

```console
$ ping -c 3 -i 2 example.com
PING example.com (93.184.216.34) 56(84) bytes of data.
64 bytes from 93.184.216.34: icmp_seq=1 ttl=56 time=11.8 ms
64 bytes from 93.184.216.34: icmp_seq=2 ttl=56 time=12.1 ms
64 bytes from 93.184.216.34: icmp_seq=3 ttl=56 time=11.9 ms

--- example.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 4005ms
rtt min/avg/max/mdev = 11.823/11.941/12.102/0.115 ms
```

### **-t ttl** / **--ttl=ttl**

Set the IP Time to Live (TTL) for outgoing packets.

```console
$ ping -c 2 -t 64 github.com
PING github.com (140.82.114.3) 56(84) bytes of data.
64 bytes from 140.82.114.3: icmp_seq=1 ttl=64 time=29.7 ms
64 bytes from 140.82.114.3: icmp_seq=2 ttl=64 time=29.5 ms

--- github.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 29.532/29.636/29.741/0.104 ms
```

### **-s packetsize** / **--size=packetsize**

Specifies the number of data bytes to be sent. The default is 56, which translates into 64 ICMP data bytes when combined with the 8 bytes of ICMP header data.

```console
$ ping -c 2 -s 100 cloudflare.com
PING cloudflare.com (104.16.132.229) 100(128) bytes of data.
108 bytes from 104.16.132.229: icmp_seq=1 ttl=57 time=10.3 ms
108 bytes from 104.16.132.229: icmp_seq=2 ttl=57 time=10.1 ms

--- cloudflare.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 10.143/10.245/10.348/0.102 ms
```

## Usage Examples

### Basic Connectivity Test

```console
$ ping google.com
PING google.com (142.250.190.78) 56(84) bytes of data.
64 bytes from lga25s74-in-f14.1e100.net (142.250.190.78): icmp_seq=1 ttl=116 time=15.2 ms
64 bytes from lga25s74-in-f14.1e100.net (142.250.190.78): icmp_seq=2 ttl=116 time=14.8 ms
^C
--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 14.816/15.008/15.201/0.192 ms
```

### Checking Network Latency

```console
$ ping -c 5 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=9.82 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=116 time=9.75 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=116 time=9.79 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=116 time=9.86 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=116 time=9.80 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 9.752/9.804/9.861/0.039 ms
```

## Tips

### Continuous Pinging

By default, ping continues until interrupted with Ctrl+C. Use `-c` to limit the number of packets sent.

### Troubleshooting Network Issues

If ping fails, it could indicate network connectivity problems. Check your network connection, DNS settings, or if a firewall is blocking ICMP packets.

### Measuring Network Quality

Use ping to measure packet loss and latency. High latency (>100ms) or packet loss indicates potential network issues.

### Flood Ping

The `-f` (flood) option can be used to send packets as fast as possible, but requires root privileges and should be used with caution as it can overwhelm networks.

## Frequently Asked Questions

#### Q1. What does "Request timeout" or "Destination host unreachable" mean?
A. These messages indicate that the target host is not responding. This could be due to the host being offline, a network issue, or a firewall blocking ICMP packets.

#### Q2. How do I interpret ping results?
A. Look at the round-trip time (RTT) and packet loss percentage. Lower RTT values indicate better connectivity. Any packet loss suggests network issues.

#### Q3. Can ping tell me if a specific port is open?
A. No, ping only tests basic connectivity using ICMP. To test if a specific port is open, use tools like `telnet` or `nc` (netcat).

#### Q4. Why does ping sometimes resolve to an IP address different from what I expected?
A. This can happen due to DNS load balancing, CDNs (Content Delivery Networks), or multiple IP addresses associated with a domain name.

## macOS Considerations

On macOS, some ping options differ from Linux:
- The `-i` option requires root privileges for intervals less than 1 second
- There is no `--count` long option format; use `-c` instead
- The flood ping (`-f`) option requires root privileges and works differently than on Linux

## References

https://linux.die.net/man/8/ping

## Revisions

2025/05/04 First revision