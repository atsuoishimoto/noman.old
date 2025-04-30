# ping command

Send ICMP ECHO_REQUEST packets to network hosts to verify connectivity.

## Overview

`ping` is a network diagnostic tool that tests if a host is reachable on an IP network. It works by sending Internet Control Message Protocol (ICMP) echo request packets to the target host and waiting for a response. This command is commonly used to troubleshoot network connectivity issues, measure network latency, and verify if a remote system is online.

## Options

### **-c count**

Limit the number of echo requests to be sent

```console
$ ping -c 4 google.com
PING google.com (142.250.190.78): 56 data bytes
64 bytes from 142.250.190.78: icmp_seq=0 ttl=116 time=14.308 ms
64 bytes from 142.250.190.78: icmp_seq=1 ttl=116 time=14.417 ms
64 bytes from 142.250.190.78: icmp_seq=2 ttl=116 time=14.303 ms
64 bytes from 142.250.190.78: icmp_seq=3 ttl=116 time=14.264 ms

--- google.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 14.264/14.323/14.417/0.057 ms
```

### **-i interval**

Wait the specified number of seconds between sending each packet

```console
$ ping -i 2 -c 3 example.com
PING example.com (93.184.216.34): 56 data bytes
64 bytes from 93.184.216.34: icmp_seq=0 ttl=56 time=11.632 ms
64 bytes from 93.184.216.34: icmp_seq=1 ttl=56 time=11.726 ms
64 bytes from 93.184.216.34: icmp_seq=2 ttl=56 time=11.978 ms

--- example.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 11.632/11.779/11.978/0.146 ms
```

### **-t ttl**

Set the IP Time to Live (TTL) for outgoing packets

```console
$ ping -t 64 -c 2 github.com
PING github.com (140.82.121.4): 56 data bytes
64 bytes from 140.82.121.4: icmp_seq=0 ttl=64 time=15.321 ms
64 bytes from 140.82.121.4: icmp_seq=1 ttl=64 time=15.256 ms

--- github.com ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 15.256/15.289/15.321/0.033 ms
```

### **-s packetsize**

Specify the number of data bytes to be sent

```console
$ ping -s 100 -c 2 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 100 data bytes
108 bytes from 8.8.8.8: icmp_seq=0 ttl=116 time=14.308 ms
108 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=14.417 ms

--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 14.308/14.363/14.417/0.055 ms
```

## Usage Examples

### Basic connectivity test

```console
$ ping google.com
PING google.com (142.250.190.78): 56 data bytes
64 bytes from 142.250.190.78: icmp_seq=0 ttl=116 time=14.308 ms
64 bytes from 142.250.190.78: icmp_seq=1 ttl=116 time=14.417 ms
64 bytes from 142.250.190.78: icmp_seq=2 ttl=116 time=14.303 ms
^C
--- google.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 14.303/14.343/14.417/0.052 ms
```

### Checking network latency

```console
$ ping -c 10 8.8.8.8 | grep time=
64 bytes from 8.8.8.8: icmp_seq=0 ttl=116 time=14.308 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=14.417 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=116 time=14.303 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=116 time=14.264 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=116 time=14.512 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=116 time=14.398 ms
64 bytes from 8.8.8.8: icmp_seq=6 ttl=116 time=14.356 ms
64 bytes from 8.8.8.8: icmp_seq=7 ttl=116 time=14.287 ms
64 bytes from 8.8.8.8: icmp_seq=8 ttl=116 time=14.329 ms
64 bytes from 8.8.8.8: icmp_seq=9 ttl=116 time=14.301 ms
```

## Tips

### Stop Ping with Ctrl+C

By default, ping runs continuously until you stop it manually. Press Ctrl+C to terminate the command and see the summary statistics.

### Use Hostnames or IP Addresses

You can ping using either domain names (like google.com) or IP addresses (like 8.8.8.8). Using IP addresses bypasses DNS resolution, which can help identify if a connectivity issue is related to DNS.

### Interpret Packet Loss

Packet loss (shown in the statistics) indicates network congestion or connectivity issues. 0% loss means perfect connectivity, while higher percentages indicate problems.

### Check for Firewall Restrictions

Many networks and servers block ICMP packets for security reasons. If ping fails, it doesn't necessarily mean the host is down—it might just be configured not to respond to ping requests.

## Frequently Asked Questions

#### Q1. What does ping actually measure?
A. Ping measures the round-trip time (RTT) for messages sent from the source to a destination and back. It helps determine network latency and connectivity.

#### Q2. How do I stop a ping command?
A. Press Ctrl+C to stop the ping command. This will display summary statistics of the packets sent and received.

#### Q3. Why might ping fail even when a website is accessible?
A. Some networks and servers block ICMP packets (used by ping) for security reasons. You might be able to access a website via HTTP/HTTPS even if ping is blocked.

#### Q4. What's a good ping time?
A. For most internet connections, ping times under 50ms are considered excellent, 50-100ms good, 100-300ms acceptable, and over 300ms may cause noticeable lag in real-time applications.

#### Q5. How can I ping multiple hosts at once?
A. The standard ping command doesn't support pinging multiple hosts simultaneously. You would need to use a script or a specialized tool like fping.

## macOS Considerations

On macOS, ping continues indefinitely by default until stopped with Ctrl+C, unlike some Linux distributions that stop after a certain number of pings. Also, some options might have slightly different syntax compared to Linux versions.

## References

https://linux.die.net/man/8/ping

## Revisions

- 2025/04/30 First revision