# false command

Returns a failure status regardless of its arguments.

## Overview

The `false` command is a simple Unix utility that does nothing except return an exit status of 1, indicating failure. It's often used in shell scripts to force a failure condition or as a placeholder in conditional statements.

## Options

The `false` command doesn't have any functional options as its sole purpose is to return a failure status.

## Usage Examples

### Basic usage

```console
$ false
$ echo $?
1
```

The command silently exits with a status code of 1, which we can verify by checking the special `$?` variable that holds the exit status of the last command.

### Using in conditional statements

```console
$ if false; then echo "This won't print"; else echo "This will print"; fi
This will print
```

Since `false` always returns a failure status, the `else` branch is executed.

### Using in a loop

```console
$ while ! false; do echo "This won't execute"; done
```

This loop won't execute at all because `false` always returns failure, so `! false` is always false.

## Tips

### Opposite of true

The `false` command is the logical opposite of the `true` command, which always returns a success status (0).

### Creating infinite loops

Be careful when using `false` in loop conditions. For example, `while false; do something; done` will never execute because the condition is always false.

### Exit codes in scripts

In shell scripting, an exit code of 0 indicates success, while any non-zero value (like 1 from `false`) indicates failure. This is important to remember when checking command results.

## Frequently Asked Questions

#### Q1. What is the purpose of the `false` command?
A. Its sole purpose is to return a failure exit status (1), typically used in shell scripts to force a failure condition.

#### Q2. What is the exit status of the `false` command?
A. It always returns 1, indicating failure.

#### Q3. How does `false` differ from `true`?
A. `true` returns a success status (0), while `false` returns a failure status (1).

#### Q4. Can I use `false` to create an empty file?
A. No, unlike some commands, `false` doesn't create any files. Use `touch` instead to create empty files.

## References

https://www.gnu.org/software/coreutils/manual/html_node/false-invocation.html

## Revisions

- 2025/04/30 First revision