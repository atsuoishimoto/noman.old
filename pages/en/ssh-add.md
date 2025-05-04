# ssh-add command

Add private keys to the SSH authentication agent for connection authentication.

## Overview

`ssh-add` manages private keys used for SSH authentication. It adds keys to the SSH agent (ssh-agent), which securely stores your decrypted private keys in memory, allowing you to connect to remote servers without re-entering passphrases for each connection.

## Options

### **-l** / **--list**

Lists fingerprints of all identities currently represented by the agent.

```console
$ ssh-add -l
2048 SHA256:abcdefghijklmnopqrstuvwxyz1234567890ABCD user@hostname (RSA)
```

### **-D** / **--delete-all**

Deletes all identities from the agent.

```console
$ ssh-add -D
All identities removed.
```

### **-d** / **--delete**

Removes the specified identity from the agent.

```console
$ ssh-add -d ~/.ssh/id_rsa
Identity removed: /home/user/.ssh/id_rsa (user@hostname)
```

### **-t** / **--lifetime seconds**

Sets a maximum lifetime when adding identities to the agent. After this time, the identity will be automatically removed.

```console
$ ssh-add -t 3600 ~/.ssh/id_rsa
Identity added: /home/user/.ssh/id_rsa (user@hostname)
Lifetime set to 3600 seconds
```

### **-k** / **--lock-agent**

Locks the agent with a password.

```console
$ ssh-add -k
Enter lock password: 
Again: 
Agent locked.
```

### **-x** / **--lock**

Locks the agent with a password (alternative to -k).

```console
$ ssh-add -x
Enter lock password: 
Again: 
Agent locked.
```

### **-X** / **--unlock**

Unlocks the agent.

```console
$ ssh-add -X
Enter unlock password: 
Agent unlocked.
```

## Usage Examples

### Adding a key without specifying a file

```console
$ ssh-add
Enter passphrase for /home/user/.ssh/id_rsa: 
Identity added: /home/user/.ssh/id_rsa (user@hostname)
```

### Adding a specific key file

```console
$ ssh-add ~/.ssh/github_key
Enter passphrase for /home/user/.ssh/github_key: 
Identity added: /home/user/.ssh/github_key (user@github)
```

### Checking if the agent has any keys

```console
$ ssh-add -l
The agent has no identities.
```

## Tips:

### Start ssh-agent Before Using ssh-add

The SSH agent must be running before you can add keys. On most systems, you can start it with:

```console
$ eval $(ssh-agent)
Agent pid 12345
```

### Add Keys Automatically on Login

Add this to your shell startup file (like `.bashrc` or `.zshrc`) to automatically add your keys when you log in:

```bash
if [ -z "$SSH_AUTH_SOCK" ]; then
   eval $(ssh-agent -s)
   ssh-add
fi
```

### Use SSH Config for Key Management

Instead of manually adding keys, you can specify which key to use for specific hosts in `~/.ssh/config`:

```
Host github.com
  IdentityFile ~/.ssh/github_key
```

## Frequently Asked Questions

#### Q1. Why do I need to use ssh-add?
A. `ssh-add` lets you decrypt your private key once and store it in memory, so you don't need to enter your passphrase every time you connect to a server.

#### Q2. How do I know if my key is already added?
A. Run `ssh-add -l` to list all keys currently loaded in the agent.

#### Q3. My ssh-add command says "Could not open a connection to your authentication agent"
A. This means the SSH agent isn't running. Start it with `eval $(ssh-agent)` first.

#### Q4. How do I make ssh-add remember my keys after reboot?
A. SSH agent doesn't persist across reboots. Use tools like `keychain` or add the keys to your login scripts.

## macOS Considerations

On macOS, the SSH agent is integrated with Keychain, so keys added with `ssh-add -K` (capital K) will be stored in Keychain and loaded automatically on login. In newer macOS versions (Monterey and later), use `--apple-use-keychain` instead of `-K`.

## References

https://man.openbsd.org/ssh-add.1

## Revisions

- 2025/05/04 First revision