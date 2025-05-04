# source command

Execute commands from a file or script in the current shell environment.

## Overview

The `source` command (also available as the `.` command) reads and executes commands from a specified file in the current shell environment. Unlike running a script directly, which creates a new shell process, `source` runs the commands in your current shell, allowing environment variables and functions defined in the sourced file to persist in your current session.

## Options

The `source` command has very few options as it's a shell builtin command.

### **-h (--help)**

Display help information about the `source` command.

```console
$ source --help
source: source filename [arguments]
    Execute commands from a file in the current shell.
    
    Read and execute commands from FILENAME in the current shell.  The
    entries in $PATH are used to find the directory containing FILENAME.
    If any ARGUMENTS are supplied, they become the positional parameters
    when FILENAME is executed.
    
    Exit Status:
    Returns the status of the last command executed in FILENAME; fails if
    FILENAME cannot be read.
```

## Usage Examples

### Sourcing a configuration file

```console
$ source ~/.bashrc
```

This reloads your bash configuration without requiring you to start a new terminal session.

### Sourcing a script with variables

```console
$ cat setup_env.sh
#!/bin/bash
export PROJECT_ROOT="/home/user/projects"
export DEBUG_MODE="true"

$ source setup_env.sh
$ echo $PROJECT_ROOT
/home/user/projects
```

### Passing arguments to a sourced file

```console
$ cat greet.sh
echo "Hello, $1!"

$ source greet.sh World
Hello, World!
```

## Tips

### Use source to activate virtual environments

When working with Python, you can use `source` to activate virtual environments:

```console
$ source venv/bin/activate
(venv) $
```

### Dot command as an alternative

The `.` command is a shorter alternative to `source` and works identically:

```console
$ . ~/.bashrc
```

### Check if a file exists before sourcing

To avoid errors, check if a file exists before sourcing it:

```console
$ [ -f ~/.env_vars ] && source ~/.env_vars
```

## Frequently Asked Questions

#### Q1. What's the difference between `source` and executing a script directly?
A. When you `source` a script, it runs in your current shell environment, allowing variables and functions to persist. When you execute a script directly (e.g., `./script.sh`), it runs in a new subshell, and any variables or functions defined in it are lost when the script completes.

#### Q2. Can I use `source` with any type of file?
A. `source` is designed to work with shell script files. It reads and executes the commands in the file as if you had typed them at the command line. It's typically used with bash, zsh, or other shell script files.

#### Q3. Does `source` work the same in all shells?
A. While the basic functionality is similar across shells, there may be subtle differences. In bash and zsh, both `source` and `.` work, but some shells like sh only support the `.` command.

#### Q4. How can I debug a sourced file?
A. You can add `set -x` at the beginning of the file to enable debug mode, which will print each command before executing it.

## References

Bash manual: https://www.gnu.org/software/bash/manual/bash.html

## Revisions

- 2025/05/04 First revision