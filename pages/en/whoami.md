# whoami command

Display the effective username of the current user.

## Overview

The `whoami` command prints the username of the person currently logged into the terminal session. It's a simple way to verify which user account is being used for the current session, which can be particularly useful when switching between multiple user accounts or when using sudo.

## Options

The `whoami` command is straightforward and typically used without options, as its primary function is simply to display the current username.

```console
$ whoami
username
```

## Usage Examples

### Basic usage

```console
$ whoami
john
```

### Using with other commands

```console
$ echo "Current user is $(whoami)"
Current user is john
```

### Checking user after sudo

```console
$ whoami
john
$ sudo whoami
root
```

## Tips

### Difference from `id` command

While `whoami` only shows the username, the `id` command provides more comprehensive information including user ID, group ID, and all groups the user belongs to.

### Use in scripts

`whoami` is useful in shell scripts when you need to perform different actions based on which user is running the script, or to verify that a script is being run with the correct permissions.

### Security context

When troubleshooting permission issues, `whoami` helps confirm which user identity is active, especially after using commands like `su` or `sudo` that change the effective user.

## Frequently Asked Questions

#### Q1. What's the difference between `whoami` and `who am i`?
A. `whoami` shows the effective username (the user you're currently running as), while `who am i` (or `who -m`) shows the original login name, which might be different if you've used `su` or similar commands.

#### Q2. Does `whoami` show the real or effective user ID?
A. `whoami` displays the effective user ID, which is the user identity the system uses to determine your permissions.

#### Q3. How can I see more information about my user account?
A. Use the `id` command instead, which shows your user ID, group ID, and all groups you belong to.

## References

https://www.gnu.org/software/coreutils/manual/html_node/whoami-invocation.html

## Revisions

- 2025/04/30 First revision