# su command

Switch user identity or become another user temporarily.

## Overview

The `su` command allows you to switch to another user account, most commonly the root user. Without specifying a username, `su` defaults to the superuser (root). It creates a new shell with the target user's environment and privileges.

## Options

### **-** or **-l**, **--login**

Provide a login environment, simulating a direct login for the specified user

```console
$ su - john
Password: 
john@hostname:~$
```

### **-c**, **--command=COMMAND**

Execute a single command as the specified user and then exit

```console
$ su -c "ls -la /root" root
Password: 
total 28
drwx------  4 root root 4096 May  4 10:15 .
drwxr-xr-x 20 root root 4096 Apr 15 09:30 ..
-rw-------  1 root root  982 May  1 14:22 .bash_history
-rw-r--r--  1 root root 3106 Dec  5  2024 .bashrc
drwxr-xr-x  3 root root 4096 Jan 10  2025 .config
-rw-r--r--  1 root root  161 Dec  5  2024 .profile
drwx------  2 root root 4096 Feb 20  2025 .ssh
```

### **-s**, **--shell=SHELL**

Run the specified shell instead of the default shell for the user

```console
$ su -s /bin/zsh john
Password: 
john@hostname:~$
```

### **-p**, **--preserve-environment**

Preserve the current environment variables when switching users

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
root@hostname:/home/user#
```

### Running a command as root and returning to normal user

```console
$ su -c "apt update && apt upgrade -y" root
Password: 
[apt update and upgrade output]
$
```

### Switching to another user with their environment

```console
$ su - john
Password: 
john@hostname:~$
```

## Tips:

### Use sudo Instead When Possible

For most administrative tasks, using `sudo command` is preferable to `su` as it:
- Logs all commands executed
- Doesn't require sharing the root password
- Provides more granular permission control

### Exit the Superuser Shell Safely

Always type `exit` or press Ctrl+D when you're done with the superuser shell to return to your regular user account.

### Be Careful with Environment Variables

When using plain `su` (without `-`), you keep your current environment variables, which might cause unexpected behavior. Use `su -` for a clean environment.

## Frequently Asked Questions

#### Q1. What's the difference between `su` and `sudo`?
A. `su` switches your entire user session to another user (typically root), while `sudo` executes just a single command with elevated privileges and then returns to your normal user.

#### Q2. Why does `su` sometimes fail with "Authentication failure"?
A. This usually happens because the root account password is incorrect or the root account is locked (common in Ubuntu and other distributions that prefer sudo).

#### Q3. How do I exit from the su session?
A. Type `exit` or press Ctrl+D to return to your original user account.

#### Q4. What's the difference between `su` and `su -`?
A. `su` only changes the user ID but keeps your current environment variables and working directory. `su -` provides a complete login environment for the new user, changing to their home directory and loading their profile.

## References

https://www.gnu.org/software/coreutils/manual/html_node/su-invocation.html

## Revisions

- 2025/05/04 First revision