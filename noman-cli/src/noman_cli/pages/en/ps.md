# ps command

Display information about active processes.

## Overview

The `ps` command shows a snapshot of currently running processes on your system. It provides details about process IDs (PIDs), resource usage, status, and more. This command is essential for monitoring system activity, troubleshooting, and managing processes.

## Options

### **-e**

Display all processes (system-wide)

```console
$ ps -e
  PID TTY          TIME CMD
    1 ?        00:00:03 systemd
  546 ?        00:00:00 sshd
  892 ?        00:00:01 nginx
 1024 tty1     00:00:00 bash
```

### **-f**

Show full-format listing with more details

```console
$ ps -f
UID        PID  PPID  C STIME TTY          TIME CMD
user      1024  1020  0 10:30 tty1     00:00:00 -bash
user      1095  1024  0 10:35 tty1     00:00:00 ps -f
```

### **-u [username]**

Display processes for a specific user

```console
$ ps -u john
  PID TTY          TIME CMD
 1024 tty1     00:00:00 bash
 1095 tty1     00:00:00 ps
 1120 ?        00:00:01 firefox
```

### **aux**

Comprehensive process listing (BSD style)

```console
$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.1 168940  9416 ?        Ss   Apr29   0:03 /sbin/init
www-data   892  0.0  0.2 142392 12284 ?        S    Apr29   0:01 nginx: worker
user      1024  0.0  0.1  21452  5724 tty1     Ss   10:30   0:00 -bash
user      1120  2.1  4.3 1852404 354216 ?      Sl   10:40   0:45 /usr/lib/firefox/firefox
```

## Usage Examples

### Finding processes by name

```console
$ ps -ef | grep nginx
root       891  1  0 Apr29 ?        00:00:00 nginx: master process
www-data   892  891  0 Apr29 ?        00:00:01 nginx: worker process
user      1245  1024  0 11:05 tty1     00:00:00 grep --color=auto nginx
```

### Sorting processes by CPU usage

```console
$ ps aux --sort=-%cpu | head -5
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
user      1120  3.2  4.5 1852404 364216 ?      Sl   10:40   0:52 /usr/lib/firefox/firefox
user      1340  1.5  2.1 1245632 172544 ?      Sl   10:55   0:23 /usr/bin/chromium
root       432  0.8  0.6  85432  48216 ?       Ss   Apr29   0:12 /usr/sbin/dockerd
user      1562  0.5  1.2 524288  98432 ?       Sl   11:02   0:05 /usr/bin/code
```

### Displaying process tree

```console
$ ps -ejH
  PID  PGID   SID TTY          TIME CMD
    1     1     1 ?        00:00:03 systemd
  432   432   432 ?        00:00:12   dockerd
  546   546   546 ?        00:00:00   sshd
  891   891   891 ?        00:00:00   nginx
  892   891   891 ?        00:00:01     nginx
 1020  1020  1020 tty1     00:00:00   login
 1024  1024  1024 tty1     00:00:00     bash
 1245  1245  1024 tty1     00:00:00       ps
```

## Tips

### Process State Codes

In the STAT column, common codes include:
- R: Running
- S: Sleeping (interruptible)
- D: Uninterruptible sleep
- Z: Zombie (terminated but not reaped)
- T: Stopped

### Memory Usage Analysis

Use `ps aux` to identify memory-intensive processes. The %MEM column shows memory usage percentage, while RSS shows actual physical memory used in kilobytes.

### Combining with Other Commands

Pipe `ps` output to `grep` to filter processes, or to `sort` to organize by specific criteria. For example, `ps aux | sort -nk6` sorts by virtual memory usage.

### Custom Format Output

Use the `-o` option to create custom output formats: `ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem` shows processes sorted by memory usage with only the specified columns.

## Frequently Asked Questions

#### Q1. How do I kill a process using ps?
A. `ps` itself doesn't kill processes. Use it to find the PID, then use the `kill` command: `kill PID` or `kill -9 PID` for forceful termination.

#### Q2. What's the difference between ps aux and ps -ef?
A. Both show all processes, but `ps aux` is BSD-style with different output format, while `ps -ef` is UNIX-style. `aux` shows %CPU and %MEM, while `-ef` shows PPID (parent process ID).

#### Q3. How can I see only my processes?
A. Use `ps -u $(whoami)` or simply `ps` without options to see processes associated with your current terminal.

#### Q4. How do I monitor processes in real-time?
A. `ps` shows a snapshot. For real-time monitoring, use `top` or `htop` instead.

## macOS Considerations

On macOS, `ps` has slightly different behavior. The BSD-style options (like `aux`) work without the leading dash. Additionally, some Linux-specific options may not be available. For macOS-specific process information, consider using `Activity Monitor` or the `top` command.

## References

https://man7.org/linux/man-pages/man1/ps.1.html

## Revisions

- 2025/04/30 First revision