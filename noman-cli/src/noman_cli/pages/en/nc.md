# nc command

Create and manage network connections for data transfer, port scanning, and network debugging.

## Overview

`nc` (netcat) is a versatile networking utility that reads and writes data across network connections using TCP or UDP protocols. It functions as a "Swiss Army knife" for network operations, allowing you to create servers, clients, transfer files, scan ports, and debug network issues. Its simplicity and flexibility make it an essential tool for system administrators and security professionals.

## Options

### **-l, --listen**

Listen for incoming connections rather than initiating a connection to a remote host.

```console
$ nc -l 8080
Hello, world!
```

### **-p, --port**

Specify the source port nc should use, subject to privilege restrictions and availability.

```console
$ nc -p 31337 example.com 80
```

### **-v, --verbose**

Enable verbose output to show more connection details.

```console
$ nc -v example.com 80
Connection to example.com 80 port [tcp/http] succeeded!
```

### **-z**

Scan for listening daemons without sending any data (port scanning mode).

```console
$ nc -zv example.com 20-30
Connection to example.com 22 port [tcp/ssh] succeeded!
```

### **-u, --udp**

Use UDP instead of the default TCP protocol.

```console
$ nc -u 192.168.1.100 53
```

### **-w, --timeout**

Set a timeout for connection attempts.

```console
$ nc -w 5 example.com 80
```

## Usage Examples

### Creating a Simple Chat Server

```console
$ nc -l 1234
```

### Connecting to the Chat Server

```console
$ nc 192.168.1.100 1234
Hello, are you there?
```

### Transferring Files

Server side:
```console
$ nc -l 1234 > received_file.txt
```

Client side:
```console
$ nc 192.168.1.100 1234 < file_to_send.txt
```

### Port Scanning

```console
$ nc -zv example.com 20-30
Connection to example.com 22 port [tcp/ssh] succeeded!
Connection to example.com 25 port [tcp/smtp] succeeded!
```

### Banner Grabbing

```console
$ nc -v example.com 22
Connection to example.com 22 port [tcp/ssh] succeeded!
SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5
```

## Tips:

### Use as a Simple Web Server

You can create a basic HTTP server to serve a file:
```console
$ while true; do nc -l 8080 < response.html; done
```

### Redirect Output to a File

When troubleshooting, save the output for later analysis:
```console
$ nc example.com 80 > output.txt
```

### Check if a Port is Open

A quick way to verify if a specific port is accessible:
```console
$ nc -zv example.com 443
```

### Use with Pipes

Netcat works well with Unix pipes for complex operations:
```console
$ echo -e "GET / HTTP/1.0\r\n\r\n" | nc example.com 80
```

## Frequently Asked Questions

#### Q1. What's the difference between nc and telnet?
A. While both can connect to remote services, `nc` is more versatile with features like port scanning, UDP support, and better scripting capabilities. Telnet is primarily designed for interactive terminal sessions.

#### Q2. How do I keep a netcat listener running after a client disconnects?
A. Use the `-k` option (if supported in your version) to keep the server listening after client disconnection. Otherwise, wrap it in a loop: `while true; do nc -l 8080; done`

#### Q3. Is netcat secure for transferring sensitive data?
A. No, netcat transmits data in plaintext. For secure transfers, consider using tools like `scp`, `sftp`, or tunneling netcat through SSH.

#### Q4. How can I test if a web server is working?
A. Use: `echo -e "GET / HTTP/1.0\r\n\r\n" | nc example.com 80`

## macOS Considerations

On macOS, the default `nc` implementation may have fewer features than GNU netcat. Some options like `-k` (keep listening) might not be available. Consider installing an alternative version through Homebrew: `brew install netcat`.

## References

https://man7.org/linux/man-pages/man1/nc.1.html

## Revisions

- 2025/05/04 First revision