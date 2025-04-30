# env command

Display the current environment variables or run a command in a modified environment.

## Overview

The `env` command shows all environment variables currently set in your shell session. It can also be used to run a program with a modified environment, allowing you to temporarily add, change, or remove environment variables for a specific command execution.

## Options

### **-i, --ignore-environment**

Starts with an empty environment, ignoring inherited variables

```console
$ env -i python3
Python 3.9.6 (default, Mar 10 2023, 20:16:38) 
[Clang 14.0.3 (clang-1403.0.22.14.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> os.environ
environ({'__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x0'})
```

### **-u, --unset=NAME**

Removes the specified variable from the environment

```console
$ env -u HOME pwd
/Users/username/projects
```

### **NAME=VALUE**

Sets an environment variable for the command execution

```console
$ env DEBUG=true python3 app.py
Debug mode enabled
Starting application...
```

## Usage Examples

### Viewing all environment variables

```console
$ env
TERM=xterm-256color
SHELL=/bin/zsh
USER=username
PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
PWD=/Users/username
HOME=/Users/username
...
```

### Running a command with modified environment

```console
$ env LANG=fr_FR.UTF-8 date
mer. 30 avr. 2025 14:30:45 CEST
```

### Combining multiple environment modifications

```console
$ env -u HOME NODE_ENV=production DEBUG=false node server.js
Server started in production mode
Listening on port 3000
```

## Tips:

### Use for Debugging

When troubleshooting application issues, use `env` to check if all required environment variables are set correctly.

### Temporary Environment Changes

Use `env` to make temporary environment changes without modifying your shell's configuration files. This is useful for testing or one-off commands.

### Isolating Command Environments

The `-i` option creates a clean environment for commands, which is useful when you want to ensure a program runs without being affected by existing environment variables.

## Frequently Asked Questions

#### Q1. What's the difference between `env` and `printenv`?
A. Both display environment variables, but `env` can also run commands with modified environments, while `printenv` is focused solely on displaying variables.

#### Q2. How do I permanently set environment variables?
A. `env` only sets variables temporarily. For permanent changes, add them to shell configuration files like `.bashrc`, `.zshrc`, or use system-wide configuration.

#### Q3. Can I use `env` in shell scripts?
A. Yes, it's useful in scripts when you need to run commands with specific environment settings without affecting the script's overall environment.

#### Q4. How do I clear all environment variables for a command?
A. Use `env -i command` to run a command with an empty environment.

## References

https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html

## Revisions

- 2025/04/30 First revision