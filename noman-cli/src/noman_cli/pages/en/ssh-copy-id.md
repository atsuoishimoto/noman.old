# ssh-copy-id command

Copies your SSH public key to a remote server to enable password-less authentication.

## Overview

`ssh-copy-id` is a utility that installs your public key in a remote machine's authorized keys file. This allows you to connect to the remote server using SSH without entering a password each time, making remote access more convenient and secure.

## Options

### **-i [identity_file]**

Specifies the identity file (private key) to use. By default, it uses ~/.ssh/id_rsa.pub.

```console
$ ssh-copy-id -i ~/.ssh/custom_key.pub user@remote-server
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-server's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-server'"
and check to make sure that only the key(s) you wanted were added.
```

### **-f**

Forces the installation, even if the key already exists on the remote server.

```console
$ ssh-copy-id -f user@remote-server
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-server's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-server'"
and check to make sure that only the key(s) you wanted were added.
```

### **-p [port]**

Specifies a different port to connect to on the remote server.

```console
$ ssh-copy-id -p 2222 user@remote-server
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-server's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh -p 2222 'user@remote-server'"
and check to make sure that only the key(s) you wanted were added.
```

## Usage Examples

### Basic Usage

```console
$ ssh-copy-id user@remote-server
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-server's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-server'"
and check to make sure that only the key(s) you wanted were added.
```

### Using a Specific Identity File

```console
$ ssh-copy-id -i ~/.ssh/id_ed25519.pub user@remote-server
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-server's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-server'"
and check to make sure that only the key(s) you wanted were added.
```

## Tips

### Generate SSH Keys First

Before using `ssh-copy-id`, make sure you have SSH keys generated. If not, create them with `ssh-keygen`.

### Verify After Installation

After running `ssh-copy-id`, verify that password-less login works by running `ssh user@remote-server`.

### Multiple Keys

You can install multiple keys by specifying them with multiple `-i` options or by using wildcards like `-i ~/.ssh/*.pub`.

### Remote Server Requirements

The remote server must have SSH access enabled and the `~/.ssh` directory must exist (it will be created if it doesn't).

## Frequently Asked Questions

#### Q1. What does ssh-copy-id actually do?
A. It copies your public SSH key to the remote server's `~/.ssh/authorized_keys` file, enabling password-less authentication.

#### Q2. What if I get a "Permission denied" error?
A. Ensure you have the correct username and password for the remote server. Also, check that the remote user has permission to write to their home directory.

#### Q3. Can I use ssh-copy-id with a custom SSH port?
A. Yes, use the `-p` option followed by the port number: `ssh-copy-id -p 2222 user@remote-server`.

#### Q4. How do I know if it worked?
A. Try logging in with `ssh user@remote-server`. If you're not prompted for a password, it worked successfully.

#### Q5. Can I use ssh-copy-id to a server that doesn't allow password authentication?
A. No, ssh-copy-id requires password authentication for the initial connection. You'll need to manually copy your public key to the server.

## macOS Considerations

On macOS, `ssh-copy-id` might not be installed by default. If you get a "command not found" error, install it using Homebrew with `brew install ssh-copy-id`. The functionality is otherwise identical to Linux systems.

## References

https://www.ssh.com/academy/ssh/copy-id

## Revisions

- 2025/04/30 First revision