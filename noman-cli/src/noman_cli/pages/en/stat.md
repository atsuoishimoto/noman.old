# stat command

Display file or file system status information.

## Overview

The `stat` command displays detailed information about files or file systems, including access permissions, ownership, size, timestamps, and inode details. It provides more comprehensive information than what you get from `ls -l`.

## Options

### **-f, --file-system**

Display file system information instead of file information.

```console
$ stat -f /home
  File: "/home"
    ID: 2f400000000000000 Namelen: 255     Type: ext4
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 244033764   Free: 146937542   Available: 134209270
Inodes: Total: 62259200    Free: 60948748
```

### **-c, --format=FORMAT**

Use the specified FORMAT instead of the default output format.

```console
$ stat -c "%n %s %y" file.txt
file.txt 1024 2025-05-01 14:30:45.123456789 +0000
```

### **-t, --terse**

Print the information in terse form.

```console
$ stat -t file.txt
file.txt 1024 8 81a4 1000 1000 fe01 1620000000 1620000000 1620000000 4096 8 0 0
```

### **-L, --dereference**

Follow links when displaying information for a symbolic link.

```console
$ stat -L symlink.txt
  File: 'symlink.txt'
  Size: 1024      	Blocks: 8          IO Block: 4096   regular file
Device: fd00h/64768d	Inode: 12345      Links: 1
Access: (0644/-rw-r--r--)  Uid: (1000/username)   Gid: (1000/groupname)
Access: 2025-05-01 10:00:00.000000000 +0000
Modify: 2025-05-01 10:00:00.000000000 +0000
Change: 2025-05-01 10:00:00.000000000 +0000
 Birth: 2025-05-01 10:00:00.000000000 +0000
```

## Usage Examples

### Basic file information

```console
$ stat file.txt
  File: file.txt
  Size: 1024      	Blocks: 8          IO Block: 4096   regular file
Device: fd00h/64768d	Inode: 12345      Links: 1
Access: (0644/-rw-r--r--)  Uid: (1000/username)   Gid: (1000/groupname)
Access: 2025-05-01 10:00:00.000000000 +0000
Modify: 2025-05-01 10:00:00.000000000 +0000
Change: 2025-05-01 10:00:00.000000000 +0000
 Birth: 2025-05-01 10:00:00.000000000 +0000
```

### Custom format to show specific information

```console
$ stat -c "File: %n, Size: %s bytes, Modified: %y" file.txt
File: file.txt, Size: 1024 bytes, Modified: 2025-05-01 10:00:00.000000000 +0000
```

### File system information

```console
$ stat -f /
  File: "/"
    ID: 2f400000000000000 Namelen: 255     Type: ext4
Block size: 4096       Fundamental block size: 4096
Blocks: Total: 244033764   Free: 146937542   Available: 134209270
Inodes: Total: 62259200    Free: 60948748
```

## Tips

### Get Only the Information You Need

Use the `-c` option with format specifiers to extract only the information you need. For example, `stat -c "%s" file.txt` will show only the file size.

### Compare File Timestamps

Use `stat` to check when a file was last accessed, modified, or had its metadata changed. This is useful for troubleshooting or verifying file operations.

### Check Inode Information

The inode number displayed by `stat` can help identify if two files are hard-linked to the same data (they'll have the same inode number).

### macOS Differences

On macOS, the format options are different. Use `-f` with format specifiers like `%z` for size, `%m` for modification time, etc. The GNU-style long options are not available.

## Frequently Asked Questions

#### Q1. What's the difference between `stat` and `ls -l`?
A. `stat` provides more detailed information than `ls -l`, including precise timestamps, inode numbers, and device IDs. It's more comprehensive for file metadata analysis.

#### Q2. How can I see only the file size?
A. Use `stat -c "%s" filename` on Linux or `stat -f "%z" filename` on macOS.

#### Q3. How do I check when a file was last modified?
A. Use `stat -c "%y" filename` on Linux or `stat -f "%m" filename` on macOS (the latter shows seconds since epoch).

#### Q4. Can I use `stat` on directories?
A. Yes, `stat` works on directories just like it does on files, showing their metadata.

## References

https://www.gnu.org/software/coreutils/manual/html_node/stat-invocation.html

## Revisions

- 2025/05/04 First revision