# ssh-copy-id command

Installs your public key in a remote machine's authorized keys file.

## Overview

`ssh-copy-id` is a utility that copies your SSH public key to a remote server's `~/.ssh/authorized_keys` file, enabling password-less SSH logins. This tool simplifies the process of setting up key-based authentication, which is more secure than password authentication and eliminates the need to type passwords for each login.

## Options

### **-i identity_file** 

Specifies the identity file (private key) to use. The corresponding public key will be copied to the server.

```console
$ ssh-copy-id -i ~/.ssh/custom_key.pub user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

### **-f**

Forces the installation, even if the key already exists on the remote server.

```console
$ ssh-copy-id -f user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

### **-n**

Performs a dry run, showing what keys would be installed without actually installing them.

```console
$ ssh-copy-id -n user@remote-host
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/user/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
Would have added the following key(s):
ssh-rsa AAAAB3NzaC1yc2EAAA...truncated...user@local-host
```

### **-p port**

Specifies the port to connect to on the remote host.

```console
$ ssh-copy-id -p 2222 user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh -p 2222 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

## Usage Examples

### Basic Usage

```console
$ ssh-copy-id user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

### Using a Specific Identity File

```console
$ ssh-copy-id -i ~/.ssh/id_ed25519.pub user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

### Using a Non-Standard SSH Port

```console
$ ssh-copy-id -p 2222 user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh -p 2222 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

## Tips

### Generate SSH Keys First

Before using `ssh-copy-id`, ensure you have SSH keys generated. If not, create them with:

```console
$ ssh-keygen -t rsa -b 4096
```

### Verify Key Installation

After running `ssh-copy-id`, verify the setup by attempting to SSH into the remote server. You should connect without being prompted for a password.

### Multiple Keys

If you have multiple SSH keys, specify which public key to install using the `-i` option. Otherwise, `ssh-copy-id` will use the default keys in your `~/.ssh` directory.

### Remote Server Requirements

The remote server must have SSH server running and allow password authentication initially (to set up key-based authentication).

## Frequently Asked Questions

#### Q1. What does ssh-copy-id actually do?
A. It copies your public SSH key to the remote server's `~/.ssh/authorized_keys` file, enabling password-less SSH logins using key-based authentication.

#### Q2. Do I need to run ssh-copy-id more than once?
A. You only need to run it once per key per server. If you generate a new key or want to access a new server, you'll need to run it again.

#### Q3. What if ssh-copy-id fails?
A. Common issues include: the remote server doesn't have the `~/.ssh` directory (it will be created), incorrect permissions on the remote `~/.ssh` directory, or SSH password authentication is disabled on the server.

#### Q4. Can I use ssh-copy-id with a custom SSH configuration?
A. Yes, `ssh-copy-id` uses your SSH configuration. If you have custom settings in `~/.ssh/config`, they will be applied.

#### Q5. How do I remove a key I've added with ssh-copy-id?
A. You need to manually edit the `~/.ssh/authorized_keys` file on the remote server and remove the line containing the key you want to remove.

## macOS Precautions

On macOS, `ssh-copy-id` may not be installed by default. You can install it via Homebrew with `brew install ssh-copy-id`. Alternatively, you can manually copy your public key to the remote server:

```console
$ cat ~/.ssh/id_rsa.pub | ssh user@remote-host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

## References

https://man.openbsd.org/ssh-copy-id

## Revisions

- 2025/05/04 First revision