# set command

Display or set shell options and positional parameters.

## Overview

The `set` command is used to manipulate shell options and positional parameters. It can display all variables, change the behavior of the shell by enabling or disabling options, or set positional parameters. It's a powerful command for controlling shell execution environments and debugging scripts.

## Options

### **-e (--errexit)**

Exit immediately if a command exits with a non-zero status.

```console
$ set -e
$ non_existent_command
bash: non_existent_command: command not found
$ echo "This won't be executed"
[Shell has already exited due to the error]
```

### **-x (--xtrace)**

Print commands and their arguments as they are executed. Useful for debugging scripts.

```console
$ set -x
$ echo "Hello World"
+ echo 'Hello World'
Hello World
```

### **-u (--nounset)**

Treat unset variables as an error when substituting.

```console
$ set -u
$ echo $UNDEFINED_VARIABLE
bash: UNDEFINED_VARIABLE: unbound variable
```

### **-o option-name**

Set the option corresponding to option-name.

```console
$ set -o pipefail
$ non_existent_command | echo "This will still run"
This will still run
$ echo $?
127
```

### **+o option-name**

Unset the option corresponding to option-name.

```console
$ set +o pipefail
$ non_existent_command | echo "This will run"
This will run
$ echo $?
0
```

### **--**

End option processing. Useful when you want to set positional parameters that start with a dash.

```console
$ set -- -a -b -c
$ echo $1 $2 $3
-a -b -c
```

## Usage Examples

### Displaying all variables and functions

```console
$ set
BASH=/bin/bash
BASHOPTS=checkwinsize:cmdhist:complete_fullquote:expand_aliases:...
...
[many more variables and functions]
```

### Setting positional parameters

```console
$ set one two three
$ echo $1 $2 $3
one two three
```

### Enabling multiple options at once

```console
$ set -ex
$ echo "Commands will be traced and script will exit on error"
+ echo 'Commands will be traced and script will exit on error'
Commands will be traced and script will exit on error
```

### Saving and restoring shell options

```console
$ oldstate=$(set +o)
$ set -e
$ # Do something that might fail
$ eval "$oldstate"  # Restore previous state
```

## Tips

### Use set -e in Scripts

Adding `set -e` at the beginning of your scripts makes them fail fast when errors occur, preventing cascading failures that might be harder to debug.

### Debugging with set -x

When a script isn't working as expected, temporarily add `set -x` to see each command as it executes with its expanded variables.

### Combine Options for Safer Scripts

The combination `set -euo pipefail` is commonly used in scripts to make them more robust by failing on errors, undefined variables, and pipeline failures.

### Reset Positional Parameters

Use `set --` with no arguments to clear all positional parameters.

## Frequently Asked Questions

#### Q1. What's the difference between `set` and `export`?
A. `set` displays/changes shell options and positional parameters, while `export` makes variables available to child processes.

#### Q2. How do I turn off a set option?
A. Use the `+` sign instead of `-`. For example, `set +x` turns off command tracing that was enabled with `set -x`.

#### Q3. How can I see what options are currently set?
A. Use `set -o` to see the current state of all shell options.

#### Q4. Can I use `set` to create variables?
A. No, `set` doesn't create regular variables. Use variable assignment like `VAR=value` instead. `set` only affects shell options and positional parameters.

## References

https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html

## Revisions

- 2025/05/04 First revision