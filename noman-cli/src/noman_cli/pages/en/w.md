# w command

Show who is logged in and what they are doing.

## Overview

The `w` command displays information about currently logged-in users and their activities. It shows login names, terminal types, remote hosts, login times, idle times, CPU usage, and the command they are currently running. This is useful for system administrators to monitor user activity on a system.

## Options

### **-h, --no-header**

Don't display the header information

```console
$ w -h
user     tty      from             login@   idle   JCPU   PCPU  what
john     tty1                      10:15    0.00s  0.05s  0.01s  w -h
alice    pts/0    192.168.1.5      09:30    2:35   0.10s  0.05s  vim report.txt
```

### **-s, --short**

Display short format, omitting login time, JCPU and PCPU times

```console
$ w -s
 10:30:25 up  1:15,  3 users,  load average: 0.15, 0.10, 0.09
USER     TTY      FROM             IDLE   WHAT
john     tty1                       0.00s  w -s
alice    pts/0    192.168.1.5       2:35  vim report.txt
bob      pts/1    10.0.0.2         23.00s  bash
```

### **-f, --from**

Toggle printing the `from` (remote hostname) field

```console
$ w -f
 10:30:25 up  1:15,  3 users,  load average: 0.15, 0.10, 0.09
USER     TTY        LOGIN@   IDLE   JCPU   PCPU  WHAT
john     tty1      10:15     0.00s  0.05s  0.01s  w -f
alice    pts/0     09:30     2:35   0.10s  0.05s  vim report.txt
bob      pts/1     10:05    23.00s  0.07s  0.02s  bash
```

### **-i, --ip-addr**

Display IP address instead of hostname in the FROM field

```console
$ w -i
 10:30:25 up  1:15,  3 users,  load average: 0.15, 0.10, 0.09
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
john     tty1                      10:15    0.00s  0.05s  0.01s  w -i
alice    pts/0    192.168.1.5      09:30     2:35  0.10s  0.05s  vim report.txt
bob      pts/1    10.0.0.2         10:05    23.00s 0.07s  0.02s  bash
```

## Usage Examples

### Basic usage

```console
$ w
 10:30:25 up  1:15,  3 users,  load average: 0.15, 0.10, 0.09
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
john     tty1                      10:15    0.00s  0.05s  0.01s  w
alice    pts/0    server2          09:30     2:35  0.10s  0.05s  vim report.txt
bob      pts/1    workstation5     10:05    23.00s 0.07s  0.02s  bash
```

### Combining options

```console
$ w -hi
USER     TTY      FROM             IDLE   JCPU   PCPU  WHAT
john     tty1                      0.00s  0.05s  0.01s  w -hi
alice    pts/0    192.168.1.5      2:35   0.10s  0.05s  vim report.txt
bob      pts/1    10.0.0.2         23.00s 0.07s  0.02s  bash
```

## Tips

### Understanding the output columns

- **USER**: Username of the logged-in user
- **TTY**: Terminal name the user is logged in on
- **FROM**: Remote hostname or IP address
- **LOGIN@**: Time when the user logged in
- **IDLE**: Time since the user's last activity
- **JCPU**: Time used by all processes attached to the tty
- **PCPU**: Time used by the current process
- **WHAT**: Current command the user is running

### Checking system load

The header shows system uptime and load averages for the last 1, 5, and 15 minutes, which helps assess system performance at a glance.

### Identifying inactive users

Look for users with high IDLE times to identify inactive sessions that might be candidates for termination to free up resources.

## Frequently Asked Questions

#### Q1. What's the difference between `w` and `who` commands?
A. `w` provides more detailed information than `who`, including what each user is doing, idle time, and CPU usage statistics. `who` simply lists who is logged in.

#### Q2. How do I interpret the load average numbers?
A. Load averages represent the average system load over 1, 5, and 15 minutes. On a single-core system, values above 1.0 indicate the system is overloaded. For multi-core systems, divide by the number of cores to assess load.

#### Q3. What does the IDLE column mean?
A. The IDLE column shows how long it's been since the user performed any activity on their terminal. This helps identify inactive sessions.

#### Q4. How can I see only a specific user's activity?
A. Use `w username` to display information only for that specific user.

## References

https://www.man7.org/linux/man-pages/man1/w.1.html

## Revisions

- 2025/05/04 First revision