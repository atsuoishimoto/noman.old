# scp command

Securely copy files between hosts on a network using SSH for data transfer.

## Overview

`scp` (secure copy) allows you to transfer files between computers over a secure, encrypted connection. It uses SSH (Secure Shell) protocol to ensure data is protected during transfer. You can copy files to/from remote servers or between two remote servers.

## Options

### **-r** (recursive)

Copy directories and their contents recursively

```console
$ scp -r documents/ user@remote-server:/home/user/backup/
documents/file1.txt                   100%  123KB  1.2MB/s  00:01
documents/file2.txt                   100%  456KB  2.3MB/s  00:02
documents/subfolder/file3.txt         100%   78KB  1.0MB/s  00:01
```

### **-P** (port)

Specify a different port for the SSH connection

```console
$ scp -P 2222 file.txt user@remote-server:/home/user/
file.txt                              100%  512KB  3.1MB/s  00:02
```

### **-p** (preserve)

Preserve file modification and access times, and modes

```console
$ scp -p important.conf user@remote-server:/etc/
important.conf                        100%   2KB  1.0MB/s  00:01
```

### **-C** (compress)

Compress file data during transfer to reduce bandwidth

```console
$ scp -C large-file.zip user@remote-server:/home/user/
large-file.zip                        100%  50MB  5.2MB/s  00:10
```

### **-l** (limit)

Limit bandwidth used (specified in Kbit/s)

```console
$ scp -l 1000 huge-file.iso user@remote-server:/home/user/
huge-file.iso                         100%  4GB   1.0MB/s  01:08:20
```

## Usage Examples

### Copying a file to a remote server

```console
$ scp document.txt user@remote-server:/path/to/destination/
document.txt                          100%  256KB  2.5MB/s  00:01
```

### Copying a file from a remote server

```console
$ scp user@remote-server:/path/to/file.txt ./
file.txt                              100%  128KB  1.8MB/s  00:01
```

### Copying between two remote servers

```console
$ scp user1@server1:/path/to/file.txt user2@server2:/destination/
file.txt                              100%  512KB  3.0MB/s  00:02
```

### Copying multiple files at once

```console
$ scp file1.txt file2.txt user@remote-server:/destination/
file1.txt                             100%  128KB  1.5MB/s  00:01
file2.txt                             100%  256KB  2.0MB/s  00:02
```

## Tips:

### Use SSH Keys for Password-less Transfers

Set up SSH key authentication to avoid typing passwords for each transfer. This is both more secure and more convenient.

### Escape Special Characters in Filenames

When filenames contain spaces or special characters, use quotes or escape them with backslashes:
```console
$ scp "file with spaces.txt" user@server:/path/
```

### Use Wildcards for Multiple Files

Transfer multiple files at once using wildcards, but remember they're expanded locally:
```console
$ scp *.pdf user@server:/path/
```

### Verify Transfers with Checksums

For critical files, verify the transfer was successful by comparing checksums:
```console
$ sha256sum file.txt
$ ssh user@server "sha256sum /path/to/file.txt"
```

## Frequently Asked Questions

#### Q1. How do I copy an entire directory?
A. Use the `-r` (recursive) option: `scp -r directory/ user@server:/path/`

#### Q2. How can I speed up transfers of large files?
A. Use the `-C` option to enable compression: `scp -C large-file.iso user@server:/path/`

#### Q3. How do I connect to a server using a non-standard SSH port?
A. Use the `-P` option to specify the port: `scp -P 2222 file.txt user@server:/path/`

#### Q4. Can I resume an interrupted transfer?
A. No, `scp` doesn't support resuming transfers. For large files that might be interrupted, consider using `rsync` instead.

#### Q5. How do I copy files between two remote servers without going through my local machine?
A. Use the syntax: `scp user1@server1:/path/file user2@server2:/destination/`

## References

https://man.openbsd.org/scp.1

## Revisions

- 2025/04/30 First revision