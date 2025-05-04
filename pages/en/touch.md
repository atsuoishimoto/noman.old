# touch command

Create or update file timestamps.

## Overview

The `touch` command is used to change file timestamps or create empty files if they don't exist. It's commonly used to create new empty files or update the access and modification times of existing files to the current time.

## Options

### **-a, --time=atime, --time=access, --time=use**

Change only the access time.

```console
$ ls -l file.txt
-rw-r--r-- 1 user group 0 May 01 10:00 file.txt
$ touch -a file.txt
$ ls -l file.txt
-rw-r--r-- 1 user group 0 May 01 10:00 file.txt  # Note: Only access time changed, not visible with ls -l
```

### **-c, --no-create**

Do not create files that do not exist.

```console
$ touch -c nonexistent.txt
$ ls nonexistent.txt
ls: cannot access 'nonexistent.txt': No such file or directory
```

### **-d, --date=STRING**

Parse STRING and use it instead of current time.

```console
$ touch -d "2023-12-25 12:00" file.txt
$ ls -l file.txt
-rw-r--r-- 1 user group 0 Dec 25  2023 file.txt
```

### **-m, --time=mtime, --time=modify**

Change only the modification time.

```console
$ touch -m file.txt
$ ls -l file.txt
-rw-r--r-- 1 user group 0 May 04 15:30 file.txt  # Modification time updated
```

### **-r, --reference=FILE**

Use this file's times instead of the current time.

```console
$ ls -l reference.txt
-rw-r--r-- 1 user group 0 Jan 15  2024 reference.txt
$ touch -r reference.txt file.txt
$ ls -l file.txt
-rw-r--r-- 1 user group 0 Jan 15  2024 file.txt
```

## Usage Examples

### Creating multiple empty files

```console
$ touch file1.txt file2.txt file3.txt
$ ls
file1.txt  file2.txt  file3.txt
```

### Updating timestamp to a specific time

```console
$ touch -d "2 days ago" oldfile.txt
$ ls -l oldfile.txt
-rw-r--r-- 1 user group 0 May 02 15:30 oldfile.txt
```

### Creating files with specific permissions

```console
$ umask 022
$ touch newfile.txt
$ ls -l newfile.txt
-rw-r--r-- 1 user group 0 May 04 15:30 newfile.txt
```

## Tips:

### Use touch for Makefile dependencies

When building software, you can use `touch` to update timestamps of files to trigger or avoid rebuilds in build systems like Make.

### Create files with specific timestamps for testing

When testing date-dependent functionality, use `touch -d` to create files with specific timestamps for testing sorting or filtering.

### Batch update timestamps

You can use wildcards to update timestamps of multiple files at once: `touch *.txt` will update all text files in the current directory.

### Check if a file exists without modifying it

Use `touch -c` with a file to check if it exists without creating it if it doesn't.

## Frequently Asked Questions

#### Q1. What happens if I touch a file that already exists?
A. It updates the file's access and modification timestamps to the current time without changing the file's content.

#### Q2. Can touch create directories?
A. No, `touch` can only create files, not directories. Use `mkdir` to create directories.

#### Q3. How can I create a file with a specific timestamp?
A. Use `touch -d "YYYY-MM-DD HH:MM:SS" filename` to set a specific timestamp.

#### Q4. Does touch change file permissions?
A. No, `touch` only affects timestamps. It creates new files with default permissions based on your umask setting.

## References

https://www.gnu.org/software/coreutils/manual/html_node/touch-invocation.html

## Revisions

- 2025/05/04 First revision