# ssh-agent command

Manages SSH private keys and their passphrases in memory for single sign-on access to SSH servers.

## Overview

`ssh-agent` is a background program that holds private keys used for SSH public key authentication. It eliminates the need to enter passphrases repeatedly when connecting to multiple SSH servers, as it stores the decrypted keys in memory for the duration of a session.

## Options

### **-c**

Generate C-shell commands on stdout. This is the default if SHELL looks like it's a csh style shell.

```console
$ ssh-agent -c
setenv SSH_AUTH_SOCK /tmp/ssh-XXXXXX2LUbUP/agent.12345;
setenv SSH_AGENT_PID 12345;
echo Agent pid 12345;
```

### **-s**

Generate Bourne shell commands on stdout. This is the default if SHELL does not look like it's a csh style shell.

```console
$ ssh-agent -s
SSH_AUTH_SOCK=/tmp/ssh-XXXXXX5TbcZp/agent.12345; export SSH_AUTH_SOCK;
SSH_AGENT_PID=12345; export SSH_AGENT_PID;
echo Agent pid 12345;
```

### **-d**

Debug mode. When this option is specified, ssh-agent will not fork and will write debug information to standard error.

```console
$ ssh-agent -d
SSH_AUTH_SOCK=/tmp/ssh-XXXXXXzUqaQn/agent.12345; export SSH_AUTH_SOCK;
SSH_AGENT_PID=12345; export SSH_AGENT_PID;
echo Agent pid 12345;
[debug output follows]
```

### **-k**

Kill the current agent (given by the SSH_AGENT_PID environment variable).

```console
$ ssh-agent -k
unset SSH_AUTH_SOCK;
unset SSH_AGENT_PID;
echo Agent pid 12345 killed;
```

## Usage Examples

### Starting ssh-agent and adding a key

```console
$ eval $(ssh-agent)
Agent pid 12345
$ ssh-add ~/.ssh/id_rsa
Enter passphrase for /home/user/.ssh/id_rsa: 
Identity added: /home/user/.ssh/id_rsa
```

### Starting ssh-agent with a specific lifetime

```console
$ ssh-agent -t 1h
SSH_AUTH_SOCK=/tmp/ssh-XXXXXXzUqaQn/agent.12345; export SSH_AUTH_SOCK;
SSH_AGENT_PID=12345; export SSH_AGENT_PID;
echo Agent pid 12345;
```

### Listing keys managed by the agent

```console
$ ssh-add -l
2048 SHA256:abcdefghijklmnopqrstuvwxyz1234567890ABCD /home/user/.ssh/id_rsa (RSA)
```

## Tips

### Use eval to Set Environment Variables

Always use `eval $(ssh-agent)` to start the agent, as this automatically sets the required environment variables.

### Add Keys Automatically on Login

Add `ssh-add` commands to your shell startup files (like `.bashrc` or `.zshrc`) to automatically load your keys when you log in.

### Forward Your Agent When Needed

Use `ssh -A user@host` to forward your agent connection to remote servers, allowing you to use your local keys for authentication on those servers. Be cautious with this feature as it poses security risks on untrusted servers.

### Kill the Agent When Done

Run `ssh-agent -k` when you're done to terminate the agent and remove the decrypted keys from memory, especially on shared systems.

## Frequently Asked Questions

#### Q1. What's the difference between ssh-agent and ssh-add?
A. `ssh-agent` is the background program that holds your decrypted keys, while `ssh-add` is used to add keys to the running agent.

#### Q2. How do I know if ssh-agent is already running?
A. Check if the SSH_AGENT_PID environment variable is set: `echo $SSH_AGENT_PID`.

#### Q3. Why do I need to use eval with ssh-agent?
A. `ssh-agent` outputs shell commands that set environment variables. Using `eval` executes these commands in your current shell.

#### Q4. How can I limit how long keys are stored in the agent?
A. Use the `-t` option with a time specification: `ssh-agent -t 1h` for one hour.

## macOS Considerations

On macOS, the system keychain can integrate with SSH keys. You can add `UseKeychain yes` to your `~/.ssh/config` file to store passphrases in the keychain. Additionally, macOS may start its own ssh-agent automatically, so check if one is already running before starting a new one.

## References

https://man.openbsd.org/ssh-agent

## Revisions

- 2025/04/30 First revision