# gpasswd command

Manage group memberships and passwords in the system's group database.

## Overview

`gpasswd` is a command for administering the `/etc/group` and `/etc/gshadow` files. It allows system administrators to add and remove users from groups, set group administrators, and manage group passwords. This tool is primarily used for group management on Linux systems.

## Options

### **-a user**

Add a user to the specified group

```console
$ sudo gpasswd -a john developers
Adding user john to group developers
```

### **-d user**

Remove a user from the specified group

```console
$ sudo gpasswd -d john developers
Removing user john from group developers
```

### **-A user1,user2,...**

Set the list of administrative users for the group

```console
$ sudo gpasswd -A jane,mike developers
```

### **-M user1,user2,...**

Set the list of members for the group, replacing the current member list

```console
$ sudo gpasswd -M john,jane,mike developers
```

### **-r**

Remove the password from the specified group

```console
$ sudo gpasswd -r developers
```

## Usage Examples

### Adding a user to multiple groups

```console
$ sudo gpasswd -a sarah developers
Adding user sarah to group developers
$ sudo gpasswd -a sarah designers
Adding user sarah to group designers
```

### Setting a group password

```console
$ sudo gpasswd developers
New Password: 
Re-enter new password: 
```

### Making a user a group administrator

```console
$ sudo gpasswd -A mike developers
```

## Tips:

### Check Group Membership

Use the `groups` command to check which groups a user belongs to:

```console
$ groups john
john : users developers docker
```

### View Group Information

The `/etc/group` file contains all group information. You can view it with:

```console
$ cat /etc/group | grep developers
developers:x:1001:john,jane,mike
```

### Root Privileges Required

Most `gpasswd` operations require root privileges or sudo access. Regular users can only use `gpasswd` to change their own group password if they're group administrators.

## Frequently Asked Questions

#### Q1. What's the difference between `gpasswd` and `usermod` for adding users to groups?
A. Both can add users to groups, but `gpasswd` is specifically designed for group management with more group-specific options. `usermod -aG` is often used for simple group additions.

#### Q2. Can regular users use `gpasswd`?
A. Regular users can only use `gpasswd` if they've been designated as group administrators with the `-A` option, and even then, they can only add/remove members.

#### Q3. How do I see all members of a group?
A. Use `getent group groupname` to see all members of a specific group.

#### Q4. What happens when I set a group password?
A. When a group has a password, users who aren't members of the group can temporarily gain group privileges by using the `newgrp` command and entering the password.

## References

https://linux.die.net/man/1/gpasswd

## Revisions

- 2025/04/30 First revision