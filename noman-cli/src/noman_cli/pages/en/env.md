# env command

Display the current environment variables or run a command in a modified environment.

## Overview

The `env` command displays all environment variables or allows you to run a program in a modified environment. Environment variables are name-value pairs that affect how processes run on your system. This command is useful for viewing the current environment, temporarily changing environment variables for a single command, or clearing the environment before running a command.

## Options

### **-i, --ignore-environment**

Start with an empty environment, ignoring inherited environment variables.

```console
$ env -i bash -c 'echo $HOME'

```

### **-u, --unset=NAME**

Remove the variable NAME from the environment.

```console
$ env -u HOME bash -c 'echo $HOME'

```

### **-0, --null**

End each output line with a null character instead of a newline.

```console
$ env -0 | tr '\0' '\n' | head -3
TERM=xterm-256color
SHELL=/bin/bash
USER=username
```

### **--help**

Display help information and exit.

```console
$ env --help
Usage: env [OPTION]... [-] [NAME=VALUE]... [COMMAND [ARG]...]
Set each NAME to VALUE in the environment and run COMMAND.
...
```

### **--version**

Display version information and exit.

```console
$ env --version
env (GNU coreutils) 8.32
Copyright (C) 2020 Free Software Foundation, Inc.
...
```

## Usage Examples

### Displaying all environment variables

```console
$ env
SHELL=/bin/bash
USER=username
HOME=/home/username
PATH=/usr/local/bin:/usr/bin:/bin
PWD=/home/username
LANG=en_US.UTF-8
...
```

### Running a command with a modified environment

```console
$ env DEBUG=true NODE_ENV=development node app.js
```

### Clearing the environment before running a command

```console
$ env -i PATH=/bin:/usr/bin HOME=/tmp bash -c 'echo $HOME'
/tmp
```

### Setting multiple environment variables for a command

```console
$ env LANG=fr_FR.UTF-8 TZ=Europe/Paris date
lun. 04 mai 2025 12:00:00 CEST
```

## Tips

### Viewing Specific Environment Variables

Use `env | grep PATTERN` to filter and find specific environment variables:

```console
$ env | grep PATH
PATH=/usr/local/bin:/usr/bin:/bin
MANPATH=/usr/local/man:/usr/local/share/man:/usr/share/man
```

### Temporary Environment Changes

The `env` command only changes the environment for the command being run, not for the current shell session. For permanent changes, modify your shell configuration files.

### Debugging Environment Issues

When troubleshooting application problems, use `env` to run the application with specific environment variables to help identify configuration issues.

### Security Considerations

Be careful when using `env -i` in scripts, as it removes important environment variables like PATH. Always specify the minimum required variables when using this option.

## Frequently Asked Questions

#### Q1. What's the difference between `env` and `export`?
A. `env` displays environment variables or runs a command with modified environment variables, but changes only affect that command. `export` makes variables available to all child processes of the current shell.

#### Q2. How do I permanently set environment variables?
A. `env` only sets variables temporarily. For permanent changes, add export commands to your shell configuration file (like ~/.bashrc or ~/.zshrc).

#### Q3. Can I use `env` to unset multiple variables at once?
A. Yes, use multiple `-u` options: `env -u VAR1 -u VAR2 command`.

#### Q4. How can I clear all environment variables before running a command?
A. Use `env -i command` to start with an empty environment, then add only the variables you need.

## References

https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html

## Revisions

- 2025/05/04 First revision