# head command

Display the first part of files.

## Overview

The `head` command outputs the first part of files to standard output. By default, it prints the first 10 lines of each specified file. If multiple files are specified, it precedes each with a header identifying the file name.

## Options

### **-n, --lines=[-]NUM**

Print the first NUM lines instead of the default 10. With a leading '-', print all but the last NUM lines of each file.

```console
$ head -n 5 file.txt
Line 1
Line 2
Line 3
Line 4
Line 5
```

### **-c, --bytes=[-]NUM**

Print the first NUM bytes instead of lines. With a leading '-', print all but the last NUM bytes of each file.

```console
$ head -c 20 file.txt
This is the first 20
```

### **-q, --quiet, --silent**

Never print headers giving file names.

```console
$ head -q file1.txt file2.txt
(Content of file1.txt)
(Content of file2.txt)
```

### **-v, --verbose**

Always print headers giving file names.

```console
$ head -v file.txt
==> file.txt <==
Line 1
Line 2
...
```

## Usage Examples

### Viewing the beginning of a log file

```console
$ head /var/log/syslog
May  3 14:22:01 hostname systemd[1]: Starting Daily apt download activities...
May  3 14:22:01 hostname systemd[1]: apt-daily.service: Succeeded.
May  3 14:22:01 hostname systemd[1]: Finished Daily apt download activities.
...
```

### Viewing multiple files at once

```console
$ head -n 2 file1.txt file2.txt
==> file1.txt <==
First line of file1
Second line of file1

==> file2.txt <==
First line of file2
Second line of file2
```

### Viewing all but the last N lines

```console
$ head -n -2 file.txt
Line 1
Line 2
Line 3
...
(all lines except the last 2)
```

## Tips

### Combine with other commands

Use `head` with pipes to limit output from other commands:

```console
$ ls -l | head -n 5
```

This shows only the first 5 entries from a directory listing.

### View beginning of large files

For very large files, use `head` to preview content without loading the entire file:

```console
$ head -n 20 huge_log.txt
```

### Use with tail for middle sections

Combine `head` with `tail` to extract a section from the middle of a file:

```console
$ head -n 20 file.txt | tail -n 10
```

This shows lines 11-20 of the file.

## Frequently Asked Questions

#### Q1. How do I view a specific number of lines from a file?
A. Use `head -n NUMBER filename` to view the first NUMBER lines.

#### Q2. Can I view multiple files at once with head?
A. Yes, simply list all filenames: `head file1.txt file2.txt file3.txt`.

#### Q3. How do I view the first few bytes instead of lines?
A. Use `head -c NUMBER filename` to view the first NUMBER bytes.

#### Q4. How can I view all lines except the last few?
A. Use `head -n -NUMBER filename` to view all lines except the last NUMBER lines.

#### Q5. How do I suppress the filename headers when viewing multiple files?
A. Use the `-q` option: `head -q file1.txt file2.txt`.

## References

https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html

## Revisions

2025/05/04 First revision