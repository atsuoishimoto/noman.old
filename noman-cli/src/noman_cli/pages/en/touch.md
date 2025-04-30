# touch command

Create or update file timestamps without changing file content.

## Overview

The `touch` command creates empty files if they don't exist, or updates the access and modification timestamps of existing files to the current time. It's commonly used to create placeholder files or to refresh file timestamps without altering their contents.

## Options

### **-a**

Update only the access time of a file

```console
$ touch -a file.txt
```

### **-m**

Update only the modification time of a file

```console
$ touch -m document.txt
```

### **-c**

Do not create files that don't exist (only update timestamps of existing files)

```console
$ touch -c nonexistent.txt
$ ls nonexistent.txt
ls: nonexistent.txt: No such file or directory
```

### **-t**

Set a specific timestamp instead of using the current time (format: [[CC]YY]MMDDhhmm[.ss])

```console
$ touch -t 202504301530.45 file.txt
$ ls -l file.txt
-rw-r--r--  1 user  staff  0 Apr 30 15:30 file.txt
```

## Usage Examples

### Creating multiple empty files

```console
$ touch file1.txt file2.txt file3.txt
$ ls
file1.txt  file2.txt  file3.txt
```

### Updating timestamps of existing files

```console
$ ls -l document.txt
-rw-r--r--  1 user  staff  1024 Apr 29 10:15 document.txt
$ touch document.txt
$ ls -l document.txt
-rw-r--r--  1 user  staff  1024 Apr 30 14:22 document.txt
```

### Setting a specific date and time

```console
$ touch -t 202501010000.00 new_year.txt
$ ls -l new_year.txt
-rw-r--r--  1 user  staff  0 Jan 1 00:00 new_year.txt
```

## Tips:

### Create Directory Structure with Files

You can use `touch` with `mkdir -p` to create a directory structure with placeholder files in one command:

```console
$ mkdir -p project/{src,docs,tests} && touch project/src/main.py project/docs/readme.md
```

### Use with Find Command

Combine `touch` with `find` to update timestamps for multiple files matching a pattern:

```console
$ find . -name "*.txt" -exec touch {} \;
```

### Preserve Reference File Timestamp

Use the `-r` option to set a file's timestamp to match another file:

```console
$ touch -r reference.txt target.txt
```

## Frequently Asked Questions

#### Q1. What happens if I touch a file that doesn't exist?
A. By default, `touch` creates an empty file with that name.

#### Q2. Can I use touch to create files with specific timestamps?
A. Yes, use the `-t` option with a timestamp in the format [[CC]YY]MMDDhhmm[.ss].

#### Q3. How do I prevent touch from creating new files?
A. Use the `-c` option, which only updates timestamps of existing files.

#### Q4. Does touch change file content?
A. No, touch only creates empty files or updates timestamps without modifying content.

## References

https://www.gnu.org/software/coreutils/manual/html_node/touch-invocation.html

## Revisions

- 2025/04/30 First revision