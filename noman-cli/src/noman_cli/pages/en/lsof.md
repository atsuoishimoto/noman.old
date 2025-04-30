# lsof command

List open files and the processes that opened them.

## Overview

`lsof` (List Open Files) displays information about files that are currently open by processes running on the system. It can show which processes are using specific files, network connections, or devices. This command is particularly useful for troubleshooting, security monitoring, and understanding system resource usage.

## Options

### **-p [PID]**

Show files opened by a specific process ID

```console
$ lsof -p 1234
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
chrome  1234 user    cwd    DIR    8,1     4096 123456 /home/user
chrome  1234 user    txt    REG    8,1  2345678 789012 /usr/lib/chrome
chrome  1234 user    mem    REG    8,1   123456 345678 /lib/x86_64-linux-gnu/libc.so.6
```

### **-i**

Show network connections (can be filtered by protocol, address, and port)

```console
$ lsof -i
COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
chrome   1234  user   52u  IPv4 123456      0t0  TCP localhost:45678->remote-server:https (ESTABLISHED)
sshd     2345  root    3u  IPv4 234567      0t0  TCP *:ssh (LISTEN)
nginx    3456  www     6u  IPv4 345678      0t0  TCP *:http (LISTEN)
```

### **-u [username]**

Show files opened by a specific user

```console
$ lsof -u john
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
bash    1234 john  cwd    DIR    8,1     4096 123456 /home/john
vim     2345 john    4u   REG    8,1    12345 234567 /home/john/document.txt
chrome  3456 john   15u  IPv4 345678      0t0   TCP localhost:45678->server:https (ESTABLISHED)
```

### **-c [command]**

Show files opened by processes with the specified command name

```console
$ lsof -c nginx
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
nginx   1234 root  cwd    DIR    8,1     4096 123456 /etc/nginx
nginx   1234 root  txt    REG    8,1   123456 234567 /usr/sbin/nginx
nginx   1234 root    6u  IPv4 345678      0t0   TCP *:http (LISTEN)
```

## Usage Examples

### Finding which process is using a specific file

```console
$ lsof /var/log/syslog
COMMAND  PID   USER   FD   TYPE DEVICE SIZE/OFF   NODE NAME
rsyslogd 1234 syslog    7w   REG    8,1   123456 234567 /var/log/syslog
```

### Checking which process is using a specific port

```console
$ lsof -i :80
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
nginx   1234 root    6u  IPv4 123456      0t0  TCP *:http (LISTEN)
nginx   2345 www     6u  IPv4 123456      0t0  TCP *:http (LISTEN)
```

### Finding all network connections for a specific process

```console
$ lsof -p 1234 -i
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
chrome  1234 user   52u  IPv4 123456      0t0  TCP localhost:45678->server:https (ESTABLISHED)
chrome  1234 user   56u  IPv4 234567      0t0  TCP localhost:45679->cdn:https (ESTABLISHED)
```

## Tips

### Identify Deleted Files Still in Use

Files that have been deleted but are still held open by a process can be found with `lsof | grep deleted`. This helps identify processes preventing disk space from being freed.

### Troubleshoot "Device or Resource Busy" Errors

When you can't unmount a filesystem because it's busy, use `lsof /mount/point` to find which processes are using files on that filesystem.

### Monitor Network Activity

Combine with `watch` for real-time monitoring: `watch -n 1 'lsof -i'` shows network connections updating every second.

### Filter Output for Readability

Use `grep` to filter the often extensive output: `lsof -i | grep LISTEN` shows only listening ports.

## Frequently Asked Questions

#### Q1. How do I find which process is using a specific port?
A. Use `lsof -i:PORT_NUMBER` (e.g., `lsof -i:80` for HTTP port).

#### Q2. How can I see all network connections on my system?
A. Use `lsof -i` to display all network connections.

#### Q3. How do I find all files opened by a specific user?
A. Use `lsof -u USERNAME` to list all files opened by that user.

#### Q4. How can I find which processes are preventing a file from being deleted?
A. Use `lsof | grep filename` to see which processes have the file open.

#### Q5. How do I see all open files for a specific process?
A. Use `lsof -p PID` where PID is the process ID number.

## References

https://man7.org/linux/man-pages/man8/lsof.8.html

## Revisions

- 2025/04/30 First revision