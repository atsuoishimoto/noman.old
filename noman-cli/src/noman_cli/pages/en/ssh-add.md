# ssh-add command

Add private keys to the SSH authentication agent for connection authentication.

## Overview

`ssh-add` manages the SSH authentication agent (ssh-agent) by adding private keys to its cache. This allows you to authenticate to SSH servers without entering your passphrase each time, as the agent securely holds your unlocked keys in memory for the duration of your session.

## Options

### **-l (List)**

Lists fingerprints of all identities currently held by the agent

```console
$ ssh-add -l
2048 SHA256:abcdefghijklmnopqrstuvwxyz1234567890ABCD user@hostname (RSA)
```

### **-d (Delete)**

Removes a specific identity from the agent

```console
$ ssh-add -d ~/.ssh/id_rsa
Identity removed: /Users/username/.ssh/id_rsa (user@hostname)
```

### **-D (Delete All)**

Removes all identities from the agent

```console
$ ssh-add -D
All identities removed.
```

### **-t (Timeout)**

Sets a timeout (in seconds) after which the key will be automatically removed

```console
$ ssh-add -t 3600 ~/.ssh/id_rsa
Identity added: /Users/username/.ssh/id_rsa (user@hostname)
Lifetime set to 3600 seconds
```

## Usage Examples

### Adding a default key

```console
$ ssh-add
Enter passphrase for /Users/username/.ssh/id_rsa: 
Identity added: /Users/username/.ssh/id_rsa (user@hostname)
```

### Adding a specific key

```console
$ ssh-add ~/.ssh/github_rsa
Enter passphrase for /Users/username/.ssh/github_rsa: 
Identity added: /Users/username/.ssh/github_rsa (user@github)
```

### Checking if agent has keys

```console
$ ssh-add -l
2048 SHA256:abcdefghijklmnopqrstuvwxyz1234567890ABCD user@hostname (RSA)
3072 SHA256:ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcd user@github (RSA)
```

## Tips

### Start ssh-agent First

Make sure ssh-agent is running before using ssh-add. On many systems, you can start it with:
```console
$ eval $(ssh-agent)
Agent pid 12345
```

### Add Keys at Login

Add your SSH keys to your login session by including ssh-add commands in your shell startup files (like ~/.bashrc or ~/.zshrc).

### Use SSH Config File

Combine ssh-add with an SSH config file (~/.ssh/config) to manage multiple keys for different hosts automatically.

### Use Keychain on macOS

On macOS, use the -K option to store your passphrase in the keychain:
```console
$ ssh-add -K ~/.ssh/id_rsa
```

## Frequently Asked Questions

#### Q1. Why do I need to use ssh-add?
A. It allows you to authenticate to SSH servers without entering your passphrase each time, as the agent securely holds your unlocked keys in memory.

#### Q2. How do I know if my keys are loaded in the agent?
A. Use `ssh-add -l` to list all loaded keys.

#### Q3. My keys keep disappearing after some time. Why?
A. SSH keys may be removed from the agent when you log out or restart. You can add them to your login scripts or use the -t option to set a specific timeout.

#### Q4. How do I use ssh-add with multiple keys?
A. Simply run ssh-add for each key: `ssh-add ~/.ssh/key1` followed by `ssh-add ~/.ssh/key2`.

## macOS Specific Information

On macOS, you can use the `-K` option to store your passphrase in the macOS keychain. This allows your keys to be automatically loaded when you log in:

```console
$ ssh-add -K ~/.ssh/id_rsa
```

Note that in newer versions of macOS (Monterey and later), the `-K` option has been deprecated. Instead, use:

```console
$ ssh-add --apple-use-keychain ~/.ssh/id_rsa
```

You may also need to add the following to your ~/.ssh/config file:
```
Host *
  UseKeychain yes
  AddKeysToAgent yes
```

## References

https://man.openbsd.org/ssh-add.1

## Revisions

- 2025/04/30 First revision