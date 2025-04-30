# w command

Display information about users currently logged in and their processes.

## Overview

The `w` command shows who is logged into the system and what they are doing. It displays a summary of the current system status, followed by a list of users who are currently logged in, along with their processes and system activity.

## Options

### **-h (--no-header)**

Suppresses the header information that normally appears at the top of the output.

```console
$ w -h
user     tty      from             login@   idle   JCPU   PCPU  what
john     tty1     -                09:15    0.00s  0.05s  0.01s  w -h
alice    pts/0    192.168.1.5      08:30    2:35   0.10s  0.05s  vim document.txt
```

### **-s (--short)**

Displays a short format, omitting the login time, JCPU, and PCPU columns.

```console
$ w -s
 10:15:24 up  1:23,  3 users,  load average: 0.15, 0.10, 0.09
USER     TTY      FROM             IDLE   WHAT
john     tty1     -                0.00s  w -s
alice    pts/0    192.168.1.5      2:35   vim document.txt
bob      pts/1    10.0.0.25        0.00s  bash
```

### **-f (--from)**

Toggles the display of the FROM field (remote hostname).

```console
$ w -f
 10:15:24 up  1:23,  3 users,  load average: 0.15, 0.10, 0.09
USER     TTY      LOGIN@   IDLE   JCPU   PCPU  WHAT
john     tty1     09:15    0.00s  0.05s  0.01s  w -f
alice    pts/0    08:30    2:35   0.10s  0.05s  vim document.txt
bob      pts/1    10:00    0.00s  0.08s  0.02s  bash
```

## Usage Examples

### Basic usage

```console
$ w
 10:15:24 up  1:23,  3 users,  load average: 0.15, 0.10, 0.09
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
john     tty1     -                09:15    0.00s  0.05s  0.01s  w
alice    pts/0    192.168.1.5      08:30    2:35   0.10s  0.05s  vim document.txt
bob      pts/1    10.0.0.25        10:00    0.00s  0.08s  0.02s  bash
```

### Checking a specific user

```console
$ w alice
 10:15:24 up  1:23,  3 users,  load average: 0.15, 0.10, 0.09
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU  WHAT
alice    pts/0    192.168.1.5      08:30    2:35   0.10s  0.05s  vim document.txt
```

## Tips:

### Understanding the Output Columns

- **USER**: Username of the logged-in user
- **TTY**: Terminal name the user is logged in on
- **FROM**: Remote hostname (IP address) the user is connected from
- **LOGIN@**: Time when the user logged in
- **IDLE**: Time since the user's last activity
- **JCPU**: Time used by all processes attached to the tty
- **PCPU**: Time used by the current process (shown in WHAT)
- **WHAT**: Command currently being run by the user

### Combine with grep for Filtering

Use `w | grep username` to quickly find information about a specific user without having to see all users.

### System Load Understanding

The load averages (shown in the header) represent system load over the last 1, 5, and 15 minutes. A value close to the number of CPU cores indicates the system is fully utilized.

## Frequently Asked Questions

#### Q1. What's the difference between `w` and `who`?
A. `w` provides more detailed information than `who`, including what each user is doing and system load information. `who` simply lists who is logged in.

#### Q2. What does the IDLE time represent?
A. IDLE shows how long it's been since the user performed any activity on their terminal. A high value might indicate an inactive or abandoned session.

#### Q3. How can I see only the summary line about system uptime?
A. Use `uptime` instead of `w`. The first line of `w` output is identical to the output of the `uptime` command.

#### Q4. What do the load average numbers mean?
A. They represent the average system load over the last 1, 5, and 15 minutes. Values below your CPU core count generally indicate the system isn't overloaded.

## References

https://www.man7.org/linux/man-pages/man1/w.1.html

## Revisions

- 2025/04/30 First revision