# groupmod command

Modify a group definition on the system.

## Overview

The `groupmod` command is used to modify the attributes of an existing group on a Linux or Unix system. It can change a group's name (GID) or numeric group ID. This command is typically used by system administrators when managing user and group accounts.

## Options

### **-g, --gid GID**

Change the group ID to the specified value.

```console
$ sudo groupmod -g 1005 developers
```

### **-n, --new-name NEW_GROUP**

Change the name of the group to NEW_GROUP.

```console
$ sudo groupmod -n programmers developers
```

### **-o, --non-unique**

Allow the use of a non-unique GID (normally GIDs must be unique).

```console
$ sudo groupmod -g 1005 -o testers
```

### **-p, --password PASSWORD**

Change the password for the group to the encrypted PASSWORD.

```console
$ sudo groupmod -p encrypted_password developers
```

### **-R, --root CHROOT_DIR**

Apply changes in the CHROOT_DIR directory and use the configuration files from the CHROOT_DIR directory.

```console
$ sudo groupmod -R /mnt/system -n programmers developers
```

## Usage Examples

### Changing a group's name

```console
$ sudo groupmod -n engineering developers
```

This changes the group name from "developers" to "engineering" while keeping the same GID.

### Changing a group's GID

```console
$ sudo groupmod -g 2000 engineering
```

This changes the GID of the "engineering" group to 2000.

### Changing both name and GID

```console
$ sudo groupmod -n tech-team -g 2500 engineering
```

This changes the group name from "engineering" to "tech-team" and changes its GID to 2500.

## Tips:

### Check Group Information Before Modifying

Always verify the current group information using `getent group groupname` before making changes to ensure you have the correct information.

### Update File Ownership After GID Changes

After changing a group's GID, you may need to update file ownership with `find /path -group old_gid -exec chgrp new_gid {} \;` to maintain proper access to files.

### Backup Before Making Changes

For critical systems, consider backing up the `/etc/group` and `/etc/gshadow` files before making changes with `groupmod`.

### Use with caution

Changing group IDs can affect file permissions and access rights across the system. Make changes during maintenance windows when possible.

## Frequently Asked Questions

#### Q1. What happens to files owned by a group if I change its GID?
A. Files will still reference the old GID number, not the new one. You'll need to manually update file ownership using the `chgrp` command.

#### Q2. Can I change a group's name and GID at the same time?
A. Yes, you can use both the `-n` and `-g` options together in a single command.

#### Q3. How do I know if a group is in use by any users?
A. Use `grep groupname /etc/group /etc/passwd` to see if the group is listed as a primary or secondary group for any users.

#### Q4. What happens if I try to rename a group to a name that already exists?
A. The command will fail with an error message indicating that the group already exists.

## References

https://www.man7.org/linux/man-pages/man8/groupmod.8.html

## Revisions

- 2025/05/04 First revision