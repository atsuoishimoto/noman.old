# sftp command

Securely transfer files between hosts over an encrypted SSH connection.

## Overview

SFTP (Secure File Transfer Protocol) is a network protocol that provides file access, file transfer, and file management over a secure connection. It's built on top of SSH (Secure Shell) and offers similar security features while allowing you to upload and download files between your local machine and remote servers.

## Options

### **-P port**

Specify a different port to connect to on the remote host

```console
$ sftp -P 2222 user@example.com
Connected to example.com.
sftp>
```

### **-i identity_file**

Selects the file from which the identity (private key) for public key authentication is read

```console
$ sftp -i ~/.ssh/my_private_key user@example.com
Connected to example.com.
sftp>
```

### **-b batchfile**

Batch mode: read a series of commands from a file instead of interactive mode

```console
$ echo "get remote_file.txt" > commands.txt
$ sftp -b commands.txt user@example.com
```

### **-r**

Recursively copy entire directories when used with get or put commands

```console
sftp> get -r remote_directory
Fetching /remote_directory/ to remote_directory
...
sftp>
```

## Usage Examples

### Connecting to a remote server

```console
$ sftp user@example.com
Connected to example.com.
sftp>
```

### Uploading a file to the remote server

```console
sftp> put local_file.txt
Uploading local_file.txt to /home/user/local_file.txt
local_file.txt                                 100%  1234     1.2KB/s   00:01
sftp>
```

### Downloading a file from the remote server

```console
sftp> get remote_file.txt
Fetching /home/user/remote_file.txt to remote_file.txt
remote_file.txt                                100%  5678     5.6KB/s   00:01
sftp>
```

### Navigating directories

```console
sftp> pwd
Remote working directory: /home/user
sftp> cd documents
sftp> lpwd
Local working directory: /Users/localuser
sftp> lcd Downloads
sftp>
```

## Tips:

### Use Tab Completion

SFTP supports tab completion for both local and remote files, making it easier to navigate without typing full paths.

### Common SFTP Commands

- `ls` - List remote files
- `lls` - List local files
- `cd` - Change remote directory
- `lcd` - Change local directory
- `mkdir` - Create remote directory
- `lmkdir` - Create local directory
- `rm` - Delete remote file
- `rmdir` - Delete remote directory
- `bye` or `exit` - Exit sftp

### Automate Transfers with Scripts

For repetitive transfers, create a batch file with SFTP commands and use the `-b` option to automate the process.

## Frequently Asked Questions

#### Q1. What's the difference between SFTP and FTP?
A. SFTP is secure and encrypted as it runs over SSH, while traditional FTP sends data (including passwords) in plain text. SFTP is generally preferred for security reasons.

#### Q2. How do I transfer an entire directory?
A. Use the `-r` (recursive) option with the get or put command: `get -r remote_directory` or `put -r local_directory`.

#### Q3. Can I use SFTP with a password instead of keys?
A. Yes, SFTP will prompt for a password if key authentication isn't set up or fails.

#### Q4. How do I resume a failed transfer?
A. Use the `reget` or `reput` commands to resume interrupted downloads or uploads.

## References

https://man.openbsd.org/sftp.1

## Revisions

- 2025/04/30 First revision