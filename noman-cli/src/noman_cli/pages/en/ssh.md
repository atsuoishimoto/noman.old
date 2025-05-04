# ssh command

Securely connect to remote machines over an encrypted network connection.

## Overview

SSH (Secure Shell) is a protocol for securely accessing remote computers. The `ssh` command establishes encrypted connections to remote servers, allowing secure terminal access, file transfers, and port forwarding. It's the standard method for administering remote systems and replacing older, insecure protocols like telnet.

## Options

### **-p, --port PORT**

Specifies the port to connect to on the remote host (default is 22)

```console
$ ssh -p 2222 user@example.com
user@example.com's password: 
Last login: Mon May 4 09:15:22 2025 from 192.168.1.5
user@example.com:~$ 
```

### **-i, --identity_file KEYFILE**

Selects a file from which the identity (private key) for public key authentication is read

```console
$ ssh -i ~/.ssh/my_private_key user@example.com
Last login: Mon May 4 10:30:15 2025 from 192.168.1.5
user@example.com:~$ 
```

### **-v, --verbose**

Enables verbose mode, showing detailed connection information (use -vv or -vvv for more detail)

```console
$ ssh -v user@example.com
OpenSSH_8.9p1, LibreSSL 3.3.6
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: Connecting to example.com port 22.
debug1: Connection established.
...
```

### **-L PORT:HOST:HOSTPORT**

Sets up local port forwarding, connecting a local port to a remote host and port

```console
$ ssh -L 8080:localhost:80 user@example.com
user@example.com's password: 
Last login: Mon May 4 11:45:33 2025 from 192.168.1.5
```

### **-X, --enable X11 forwarding**

Enables X11 forwarding for running graphical applications remotely

```console
$ ssh -X user@example.com
user@example.com's password: 
Last login: Mon May 4 12:20:10 2025 from 192.168.1.5
user@example.com:~$ firefox &
[1] 12345
```

## Usage Examples

### Basic Connection

```console
$ ssh username@hostname
username@hostname's password: 
Last login: Mon May 4 08:30:45 2025 from 192.168.1.5
username@hostname:~$ 
```

### Running a Command on Remote Server

```console
$ ssh user@example.com "ls -la /var/log"
total 1024
drwxr-xr-x 10 root root   4096 May  4 08:15 .
drwxr-xr-x 14 root root   4096 Apr 30 09:22 ..
-rw-r-----  1 root adm  125376 May  4 08:10 auth.log
-rw-r-----  1 root adm   15233 May  4 08:12 syslog
```

### Secure File Copy Using SSH

```console
$ scp -P 2222 localfile.txt user@example.com:/home/user/
user@example.com's password: 
localfile.txt                                 100%  156KB  2.5MB/s  00:00
```

### Port Forwarding to Access a Remote Web Server

```console
$ ssh -L 8080:localhost:80 user@example.com
user@example.com's password: 
Last login: Mon May 4 14:30:22 2025 from 192.168.1.5
```

## Tips

### Use SSH Config File

Create a `~/.ssh/config` file to store connection settings for different hosts:

```
Host myserver
    HostName example.com
    User username
    Port 2222
    IdentityFile ~/.ssh/id_rsa_example
```

Then simply use `ssh myserver` to connect.

### Set Up SSH Keys for Password-less Login

Generate keys with `ssh-keygen` and copy to remote server with `ssh-copy-id user@hostname` to avoid typing passwords.

### Keep SSH Connections Alive

Add these lines to `~/.ssh/config` to prevent timeouts:

```
Host *
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

### Use Agent Forwarding for Multi-hop Connections

Use `ssh -A user@server1` to forward your authentication agent, allowing you to connect from server1 to other servers without copying your keys.

## Frequently Asked Questions

#### Q1. How do I generate SSH keys?
A. Use `ssh-keygen -t rsa -b 4096` to generate a strong RSA key pair. The public key (.pub) is shared with servers, while the private key remains secret.

#### Q2. How can I make SSH connections faster?
A. Use `ssh -o ControlMaster=auto -o ControlPath=~/.ssh/control-%h-%p-%r -o ControlPersist=yes user@host` to enable connection sharing, or add these settings to your SSH config file.

#### Q3. How do I troubleshoot SSH connection issues?
A. Use `ssh -v user@host` (or `-vv` or `-vvv` for more detail) to see verbose connection information that can help identify problems.

#### Q4. How can I securely copy files between servers?
A. Use `scp` for individual files or `rsync -e ssh` for directories and efficient transfers with resume capability.

## macOS Precautions

On macOS, the SSH agent behavior differs slightly from Linux. To ensure your SSH keys are properly loaded:

1. Use `ssh-add -K ~/.ssh/your_key` to store keys in the macOS keychain
2. For macOS Monterey (12) and later, add this to `~/.ssh/config`:
   ```
   Host *
     UseKeychain yes
     AddKeysToAgent yes
   ```
3. macOS may prompt for keychain access when using SSH keys

## References

https://man.openbsd.org/ssh.1

## Revisions

- 2025/05/04 First revision