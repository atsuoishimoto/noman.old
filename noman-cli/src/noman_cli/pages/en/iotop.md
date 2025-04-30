# iotop command

Monitor and display real-time I/O usage by processes.

## Overview

`iotop` is a top-like utility that shows I/O usage information for processes. It helps identify which processes are causing disk I/O load, making it useful for diagnosing system slowdowns related to disk activity. The command requires root privileges to access the necessary kernel information.

## Options

### **-o, --only**

Show only processes or threads that are actually doing I/O

```console
$ sudo iotop -o
Total DISK READ:         0.00 B/s | Total DISK WRITE:         7.81 K/s
Current DISK READ:       0.00 B/s | Current DISK WRITE:       0.00 B/s
    PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
   1234  be/4  root        0.00 B      7.81 K  0.00 %  0.12 %  rsyslogd
   5678  be/4  mysql       0.00 B     15.62 K  0.00 %  0.05 %  mysqld
```

### **-b, --batch**

Run in non-interactive mode, useful for logging

```console
$ sudo iotop -b -n 3
Total DISK READ:       0.00 B/s | Total DISK WRITE:       7.81 K/s
Current DISK READ:     0.00 B/s | Current DISK WRITE:     0.00 B/s
    PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
   1234  be/4  root        0.00 B      7.81 K  0.00 %  0.12 %  rsyslogd
[...]
```

### **-n, --iter=NUM**

Exit after NUM iterations (when used with batch mode)

```console
$ sudo iotop -b -n 2
Total DISK READ:       0.00 B/s | Total DISK WRITE:       7.81 K/s
[...]
Total DISK READ:       0.00 B/s | Total DISK WRITE:       8.12 K/s
[...]
```

### **-P, --processes**

Show only processes (not threads)

```console
$ sudo iotop -P
Total DISK READ:       0.00 B/s | Total DISK WRITE:       7.81 K/s
Current DISK READ:     0.00 B/s | Current DISK WRITE:     0.00 B/s
    PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
   1234  be/4  root        0.00 B      7.81 K  0.00 %  0.12 %  rsyslogd
```

## Usage Examples

### Monitoring I/O with automatic updates

```console
$ sudo iotop
Total DISK READ:       0.00 B/s | Total DISK WRITE:       7.81 K/s
Current DISK READ:     0.00 B/s | Current DISK WRITE:     0.00 B/s
    PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
   1234  be/4  root        0.00 B      7.81 K  0.00 %  0.12 %  rsyslogd
   5678  be/4  mysql       0.00 B     15.62 K  0.00 %  0.05 %  mysqld
   9012  be/4  www-data    0.00 B      3.91 K  0.00 %  0.02 %  apache2
```

### Logging I/O activity to a file

```console
$ sudo iotop -botq -n 10 > disk_activity.log
$ cat disk_activity.log
   1234  be/4  root        0.00 B      7.81 K  0.00 %  0.12 %  rsyslogd
   5678  be/4  mysql       0.00 B     15.62 K  0.00 %  0.05 %  mysqld
[...]
```

## Tips

### Interactive Commands

While iotop is running in interactive mode, you can use these keys:
- `o`: Toggle the --only option to show only active I/O processes
- `p`: Toggle the --processes option to show only processes (not threads)
- `a`: Toggle accumulated I/O instead of bandwidth
- `q`: Quit the program

### Focus on Accumulated I/O

Press 'a' in interactive mode to see the total I/O done by each process since iotop started, which helps identify processes that do sporadic I/O.

### Combine with Other Tools

Use `iotop -b -n 5 | grep mysql` to monitor specific processes or services.

## Frequently Asked Questions

#### Q1. Why do I get "iotop: permission denied" error?
A. `iotop` requires root privileges. Run it with `sudo iotop` or as the root user.

#### Q2. How can I see only processes that are actively using I/O?
A. Use `iotop -o` or press 'o' in interactive mode to toggle showing only active I/O processes.

#### Q3. How do I save iotop output to a file?
A. Use batch mode: `sudo iotop -b -n 10 > output.log` to capture 10 iterations to a file.

#### Q4. What do the SWAPIN and IO columns mean?
A. SWAPIN shows the percentage of time the process spent swapping in, while IO shows the percentage of time the process spent waiting on I/O.

## References

https://linux.die.net/man/1/iotop

## Revisions

- 2025/04/30 First revision