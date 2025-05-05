# which command

Locate a command by searching through the PATH environment variable.

## Overview

The `which` command finds the location of executable files in your PATH. It helps you determine which version of a program would run if you typed its name at the command line, showing the full path to the executable.

## Options

### **-a, --all**

Display all matching executables in PATH, not just the first one.

```console
$ which -a python
/usr/bin/python
/usr/local/bin/python
```

### **-s, --silent, --quiet**

Suppress normal output; return exit status 0 if any executable is found, 1 if not.

```console
$ which -s python
$ echo $?
0
```

### **-v, --version**

Display version information and exit.

```console
$ which --version
GNU which v2.21, Copyright (C) 1999 - 2015 Carlo Wood.
```

## Usage Examples

### Basic usage

```console
$ which ls
/bin/ls
```

### Finding multiple commands at once

```console
$ which bash python grep
/bin/bash
/usr/bin/python
/bin/grep
```

### Using with other commands

```console
$ file $(which python)
/usr/bin/python: symbolic link to python3
```

## Tips

### Check if a Command Exists

Use `which` with a conditional to check if a command is available before using it:

```console
$ if which git >/dev/null; then echo "Git is installed"; else echo "Git is not installed"; fi
Git is installed
```

### Combine with `type` for More Information

The `type` command provides more details about a command (builtin, alias, or executable):

```console
$ type ls
ls is aliased to `ls --color=auto'
```

### Remember PATH Order Matters

The first matching executable in your PATH is the one that will be executed. Use `which -a` to see all possible matches.

## Frequently Asked Questions

#### Q1. What's the difference between `which` and `whereis`?
A. `which` only shows executable locations in your PATH, while `whereis` also finds manual pages and source files.

#### Q2. Why does `which` not find shell builtins or aliases?
A. `which` only finds executable files in your PATH. For shell builtins, aliases, or functions, use the `type` command instead.

#### Q3. How can I find all instances of a command in my PATH?
A. Use `which -a command` to show all matching executables, not just the first one.

#### Q4. Why does `which` sometimes return nothing?
A. If `which` returns nothing, the command either doesn't exist in your PATH or might be a shell builtin/alias.

## macOS Considerations

On macOS, the `which` command may behave differently than on Linux systems. The macOS version doesn't support all the GNU options like `--all` (though `-a` works). For more consistent behavior across systems, consider using `command -v` which is a POSIX-compliant alternative.

## References

https://man7.org/linux/man-pages/man1/which.1.html

## Revisions

2025/05/04 First revision