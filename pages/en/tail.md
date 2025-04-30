# tail command

Display the last part of files.

## Overview

The `tail` command outputs the last portion of files, typically the last 10 lines by default. It's particularly useful for viewing recent entries in log files, monitoring file changes in real-time, and checking the end of large files without opening them entirely.

## Options

### **-n, --lines=NUM**

Display the last NUM lines instead of the default 10 lines

```console
$ tail -n 5 /var/log/syslog
Apr 30 10:15:22 server systemd[1]: Started Daily apt upgrade and clean activities.
Apr 30 10:15:22 server systemd[1]: apt-daily-upgrade.service: Deactivated successfully.
Apr 30 10:17:01 server CRON[12345]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
Apr 30 10:30:01 server CRON[12346]: (root) CMD ([ -x /etc/init.d/anacron ] && /etc/init.d/anacron start)
Apr 30 10:45:01 server CRON[12347]: (user) CMD (/usr/local/bin/backup.sh)
```

### **-f, --follow**

Output appended data as the file grows (follow mode)

```console
$ tail -f /var/log/apache2/access.log
192.168.1.101 - - [30/Apr/2025:10:42:15 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.102 - - [30/Apr/2025:10:42:18 +0000] "GET /images/logo.png HTTP/1.1" 200 5678
192.168.1.103 - - [30/Apr/2025:10:42:20 +0000] "POST /login HTTP/1.1" 302 0
...
```

### **-c, --bytes=NUM**

Output the last NUM bytes instead of lines

```console
$ tail -c 50 document.txt
end of the document with the last 50 characters only.
```

### **-q, --quiet, --silent**

Never output headers giving file names

```console
$ tail -q file1.txt file2.txt
Last lines of file1.txt
Last lines of file2.txt
```

## Usage Examples

### Following multiple files simultaneously

```console
$ tail -f /var/log/syslog /var/log/auth.log
==> /var/log/syslog <==
Apr 30 11:01:22 server systemd[1]: Started Session 123 of user admin.

==> /var/log/auth.log <==
Apr 30 11:01:22 server sshd[12345]: Accepted publickey for admin from 192.168.1.10
```

### Monitoring a log file with line numbers

```console
$ tail -f -n 3 /var/log/nginx/error.log
2025/04/30 11:05:12 [error] 12345#0: *67 open() "/var/www/html/favicon.ico" failed (2: No such file or directory)
2025/04/30 11:05:15 [error] 12345#0: *68 connect() failed (111: Connection refused) while connecting to upstream
2025/04/30 11:05:20 [notice] 12345#0: signal process started
```

### Viewing the last 20 lines with a specific pattern

```console
$ tail -n 20 access.log | grep "404"
192.168.1.105 - - [30/Apr/2025:11:10:15 +0000] "GET /missing-page.html HTTP/1.1" 404 345
192.168.1.106 - - [30/Apr/2025:11:12:18 +0000] "GET /old-link.php HTTP/1.1" 404 345
```

## Tips

### Monitor Multiple Files Efficiently

When monitoring multiple log files, use `tail -f file1 file2 file3` instead of running multiple tail commands. This is more efficient and keeps your terminal organized.

### Combine with grep for Filtering

Pipe `tail` output to `grep` to filter for specific patterns: `tail -f log.txt | grep ERROR` will show only lines containing "ERROR" as they appear.

### Use --follow=name for Rotating Logs

For log files that get rotated (renamed and recreated), use `tail --follow=name logfile` to continue following the file even after rotation.

### Limit Buffer Size for Long-Running Tail

For long-running `tail -f` sessions, consider using `tail -f -n 0` to start with zero lines and only show new content, reducing initial output.

## Frequently Asked Questions

#### Q1. How do I stop a running tail -f command?
A. Press Ctrl+C to terminate the command and return to the prompt.

#### Q2. Can tail show lines from the beginning of a file?
A. No, use the `head` command instead. `tail` only shows the end of files.

#### Q3. How can I see both the beginning and end of a file?
A. Use `head` for the beginning and `tail` for the end, or use `less` to navigate through the entire file.

#### Q4. Does tail work with compressed files?
A. Not directly. For compressed files, use tools like `zcat file.gz | tail` or specialized commands like `zless`.

#### Q5. How can I monitor a file for specific changes?
A. Use `tail -f file | grep "pattern"` to monitor and filter for specific content.

## References

https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html

## Revisions

- 2025/04/30 First revision