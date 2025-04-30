# groupmod command

Modify a group definition on the system.

## Overview

The `groupmod` command allows system administrators to modify existing group accounts. It can change a group's name, group ID (GID), or other attributes stored in the system group database.

## Options

### **-g GID**

Change the group ID to the specified value.

```console
$ sudo groupmod -g 1001 developers
```

### **-n NEW_NAME**

Change the name of the group to the specified value.

```console
$ sudo groupmod -n engineering developers
```

### **-p PASSWORD**

Set the encrypted password for the group (rarely used on modern systems).

```console
$ sudo groupmod -p encrypted_password groupname
```

### **-o**

Allow the use of a non-unique GID (permits multiple groups to share the same GID).

```console
$ sudo groupmod -g 1001 -o newgroup
```

## Usage Examples

### Renaming a group

```console
$ sudo groupmod -n devteam developers
$ grep devteam /etc/group
devteam:x:1001:user1,user2,user3
```

### Changing a group's GID

```console
$ sudo groupmod -g 2000 devteam
$ grep devteam /etc/group
devteam:x:2000:user1,user2,user3
```

### Combining options to rename and change GID

```console
$ sudo groupmod -n engineering -g 3000 devteam
$ grep engineering /etc/group
engineering:x:3000:user1,user2,user3
```

## Tips

### Check Group Information First

Always verify the current group information before making changes:

```console
$ grep groupname /etc/group
```

### Update File Ownership After GID Changes

After changing a group's GID, you may need to update file ownership:

```console
$ sudo find /path/to/directory -group old_gid -exec chgrp new_gid {} \;
```

### Back Up Group Files

Before making changes, consider backing up your group files:

```console
$ sudo cp /etc/group /etc/group.bak
$ sudo cp /etc/gshadow /etc/gshadow.bak
```

## Frequently Asked Questions

#### Q1. What's the difference between `groupmod` and `usermod`?
A. `groupmod` modifies group attributes, while `usermod` modifies user account attributes. Use `groupmod` for changing group properties and `usermod` for user properties.

#### Q2. Can I change a group's GID to one that's already in use?
A. By default, no. However, you can use the `-o` option to allow non-unique GIDs, though this is generally not recommended.

#### Q3. Will changing a group's GID affect files owned by that group?
A. Yes. Files owned by the group will still reference the old GID. You'll need to manually update file ownership using `chgrp` or `find` with `chgrp`.

#### Q4. How do I see what changes I've made to a group?
A. Check the group database with `getent group groupname` or look at the `/etc/group` file directly.

## References

https://www.man7.org/linux/man-pages/man8/groupmod.8.html

## Revisions

- 2025/04/30 First revision