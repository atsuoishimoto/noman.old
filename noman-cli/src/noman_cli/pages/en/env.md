# env

The `env` command displays the current environment variables or runs a command in a modified environment.

## Options

### **-i, --ignore-environment**

Starts with an empty environment, ignoring inherited environment variables.

```bash
$ env -i bash
$ echo $HOME
# No output because HOME variable is not set
```

### **-u, --unset=NAME**

Removes the specified variable from the environment.

```bash
$ env -u HOME bash -c 'echo $HOME'
# No output because HOME variable was unset
```

### **NAME=VALUE**

Sets an environment variable for the command execution.

```bash
$ env DEBUG=true python script.py
```

## Usage Examples

### Display all environment variables

```bash
$ env
SHELL=/bin/bash
USER=username
HOME=/home/username
PATH=/usr/local/bin:/usr/bin:/bin
PWD=/current/directory
...
```

### Run a command with a modified environment

```bash
$ env LANG=fr_FR.UTF-8 date
mar. 25 avril 2023 14:30:45 CEST
```

### Run a command with a clean environment plus specific variables

```bash
$ env -i PATH=/usr/bin HOME=/tmp bash -c 'echo $HOME && pwd'
/tmp
/current/directory
```

## Frequently Asked Questions

### Q1. What's the difference between `env` and `export`?
A. `env` is a command that can display variables or run a program with modified environment variables. `export` is a shell built-in that sets variables for the current shell and all its child processes.

### Q2. How can I use `env` to run a script with a specific interpreter?
A. Use the shebang line at the top of your script: `#!/usr/bin/env python` to run with the first Python interpreter found in PATH.

### Q3. Can I use `env` to temporarily change environment variables?
A. Yes, changes made with `env` only affect the command being run and don't persist after the command completes.

## Additional Notes

- The `env` command is particularly useful in scripts to ensure consistent execution environments.
- On macOS, `env` works the same way as on other Unix-like systems, with no significant differences.
- Using `env` in shebang lines (e.g., `#!/usr/bin/env python`) is a portable way to locate interpreters across different systems.

## References

https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html