# rsync command

Synchronize files and directories between locations, locally or remotely.

## Overview

`rsync` is a fast, versatile file copying and synchronization tool that can work locally or over remote connections. It's designed to efficiently transfer and synchronize files between directories or hosts, copying only the differences between source and destination. This makes it faster than regular copy commands, especially for large files or when synchronizing frequently.

## Options

### **-a, --archive**

Archive mode, which preserves almost everything (equivalent to -rlptgoD). This is the most commonly used option for backup operations.

```console
$ rsync -a /source/directory/ /destination/directory/
```

### **-v, --verbose**

Increase verbosity, showing which files are being transferred.

```console
$ rsync -av /source/directory/ /destination/directory/
sending incremental file list
file1.txt
file2.txt
directory/
directory/file3.txt

sent 1,234 bytes  received 42 bytes  2,552.00 bytes/sec
total size is 10,240  speedup is 8.04
```

### **-z, --compress**

Compress file data during the transfer to reduce bandwidth usage.

```console
$ rsync -avz /source/directory/ user@remote-host:/destination/directory/
```

### **-P, --partial --progress**

Shows progress during transfer and keeps partially transferred files.

```console
$ rsync -avP large_file.iso /backup/
sending incremental file list
large_file.iso
    852,492,288 100%   85.23MB/s    0:00:09 (xfr#1, to-chk=0/1)
```

### **--delete**

Delete files in the destination that don't exist in the source, making the destination an exact mirror.

```console
$ rsync -av --delete /source/directory/ /destination/directory/
```

### **-n, --dry-run**

Perform a trial run without making any changes.

```console
$ rsync -avn --delete /source/directory/ /destination/directory/
sending incremental file list
./
file1.txt
file2.txt

sent 123 bytes  received 42 bytes  330.00 bytes/sec
total size is 10,240  speedup is 62.07 (DRY RUN)
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

sent 2,345,678 bytes  received 1,234 bytes  469,382.40 bytes/sec
total size is 2,340,000  speedup is 0.99
```

### Creating a Backup with Exclusions

```console
$ rsync -av --exclude='*.tmp' --exclude='cache/' /home/user/ /mnt/backup/home/
```

### Mirroring a Website

```console
$ rsync -avz --delete user@remote-server:/var/www/html/ /local/mirror/
```

### Resuming a Large Transfer

```console
$ rsync -avP --partial user@remote-server:large_file.iso /downloads/
```

## Tips:

### Use Trailing Slashes Carefully

When copying directories, a trailing slash on the source (`/source/`) means "copy the contents of this directory" while no trailing slash (`/source`) means "copy this directory and its contents."

### Set Up SSH Keys for Passwordless Transfers

For frequent remote transfers, set up SSH key authentication to avoid entering passwords repeatedly.

### Use Bandwidth Limiting for Background Transfers

```console
$ rsync --bwlimit=1000 -av /source/ /destination/
```
This limits transfer speed to 1000 KB/s, useful for background transfers that shouldn't consume all bandwidth.

### Create Snapshots with Hard Links

```console
$ rsync -a --link-dest=/backup/previous /source/ /backup/current/
```
This creates space-efficient backups by hard-linking unchanged files to previous backups.

## Frequently Asked Questions

#### Q1. How does rsync differ from scp or cp?
A. Unlike `cp` or `scp`, rsync only transfers the differences between files, making it much faster for subsequent transfers of the same data. It also offers more options for preserving file attributes and handling synchronization.

#### Q2. Can rsync resume interrupted transfers?
A. Yes, with the `--partial` option (or `-P`), rsync can resume partially transferred files instead of starting over.

#### Q3. How do I ensure rsync doesn't delete any files in the destination?
A. By default, rsync doesn't delete files. It only adds or updates files from the source. The `--delete` option must be explicitly specified to remove files in the destination that don't exist in the source.

#### Q4. How can I test what rsync will do before actually doing it?
A. Use the `--dry-run` or `-n` option to see what would be transferred without making any actual changes.

#### Q5. Can rsync synchronize files between two remote servers?
A. Yes, but you need to run rsync on one of the servers or use the `--rsync-path` option to specify the path to rsync on the remote machine.

## References

https://download.samba.org/pub/rsync/rsync.html

## Revisions

- 2025/05/04 First revision