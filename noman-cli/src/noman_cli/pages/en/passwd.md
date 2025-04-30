# passwd command

Change user password.

## Overview

The `passwd` command allows users to change their own password or, for system administrators, to change or manage other users' passwords. It handles password authentication, modification, and enforces password policies on Unix-like systems.

## Options

### **-d, --delete**

Delete a user's password (make it empty)

```console
$ sudo passwd -d username
Password for username deleted
```

### **-l, --lock**

Lock a user's password (disable the account)

```console
$ sudo passwd -l username
Password for username has been locked
```

### **-u, --unlock**

Unlock a user's password (re-enable the account)

```console
$ sudo passwd -u username
Password for username has been unlocked
```

### **-e, --expire**

Force password expiration (user must change password at next login)

```console
$ sudo passwd -e username
Password for username has been expired
```

### **-S, --status**

Display password status information for a user

```console
$ passwd -S username
username PS 2025-04-15 0 99999 7 -1
```

## Usage Examples

### Changing your own password

```console
$ passwd
Changing password for current_user
Current password: 
New password: 
Retype new password: 
passwd: password updated successfully
```

### Changing another user's password (requires root privileges)

```console
$ sudo passwd username
New password: 
Retype new password: 
passwd: password updated successfully
```

### Checking password status for a user

```console
$ passwd -S username
username PS 2025-04-15 0 99999 7 -1
```

## Tips:

### Understanding Password Status Output

The output of `passwd -S` shows several fields: username, password status (PS=set, LK=locked, NP=no password), date of last change, minimum age, maximum age, warning period, and inactivity period.

### Password Security

Create strong passwords with a mix of uppercase, lowercase, numbers, and special characters. Avoid using personal information or common words.

### Root Password Management

Be extremely careful when changing the root password. If forgotten, recovery can be difficult and might require booting into single-user mode.

### Password Files

The `passwd` command modifies `/etc/passwd` and `/etc/shadow` files. Never edit these files directly; always use the proper commands.

## Frequently Asked Questions

#### Q1. How do I change my own password?
A. Simply type `passwd` and follow the prompts to enter your current password and then your new password twice.

#### Q2. How can I force a user to change their password at next login?
A. Use `sudo passwd -e username` to expire a user's password.

#### Q3. What happens when I lock a user account?
A. The `passwd -l` command prepends the encrypted password with an exclamation mark (!), preventing the user from logging in with their password, but other authentication methods might still work.

#### Q4. Can I make a user account passwordless?
A. Yes, with `sudo passwd -d username`, but this is generally insecure and should be avoided in most cases.

#### Q5. How do I know if a password is locked?
A. Use `passwd -S username` and check if the status shows "LK" (locked).

## References

https://man7.org/linux/man-pages/man1/passwd.1.html

## Revisions

- 2025/04/30 First revision