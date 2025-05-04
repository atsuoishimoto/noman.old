# false command

Returns a failure status regardless of any arguments.

## Overview

The `false` command is a simple Unix utility that does nothing except return an exit status of 1, indicating failure. It's often used in shell scripts to force a failure condition or as a placeholder in conditional statements.

## Options

The `false` command typically doesn't accept any options. It simply returns a non-zero exit status (failure) regardless of any arguments passed to it.

```console
$ false
$ echo $?
1
```

## Usage Examples

### Using in conditional statements

```console
$ if false; then echo "This won't print"; else echo "This will print"; fi
This will print
```

### Creating an infinite loop with false

```console
$ while false; do echo "This won't execute"; done
$
```

### Using as a placeholder in scripts

```console
$ false || echo "The false command failed"
The false command failed
```

## Tips:

### Opposite of true

The `false` command is the logical opposite of the `true` command, which returns a success status (0).

### Testing error handling

Use `false` to test error handling in scripts by forcing a command to fail.

### Exit status

The exit status of `false` is always 1, which can be checked using `echo $?` immediately after running the command.

## Frequently Asked Questions

#### Q1. What is the purpose of the `false` command?
A. The `false` command exists to provide a guaranteed failure exit status (1), which is useful in shell scripting for testing conditions or forcing failure paths.

#### Q2. Does `false` accept any arguments?
A. While `false` may accept arguments on some systems, it ignores them and always returns a failure status.

#### Q3. What is the difference between `false` and `true`?
A. `false` returns an exit status of 1 (failure), while `true` returns an exit status of 0 (success).

#### Q4. Can I use `false` in a pipeline?
A. Yes, but be aware that in a pipeline, the exit status of the last command determines the pipeline's overall status, not the `false` command if it's not last.

## References

https://www.gnu.org/software/coreutils/manual/html_node/false-invocation.html

## Revisions

- 2025/05/04 First revision