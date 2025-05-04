# groups command

Display the groups a user belongs to.

## Overview

The `groups` command shows all the groups that a specified user is a member of. If no user is specified, it displays the groups for the current user. This command is useful for checking user permissions and access rights in Unix/Linux systems.

## Options

The `groups` command has very few options as it's a simple utility:

### **username**

Displays the groups for the specified username

```console
$ groups john
john : users wheel developers
```

## Usage Examples

### Checking your own groups

```console
$ groups
user wheel audio video
```

### Checking groups for multiple users

```console
$ groups root alice bob
root : root bin daemon sys adm
alice : users wheel developers
bob : users guests
```

## Tips:

### Understanding Group Membership

Group membership determines what files and resources a user can access. The first group listed is typically the user's primary group, while others are supplementary groups.

### Related Commands

Use `id -Gn` as an alternative to see your groups. For more detailed information including numeric group IDs, use `id` without options.

### Checking System Group Files

If you need to see all groups defined on the system, check the `/etc/group` file with `cat /etc/group` or `getent group`.

## Frequently Asked Questions

#### Q1. What's the difference between primary and supplementary groups?
A. The primary group (usually the first one listed) is the default group assigned to files created by the user. Supplementary groups provide additional access permissions.

#### Q2. How do I add a user to a group?
A. Use `usermod -aG groupname username` to add a user to a supplementary group.

#### Q3. Why do I need to know my groups?
A. Group membership determines what files and resources you can access on the system. Troubleshooting permission issues often involves checking group membership.

#### Q4. Can I see the numeric group IDs instead of names?
A. Yes, use `id -G` instead of `groups` to see numeric group IDs.

## References

https://www.gnu.org/software/coreutils/manual/html_node/groups-invocation.html

## Revisions

- 2025/05/04 First revision