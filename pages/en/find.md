# find command

Search for files in a directory hierarchy based on various criteria.

## Overview

The `find` command searches for files and directories in a specified location based on criteria like name, size, type, or modification time. It's a powerful tool for locating files across your filesystem and can execute commands on the files it finds.

## Options

### **-name pattern**

Search for files by name using a pattern (case-sensitive)

```console
$ find . -name "*.txt"
./documents/notes.txt
./readme.txt
./archive/old.txt
```

### **-iname pattern**

Search for files by name using a pattern (case-insensitive)

```console
$ find . -iname "README*"
./README.md
./projects/readme.txt
./docs/ReadMe.rst
```

### **-type**

Search for files by type (f=regular file, d=directory, l=symbolic link)

```console
$ find . -type d
.
./documents
./projects
./archive
```

### **-mtime n**

Find files modified n days ago (use -n for less than n days, +n for more than n days)

```console
$ find . -mtime -7
./documents/recent.txt
./projects/new-feature.py
```

### **-size n[cwbkMG]**

Find files by size (c=bytes, k=kilobytes, M=megabytes, G=gigabytes)

```console
$ find . -size +10M
./videos/tutorial.mp4
./backups/database.sql
```

### **-exec command {} \;**

Execute a command on each found file (replace {} with the filename)

```console
$ find . -name "*.log" -exec rm {} \;
```

## Usage Examples

### Finding and deleting files

```console
$ find /tmp -name "temp*" -mtime +7 -exec rm {} \;
```

### Finding empty files

```console
$ find ~/documents -type f -empty
/home/user/documents/empty.txt
/home/user/documents/drafts/blank.md
```

### Finding files with specific permissions

```console
$ find /home -type f -perm 0777
/home/user/scripts/backup.sh
/home/user/bin/helper.sh
```

### Finding and counting files by type

```console
$ find . -name "*.jpg" | wc -l
42
```

## Tips

### Use -maxdepth to Limit Search Depth

```console
$ find . -maxdepth 2 -name "*.txt"
```
This limits the search to the current directory and its immediate subdirectories, making searches faster.

### Combine Multiple Conditions

Use `-and`, `-or`, and `-not` (or `!`) to create complex search criteria:
```console
$ find . -name "*.log" -and -size +1M -and -mtime +30
```

### Avoid Permission Denied Errors

Redirect error messages to /dev/null when searching system directories:
```console
$ find /etc -name "*.conf" 2>/dev/null
```

### Use -print0 with xargs for Filenames with Spaces

```console
$ find . -name "*.mp3" -print0 | xargs -0 cp -t ~/music/
```

## Frequently Asked Questions

#### Q1. How do I find files modified in the last 24 hours?
A. Use `find . -mtime -1` to find files modified less than 1 day ago.

#### Q2. How can I find all empty directories?
A. Use `find /path -type d -empty` to find all empty directories.

#### Q3. How do I search for files containing specific text?
A. Combine `find` with `grep`: `find . -type f -name "*.txt" -exec grep "search text" {} \;`

#### Q4. How do I exclude directories from my search?
A. Use `-not -path`: `find . -type f -not -path "./node_modules/*"`

#### Q5. Why is my find command so slow?
A. Large directory trees, network filesystems, or complex criteria can slow down searches. Use `-maxdepth` to limit the search depth.

## References

https://www.gnu.org/software/findutils/manual/html_node/find_html/index.html

## Revisions

- 2025/04/30 First revision