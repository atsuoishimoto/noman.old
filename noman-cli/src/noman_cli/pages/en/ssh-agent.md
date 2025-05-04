# ssh-agent command

Authentication agent that manages SSH private keys for secure connections without repeated passphrase entry.

## Overview

`ssh-agent` is a program that holds private keys used for SSH public key authentication. It runs in the background and eliminates the need to enter your passphrase each time you use SSH to connect to a remote server. When you add a key to the agent, you enter the passphrase once, and the agent keeps the decrypted key in memory for future use.

## Options

### **-a socket**

Bind the agent to a specific Unix-domain socket.

```console
$ ssh-agent -a /tmp/ssh-agent.socket
SSH_AUTH_SOCK=/tmp/ssh-agent.socket; export SSH_AUTH_SOCK;
SSH_AGENT_PID=1234; export SSH_AGENT_PID;
echo Agent pid 1234;
```

### **-c**

Generate C-shell commands on stdout. This is the default if SHELL looks like it's a csh style shell.

```console
$ ssh-agent -c
setenv SSH_AUTH_SOCK /tmp/ssh-XXXXXXXXXX/agent.1234;
setenv SSH_AGENT_PID 1234;
echo Agent pid 1234;
```

### **-d**

Debug mode. The agent will not fork and will write debug information to standard error.

```console
$ ssh-agent -d
debug: ssh-agent: starting
debug: ssh-agent: listening on socket: /tmp/ssh-XXXXXXXXXX/agent.1234
```

### **-k**

Kill the current agent (given by the SSH_AGENT_PID environment variable).

```console
$ ssh-agent -k
Agent pid 1234 killed
```

### **-s**

Generate Bourne shell commands on stdout. This is the default if SHELL does not look like it's a csh style shell.

```console
$ ssh-agent -s
SSH_AUTH_SOCK=/tmp/ssh-XXXXXXXXXX/agent.1234; export SSH_AUTH_SOCK;
SSH_AGENT_PID=1234; export SSH_AGENT_PID;
echo Agent pid 1234;
```

### **-t life**

Set a default maximum lifetime for identities added to the agent. The lifetime may be specified in seconds or in a time format specified in sshd_config(5).

```console
$ ssh-agent -t 1h
SSH_AUTH_SOCK=/tmp/ssh-XXXXXXXXXX/agent.1234; export SSH_AUTH_SOCK;
SSH_AGENT_PID=1234; export SSH_AGENT_PID;
echo Agent pid 1234;
```

## Usage Examples

### Starting ssh-agent and adding a key

```console
$ eval $(ssh-agent)
Agent pid 1234
$ ssh-add ~/.ssh/id_rsa
Enter passphrase for /home/user/.ssh/id_rsa: 
Identity added: /home/user/.ssh/id_rsa
```

### Starting ssh-agent with a specific lifetime

```console
$ eval $(ssh-agent -t 4h)
Agent pid 1235
$ ssh-add
Enter passphrase for /home/user/.ssh/id_rsa: 
Identity added: /home/user/.ssh/id_rsa
```

### Listing keys in the agent

```console
$ ssh-add -l
2048 SHA256:abcdefghijklmnopqrstuvwxyz1234567890ABCD /home/user/.ssh/id_rsa (RSA)
```

### Killing the ssh-agent

```console
$ eval $(ssh-agent -k)
Agent pid 1234 killed
```

## Tips:

### Start ssh-agent Automatically

Add `eval $(ssh-agent)` to your shell startup file (like `.bashrc` or `.zshrc`) to automatically start the agent when you log in.

### Use ssh-agent with SSH Config

Combine ssh-agent with SSH config files (~/.ssh/config) to manage different keys for different hosts automatically.

### Forward Your SSH Agent

When connecting to a remote server that needs to access other servers, use `ssh -A user@host` to forward your local agent to the remote server. Be cautious with this feature as it poses security risks on untrusted servers.

### Check for Running Agents

Before starting a new agent, check if one is already running with `echo $SSH_AGENT_PID` to avoid having multiple agents.

## Frequently Asked Questions

#### Q1. What's the difference between ssh-agent and ssh-add?
A. `ssh-agent` is the background program that holds your decrypted keys, while `ssh-add` is used to add keys to the running agent.

#### Q2. How do I make ssh-agent remember my keys after a reboot?
A. ssh-agent doesn't persist across reboots. You need to restart it and add your keys again. Consider using tools like keychain or a startup script.

#### Q3. How can I tell if ssh-agent is running?
A. Check if the SSH_AGENT_PID environment variable is set: `echo $SSH_AGENT_PID`. If it returns a number, an agent is running.

#### Q4. How do I remove a key from ssh-agent?
A. Use `ssh-add -d ~/.ssh/keyfile` to remove a specific key, or `ssh-add -D` to remove all keys.

## macOS Considerations

On macOS, the system keychain integration allows for automatic loading of keys. The built-in ssh-agent is managed by launchd and starts automatically. You can add keys to the macOS keychain with `ssh-add -K ~/.ssh/id_rsa` (older versions) or `ssh-add --apple-use-keychain ~/.ssh/id_rsa` (newer versions), which will make them persist across reboots.

## References

https://man.openbsd.org/ssh-agent

## Revisions

- 2025/05/04 First revision