# chsh command

Change the login shell for a user.

## Overview

The `chsh` command allows users to change their login shell - the command interpreter that starts when they log in. It modifies the user's entry in the password file to set which shell program runs when they log into the system. Regular users can only change their own shell, while the superuser (root) can change any user's shell.

## Options

### **-s, --shell SHELL**

Specify the login shell to use. The shell must be listed in the /etc/shells file, unless you're the superuser.

```console
$ chsh -s /bin/bash
Password: 
Shell changed.
```

### **-l, --list-shells**

Print the list of shells listed in /etc/shells and exit.

```console
$ chsh -l
/bin/sh
/bin/bash
/bin/rbash
/bin/dash
/bin/zsh
/usr/bin/zsh
/usr/bin/fish
```

### **-h, --help**

Display help message and exit.

```console
$ chsh --help
Usage: chsh [options] [LOGIN]

Options:
  -h, --help                    display this help message and exit
  -s, --shell SHELL             specify login shell
  -l, --list-shells             print list of shells and exit

For more details see chsh(1).
```

## Usage Examples

### Changing your shell to zsh

```console
$ chsh -s /usr/bin/zsh
Password: 
Shell changed.
```

### Changing another user's shell (requires root privileges)

```console
$ sudo chsh -s /bin/bash username
[sudo] password for current_user: 
Shell changed.
```

### Checking your current shell

```console
$ echo $SHELL
/bin/bash
```

## Tips

### Verify Available Shells First

Always use `chsh -l` to check which shells are available on your system before changing your shell. Only shells listed in `/etc/shells` can be set as login shells (unless you're root).

### Shell Change Takes Effect on Next Login

The shell change doesn't take effect until you log out and log back in. Your current terminal session will continue using the previous shell.

### Avoid Setting Incompatible Shells

Be careful not to set a shell that doesn't exist on your system or that you're not familiar with. If you set an invalid shell, you might have trouble logging in.

### Backup Your Configuration

Before changing shells, back up any shell-specific configuration files (like `.bashrc` or `.zshrc`) so you can restore your settings if needed.

## Frequently Asked Questions

#### Q1. How do I know which shell I'm currently using?
A. Run `echo $SHELL` to see your current login shell. Note that this shows your configured login shell, not necessarily the shell of your current session.

#### Q2. Can I use any program as my shell?
A. No, for security reasons, you can only use shells listed in the `/etc/shells` file (unless you're the superuser).

#### Q3. How do I add a new shell to the available options?
A. Install the shell package, then add its path to `/etc/shells` (requires root privileges).

#### Q4. What happens if I set an invalid shell?
A. If you set a shell that doesn't exist or isn't executable, you might be unable to log in through normal means. You'd need to fix this from a recovery mode or have an administrator change it back.

#### Q5. Do I need to restart my computer after changing my shell?
A. No, you only need to log out and log back in for the change to take effect.

## References

https://man7.org/linux/man-pages/man1/chsh.1.html

## Revisions

- 2025/05/04 First revision