# sftp command

Securely transfer files between hosts over an encrypted connection.

## Overview

SFTP (Secure File Transfer Protocol) is a network protocol for securely transferring files between computers. It runs over SSH, providing encryption and authentication. The `sftp` command provides an interactive file transfer program similar to FTP but with SSH encryption.

## Options

### **-b** / **--batch** *batchfile*

Processes a batch file of sftp commands instead of running interactively.

```console
$ sftp -b commands.txt user@remote.server
Connecting to remote.server...
Batch file commands.txt processed
```

### **-P** / **--port** *port*

Specifies the port to connect to on the remote host.

```console
$ sftp -P 2222 user@remote.server
Connecting to remote.server port 2222...
sftp>
```

### **-i** / **--identity** *identity_file*

Selects the file from which the identity (private key) for public key authentication is read.

```console
$ sftp -i ~/.ssh/my_key user@remote.server
Connecting to remote.server...
sftp>
```

### **-r** / **--recursive**

Recursively copy entire directories when uploading or downloading.

```console
$ sftp user@remote.server
sftp> get -r remote_directory
Fetching /remote_directory/ to remote_directory
sftp>
```

### **-v** / **--verbose**

Raises the logging level, providing verbose debugging output.

```console
$ sftp -v user@remote.server
OpenSSH_8.9p1, LibreSSL 3.3.6
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: Connecting to remote.server port 22.
...
sftp>
```

## Usage Examples

### Connecting to a Remote Server

```console
$ sftp user@remote.server
Connected to remote.server.
sftp>
```

### Downloading Files

```console
$ sftp user@remote.server
sftp> get remote_file.txt
Fetching /home/user/remote_file.txt to remote_file.txt
sftp>
```

### Uploading Files

```console
$ sftp user@remote.server
sftp> put local_file.txt
Uploading local_file.txt to /home/user/local_file.txt
sftp>
```

### Navigating Directories

```console
$ sftp user@remote.server
sftp> pwd
Remote working directory: /home/user
sftp> cd documents
sftp> lpwd
Local working directory: /Users/localuser
sftp> lcd Downloads
```

## Tips

### Use Tab Completion

SFTP supports tab completion for both local and remote files, making it easier to navigate without typing full paths.

### Interactive Commands

- `ls` - List remote files
- `lls` - List local files
- `cd` - Change remote directory
- `lcd` - Change local directory
- `mkdir` - Create remote directory
- `rmdir` - Remove remote directory
- `rm` - Delete remote files
- `help` or `?` - Show available commands

### Batch Mode for Automation

Create a text file with sftp commands and use the `-b` option for automated transfers in scripts.

### Use Wildcards for Multiple Files

```console
sftp> get *.txt
```

## Frequently Asked Questions

#### Q1. What's the difference between SFTP and SCP?
A. SFTP is an interactive file transfer protocol that runs over SSH, while SCP is a non-interactive command for secure copying. SFTP offers more functionality like resuming transfers and directory listings.

#### Q2. How do I transfer an entire directory?
A. Use the `-r` (recursive) option with the get or put command: `get -r remote_directory` or `put -r local_directory`.

#### Q3. Can I use SFTP in scripts?
A. Yes, use the `-b` option with a batch file containing SFTP commands: `sftp -b commands.txt user@remote.server`.

#### Q4. How do I change permissions of remote files?
A. Use the `chmod` command within the SFTP session: `chmod 644 remote_file.txt`.

#### Q5. How can I resume an interrupted file transfer?
A. Use the `reget` command to resume downloading a file or `reput` to resume uploading.

## References

https://man.openbsd.org/sftp.1

## Revisions

- 2025/05/04 First revision