# passwd command

Change user password.

## Overview

The `passwd` command allows users to change their own password or, for system administrators, to change or administer passwords for other users. It modifies the `/etc/passwd` and `/etc/shadow` files that store user account information and encrypted passwords.

## Options

### **-d, --delete**

Delete a user's password (make it empty)

```console
$ sudo passwd -d username
passwd: password expiry information changed.
```

### **-e, --expire**

Force password to expire immediately, requiring the user to change it at next login

```console
$ sudo passwd -e username
passwd: password expiry information changed.
```

### **-l, --lock**

Lock the specified account by adding a '!' character at the beginning of the password, disabling the account

```console
$ sudo passwd -l username
passwd: password expiry information changed.
```

### **-u, --unlock**

Unlock a previously locked account by removing the '!' character from the password

```console
$ sudo passwd -u username
passwd: password expiry information changed.
```

### **-S, --status**

Display account status information for a user

```console
$ passwd -S username
username PS 2023-05-04 0 99999 7 -1
```

## Usage Examples

### Changing your own password

```console
$ passwd
Changing password for user1.
Current password: 
New password: 
Retype new password: 
passwd: all authentication tokens updated successfully.
```

### Changing another user's password (as root)

```console
$ sudo passwd username
New password: 
Retype new password: 
passwd: all authentication tokens updated successfully.
```

### Checking password status for a user

```console
$ sudo passwd -S username
username PS 2023-05-04 0 99999 7 -1
```

## Tips:

### Understanding Password Status Output

When using `passwd -S`, the output format is: `username PASSWORD-STATUS CHANGE-DATE MIN-DAYS MAX-DAYS WARN-DAYS INACTIVE-DAYS EXPIRE-DATE`. The PASSWORD-STATUS field can be PS (usable password), LK (locked password), or NP (no password).

### Secure Password Practices

When creating passwords, use a mix of uppercase, lowercase, numbers, and special characters. The system may enforce password complexity requirements depending on your configuration.

### Password Files Location

The encrypted passwords are stored in `/etc/shadow`, which is only readable by root. This provides better security than the older method of storing hashed passwords in the world-readable `/etc/passwd` file.

## Frequently Asked Questions

#### Q1. How do I change my own password?
A. Simply type `passwd` without any options and follow the prompts to enter your current password and then your new password twice.

#### Q2. Why does the system reject my new password?
A. Most systems have password complexity requirements. Your password might be rejected if it's too short, too simple, based on a dictionary word, or reuses too many characters from your previous password.

#### Q3. How can I force a user to change their password at next login?
A. Use `sudo passwd -e username` to expire the user's password, forcing them to change it when they next log in.

#### Q4. What's the difference between locking an account and deleting its password?
A. Locking an account (`passwd -l`) prevents login while preserving the password hash. Deleting a password (`passwd -d`) removes the password entirely, which might allow passwordless login depending on system configuration.

## References

https://man7.org/linux/man-pages/man1/passwd.1.html

## Revisions

- 2025/05/04 First revision