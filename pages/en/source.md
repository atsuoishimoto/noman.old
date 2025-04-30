# source command

Execute commands from a file or script in the current shell environment.

## Overview

The `source` command (also accessible via the `.` shorthand) reads and executes commands from a specified file in the current shell session. Unlike running a script normally, which creates a new shell process, `source` runs commands in your current shell, allowing environment variables and functions defined in the sourced file to persist in your current session.

## Options

The `source` command has very few options as its primary purpose is straightforward.

### **Basic Usage**

Source a file to execute its contents in the current shell:

```console
$ source filename
```

or using the shorthand:

```console
$ . filename
```

### **With Arguments**

Pass arguments to the sourced script:

```console
$ source script.sh arg1 arg2
```

## Usage Examples

### Sourcing a configuration file

```console
$ source ~/.bashrc
```

This reloads your bash configuration without needing to start a new terminal session.

### Loading environment variables

```console
$ cat env.sh
export PROJECT_ROOT="/home/user/projects"
export API_KEY="abc123"

$ source env.sh
$ echo $PROJECT_ROOT
/home/user/projects
```

### Activating a virtual environment

```console
$ source venv/bin/activate
(venv) $
```

This is commonly used with Python virtual environments to set up the necessary environment variables.

## Tips

### Use source for Shell Functions

When defining shell functions in a file, you must use `source` to make them available in your current shell:

```console
$ cat functions.sh
function hello() {
  echo "Hello, $1!"
}

$ source functions.sh
$ hello World
Hello, World!
```

### Debugging Sourced Files

If a sourced file has errors, they will affect your current shell. To debug, consider using `set -x` at the beginning of the file to see each command as it executes.

### Relative Paths

When sourcing files, paths are relative to your current working directory, not the location of the script doing the sourcing.

## Frequently Asked Questions

#### Q1. What's the difference between `source` and executing a script directly?
A. When you execute a script directly (e.g., `./script.sh`), it runs in a new subshell. Changes to variables or functions don't affect your current shell. With `source`, the commands run in your current shell, so any changes persist after the script completes.

#### Q2. Can I use `source` with any type of file?
A. `source` works with any text file containing valid shell commands. It's commonly used with shell scripts (`.sh`), configuration files, and environment setup files.

#### Q3. What's the difference between `source` and the dot operator (`.`)?
A. They are functionally identical. The dot operator (`.`) is the POSIX-standard version, while `source` is a more readable synonym available in bash and some other shells.

#### Q4. Does `source` work in all shells?
A. The `.` command works in all POSIX-compliant shells. The `source` command is specific to bash and some other shells like zsh. For maximum portability, use the `.` command.

## References

https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html

## Revisions

- 2025/04/30 First revision