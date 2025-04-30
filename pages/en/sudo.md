# sudo command

Execute a command as another user, typically with elevated privileges.

## Overview

`sudo` (superuser do) allows users to run programs with the security privileges of another user, most commonly the superuser (root). It provides a way to grant limited root access to specific users without giving them the root password, enhancing system security while allowing necessary administrative tasks.

## Options

### **-u [username]**

Execute the command as a user other than root

```console
$ sudo -u postgres psql
psql (14.9)
Type "help" for help.

postgres=#
```

### **-s**

Start a shell with elevated privileges instead of running a single command

```console
$ sudo -s
root@hostname:/home/user#
```

### **-i**

Simulate a full login as the target user (loads the user's environment)

```console
$ sudo -i
root@hostname:~#
```

### **-l**

List the allowed (and forbidden) commands for the current user

```console
$ sudo -l
User user may run the following commands on hostname:
    (ALL : ALL) ALL
```

### **-v**

Validate and extend the user's sudo timestamp without running a command

```console
$ sudo -v
[No output means validation succeeded]
```

## Usage Examples

### Installing software with elevated privileges

```console
$ sudo apt update && sudo apt install nginx
[sudo] password for user: 
[Package installation output]
```

### Editing system configuration files

```console
$ sudo nano /etc/hosts
[sudo] password for user:
[Opens the hosts file in nano editor with write permissions]
```

### Running commands as a different user

```console
$ sudo -u www-data php /var/www/html/maintenance.php
[Output from the PHP script running as www-data user]
```

## Tips

### Use `sudo !!` to Repeat the Previous Command with sudo

If you forget to use sudo for a command that requires it, type `sudo !!` to repeat the previous command with sudo privileges.

### Configure sudo Without Password for Specific Commands

Edit the sudoers file with `sudo visudo` to allow certain commands to run without a password prompt, improving efficiency for trusted users.

### Be Careful with sudo and Redirection

When using sudo with output redirection (e.g., `sudo echo "text" > /protected/file`), the redirection happens as your user, not as root. Use `sudo sh -c 'echo "text" > /protected/file'` instead.

### Use sudoedit for Safely Editing Protected Files

`sudoedit` (or `sudo -e`) is safer than directly using an editor with sudo as it edits a temporary copy of the file and preserves file permissions.

## Frequently Asked Questions

#### Q1. What's the difference between sudo and su?
A. `sudo` executes a single command with elevated privileges and requires the user's password, while `su` switches to another user account (typically root) and requires that account's password.

#### Q2. How long does sudo authentication last?
A. By default, sudo remembers your password for 15 minutes, after which you'll need to enter it again.

#### Q3. How can I run multiple commands with sudo?
A. Use `sudo sh -c "command1 && command2"` or start a root shell with `sudo -s` or `sudo -i`.

#### Q4. Can I use sudo in scripts?
A. Yes, but it's better to run the entire script with sudo rather than using sudo for individual commands within the script. For automated scripts, consider using passwordless sudo for specific commands.

## macOS Considerations

On macOS, sudo works similarly to Linux but with some differences:
- The first time you use sudo, you'll see a message about responsibility
- macOS uses a separate sudoers file at `/etc/sudoers`
- TouchID can be configured to authenticate sudo on supported Mac models
- The sudo timeout may behave differently depending on your macOS version

## References

https://www.sudo.ws/docs/man/sudo.man/

## Revisions

- 2025/04/30 First revision