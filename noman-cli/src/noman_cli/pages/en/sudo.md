# sudo command

Execute a command as another user, typically with administrative privileges.

## Overview

`sudo` (superuser do) allows authorized users to execute commands with the security privileges of another user, by default the superuser (root). This provides a way to perform administrative tasks without logging in as the root user, enhancing system security by limiting privileged access.

## Options

### **-u, --user=USER**

Execute the command as a user other than the default target user (root)

```console
$ sudo -u postgres psql
psql (14.5)
Type "help" for help.

postgres=#
```

### **-i, --login**

Run a login shell as the target user; simulates a full login

```console
$ sudo -i
[root@hostname ~]#
```

### **-s, --shell**

Run the shell specified in the password database entry of the target user

```console
$ sudo -s
root@hostname:/home/user#
```

### **-l, --list**

List the allowed (and forbidden) commands for the invoking user

```console
$ sudo -l
User user may run the following commands on hostname:
    (ALL : ALL) ALL
```

### **-v, --validate**

Update the user's cached credentials, extending the sudo timeout

```console
$ sudo -v
[sudo] password for user: 
```

### **-k, --reset-timestamp**

Invalidate the user's cached credentials

```console
$ sudo -k
```

## Usage Examples

### Running a command with root privileges

```console
$ sudo apt update
[sudo] password for user: 
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
...
```

### Editing a system configuration file

```console
$ sudo nano /etc/hosts
[sudo] password for user:
```

### Running commands as a different user

```console
$ sudo -u www-data ls -la /var/www/html
total 16
drwxr-xr-x 2 www-data www-data 4096 May  4 10:15 .
drwxr-xr-x 3 root     root     4096 May  4 10:14 ..
-rw-r--r-- 1 www-data www-data  612 May  4 10:15 index.html
```

## Tips

### Use `sudo !!` to Repeat the Previous Command with sudo

If you forget to use sudo for a command that requires it, type `sudo !!` to repeat the previous command with sudo privileges.

### Configure sudo Without Password for Specific Commands

Edit the sudoers file with `sudo visudo` to allow certain commands to run without a password prompt. For example:
```
username ALL=(ALL) NOPASSWD: /usr/bin/apt update
```

### Use `sudo -E` to Preserve Environment Variables

When you need to run a command with sudo but keep your current environment variables, use the `-E` option.

### Always Use `visudo` to Edit the sudoers File

Never edit `/etc/sudoers` directly. Always use `sudo visudo` which checks for syntax errors before saving, preventing you from locking yourself out of sudo access.

## Frequently Asked Questions

#### Q1. What's the difference between `sudo -i` and `sudo -s`?
A. `sudo -i` simulates a full login and changes to the target user's home directory with their environment. `sudo -s` just starts a shell as the target user but keeps your current environment and working directory.

#### Q2. How long does sudo authentication last?
A. By default, sudo caches your credentials for 15 minutes. You can extend this with `sudo -v` or reset it with `sudo -k`.

#### Q3. How can I run multiple commands with sudo?
A. Use `sudo sh -c "command1 && command2"` or start a root shell with `sudo -i` and then run your commands.

#### Q4. How do I add a user to sudoers?
A. Add the user to the sudo group with `usermod -aG sudo username` on Debian/Ubuntu or to the wheel group on RHEL/CentOS systems.

## References

https://www.sudo.ws/docs/man/sudo.man/

## Revisions

- 2025/05/04 First revision