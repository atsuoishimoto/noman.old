# stat command

Display file or file system status information.

## Overview

The `stat` command shows detailed information about files, directories, or file systems. It provides metadata such as file size, permissions, access times, inode information, and more. This is useful for troubleshooting, scripting, or when you need detailed information beyond what `ls` provides.

## Options

### **-f**

Display information about the file system instead of individual files

```console
$ stat -f /
  File: "/"
    ID: 0        Namelen: 255     Type: APFS
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 244108262  Free: 146464768  Available: 146464768
Inodes: Total: 1000000000 Free: 999739317
```

### **-t, --terse**

Print the information in a terse, more machine-readable format

```console
$ stat -t file.txt
file.txt 8 8 81a4 1000 1000 103 1714503412 1714503412 1714503412 1714503412 4096 8 0
```

### **-c, --format=FORMAT**

Use a custom format for the output, allowing you to specify exactly what information you want

```console
$ stat -c "%n %s %U" file.txt
file.txt 1024 user
```

### **-L, --dereference**

Follow links and display information about the file they refer to, not the link itself

```console
$ stat -L symlink.txt
  File: symlink.txt
  Size: 1024      Blocks: 8          IO Block: 4096   regular file
Device: 801h/2049d Inode: 8193       Links: 1
Access: (0644/-rw-r--r--)  Uid: (1000/user)   Gid: (1000/user)
Access: 2025-04-30 10:30:12.000000000 +0000
Modify: 2025-04-30 10:30:12.000000000 +0000
Change: 2025-04-30 10:30:12.000000000 +0000
 Birth: 2025-04-30 10:30:12.000000000 +0000
```

## Usage Examples

### Viewing detailed file information

```console
$ stat document.txt
  File: document.txt
  Size: 1024      Blocks: 8          IO Block: 4096   regular file
Device: 801h/2049d Inode: 8193       Links: 1
Access: (0644/-rw-r--r--)  Uid: (1000/user)   Gid: (1000/user)
Access: 2025-04-30 10:30:12.000000000 +0000
Modify: 2025-04-30 10:30:12.000000000 +0000
Change: 2025-04-30 10:30:12.000000000 +0000
 Birth: 2025-04-30 10:30:12.000000000 +0000
```

### Checking file system information

```console
$ stat -f /home
  File: "/home"
    ID: 0        Namelen: 255     Type: APFS
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 244108262  Free: 146464768  Available: 146464768
Inodes: Total: 1000000000 Free: 999739317
```

### Custom format to extract specific information

```console
$ stat -c "File: %n, Size: %s bytes, Owner: %U, Permissions: %A" document.txt
File: document.txt, Size: 1024 bytes, Owner: user, Permissions: -rw-r--r--
```

## Tips:

### Use Custom Formats for Scripts

The `-c` option with format specifiers is extremely useful in scripts when you need to extract specific information. For example, `stat -c "%s" file.txt` will output only the file size.

### Check File Times

`stat` shows all file timestamps (access, modify, change, and birth), which is useful for forensics or debugging file access issues.

### Compare Files

Use `stat` to compare metadata between files, especially when troubleshooting permission or ownership problems.

### macOS Differences

On macOS, the format options are different from Linux. Use `-f "%z %N"` instead of `-c "%s %n"` to get file size and name.

## Frequently Asked Questions

#### Q1. What's the difference between `stat` and `ls -l`?
A. `stat` provides more detailed metadata than `ls -l`, including all timestamps, inode information, and device IDs.

#### Q2. How can I get only the file size?
A. Use `stat -c "%s" filename` on Linux or `stat -f "%z" filename` on macOS.

#### Q3. Can I use `stat` to check if a file exists?
A. Yes, `stat` returns an error if the file doesn't exist, making it useful in scripts to check file existence.

#### Q4. How do I check disk space with `stat`?
A. Use `stat -f filesystem_path` to see total, free, and available blocks on a file system.

## References

https://man7.org/linux/man-pages/man1/stat.1.html

## Revisions

- 2025/04/30 First revision