# groupadd command

Create a new group on the system.

## Overview

The `groupadd` command creates a new group account on the system. It adds an entry to the system group file (usually `/etc/group`) with the specified group name and assigns it a unique group ID (GID).

## Options

### **-f, --force**

Exit successfully if the group already exists, and cancel -g if the GID is already used.

```console
$ sudo groupadd -f developers
```

### **-g, --gid GID**

Specify the numerical value of the group's ID (GID). This value must be unique unless the -o option is used.

```console
$ sudo groupadd -g 1500 project-team
```

### **-K, --key KEY=VALUE**

Override /etc/login.defs defaults (GID_MIN, GID_MAX, etc.).

```console
$ sudo groupadd -K GID_MIN=5000 new-group
```

### **-o, --non-unique**

Allow creating a group with a non-unique GID.

```console
$ sudo groupadd -o -g 1500 another-group
```

### **-p, --password PASSWORD**

Set the encrypted password for the new group.

```console
$ sudo groupadd -p encrypted_password finance
```

### **-r, --system**

Create a system group with a GID in the system GID range.

```console
$ sudo groupadd -r sysgroup
```

## Usage Examples

### Creating a basic group

```console
$ sudo groupadd developers
```

### Creating a system group

```console
$ sudo groupadd -r docker
```

### Creating a group with a specific GID

```console
$ sudo groupadd -g 2000 project-team
```

### Creating a group that may already exist

```console
$ sudo groupadd -f webadmins
```

## Tips:

### Check Group Creation

After creating a group, verify it was added correctly using the `getent group` command:

```console
$ getent group developers
developers:x:1001:
```

### Group ID Ranges

System groups typically use lower GIDs (often below 1000), while user groups use higher GIDs. Check your system's `/etc/login.defs` file for the specific ranges.

### Group Management

Remember that `groupadd` only creates groups. Use `groupmod` to modify existing groups and `groupdel` to remove them.

### Group Membership

After creating a group, use `usermod -aG groupname username` to add users to the group.

## Frequently Asked Questions

#### Q1. How do I create a new group?
A. Use `sudo groupadd groupname` to create a new group with the specified name.

#### Q2. How do I specify a custom GID when creating a group?
A. Use `sudo groupadd -g GID groupname` where GID is the numerical group ID you want to assign.

#### Q3. What's the difference between system and regular groups?
A. System groups (created with `-r`) are typically used for system services and daemons, while regular groups are for human users. System groups usually have lower GIDs.

#### Q4. How do I check if a group already exists?
A. Use `getent group groupname` to check if a group exists.

#### Q5. Can I create a group with the same GID as an existing group?
A. Yes, but only by using the `-o` (non-unique) option: `sudo groupadd -o -g existing_gid new_group`.

## References

https://man7.org/linux/man-pages/man8/groupadd.8.html

## Revisions

- 2025/05/04 First revision