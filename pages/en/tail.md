# tail command

Display the last part of files.

## Overview

The `tail` command outputs the last part (tail) of files. By default, it prints the last 10 lines of each specified file to standard output. It's commonly used to view recent entries in log files, monitor file changes in real-time, or check the end of any text file.

## Options

### **-n, --lines=NUM**

Output the last NUM lines, instead of the default 10

```console
$ tail -n 5 /var/log/syslog
May  3 21:45:12 hostname systemd[1]: Started Daily apt download activities.
May  3 21:45:12 hostname systemd[1]: apt-daily.service: Succeeded.
May  3 22:17:01 hostname CRON[12345]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
May  3 23:17:01 hostname CRON[12346]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
May  4 00:17:01 hostname CRON[12347]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
```

### **-f, --follow**

Output appended data as the file grows; follow the file's end

```console
$ tail -f /var/log/syslog
May  4 00:17:01 hostname CRON[12347]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
May  4 01:17:01 hostname CRON[12348]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
May  4 02:17:01 hostname CRON[12349]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
[new entries appear in real-time as they're added to the file]
```

### **-c, --bytes=NUM**

Output the last NUM bytes, instead of the last 10 lines

```console
$ tail -c 50 file.txt
last 50 bytes of the file will be displayed here.
```

### **-q, --quiet, --silent**

Never output headers giving file names

```console
$ tail -q file1.txt file2.txt
[displays last 10 lines of each file without headers]
```

## Usage Examples

### Monitoring a log file in real-time

```console
$ tail -f /var/log/apache2/access.log
192.168.1.1 - - [04/May/2025:10:15:32 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.2 - - [04/May/2025:10:15:45 +0000] "GET /images/logo.png HTTP/1.1" 200 5678
[continues to show new entries as they appear]
```

### Viewing the last 20 lines of multiple files

```console
$ tail -n 20 file1.txt file2.txt
==> file1.txt <==
[last 20 lines of file1.txt]

==> file2.txt <==
[last 20 lines of file2.txt]
```

### Following multiple files simultaneously

```console
$ tail -f /var/log/syslog /var/log/auth.log
==> /var/log/syslog <==
[last 10 lines of syslog]

==> /var/log/auth.log <==
[last 10 lines of auth.log]
[continues to show new entries from both files]
```

## Tips

### Use with grep for filtering

Combine `tail` with `grep` to filter specific entries from log files:

```console
$ tail -f /var/log/syslog | grep ERROR
```

### Follow files even if they're rotated

Use `tail -F` (capital F) instead of `-f` to continue following a file even if it gets rotated or recreated:

```console
$ tail -F /var/log/application.log
```

### Specify number of lines with a shorthand

You can use `-n` with a number without a space:

```console
$ tail -n50 file.txt
```

## Frequently Asked Questions

#### Q1. What's the difference between `tail -f` and `tail -F`?
A. `tail -f` follows the file descriptor, which means it may stop if the file is renamed. `tail -F` follows the filename, continuing to display content even if the file is rotated or recreated.

#### Q2. How do I exit from `tail -f`?
A. Press Ctrl+C to terminate the command and return to the prompt.

#### Q3. Can I see both the beginning and end of a file?
A. No, `tail` only shows the end. Use `head` for the beginning or combine them with a pipe: `head -n 5 file.txt && tail -n 5 file.txt`.

#### Q4. How can I monitor multiple log files at once?
A. Simply list all files after the `tail -f` command: `tail -f file1.log file2.log file3.log`.

## References

https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html

## Revisions

- 2025/05/04 First revision