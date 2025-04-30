# su command

Switch user identity or become another user temporarily.

## Overview

The `su` command allows you to switch to another user account, most commonly the root (superuser) account. Without specifying a username, `su` defaults to the root user. It creates a new shell with the target user's environment and privileges.

## Options

### **-l, --login**

Provides a login shell, simulating a full login as the target user, including their environment variables and home directory

```console
$ su -l john
Password: 
john@hostname:~$
```

### **-c, --command**

Executes a single command as the specified user and then exits

```console
$ su -c "apt update" root
Password: 
[apt update output]
$
```

### **-s, --shell**

Specifies the shell to use instead of the default shell for the target user

```console
$ su -s /bin/zsh john
Password:
john@hostname:~$
```

### **-p, --preserve-environment**

Preserves the current environment variables when switching users

```console
$ su -p john
Password:
john@hostname:/current/directory$
```

## Usage Examples

### Becoming the root user

```console
$ su
Password: 
#
```

### Switching to another user with their environment

```console
$ su -l sarah
Password: 
sarah@hostname:~$
```

### Running a command as root without staying in root shell

```console
$ su -c "systemctl restart nginx" root
Password: 
[command output]
$
```

### Switching to root with login environment

```console
$ su -
Password: 
root@hostname:~#
```

## Tips

### Use sudo Instead When Possible

On many modern systems, using `sudo command` is preferred over `su` as it provides better logging and more granular permission control.

### Exit the Superuser Shell When Done

Always exit the root shell when you've finished your administrative tasks to avoid accidentally running commands with elevated privileges.

### Be Careful with Environment Variables

When switching users without the `-l` option, you keep your current environment variables, which might cause unexpected behavior.

### Root Password vs. Your Password

With `su`, you need to know the target user's password. With `sudo`, you typically use your own password (if you have sudo privileges).

## Frequently Asked Questions

#### Q1. What's the difference between `su` and `sudo`?
A. `su` switches your entire user context and requires the target user's password, while `sudo` runs a single command with elevated privileges and typically requires your own password.

#### Q2. How do I exit from a su session?
A. Type `exit` or press Ctrl+D to return to your original user account.

#### Q3. Why does `su -` work the same as `su -l root`?
A. The hyphen alone (`su -`) is a shorthand for `su -l root`, providing a login shell for the root user.

#### Q4. Can I use `su` to switch to any user?
A. Yes, but you need to know that user's password unless you're already the root user.

## macOS Considerations

On macOS, the root account is disabled by default for security reasons. Instead of using `su`, Apple recommends using `sudo` for administrative tasks. If you need a root shell, use `sudo -s` or `sudo -i`.

## References

https://www.man7.org/linux/man-pages/man1/su.1.html

## Revisions

- 2025/04/30 First revision