# whoami command

Display the effective username of the current user.

## Overview

The `whoami` command prints the username associated with the current effective user ID. This simple utility helps identify which user account is being used for the current session, which is particularly useful in scripts, when switching between users, or when troubleshooting permission issues.

## Options

The `whoami` command has very few options as it performs a single, straightforward function.

### **--help**

Display help information and exit.

```console
$ whoami --help
Usage: whoami [OPTION]...
Print the user name associated with the current effective user ID.
Same as id -un.

      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report whoami translation bugs to <https://translationproject.org/team/>
```

### **--version**

Display version information and exit.

```console
$ whoami --version
whoami (GNU coreutils) 8.32
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Richard Mlynarik.
```

## Usage Examples

### Basic Usage

Simply type `whoami` to see your current effective username:

```console
$ whoami
alice
```

### Using in Scripts

The command is often used in shell scripts to check the current user:

```console
$ if [ "$(whoami)" != "root" ]; then
>   echo "This script must be run as root"
>   exit 1
> fi
This script must be run as root
```

### After Switching Users

After using `su` or `sudo` to change users, `whoami` shows the new effective user:

```console
$ whoami
alice
$ sudo -s
# whoami
root
```

## Tips

### Understanding Effective vs. Real User ID

`whoami` shows the effective user ID, which may differ from your real user ID when using commands like `sudo`. To see both real and effective IDs, use the `id` command instead.

### Alternative Commands

The `id -un` command provides the same information as `whoami` and is available on all UNIX-like systems, making it a more portable alternative in scripts.

### Security Considerations

When writing security-sensitive scripts, remember that `whoami` only shows the effective user, not necessarily the user who originally launched the process.

## Frequently Asked Questions

#### Q1. What's the difference between `whoami` and `who am i`?
A. `whoami` shows the effective username of the current process, while `who am i` (or `who -m`) shows the original login name, terminal, and login time.

#### Q2. Can `whoami` tell me if I'm running as root?
A. Yes. If `whoami` returns "root", you're running with root privileges.

#### Q3. Does `whoami` work the same on all Unix/Linux systems?
A. Yes, the basic functionality is consistent across Unix-like systems, though some systems might have slightly different output formatting.

#### Q4. Why would I use `whoami` instead of `id`?
A. `whoami` is simpler and provides just the username, while `id` gives more comprehensive information including user ID, group ID, and group memberships.

## References

https://www.gnu.org/software/coreutils/manual/html_node/whoami-invocation.html

## Revisions

- 2025/05/04 First revision