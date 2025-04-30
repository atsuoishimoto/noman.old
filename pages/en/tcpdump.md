# tcpdump command

Capture and analyze network traffic on a system.

## Overview

`tcpdump` is a powerful command-line packet analyzer that allows you to capture and display network packets being transmitted or received over a network interface. It's commonly used for network troubleshooting, security analysis, and monitoring network activity. The tool can filter packets based on various criteria and display their contents in different formats.

## Options

### **-i [interface]**

Specify the network interface to capture packets from

```console
$ tcpdump -i eth0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:45:22.357928 IP 192.168.1.5.58642 > 172.217.169.36.443: Flags [.], ack 1, win 502, options [nop,nop,TS val 3987654321 ecr 987654321], length 0
```

### **-n**

Don't convert addresses (like host addresses, port numbers, etc.) to names

```console
$ tcpdump -n
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on en0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:46:15.123456 IP 192.168.1.5.58642 > 172.217.169.36.443: Flags [P.], seq 1:517, ack 1, win 502, length 516
```

### **-c [count]**

Capture only a specific number of packets and then stop

```console
$ tcpdump -c 5
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on en0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:47:01.234567 IP host1.local.58642 > host2.local.443: Flags [.], ack 1, win 502, length 0
13:47:01.345678 IP host1.local.58642 > host2.local.443: Flags [P.], seq 1:517, ack 1, win 502, length 516
13:47:01.456789 IP host2.local.443 > host1.local.58642: Flags [.], ack 517, win 501, length 0
13:47:01.567890 IP host2.local.443 > host1.local.58642: Flags [P.], seq 1:1448, ack 517, win 501, length 1447
13:47:01.678901 IP host1.local.58642 > host2.local.443: Flags [.], ack 1448, win 501, length 0
5 packets captured
10 packets received by filter
0 packets dropped by kernel
```

### **-w [file]**

Write the raw packets to a file instead of displaying them

```console
$ tcpdump -w capture.pcap
tcpdump: listening on en0, link-type EN10MB (Ethernet), capture size 262144 bytes
^C
45 packets captured
50 packets received by filter
0 packets dropped by kernel
```

## Usage Examples

### Capturing packets with a specific protocol

```console
$ tcpdump tcp
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on en0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:50:22.123456 IP host1.local.58642 > host2.local.443: Flags [P.], seq 1:517, ack 1, win 502, length 516
13:50:22.234567 IP host2.local.443 > host1.local.58642: Flags [.], ack 517, win 501, length 0
```

### Filtering by host and port

```console
$ tcpdump -n host 192.168.1.5 and port 443
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on en0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:51:33.123456 IP 192.168.1.5.58642 > 172.217.169.36.443: Flags [P.], seq 1:517, ack 1, win 502, length 516
13:51:33.234567 IP 172.217.169.36.443 > 192.168.1.5.58642: Flags [.], ack 517, win 501, length 0
```

## Tips

### Use sudo for Full Access

Most systems require root privileges to capture packets. Use `sudo tcpdump` to ensure you have proper access to the network interfaces.

### Limit Verbosity for Better Performance

When capturing high-volume traffic, use `-q` (quiet mode) to reduce the output and prevent performance issues.

### Read Captured Files Later

Use `tcpdump -r capture.pcap` to read and analyze previously captured packet files without having to recapture the traffic.

### Combine with grep for Quick Filtering

Pipe tcpdump output to grep to quickly filter for specific information: `tcpdump -n | grep "192.168.1.5"`.

## Frequently Asked Questions

#### Q1. How do I see a list of available network interfaces?
A. Use `tcpdump -D` to display a list of all interfaces that tcpdump can capture on.

#### Q2. How can I see the packet contents and not just headers?
A. Use the `-X` option to display packet contents in hex and ASCII, or `-A` to display in ASCII only.

#### Q3. How do I capture packets on multiple interfaces simultaneously?
A. Use `tcpdump -i any` to capture on all interfaces, though this may not work on all systems.

#### Q4. How can I make the output more readable?
A. Use `-n` to avoid DNS lookups, `-v`, `-vv`, or `-vvv` for increasing verbosity, and consider using `-l` with pipe to `less` for scrollable output.

## macOS Considerations

On macOS, you may need to use `sudo` even more frequently than on Linux systems. Additionally, the default capture interface names typically start with "en" (like en0 for Ethernet, en1 for Wi-Fi) rather than "eth" as on Linux. Use `ifconfig` to identify the correct interface names on your Mac.

## References

https://www.tcpdump.org/manpages/tcpdump.1.html

## Revisions

- 2025/04/30 First revision