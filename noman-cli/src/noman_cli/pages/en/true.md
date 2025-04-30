# true command

Return a successful exit status (0).

## Overview

The `true` command does nothing except return a successful exit status (0). It's primarily used in shell scripts for creating infinite loops, conditional statements, or when you need a command that always succeeds.

## Options

The `true` command doesn't have any options as its sole purpose is to exit with a success status code.

## Usage Examples

### Basic Usage

```console
$ true
$ echo $?
0
```

The command produces no output, but returns exit code 0 (success), which can be verified by checking the special variable `$?`.

### Creating an Infinite Loop

```console
$ while true; do echo "Press Ctrl+C to exit"; sleep 1; done
Press Ctrl+C to exit
Press Ctrl+C to exit
Press Ctrl+C to exit
^C
```

This creates an infinite loop that prints a message every second until interrupted with Ctrl+C.

### Using in Conditional Statements

```console
$ if true; then echo "This will always execute"; fi
This will always execute
```

Since `true` always succeeds, the condition is always met, and the code block always executes.

## Tips:

### Placeholder for Required Commands

Use `true` as a placeholder when a command is required but you don't want any action to be performed.

```console
$ grep "pattern" file.txt || true
```

This ensures the script continues even if `grep` fails to find the pattern.

### Creating Empty Files

While not its primary purpose, `true` can be used with redirection to create empty files:

```console
$ true > empty_file.txt
```

### Comparison with `false`

The opposite of `true` is `false`, which always returns a failure exit status (1).

## Frequently Asked Questions

#### Q1. What is the purpose of the `true` command?
A. `true` exists solely to return a successful exit status (0), which is useful in shell scripts for conditional logic or creating loops.

#### Q2. Does `true` produce any output?
A. No, `true` produces no output; it only returns an exit status.

#### Q3. How is `true` different from `:`?
A. In most shells, `:` (colon) is a shell builtin that functions similarly to `true`. Both do nothing and return success, but `:` is a shell builtin while `true` is typically an external command.

#### Q4. Can `true` be used to create an infinite loop?
A. Yes, `while true; do commands; done` creates an infinite loop that must be manually terminated.

## References

https://www.gnu.org/software/coreutils/manual/html_node/true-invocation.html

## Revisions

- 2025/04/30 First revision