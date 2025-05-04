# df command

Display information about disk space usage on mounted filesystems.

## Overview

The `df` command reports the amount of disk space used and available on file systems. By default, it shows space in 1K blocks, but can be configured to display in human-readable formats. It's commonly used to monitor disk usage and identify filesystems that are running low on space.

## Options

### **-h, --human-readable**

Display sizes in human-readable format (e.g., 1K, 234M, 2G)

```console
$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        20G  7.8G   11G  42% /
tmpfs           3.9G     0  3.9G   0% /dev/shm
/dev/sda3       450G  254G  174G  60% /home
```

### **-T, --print-type**

Print filesystem type (e.g., ext4, xfs)

```console
$ df -T
Filesystem     Type     1K-blocks     Used Available Use% Mounted on
/dev/sda1      ext4      20971520  8126464  11714048  42% /
tmpfs          tmpfs      4048380        0   4048380   0% /dev/shm
/dev/sda3      ext4     471859200 266338304 181889024  60% /home
```

### **-i, --inodes**

List inode information instead of block usage

```console
$ df -i
Filesystem      Inodes  IUsed    IFree IUse% Mounted on
/dev/sda1      1310720 248932  1061788   19% /
tmpfs          1012095      1  1012094    1% /dev/shm
/dev/sda3      29491200 845621 28645579    3% /home
```

### **-a, --all**

Include filesystems with 0 blocks or that are otherwise ignored by default

```console
$ df -a
Filesystem     1K-blocks     Used Available Use% Mounted on
/dev/sda1       20971520  8126464  11714048  42% /
proc                   0        0         0    - /proc
sysfs                  0        0         0    - /sys
tmpfs            4048380        0   4048380   0% /dev/shm
/dev/sda3      471859200 266338304 181889024  60% /home
```

## Usage Examples

### Checking space on a specific filesystem

```console
$ df -h /home
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda3       450G  254G  174G  60% /home
```

### Combining options for detailed output

```console
$ df -hT
Filesystem     Type   Size  Used Avail Use% Mounted on
/dev/sda1      ext4    20G  7.8G   11G  42% /
tmpfs          tmpfs  3.9G     0  3.9G   0% /dev/shm
/dev/sda3      ext4   450G  254G  174G  60% /home
```

## Tips:

### Focus on Important Filesystems

Use `df -h | grep -v tmpfs` to exclude temporary filesystems when you only want to see physical disks.

### Monitor Critical Filesystems

Set up alerts when filesystems exceed a certain percentage. For example, check if root is over 90% full: `df -h / | awk 'NR==2 {print $5}' | sed 's/%//'`.

### Check Inode Usage

Sometimes filesystems run out of inodes before they run out of space, especially when there are many small files. Use `df -i` to monitor inode usage.

## Frequently Asked Questions

#### Q1. What does "Use%" mean in the df output?
A. It shows the percentage of the filesystem that is currently in use. Values approaching 100% indicate the filesystem is nearly full.

#### Q2. Why does df show less free space than I expected?
A. By default, most filesystems reserve 5% of space for the root user and system processes. This reserved space isn't counted as available to regular users.

#### Q3. How can I see disk usage in gigabytes instead of kilobytes?
A. Use `df -h` for human-readable output that automatically scales to the appropriate unit (KB, MB, GB, etc.).

#### Q4. Why do some filesystems show 0 blocks or 100% usage?
A. Virtual filesystems like /proc and /sys show 0 blocks because they don't use actual disk space. They exist only in memory.

## macOS Considerations

On macOS, the `df` command has slightly different options. The `-T` option is not available, and the output format differs. Use `df -h` for human-readable output, which works consistently across platforms.

## References

https://www.gnu.org/software/coreutils/manual/html_node/df-invocation.html

## Revisions

- 2025/05/04 First revision