# tcpdump command

Capture and analyze network traffic on a system.

## Overview

`tcpdump` is a powerful command-line packet analyzer that allows you to capture and display network packets being transmitted or received over a network interface. It's commonly used for network troubleshooting, security analysis, and monitoring network activity. The tool can filter packets based on various criteria and display the packet contents in different formats.

## Options

### **-i interface**

Specify the network interface to capture packets from

```console
$ tcpdump -i eth0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:45:22.357928 IP host1.ssh > host2.52986: Flags [P.], seq 196:392, ack 1, win 501, options [nop,nop,TS val 1089067 ecr 1089067], length 196
```

### **-n**

Don't convert addresses (like host addresses, port numbers, etc.) to names

```console
$ tcpdump -n
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:46:15.123456 IP 192.168.1.100.22 > 192.168.1.101.52986: Flags [P.], seq 196:392, ack 1, win 501, length 196
```

### **-c count**

Exit after capturing count packets

```console
$ tcpdump -c 5
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:47:01.123456 IP host1.ssh > host2.52986: Flags [P.], seq 196:392, ack 1, win 501, length 196
13:47:01.234567 IP host2.52986 > host1.ssh: Flags [.], ack 392, win 501, length 0
13:47:01.345678 IP host1.ssh > host2.52986: Flags [P.], seq 392:588, ack 1, win 501, length 196
13:47:01.456789 IP host2.52986 > host1.ssh: Flags [.], ack 588, win 501, length 0
13:47:01.567890 IP host1.ssh > host2.52986: Flags [P.], seq 588:784, ack 1, win 501, length 196
5 packets captured
10 packets received by filter
0 packets dropped by kernel
```

### **-w file**

Write the raw packets to a file instead of parsing and printing them

```console
$ tcpdump -w capture.pcap
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
^C
45 packets captured
50 packets received by filter
0 packets dropped by kernel
```

### **-r file**

Read packets from a file (previously created with -w)

```console
$ tcpdump -r capture.pcap
reading from file capture.pcap, link-type EN10MB (Ethernet)
13:50:01.123456 IP host1.ssh > host2.52986: Flags [P.], seq 196:392, ack 1, win 501, length 196
13:50:01.234567 IP host2.52986 > host1.ssh: Flags [.], ack 392, win 501, length 0
```

### **-v, -vv, -vvv**

Increase verbosity level (more packet information)

```console
$ tcpdump -vv
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:51:22.357928 IP (tos 0x10, ttl 64, id 12345, offset 0, flags [DF], proto TCP (6), length 240) host1.ssh > host2.52986: Flags [P.], cksum 0x1234 (correct), seq 196:392, ack 1, win 501, options [nop,nop,TS val 1089067 ecr 1089067], length 196
```

## Usage Examples

### Capturing TCP traffic on port 80 (HTTP)

```console
$ tcpdump -i eth0 tcp port 80
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:55:01.123456 IP host1.52986 > webserver.http: Flags [S], seq 123456789, win 64240, options [mss 1460,sackOK,TS val 1089067 ecr 0,nop,wscale 7], length 0
13:55:01.234567 IP webserver.http > host1.52986: Flags [S.], seq 987654321, ack 123456790, win 65535, options [mss 1460,sackOK,TS val 1089067 ecr 1089067,nop,wscale 7], length 0
```

### Capturing traffic from a specific host

```console
$ tcpdump -i eth0 host 192.168.1.100
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:56:01.123456 IP 192.168.1.100.22 > 192.168.1.101.52986: Flags [P.], seq 196:392, ack 1, win 501, length 196
13:56:01.234567 IP 192.168.1.101.52986 > 192.168.1.100.22: Flags [.], ack 392, win 501, length 0
```

### Capturing and saving packets with timestamps

```console
$ tcpdump -i eth0 -w capture_$(date +%Y%m%d_%H%M%S).pcap
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
^C
120 packets captured
125 packets received by filter
0 packets dropped by kernel
```

## Tips

### Run with Elevated Privileges

Most systems require root or administrator privileges to capture packets. Use `sudo tcpdump` to ensure you have the necessary permissions.

### Use Expressions to Filter Traffic

Combine expressions with `and`, `or`, and `not` to create complex filters:
```console
$ tcpdump -i eth0 'tcp port 80 and not host 192.168.1.5'
```

### Limit Packet Capture Size

Use `-s snaplen` to limit the number of bytes captured per packet. For headers only, use `-s 96`:
```console
$ tcpdump -i eth0 -s 96 -c 100
```

### Disable Name Resolution for Faster Output

Use `-n` to disable hostname resolution and `-nn` to disable both hostname and port name resolution, which makes tcpdump run faster:
```console
$ tcpdump -i eth0 -nn
```

## Frequently Asked Questions

#### Q1. How do I capture packets on all interfaces?
A. Use `tcpdump -i any` to capture on all interfaces.

#### Q2. How can I see the packet contents in ASCII?
A. Use the `-A` flag to print each packet in ASCII, or `-X` for both hex and ASCII output.

#### Q3. How do I save captured packets to analyze later?
A. Use `tcpdump -w filename.pcap` to save raw packets, then analyze with `tcpdump -r filename.pcap` or tools like Wireshark.

#### Q4. How can I filter packets by IP address?
A. Use `tcpdump host 192.168.1.100` to capture traffic to/from that IP, or `src host` or `dst host` to specify direction.

#### Q5. How do I capture only TCP SYN packets?
A. Use `tcpdump 'tcp[tcpflags] & (tcp-syn) != 0'` to capture TCP SYN packets.

## References

https://www.tcpdump.org/manpages/tcpdump.1.html

## Revisions

- 2025/05/04 First revision