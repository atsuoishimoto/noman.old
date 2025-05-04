# scp command

Securely copy files between hosts on a network using SSH for data transfer.

## Overview

`scp` (secure copy) is a command-line utility that allows you to securely transfer files between computers over an encrypted SSH connection. It combines the functionality of the `cp` command with the security of SSH, making it a safe way to copy files to, from, or between remote servers.

## Options

### **-r, --recursive**

Recursively copy entire directories

```console
$ scp -r documents/ user@remote:/home/user/backup/
documents/file1.txt                 100%  123     1.2KB/s   00:00    
documents/file2.txt                 100%  456     2.3KB/s   00:00
documents/subfolder/file3.txt       100%  789     3.4KB/s   00:00
```

### **-P, --port**

Specify a different port to connect to on the remote host

```console
$ scp -P 2222 file.txt user@remote:/home/user/
file.txt                            100%  123     1.2KB/s   00:00
```

### **-p**

Preserve modification times, access times, and modes from the original file

```console
$ scp -p important.txt user@remote:/home/user/
important.txt                       100%  123     1.2KB/s   00:00
```

### **-q, --quiet**

Quiet mode: disables progress meter and warning/diagnostic messages

```console
$ scp -q large_file.zip user@remote:/home/user/
```

### **-C, --compress**

Enable compression during file transfer

```console
$ scp -C large_file.zip user@remote:/home/user/
large_file.zip                      100%  10MB    5.0MB/s   00:02
```

### **-l, --limit-bandwidth**

Limit bandwidth used (specified in Kbit/s)

```console
$ scp -l 1000 large_file.zip user@remote:/home/user/
large_file.zip                      100%  10MB    1.0MB/s   00:10
```

## Usage Examples

### Copying a local file to a remote server

```console
$ scp document.txt user@remote.server:/path/to/destination/
document.txt                        100%  123     1.2KB/s   00:00
```

### Copying a file from a remote server to local machine

```console
$ scp user@remote.server:/path/to/file.txt ./
file.txt                            100%  123     1.2KB/s   00:00
```

### Copying between two remote servers

```console
$ scp user1@server1:/path/to/file.txt user2@server2:/path/to/destination/
file.txt                            100%  123     1.2KB/s   00:00
```

### Copying multiple files at once

```console
$ scp file1.txt file2.txt user@remote:/home/user/
file1.txt                           100%  123     1.2KB/s   00:00
file2.txt                           100%  456     2.3KB/s   00:00
```

## Tips:

### Use SSH Keys for Passwordless Transfers

Set up SSH key authentication to avoid entering passwords for each transfer. This is both more secure and more convenient for frequent transfers.

### Escape Special Characters in Filenames

When transferring files with spaces or special characters, use quotes or escape the characters:
```console
$ scp "file with spaces.txt" user@remote:/home/user/
```

### Verify Fingerprints for New Connections

Always verify the SSH fingerprint when connecting to a new server to prevent man-in-the-middle attacks.

### Use Compression for Slow Connections

The `-C` option enables compression, which can significantly speed up transfers over slow network connections, especially for text files.

## Frequently Asked Questions

#### Q1. How does scp differ from regular cp?
A. `scp` works over a network using SSH encryption, while `cp` only works locally. `scp` requires authentication and provides secure, encrypted file transfers.

#### Q2. Can I resume an interrupted file transfer with scp?
A. No, `scp` doesn't support resuming interrupted transfers. For that functionality, consider using `rsync` with the `-P` option.

#### Q3. How can I transfer an entire directory?
A. Use the `-r` (recursive) option: `scp -r /path/to/directory user@remote:/destination/`

#### Q4. How do I specify a non-standard SSH port?
A. Use the `-P` option: `scp -P 2222 file.txt user@remote:/home/user/`

## References

https://man.openbsd.org/scp.1

## Revisions

- 2025/05/04 First revision