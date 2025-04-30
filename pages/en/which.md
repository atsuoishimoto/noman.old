# which command

Locate a command's executable file in the user's PATH.

## Overview

The `which` command searches through the directories listed in your PATH environment variable to find the location of executable programs. It helps you determine which version of a command would run if you typed it at the command line.

## Options

### **-a (all)**

Shows all matching executables in PATH, not just the first one.

```console
$ which -a python
/usr/local/bin/python
/usr/bin/python
```

### **-s (silent)**

Suppresses normal output; returns only an exit status (0 if found, 1 if not found).

```console
$ which -s git
$ echo $?
0
```

## Usage Examples

### Finding a command's location

```console
$ which ls
/bin/ls
```

### Checking if a command exists

```console
$ which nonexistentcommand
which: no nonexistentcommand in (/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin)
```

### Finding multiple versions of a command

```console
$ which -a python3
/usr/local/bin/python3
/usr/bin/python3
```

## Tips

### Understanding Command Precedence

The first executable found in your PATH is the one that will run when you type the command. This is important when you have multiple versions installed.

### Troubleshooting "Command Not Found" Errors

If a command isn't found with `which`, check that it's installed and that its directory is in your PATH environment variable.

### Combine with Other Commands

Use `which` with other commands for more information:
```console
$ ls -l $(which python)
-rwxr-xr-x 1 root wheel 31488 Jan 1 2023 /usr/bin/python
```

## Frequently Asked Questions

#### Q1. What's the difference between `which` and `whereis`?
A. `which` only finds executables in your PATH, while `whereis` can also find source, man pages, and other related files.

#### Q2. Why does `which` show a different location than where I installed a program?
A. Your PATH environment variable might be prioritizing a different version, or you might have aliases set up in your shell configuration.

#### Q3. Can `which` find built-in shell commands?
A. No, `which` only finds executable files in your PATH. Built-in commands like `cd` won't be found because they're part of the shell itself.

#### Q4. How do I see my current PATH?
A. Run `echo $PATH` to see the directories that are searched for commands.

## References

https://pubs.opengroup.org/onlinepubs/9699919799/utilities/which.html

## Revisions

- 2025/04/30 First revision