# iotop command

Monitor I/O usage by processes on the system.

## Overview

`iotop` is a top-like utility that displays real-time disk I/O usage information for processes. It shows which processes are using the disk, how much they're reading and writing, and their I/O priority. This tool is particularly useful for identifying which processes are causing high disk activity.

## Options

### **-o, --only**

Only show processes or threads that are actually doing I/O

```console
$ sudo iotop -o
Total DISK READ:         0.00 B/s | Total DISK WRITE:         7.56 K/s
Current DISK READ:       0.00 B/s | Current DISK WRITE:       0.00 B/s
    PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
   1234 be/4 root        0.00 B/s    7.56 K/s  0.00 %  0.00 % systemd-journald
```

### **-b, --batch**

Run in non-interactive mode, useful for logging

```console
$ sudo iotop -b -n 3
Total DISK READ:         0.00 B/s | Total DISK WRITE:        15.69 K/s
Current DISK READ:       0.00 B/s | Current DISK WRITE:       0.00 B/s
    PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
      1 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % systemd
    346 be/4 root        0.00 B/s    7.84 K/s  0.00 %  0.00 % systemd-journald
[...]
```

### **-n NUM, --iter=NUM**

Set the number of iterations before exiting (for non-interactive mode)

```console
$ sudo iotop -b -n 2
[output shows 2 iterations of disk I/O statistics]
```

### **-d SEC, --delay=SEC**

Set the delay between iterations in seconds (default 1.0)

```console
$ sudo iotop -d 5
[updates display every 5 seconds]
```

### **-p PID, --pid=PID**

Monitor only the specified process ID

```console
$ sudo iotop -p 1234
[shows I/O statistics only for process with PID 1234]
```

### **-a, --accumulated**

Show accumulated I/O instead of bandwidth

```console
$ sudo iotop -a
[shows total I/O performed by each process since iotop started]
```

## Usage Examples

### Basic monitoring

```console
$ sudo iotop
Total DISK READ:         0.00 B/s | Total DISK WRITE:        23.45 K/s
Current DISK READ:       0.00 B/s | Current DISK WRITE:       7.84 K/s
    PID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
      1 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % systemd
    346 be/4 root        0.00 B/s    7.84 K/s  0.00 %  0.00 % systemd-journald
[...]
```

### Monitoring only active I/O processes and logging to a file

```console
$ sudo iotop -bo -n 60 -d 10 > disk_activity.log
[captures 60 snapshots at 10-second intervals of processes doing I/O]
```

### Monitoring specific processes

```console
$ sudo iotop -p 1234,5678
[shows I/O statistics only for processes with PIDs 1234 and 5678]
```

## Tips:

### Run with sudo

`iotop` requires root privileges to access the I/O statistics. Always run it with `sudo` or as the root user.

### Use -o for busy systems

On systems with many processes, use the `-o` option to show only processes that are actually performing I/O operations, making it easier to identify problematic processes.

### Keyboard shortcuts

While running interactively, you can use:
- `o` to toggle the --only option
- `p` to toggle showing processes (not threads)
- `a` to toggle accumulated I/O mode
- `q` to quit

### Combine with logging

For troubleshooting intermittent I/O issues, run `iotop` in batch mode and redirect output to a log file that you can analyze later.

## Frequently Asked Questions

#### Q1. Why do I get "iotop: command not found"?
A. `iotop` may not be installed by default. Install it using your distribution's package manager (e.g., `apt install iotop` on Debian/Ubuntu or `yum install iotop` on RHEL/CentOS).

#### Q2. Why do I get "Permission denied" when running iotop?
A. `iotop` requires root privileges to access I/O statistics. Run it with `sudo iotop` or as the root user.

#### Q3. How can I see which process is causing disk I/O spikes?
A. Run `sudo iotop -o` to show only processes that are actively performing I/O operations.

#### Q4. What do the SWAPIN and IO columns mean?
A. SWAPIN shows the percentage of time the process spent swapping in, while IO shows the percentage of time the process spent waiting for I/O.

## References

https://man7.org/linux/man-pages/man8/iotop.8.html

## Revisions

- 2025/05/04 First revision