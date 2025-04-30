# set command

Display, set, or unset shell options and positional parameters.

## Overview

The `set` command is a built-in shell command that allows you to control various aspects of the shell's behavior. It can display all shell variables, set shell options that change how the shell behaves, and manipulate positional parameters. It's commonly used in shell scripts to enable error handling, debugging, and to control script execution flow.

## Options

### **-e (errexit)**

Exits immediately if a command returns a non-zero status (fails)

```console
$ set -e
$ non_existent_command
bash: non_existent_command: command not found
$ echo "This won't be executed"
[Shell has already exited due to the error]
```

### **-x (xtrace)**

Prints each command before executing it, prefixed with '+'

```console
$ set -x
$ echo "Hello World"
+ echo 'Hello World'
Hello World
```

### **-u (nounset)**

Treats unset variables as errors when referenced

```console
$ set -u
$ echo $UNDEFINED_VARIABLE
bash: UNDEFINED_VARIABLE: unbound variable
```

### **-o option**

Sets a specific option by name

```console
$ set -o pipefail
$ non_existent_command | echo "This command runs"
This command runs
$ echo $?
127
```

### **+o option**

Unsets a specific option by name

```console
$ set +o pipefail
$ non_existent_command | echo "This command runs"
This command runs
$ echo $?
0
```

### **--**

Assigns following arguments to positional parameters

```console
$ set -- arg1 arg2 arg3
$ echo $1 $2 $3
arg1 arg2 arg3
```

## Usage Examples

### Setting multiple options at once

```console
$ set -exu
$ echo "Now the script will exit on errors, show commands, and error on unset variables"
+ echo 'Now the script will exit on errors, show commands, and error on unset variables'
Now the script will exit on errors, show commands, and error on unset variables
```

### Displaying all variables

```console
$ set
BASH=/bin/bash
BASHOPTS=checkwinsize:cmdhist:complete_fullquote:expand_aliases:extglob:extquote:force_fignore:histappend:interactive_comments:progcomp:promptvars:sourcepath
BASH_ALIASES=()
...
[many more variables shown]
```

### Using set in a script for error handling

```console
$ cat error_handling.sh
#!/bin/bash
set -e  # Exit immediately if a command fails
set -u  # Treat unset variables as errors
set -o pipefail  # Return value of a pipeline is the value of the last command to exit with non-zero status

echo "Starting script with error handling enabled"
# Script continues...
```

## Tips

### Use set -e in Scripts

Adding `set -e` at the beginning of your scripts makes them fail fast when errors occur, preventing cascading failures that can be hard to debug.

### Combine Options for Robust Scripts

The combination `set -euo pipefail` is often used in production scripts as a best practice for error handling. It's sometimes called "strict mode."

### Save and Restore Settings

You can save the current options with `old_opts=$(set +o)` and restore them later with `eval "$old_opts"` when you need to temporarily change settings.

### Debugging with set -x

When troubleshooting scripts, temporarily adding `set -x` helps you see exactly what commands are being executed and with what values.

## Frequently Asked Questions

#### Q1. What's the difference between `set` and `export`?
A. `set` controls shell behavior and positional parameters, while `export` makes variables available to child processes.

#### Q2. How do I turn off an option that was set with `set -o`?
A. Use `set +o option_name`. The plus sign (+) disables the option.

#### Q3. How can I see what options are currently enabled?
A. Use `set -o` to see a list of all options and their current status.

#### Q4. What does `set --` do?
A. It assigns the arguments that follow to the positional parameters ($1, $2, etc.), replacing any existing values.

## References

https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html

## Revisions

- 2025/04/30 First revision