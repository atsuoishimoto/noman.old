# ssh command

Securely connect to and manage remote systems over an encrypted network connection.

## Overview

SSH (Secure Shell) is a protocol for securely accessing and managing remote computers over an unsecured network. It provides encrypted communication between two hosts, allowing secure remote login, file transfers, and command execution. SSH replaces older, insecure protocols like Telnet and rsh.

## Options

### **-p [port]**

Specify a custom port number (default is 22)

```console
$ ssh -p 2222 user@example.com
user@example.com's password: 
Last login: Wed Apr 30 09:15:22 2025 from 192.168.1.5
user@example.com:~$ 
```

### **-i [identity_file]**

Use a specific private key file for authentication

```console
$ ssh -i ~/.ssh/my_private_key user@example.com
Last login: Wed Apr 30 10:22:45 2025 from 192.168.1.5
user@example.com:~$ 
```

### **-L [local_port:remote_host:remote_port]**

Set up local port forwarding (create a secure tunnel)

```console
$ ssh -L 8080:localhost:80 user@example.com
user@example.com's password: 
Last login: Wed Apr 30 11:30:15 2025 from 192.168.1.5
```

### **-v**

Enable verbose mode for debugging connection issues

```console
$ ssh -v user@example.com
OpenSSH_8.9p1, LibreSSL 3.3.6
debug1: Reading configuration data /Users/user/.ssh/config
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: Connecting to example.com port 22.
...
```

## Usage Examples

### Basic SSH Connection

```console
$ ssh user@example.com
user@example.com's password: 
Last login: Wed Apr 30 08:45:12 2025 from 192.168.1.5
user@example.com:~$ 
```

### Running a Command on a Remote Server

```console
$ ssh user@example.com "ls -la /var/www"
total 24
drwxr-xr-x  5 root     root     4096 Apr 29 14:22 .
drwxr-xr-x 14 root     root     4096 Apr 28 09:15 ..
drwxr-xr-x  2 www-data www-data 4096 Apr 30 10:05 html
```

### Copying Files with SCP (SSH-based file transfer)

```console
$ scp myfile.txt user@example.com:/home/user/
myfile.txt                                 100%  256KB  2.5MB/s  00:01
```

## Tips

### Set Up SSH Key Authentication

Generate and use SSH keys instead of passwords for more secure and convenient logins:

```console
$ ssh-keygen -t ed25519 -C "your_email@example.com"
$ ssh-copy-id user@example.com
```

### Create SSH Config File

Create a `~/.ssh/config` file to store connection settings for frequently accessed servers:

```
Host myserver
    HostName example.com
    User username
    Port 2222
    IdentityFile ~/.ssh/special_key
```

Then simply use: `ssh myserver`

### Keep Connections Alive

Add these lines to your `~/.ssh/config` file to prevent timeouts:

```
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

## Frequently Asked Questions

#### Q1. How do I generate SSH keys?
A. Use `ssh-keygen -t ed25519` (or `ssh-keygen -t rsa -b 4096` for older systems). This creates a public/private key pair in your `~/.ssh` directory.

#### Q2. How can I copy my SSH key to a server?
A. Use `ssh-copy-id user@example.com` to copy your public key to the server's authorized_keys file.

#### Q3. How do I fix "Permission denied (publickey)" errors?
A. Check that your private key permissions are set to 600 (`chmod 600 ~/.ssh/id_ed25519`), ensure the key is added to the server's authorized_keys file, and verify you're using the correct username.

#### Q4. How can I transfer files using SSH?
A. Use the `scp` command (e.g., `scp file.txt user@example.com:~/destination/`) or `sftp` for interactive file transfers.

## macOS Considerations

On macOS, SSH keys are managed through the Keychain by default. To prevent this behavior (which can cause issues with some configurations), add `IdentityAgent none` to your SSH config file or use `ssh -o "IdentityAgent=none"` when connecting.

The macOS SSH client may behave slightly differently than Linux versions, particularly with respect to key management and agent forwarding.

## References

https://www.openssh.com/manual.html

## Revisions

- 2025/04/30 First revision