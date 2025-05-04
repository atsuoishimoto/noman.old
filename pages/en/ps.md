# ps command

Display information about active processes.

## Overview

The `ps` command shows a snapshot of currently running processes on your system. It provides details about process IDs (PIDs), CPU usage, memory consumption, and other process-related information. The command is highly customizable with numerous options to filter and format the output according to your needs.

## Options

### **-e, --everyone**

Display information about all processes (equivalent to -A)

```console
$ ps -e
  PID TTY          TIME CMD
    1 ?        00:00:03 systemd
    2 ?        00:00:00 kthreadd
   11 ?        00:00:00 rcu_sched
  950 ?        00:00:00 sshd
 1050 ?        00:00:01 bash
 1234 ?        00:00:00 ps
```

### **-f, --forest**

Display process hierarchy in a tree-like format

```console
$ ps -ef
UID        PID  PPID  C STIME TTY          TIME CMD
root         1     0  0 May01 ?        00:00:03 /sbin/init
root         2     0  0 May01 ?        00:00:00 [kthreadd]
user      1050   950  0 May01 pts/0    00:00:01 bash
user      1234  1050  0 10:15 pts/0    00:00:00 ps -ef
```

### **-u, --user**

Display processes for a specific user

```console
$ ps -u username
  PID TTY          TIME CMD
 1050 pts/0    00:00:01 bash
 1234 pts/0    00:00:00 ps
 1500 pts/1    00:00:03 vim
```

### **-a, --all**

Show processes of all users except session leaders and processes not associated with a terminal

```console
$ ps -a
  PID TTY          TIME CMD
 1234 pts/0    00:00:00 ps
 1500 pts/1    00:00:03 vim
```

### **-x, --all**

Include processes without controlling terminals

```console
$ ps -ax
  PID TTY      STAT   TIME COMMAND
    1 ?        Ss     0:03 /sbin/init
    2 ?        S      0:00 [kthreadd]
 1050 pts/0    Ss     0:01 bash
 1234 pts/0    R+     0:00 ps -ax
```

## Usage Examples

### Displaying processes with full details

```console
$ ps -ef | grep firefox
user      2345  1050  2 10:20 ?        00:00:45 /usr/lib/firefox/firefox
user      2346  2345  0 10:20 ?        00:00:02 /usr/lib/firefox/firefox-bin
```

### Showing processes sorted by memory usage

```console
$ ps aux --sort=-%mem
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
user      2345  2.0  5.4 1254208 220800 ?      Sl   10:20   0:45 /usr/lib/firefox/firefox
mysql     1234  1.2  3.2  987654 130400 ?      Ssl  May01   2:34 /usr/sbin/mysqld
```

### Displaying process tree for a specific user

```console
$ ps -f --forest -u username
UID        PID  PPID  C STIME TTY          TIME CMD
user      1050   950  0 May01 pts/0    00:00:01 bash
user      2345  1050  2 10:20 ?        00:00:45  \_ firefox
user      2346  2345  0 10:20 ?        00:00:02      \_ firefox-bin
user      1500  1050  0 10:15 pts/0    00:00:03  \_ vim document.txt
```

## Tips

### Customize Output Format

Use the `-o` option to specify exactly which columns you want to see:
```console
$ ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem
```

### Find Resource-Intensive Processes

Combine `ps` with `sort` to identify processes consuming the most resources:
```console
$ ps aux | sort -nrk 3 | head -5  # Top 5 CPU-intensive processes
```

### Use with grep for Filtering

Pipe `ps` output to `grep` to find specific processes:
```console
$ ps -ef | grep nginx
```
Remember to exclude the grep process itself with: `ps -ef | grep [n]ginx`

## Frequently Asked Questions

#### Q1. How do I find the PID of a specific process?
A. Use `ps -C process_name` or `ps -ef | grep process_name` to find the PID of a specific process.

#### Q2. How can I see all processes including those without a terminal?
A. Use `ps aux` or `ps -ef` to see all processes on the system.

#### Q3. How do I monitor processes in real-time?
A. While `ps` provides a snapshot, use `top` or `htop` for real-time monitoring of processes.

#### Q4. What's the difference between ps aux and ps -ef?
A. Both show all processes, but `ps aux` uses BSD syntax and includes %CPU and %MEM columns, while `ps -ef` uses UNIX syntax and shows PPID (parent process ID).

## macOS Considerations

On macOS, the `ps` command has slightly different options than Linux. The BSD-style options (without dashes) are more commonly used. For example, `ps aux` works on macOS, but some GNU-specific options like `--forest` may not be available.

## References

https://man7.org/linux/man-pages/man1/ps.1.html

## Revisions

- 2025/05/04 First revision