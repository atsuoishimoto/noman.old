# head command

Display the first part of files.

## Overview

The `head` command outputs the beginning of files, showing the first 10 lines by default. It's useful for quickly previewing file contents without displaying the entire file, especially when working with large files.

## Options

### **-n, --lines=NUM**

Display the first NUM lines instead of the default 10

```console
$ head -n 5 file.txt
Line 1
Line 2
Line 3
Line 4
Line 5
```

### **-c, --bytes=SIZE**

Display the first SIZE bytes of the file

```console
$ head -c 20 file.txt
This is the first 20
```

### **-q, --quiet, --silent**

Suppress the header that shows the filename when displaying multiple files

```console
$ head -q file1.txt file2.txt
(content of file1.txt)
(content of file2.txt)
```

### **-v, --verbose**

Always display the filename header when showing file contents

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
$ head /var/log/system.log
Apr 30 09:15:23 hostname process[123]: Started service
Apr 30 09:15:24 hostname process[123]: Initialized components
...
```

### Viewing multiple files at once

```console
$ head file1.txt file2.txt
==> file1.txt <==
First lines of file1

==> file2.txt <==
First lines of file2
```

### Combining with other commands using pipes

```console
$ ls -l | head -n 3
total 128
drwxr-xr-x  15 user  staff  480 Apr 29 14:22 Documents
drwxr-xr-x  12 user  staff  384 Apr 28 10:15 Downloads
```

## Tips

### Quickly Check File Format

Use `head` to quickly check the format of data files like CSV or JSON without loading the entire file.

### Combine with tail for Middle Content

Use `head` with `tail` to view a specific section in the middle of a file: `head -n 20 file.txt | tail -n 10` shows lines 11-20.

### Use with Process Substitution

In bash, you can use process substitution to compare the beginnings of files: `diff <(head file1) <(head file2)`.

## Frequently Asked Questions

#### Q1. How do I view a specific number of lines?
A. Use `head -n NUMBER file.txt` where NUMBER is the number of lines you want to see.

#### Q2. Can I view multiple files at once?
A. Yes, simply list all the files you want to view: `head file1.txt file2.txt file3.txt`.

#### Q3. How do I view the beginning of a file by bytes instead of lines?
A. Use `head -c NUMBER file.txt` where NUMBER is the number of bytes to display.

#### Q4. How can I hide the filename headers when viewing multiple files?
A. Use the `-q` option: `head -q file1.txt file2.txt`.

## References

https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html

## Revisions

- 2025/04/30 First revision