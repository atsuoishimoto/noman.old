# journalctl command

Query and display messages from the systemd journal.

## Overview

`journalctl` is a command-line utility that allows you to view and query the systemd journal logs. The systemd journal is a centralized logging system that collects and stores logging data from various sources including the kernel, system services, and applications. It provides powerful filtering capabilities to help troubleshoot system issues.

## Options

### **-f, --follow**

Follow the journal in real-time, similar to `tail -f`

```console
$ journalctl -f
May 04 14:32:15 hostname systemd[1]: Started Daily apt download activities.
May 04 14:32:16 hostname CRON[12345]: (root) CMD (command being executed)
May 04 14:32:20 hostname sshd[12346]: Accepted publickey for user from 192.168.1.10
```

### **-u, --unit=UNIT**

Show logs from a specific systemd unit (service)

```console
$ journalctl -u ssh
May 03 09:15:22 hostname sshd[1234]: Server listening on 0.0.0.0 port 22.
May 03 09:15:22 hostname sshd[1234]: Server listening on :: port 22.
May 04 10:23:45 hostname sshd[5678]: Accepted password for user from 192.168.1.5
```

### **-b, --boot[=ID]**

Show logs from the current boot or a specific boot

```console
$ journalctl -b
[Shows all logs since the most recent boot]

$ journalctl -b -1
[Shows logs from the previous boot]
```

### **-n, --lines=N**

Show the last N log lines

```console
$ journalctl -n 5
May 04 14:45:10 hostname systemd[1]: Starting Daily apt upgrade and clean activities...
May 04 14:45:11 hostname systemd[1]: Started Daily apt upgrade and clean activities.
May 04 14:45:12 hostname CRON[12347]: (root) CMD (apt-get update)
May 04 14:45:15 hostname kernel: [12345.678901] USB disconnect, device number 5
May 04 14:45:20 hostname NetworkManager[789]: Connectivity established
```

### **--since=DATE, --until=DATE**

Show entries newer or older than the specified date

```console
$ journalctl --since="2025-05-03 10:00:00" --until="2025-05-03 11:00:00"
[Shows logs between 10 AM and 11 AM on May 3rd, 2025]
```

### **-p, --priority=PRIORITY**

Filter output by message priority (0-7 or name like "err")

```console
$ journalctl -p err
May 02 15:30:45 hostname kernel: [12345.678901] CPU: 2 PID: 1234 Comm: process Tainted: G        W  5.15.0-91-generic
May 03 08:12:33 hostname application[5678]: Error: Failed to connect to database
May 04 02:45:12 hostname systemd[1]: Failed to start Apache Web Server.
```

### **-o, --output=FORMAT**

Control the output format (short, verbose, json, etc.)

```console
$ journalctl -o json -n 1
{"_BOOT_ID":"abcdef123456789","_MACHINE_ID":"fedcba987654321","MESSAGE":"System startup complete","PRIORITY":"6","SYSLOG_FACILITY":"3","SYSLOG_IDENTIFIER":"systemd","_UID":"0","_GID":"0","_COMM":"systemd","_PID":"1","_SOURCE_REALTIME_TIMESTAMP":"1714896000000000"}
```

## Usage Examples

### Viewing logs for a specific time period

```console
$ journalctl --since yesterday --until today
[Shows all logs from yesterday up to the current time today]
```

### Filtering logs by executable

```console
$ journalctl _COMM=sshd
May 01 08:15:22 hostname sshd[1234]: Server listening on 0.0.0.0 port 22.
May 01 08:15:22 hostname sshd[1234]: Server listening on :: port 22.
May 02 14:23:45 hostname sshd[5678]: Accepted publickey for user from 192.168.1.10
```

### Combining multiple filters

```console
$ journalctl -u nginx -p err --since today
May 04 03:15:22 hostname nginx[1234]: 2025/05/04 03:15:22 [error] 1234#0: *123 open() "/var/www/html/favicon.ico" failed (2: No such file or directory)
```

### Viewing kernel messages

```console
$ journalctl -k
May 04 00:00:01 hostname kernel: Linux version 5.15.0-91-generic (buildd@ubuntu) (gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0)
May 04 00:00:01 hostname kernel: Command line: BOOT_IMAGE=/boot/vmlinuz-5.15.0-91-generic root=UUID=abcdef-1234-5678 ro quiet splash
```

## Tips:

### Use Pager Controls

When viewing large logs, journalctl uses a pager (like less). Use `/pattern` to search, `n` for next match, `g` to go to beginning, `G` to go to end, and `q` to quit.

### Persistent Journal Storage

By default, journal logs may be stored only in memory. To make them persistent across reboots, ensure `/etc/systemd/journald.conf` has `Storage=persistent` and the `/var/log/journal/` directory exists.

### Disk Space Management

Journal logs can consume significant disk space. Use `journalctl --disk-usage` to check space usage and `journalctl --vacuum-size=1G` to limit the journal size to 1GB.

### Export Logs for Analysis

Use `journalctl -o export` to export logs in a format that can be transferred to another machine and imported with `journalctl --file=exported.journal`.

## Frequently Asked Questions

#### Q1. How do I see logs from the current boot only?
A. Use `journalctl -b` to see logs from the current boot only.

#### Q2. How can I see logs from a specific service?
A. Use `journalctl -u service-name`, for example `journalctl -u ssh` to see SSH service logs.

#### Q3. How do I filter logs by severity level?
A. Use `journalctl -p priority` where priority can be a number (0-7) or name (emerg, alert, crit, err, warning, notice, info, debug).

#### Q4. How can I clear old journal logs?
A. Use `journalctl --vacuum-time=2d` to remove entries older than 2 days, or `journalctl --vacuum-size=500M` to limit the total size to 500MB.

#### Q5. How do I follow logs in real-time?
A. Use `journalctl -f` to follow logs as they are written, similar to `tail -f`.

## References

https://www.freedesktop.org/software/systemd/man/journalctl.html

## Revisions

- 2025/05/04 First revision