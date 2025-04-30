# rsync command

Synchronize files and directories between locations efficiently.

## Overview

`rsync` is a fast, versatile file copying and synchronization tool that can work locally or over remote connections. It's designed to efficiently transfer and synchronize files between directories or systems by copying only the differences between source and destination, making it much faster than regular copy tools for subsequent transfers.

## Options

### **-a, --archive**

Archive mode, which preserves permissions, ownership, timestamps, and recursively copies directories.

```console
$ rsync -a /source/directory/ /destination/directory/
```

### **-v, --verbose**

Displays detailed information about the transfer process.

```console
$ rsync -av /source/directory/ /destination/directory/
sending incremental file list
./
file1.txt
file2.txt
directory/
directory/file3.txt

sent 1,234 bytes  received 42 bytes  2,552.00 bytes/sec
total size is 10,240  speedup is 8.04
```

### **-z, --compress**

Compresses file data during the transfer, useful for slow connections.

```console
$ rsync -avz /source/directory/ user@remote-host:/destination/directory/
```

### **--delete**

Deletes files in the destination that don't exist in the source, making the destination an exact mirror.

```console
$ rsync -av --delete /source/directory/ /destination/directory/
```

### **-n, --dry-run**

Performs a trial run without making any changes, showing what would happen.

```console
$ rsync -avn --delete /source/directory/ /destination/directory/
```

## Usage Examples

### Synchronizing to a Remote Server

```console
$ rsync -avz ~/Documents/ user@remote-server:/backup/documents/
sending incremental file list
./
report.docx
presentation.pptx
data.xlsx

sent 15,234 bytes  received 52 bytes  10,190.67 bytes/sec
total size is 45,678  speedup is 2.99
```

### Backing Up with Exclusions

```console
$ rsync -av --exclude='*.tmp' --exclude='cache/' /home/user/ /media/backup/
```

### Mirroring a Website

```console
$ rsync -avz --delete user@website.com:/var/www/html/ /local/mirror/
```

## Tips

### Use Trailing Slashes Carefully

A trailing slash on the source means "copy the contents of this directory," while no trailing slash means "copy this directory and its contents." This subtle difference can significantly affect the result.

### Protect Against Accidental Overwrites

Use `--dry-run` first to see what changes would be made before running the actual command, especially when using `--delete`.

### Limit Bandwidth Usage

Use `--bwlimit=RATE` to limit bandwidth usage (in KB/s), which is helpful when syncing over a network without consuming all available bandwidth.

### Resume Interrupted Transfers

If a transfer is interrupted, simply run the same command again, and rsync will continue where it left off, transferring only the remaining data.

## Frequently Asked Questions

#### Q1. How does rsync differ from regular copy commands?
A. rsync only transfers the differences between files, making subsequent transfers much faster, and it offers many options for preserving file attributes and handling remote transfers.

#### Q2. Can rsync work over SSH?
A. Yes, rsync uses SSH by default for remote transfers, providing security and authentication.

#### Q3. How do I exclude multiple file types?
A. Use multiple `--exclude` options or create an exclude file with patterns and use `--exclude-from=FILE`.

#### Q4. Can rsync delete files?
A. Yes, with the `--delete` option, rsync will remove files in the destination that don't exist in the source.

#### Q5. How do I sync files while preserving hard links?
A. Use the `-H` or `--hard-links` option to preserve hard links between files in the transfer.

## References

https://rsync.samba.org/documentation.html

## Revisions

- 2025/04/30 First revision