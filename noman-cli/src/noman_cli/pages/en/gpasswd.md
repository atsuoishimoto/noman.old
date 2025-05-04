# gpasswd command

Administers group membership and authentication information in the /etc/group and /etc/gshadow files.

## Overview

`gpasswd` is a command used to administer groups on Linux systems. It allows administrators to add or remove users from groups, set group passwords, and designate group administrators and members. This command manages the information stored in the `/etc/group` and `/etc/gshadow` files.

## Options

### **-a, --add** *USER*

Add a user to the specified group.

```console
$ sudo gpasswd -a john developers
Adding user john to group developers
```

### **-d, --delete** *USER*

Remove a user from the specified group.

```console
$ sudo gpasswd -d john developers
Removing user john from group developers
```

### **-r, --remove-password**

Remove the password from the specified group.

```console
$ sudo gpasswd -r developers
Removing password from group developers
```

### **-R, --restrict**

Restrict access to the group to its members only.

```console
$ sudo gpasswd -R developers
```

### **-A, --administrators** *USER1,USER2,...*

Set the list of administrative users for the group.

```console
$ sudo gpasswd -A jane,mike developers
```

### **-M, --members** *USER1,USER2,...*

Set the list of members for the group.

```console
$ sudo gpasswd -M john,jane,mike developers
```

## Usage Examples

### Adding a user to a group

```console
$ sudo gpasswd -a username groupname
Adding user username to group groupname
```

### Setting a group password

```console
$ sudo gpasswd developers
Changing the password for group developers
New Password: 
Re-enter new password: 
```

### Setting multiple administrators for a group

```console
$ sudo gpasswd -A user1,user2,user3 groupname
```

### Removing all members from a group

```console
$ sudo gpasswd -M "" groupname
```

## Tips:

### Check Group Membership

Use the `groups` command to check which groups a user belongs to:

```console
$ groups username
```

### View Group Information

The `/etc/group` file contains group information. View it with:

```console
$ cat /etc/group | grep groupname
```

### Group Administration Workflow

When setting up a new project team, first create the group with `groupadd`, then add members with `gpasswd -a` or set all members at once with `gpasswd -M`.

## Frequently Asked Questions

#### Q1. What's the difference between `gpasswd` and `usermod -G`?
A. `gpasswd` is specifically designed for group management and can set group administrators and passwords. `usermod -G` can add users to groups but replaces all existing group memberships unless you use `-a` with it.

#### Q2. Can regular users use `gpasswd`?
A. Regular users can only use `gpasswd` if they are designated as group administrators with the `-A` option, and even then they have limited capabilities.

#### Q3. How do I remove a group password?
A. Use `gpasswd -r groupname` to remove a password from a group.

#### Q4. What happens when I set a group password?
A. When a group has a password, users who are not members of the group can temporarily join the group during a session by using the `newgrp` command and providing the correct password.

## References

https://man7.org/linux/man-pages/man1/gpasswd.1.html

## Revisions

- 2025/05/04 First revision