# lsof command

List open files and the processes that opened them.

## Overview

`lsof` (List Open Files) displays information about files that are currently open by processes running on the system. It can show which processes have a particular file open, what files a specific process has open, and various other file usage details. This command is particularly useful for system administrators and developers for troubleshooting and monitoring system resources.

## Options

### **-p PID**

List files opened by a specific process ID

```console
$ lsof -p 1234
COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
bash     1234   user  cwd    DIR    8,1     4096 131073 /home/user
bash     1234   user  rtd    DIR    8,1     4096      2 /
bash     1234   user  txt    REG    8,1  1113504 917562 /bin/bash
```

### **-i [protocol][@hostname|hostaddr][:service|port]**

List files opened for Internet connections (optional protocol, host, and port specifications)

```console
$ lsof -i TCP:22
COMMAND  PID    USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
sshd    1234    root    3u  IPv4  12345      0t0  TCP *:ssh (LISTEN)
sshd    5678    root    4u  IPv6  23456      0t0  TCP *:ssh (LISTEN)
```

### **-u username**

List files opened by a specific user

```console
$ lsof -u john
COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
bash     1234   john  cwd    DIR    8,1     4096 131073 /home/john
chrome   2345   john   10u   REG    8,1    12345 262144 /tmp/file.tmp
```

### **-c command**

List files opened by processes with the specified command name

```console
$ lsof -c nginx
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
nginx   1234 root  cwd    DIR    8,1     4096      2 /
nginx   1234 root  txt    REG    8,1  1234567 917562 /usr/sbin/nginx
nginx   1235 www   cwd    DIR    8,1     4096      2 /
```

### **-t**

Display only process IDs (useful for scripting)

```console
$ lsof -t -i TCP:80
1234
5678
```

## Usage Examples

### Finding which process has a specific file open

```console
$ lsof /var/log/syslog
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
rsyslogd 854 syslog    7w   REG    8,1   256789 131074 /var/log/syslog
```

### Checking which processes are listening on network ports

```console
$ lsof -i -P -n | grep LISTEN
sshd      1234    root    3u  IPv4  12345      0t0  TCP *:22 (LISTEN)
nginx     2345    root    6u  IPv4  23456      0t0  TCP *:80 (LISTEN)
mysqld    3456   mysql   10u  IPv4  34567      0t0  TCP 127.0.0.1:3306 (LISTEN)
```

### Finding all files opened by a specific user in a directory

```console
$ lsof -u john /home/john
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
bash    1234  john  cwd    DIR    8,1     4096 131073 /home/john
vim     2345  john    4u   REG    8,1    12345 262144 /home/john/document.txt
```

## Tips:

### Combine Multiple Filters

You can combine multiple options to narrow down results. For example, `lsof -u username -i TCP` shows TCP connections for a specific user.

### Find Deleted Files Still in Use

Use `lsof +L1` to find deleted files that are still being held open by processes. This helps identify processes preventing disk space from being freed.

### Monitor Network Connections

Use `lsof -i` regularly to monitor network connections and identify unexpected network activity that might indicate security issues.

### Use with grep for Targeted Results

Pipe `lsof` output to `grep` to filter for specific information, like `lsof | grep "/var/log"` to find processes accessing log files.

## Frequently Asked Questions

#### Q1. How do I find which process is using a specific port?
A. Use `lsof -i:PORT_NUMBER` (e.g., `lsof -i:80` for HTTP port).

#### Q2. How can I see all network connections?
A. Use `lsof -i` to display all network connections. Add `-P` to show port numbers instead of service names.

#### Q3. How do I find which processes are accessing a specific file?
A. Simply run `lsof /path/to/file` to see all processes that have the file open.

#### Q4. How can I find all files opened by a specific process?
A. Use `lsof -p PID` where PID is the process ID of interest.

## References

https://man7.org/linux/man-pages/man8/lsof.8.html

## Revisions

- 2025/05/04 First revision