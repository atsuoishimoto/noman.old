# true command

Returns a successful exit status (0) regardless of its input.

## Overview

The `true` command is a simple utility that does nothing except return a successful exit status (0). It's commonly used in shell scripts, conditionals, and loops where a command that always succeeds is needed.

## Options

The `true` command doesn't have any functional options as its sole purpose is to exit with a success status.

### **--help**

Display help information and exit.

```console
$ true --help
Usage: true [ignored command line arguments]
  or:  true OPTION
Exit with a status code indicating success.

      --help     display this help and exit
      --version  output version information and exit

NOTE: your shell may have its own version of true, which usually supersedes
the version described here.  Please refer to your shell's documentation
for details about the options it supports.
```

### **--version**

Output version information and exit.

```console
$ true --version
true (GNU coreutils) 8.32
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Jim Meyering.
```

## Usage Examples

### In conditional statements

```console
$ if true; then echo "This will always execute"; fi
This will always execute
```

### In loops

```console
$ while true; do echo "Press Ctrl+C to exit"; sleep 1; done
Press Ctrl+C to exit
Press Ctrl+C to exit
Press Ctrl+C to exit
^C
```

### As a placeholder

```console
$ true || echo "This will never execute"
$
```

## Tips

### Creating Infinite Loops

`while true; do [commands]; done` creates an infinite loop that must be manually terminated with Ctrl+C or by a break statement within the loop.

### Suppressing Errors

Use `command || true` to ensure a script continues even if a command fails, as the `true` command will always return success.

### Empty Functions

In shell scripts, you can use `true` as the body of a function that needs to exist but doesn't need to do anything:
```bash
empty_function() { true; }
```

## Frequently Asked Questions

#### Q1. What's the difference between `true` and `:`?
A. In most shells, `:` (colon) is a built-in command that also returns success (0), similar to `true`. The colon is often preferred in scripts because it's a shell builtin and doesn't require executing an external command.

#### Q2. Can I use `true` to create an empty file?
A. No, use `touch filename` instead. While `true > filename` would create an empty file, it's not the intended use of the command.

#### Q3. How do I create an infinite loop with `true`?
A. Use `while true; do commands; done`. Remember to include a way to break out of the loop or it will run forever.

#### Q4. What is the exit status of `true`?
A. The exit status is always 0, indicating success.

## References

https://www.gnu.org/software/coreutils/manual/html_node/true-invocation.html

## Revisions

- 2025/05/04 First revision