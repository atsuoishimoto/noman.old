# df command

Display free disk space on the file system.

## Overview

The `df` command reports file system disk space usage, showing the amount of used and available space on mounted file systems. It helps monitor disk usage and identify file systems that are running low on space.

## Options

### **-h, --human-readable**

Display sizes in human-readable format (e.g., KB, MB, GB) instead of blocks.

```console
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G   12G  6.8G  64% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
/dev/sda2       450G  298G  130G  70% /home
```

### **-T, --print-type**

Show the file system type for each mount point.

```console
$ df -T
Filesystem     Type     1K-blocks     Used Available Use% Mounted on
/dev/sda1      ext4      20971520 12582912   7077888  64% /
tmpfs          tmpfs      4096000        0   4096000   0% /dev/shm
/dev/sda2      ext4     471859200 312475648 136314880  70% /home
```

### **-i, --inodes**

Display inode information instead of block usage.

```console
$ df -i
Filesystem      Inodes  IUsed    IFree IUse% Mounted on
/dev/sda1      1310720 248930  1061790   19% /
tmpfs          1024000     12  1023988    1% /dev/shm
/dev/sda2      29491200 983041 28508159    4% /home
```

## Usage Examples

### Check space on a specific file system

```console
$ df -h /home
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda2       450G  298G  130G  70% /home
```

### Combine options for comprehensive output

```console
$ df -hT
Filesystem     Type   Size  Used Avail Use% Mounted on
/dev/sda1      ext4    20G   12G  6.8G  64% /
tmpfs          tmpfs  3.9G     0  3.9G   0% /dev/shm
/dev/sda2      ext4   450G  298G  130G  70% /home
```

## Tips

### Focus on Important File Systems

Use `df -h | grep -v tmpfs` to exclude temporary file systems and focus on physical disks.

### Check Inode Usage

Sometimes a file system appears to have space but can't create new files. Use `df -i` to check if you're running out of inodes, which can happen with many small files.

### Combine with Sort

Use `df -h | sort -k 5 -h` to sort file systems by usage percentage, helping identify the most filled partitions.

## Frequently Asked Questions

#### Q1. What's the difference between `df` and `du`?
A. `df` shows disk space usage at the file system level, while `du` shows disk usage at the directory/file level.

#### Q2. Why does `df` show different available space than my file manager?
A. Most file systems reserve some space for the root user (typically 5%), which `df` includes in its calculations.

#### Q3. How do I check disk space on a specific directory?
A. `df` reports on file systems, not directories. Use `du -sh /path/to/directory` to check space used by a specific directory.

#### Q4. Why does `df` show 100% usage but I can still write files?
A. Reserved space for the root user allows the system to continue functioning even when user space is full.

## macOS Considerations

On macOS, `df` behaves slightly differently:
- The default output uses 512-byte blocks instead of 1K blocks
- Use `df -h` to get human-readable output similar to Linux
- macOS doesn't support all GNU options; `-T` may not work as expected

## References

https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html

## Revisions

- 2025/04/30 First revision