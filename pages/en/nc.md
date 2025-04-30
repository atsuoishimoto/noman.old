# nc command

Create and manage network connections for data transfer, port scanning, and network debugging.

## Overview

`nc` (netcat) is a versatile networking utility that reads and writes data across network connections using TCP or UDP protocols. It functions as a "Swiss Army knife" for network operations, allowing you to create servers, connect to services, transfer files, scan ports, and debug network issues.

## Options

### **-l** (Listen mode)

Sets up nc as a server that listens for incoming connections

```console
$ nc -l 8080
```

This command makes nc listen on port 8080, waiting for incoming connections.

### **-p** (Source port)

Specifies the source port nc should use

```console
$ nc -p 12345 example.com 80
```

This connects to example.com on port 80, using 12345 as the source port.

### **-v** (Verbose)

Provides more detailed output about the connection

```console
$ nc -v example.com 80
Connection to example.com port 80 [tcp/http] succeeded!
```

### **-z** (Zero I/O mode)

Used for port scanning without sending data

```console
$ nc -z -v example.com 20-30
Connection to example.com 22 port [tcp/ssh] succeeded!
Connection to example.com 25 port [tcp/smtp] succeeded!
```

### **-u** (UDP mode)

Uses UDP instead of the default TCP protocol

```console
$ nc -u 192.168.1.5 53
```

This establishes a UDP connection to 192.168.1.5 on port 53 (DNS).

## Usage Examples

### Creating a simple chat server

```console
$ nc -l 1234
```

In another terminal or from another computer:

```console
$ nc 192.168.1.100 1234
Hello there!
```

Messages typed in either terminal will appear in both.

### Transferring files

On the receiving end:

```console
$ nc -l 1234 > received_file.txt
```

On the sending end:

```console
$ nc 192.168.1.100 1234 < file_to_send.txt
```

### Port scanning

```console
$ nc -z -v example.com 20-25
Connection to example.com 22 port [tcp/ssh] succeeded!
Connection to example.com 25 port [tcp/smtp] succeeded!
```

## Tips:

### Set a Connection Timeout

Use `-w` to set a timeout in seconds. This is useful for scripts or when scanning multiple hosts:

```console
$ nc -w 2 -v example.com 80
```

### Create a Persistent Listener

The `-k` option keeps the listener open after a client disconnects, allowing multiple sequential connections:

```console
$ nc -k -l 8080
```

### Use as a Simple Web Server

You can create a basic HTTP server by combining nc with a prepared HTTP response:

```console
$ while true; do nc -l 8080 < response.http; done
```

## Frequently Asked Questions

#### Q1. What's the difference between nc and telnet?
A. While both can connect to remote services, nc is more versatile with features for both client and server roles, UDP support, and port scanning capabilities. Telnet is primarily designed for interactive terminal sessions.

#### Q2. How can I check if a specific port is open?
A. Use `nc -z -v hostname port` to check if a port is open without sending data.

#### Q3. Can nc transfer binary files?
A. Yes, nc can transfer any type of data, including binary files, using the redirection examples shown above.

#### Q4. How do I terminate a nc connection?
A. Press Ctrl+C to terminate the connection, or use Ctrl+D to send EOF in some scenarios.

## References

https://man.openbsd.org/nc.1

## Revisions

- 2025/04/30 First revision