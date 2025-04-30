# journalctl command

Query and display messages from the systemd journal.

## Overview

`journalctl` is a command-line utility that allows you to view and query the logs collected by the systemd journal system. It provides access to structured, indexed system logs with powerful filtering capabilities, making it easier to troubleshoot system issues and monitor system events.

## Options

### **-f, --follow**

Follow the journal in real-time, similar to `tail -f`

```console
$ journalctl -f
Apr 30 10:15:23 hostname systemd[1]: Starting Daily apt upgrade and clean activities...
Apr 30 10:15:24 hostname systemd[1]: apt-daily-upgrade.service: Deactivated successfully.
Apr 30 10:15:24 hostname systemd[1]: Finished Daily apt upgrade and clean activities.
-- Logs begin at Wed 2025-04-30 10:15:25 UTC. --
```

### **-u, --unit=UNIT**

Show logs from a specific systemd unit (service)

```console
$ journalctl -u ssh
Apr 29 09:12:34 hostname sshd[1234]: Accepted publickey for user from 192.168.1.10 port 54321
Apr 29 09:12:34 hostname sshd[1234]: pam_unix(sshd:session): session opened for user by (uid=0)
Apr 29 15:45:12 hostname sshd[5678]: Disconnected from user 192.168.1.10 port 54321
```

### **-b, --boot**

Show logs from the current boot

```console
$ journalctl -b
Apr 30 08:00:12 hostname kernel: Linux version 5.15.0-25-generic (buildd@lcy02)
Apr 30 08:00:13 hostname systemd[1]: Detected virtualization kvm.
Apr 30 08:00:14 hostname systemd[1]: Detected architecture x86-64.
```

### **-p, --priority=**

Filter logs by priority level (emerg, alert, crit, err, warning, notice, info, debug)

```console
$ journalctl -p err
Apr 29 14:23:45 hostname kernel: CPU: 2 PID: 1234 Comm: process Tainted: G        W  OE    5.15.0-25-generic
Apr 29 14:23:45 hostname app[1234]: [ERROR] Failed to connect to database: Connection refused
Apr 30 02:15:33 hostname kernel: EXT4-fs error: unable to read inode block
```

### **--since, --until**

Show logs within a specific time range

```console
$ journalctl --since "2025-04-29 10:00:00" --until "2025-04-29 11:00:00"
Apr 29 10:00:12 hostname systemd[1]: Starting Daily apt download activities...
Apr 29 10:15:45 hostname CRON[1234]: (root) CMD (/usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown)
Apr 29 10:59:58 hostname systemd[1]: Starting Message of the Day...
```

## Usage Examples

### Viewing logs for a specific process

```console
$ journalctl _PID=1234
Apr 30 09:12:34 hostname process[1234]: Starting application...
Apr 30 09:12:35 hostname process[1234]: Loaded configuration from /etc/app/config.json
Apr 30 09:12:36 hostname process[1234]: Listening on port 8080
```

### Viewing kernel messages

```console
$ journalctl -k
Apr 30 08:00:12 hostname kernel: Linux version 5.15.0-25-generic (buildd@lcy02)
Apr 30 08:00:12 hostname kernel: Command line: BOOT_IMAGE=/boot/vmlinuz-5.15.0-25-generic
Apr 30 08:00:12 hostname kernel: ACPI: RSDP 0x00000000000F0490 000024 (v02 VBOX  )
```

### Viewing logs with JSON output

```console
$ journalctl -u ssh -o json
{"_HOSTNAME":"hostname","_SYSTEMD_UNIT":"ssh.service","MESSAGE":"Server listening on 0.0.0.0 port 22.","_PID":"1234","PRIORITY":"6"}
{"_HOSTNAME":"hostname","_SYSTEMD_UNIT":"ssh.service","MESSAGE":"Accepted publickey for user from 192.168.1.10 port 54321","_PID":"1234","PRIORITY":"6"}
```

## Tips:

### Persistent Journal Storage

By default, journal logs may be stored only in memory. To make them persistent across reboots, create the directory `/var/log/journal` with proper permissions:

```console
$ sudo mkdir -p /var/log/journal
$ sudo systemctl restart systemd-journald
```

### Clearing Journal Logs

To free up disk space, you can clear old journal entries:

```console
$ sudo journalctl --vacuum-time=2d  # Keep only last 2 days
$ sudo journalctl --vacuum-size=500M  # Limit journal size to 500MB
```

### Using Grep with journalctl

While journalctl has built-in filtering, you can combine it with grep for more complex pattern matching:

```console
$ journalctl | grep -i "error\|failed"
```

## Frequently Asked Questions

#### Q1. How do I see logs from previous boots?
A. Use `journalctl --list-boots` to see available boot IDs, then use `journalctl -b -1` for the previous boot, `-2` for the one before that, etc.

#### Q2. How can I see logs for a specific time period?
A. Use `journalctl --since "YYYY-MM-DD HH:MM:SS" --until "YYYY-MM-DD HH:MM:SS"`. You can also use relative times like "yesterday" or "2 hours ago".

#### Q3. How do I see logs for a specific user?
A. Use `journalctl _UID=1000` (replace 1000 with the user's UID).

#### Q4. How can I export journal logs to a file?
A. Use `journalctl > logfile.txt` to save in text format, or `journalctl -o json > logfile.json` for structured JSON output.

## References

https://www.freedesktop.org/software/systemd/man/journalctl.html

## Revisions

- 2025/04/30 First revision