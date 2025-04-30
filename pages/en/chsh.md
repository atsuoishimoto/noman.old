# chsh command

Change the login shell for a user.

## Overview

The `chsh` command allows users to change their login shell - the command interpreter that starts when they log in. It modifies the user's entry in the password file to set which shell program runs by default when they open a terminal or log into the system.

## Options

### **-s, --shell SHELL**

Specify the login shell to use. The shell must be listed in the /etc/shells file.

```console
$ chsh -s /bin/zsh
Password: 
Shell changed.
```

### **-l, --list-shells**

Display the list of shells listed in the /etc/shells file.

```console
$ chsh -l
/bin/bash
/bin/csh
/bin/dash
/bin/ksh
/bin/sh
/bin/tcsh
/bin/zsh
```

### **-u, --help**

Display help information and exit.

```console
$ chsh --help
Usage: chsh [options] [LOGIN]

Options:
  -s, --shell SHELL         specify login shell
  -l, --list-shells         print list of shells and exit
  -h, --help                display this help message and exit
  -v, --version             display version information and exit
```

## Usage Examples

### Changing your own shell

```console
$ chsh -s /bin/zsh
Password: 
Shell changed.
```

### Checking your current shell

```console
$ echo $SHELL
/bin/bash
```

### Changing another user's shell (requires root privileges)

```console
$ sudo chsh -s /bin/bash username
```

## Tips:

### Verify Available Shells First

Always use `chsh -l` to check which shells are available on your system before changing your shell. Using a shell not listed in /etc/shells will fail.

### Shell Changes Take Effect on Next Login

The shell change only takes effect when you log in again. Your current terminal session will continue using the previous shell.

### Keep a Backup Shell

If you're experimenting with a new shell, make sure you have access to a backup terminal or user account with a working shell in case something goes wrong.

### Adding Custom Shells

If you want to use a shell that's not in /etc/shells, you'll need to add it to that file first (requires root privileges).

## Frequently Asked Questions

#### Q1. How do I know which shell I'm currently using?
A. Run `echo $SHELL` to see your current default shell.

#### Q2. Why do I need to enter my password when using chsh?
A. For security reasons, `chsh` requires authentication to prevent unauthorized shell changes.

#### Q3. Can I use any program as my shell?
A. No, for security reasons, you can only use shells listed in the /etc/shells file.

#### Q4. How do I revert to my previous shell if I don't like the new one?
A. Simply run `chsh -s /path/to/previous/shell` to switch back.

#### Q5. What happens if I set an invalid shell?
A. If you set a shell that doesn't exist or isn't in /etc/shells, you might be unable to log in normally and may need to fix it in recovery mode.

## macOS Considerations

On macOS, you can also change your shell using the Users & Groups preference pane in System Preferences. Additionally, macOS may have a different set of available shells compared to Linux systems. Use `chsh -l` to see the available options.

## References

https://linux.die.net/man/1/chsh

## Revisions

- 2025/04/30 First revision