# groupadd command

Create a new group on the system.

## Overview

The `groupadd` command creates a new group account on the system. It adds an entry to the system group files with the specified group name and assigns it a unique group ID (GID). This command is typically used by system administrators to manage user groups for access control and permission management.

## Options

### **-g GID**

Specify the numerical value of the group's ID manually instead of using the next available GID.

```console
$ sudo groupadd -g 1500 developers
```

### **-r**

Create a system group with a GID in the system group range (typically below 1000).

```console
$ sudo groupadd -r docker
```

### **-f**

Force the command to exit successfully even if the group already exists. Without this option, the command would fail with an error.

```console
$ sudo groupadd -f marketing
```

### **-K KEY=VALUE**

Override the default values from /etc/login.defs configuration file.

```console
$ sudo groupadd -K GID_MIN=5000 newgroup
```

## Usage Examples

### Creating a standard group

```console
$ sudo groupadd engineering
```

### Creating a system group with a specific GID

```console
$ sudo groupadd -r -g 850 mysql
```

### Verifying a group was created

```console
$ grep engineering /etc/group
engineering:x:1001:
```

## Tips:

### Check Available GIDs

Before manually specifying a GID with `-g`, check existing GIDs to avoid conflicts:

```console
$ getent group
```

### Group Naming Conventions

Use lowercase letters without spaces for group names. Hyphens or underscores are acceptable separators for multi-word group names (e.g., `web-developers` or `web_developers`).

### System vs. Regular Groups

System groups (created with `-r`) are typically used for services and daemons, while regular groups are for human users. System groups usually have lower GIDs than regular user groups.

## Frequently Asked Questions

#### Q1. How do I add users to a newly created group?
A. After creating the group, use the `usermod -aG groupname username` command to add existing users to the group.

#### Q2. What's the difference between system and regular groups?
A. System groups (created with `-r`) are meant for system services and typically have lower GIDs. Regular groups are intended for organizing human users.

#### Q3. How can I check if a group already exists?
A. Use `getent group groupname` or `grep groupname /etc/group` to check if a group exists.

#### Q4. Can I delete a group after creating it?
A. Yes, use the `groupdel groupname` command to delete a group.

## References

https://www.man7.org/linux/man-pages/man8/groupadd.8.html

## Revisions

- 2025/04/30 First revision