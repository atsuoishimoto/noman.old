# pstree command

Display running processes as a tree structure.

## Overview

The `pstree` command shows the relationships between processes in a tree format, making it easy to visualize process hierarchies. It displays the parent-child relationships between processes, helping users understand how processes are spawned and related to each other in the system.

## Options

### **-a**

Show command line arguments for each process

```console
$ pstree -a
systemd
  ├─NetworkManager --no-daemon
  ├─sshd -D
  │   └─sshd
  │       └─sshd
  │           └─bash
  │               └─pstree -a
  └─systemd-journald
```

### **-p**

Show PIDs (Process IDs) for each process

```console
$ pstree -p
systemd(1)
  ├─NetworkManager(687)
  ├─sshd(1025)─┬─sshd(2156)───sshd(2189)───bash(2190)───pstree(3421)
  └─systemd-journald(346)
```

### **-u**

Show the user name for each process

```console
$ pstree -u
systemd
  ├─NetworkManager(root)
  ├─sshd(root)─┬─sshd(root)───sshd(user)───bash(user)───pstree(user)
  └─systemd-journald(root)
```

### **-h**

Highlight the current process and its ancestors

```console
$ pstree -h
systemd
  ├─NetworkManager
  ├─sshd───sshd───sshd───bash───pstree
  └─systemd-journald
```

## Usage Examples

### Combining options for detailed view

```console
$ pstree -apu
systemd(1,root)
  ├─NetworkManager(687,root) --no-daemon
  ├─sshd(1025,root) -D
  │   └─sshd(2156,root)
  │       └─sshd(2189,user)
  │           └─bash(2190,user)
  │               └─pstree(3421,user) -apu
  └─systemd-journald(346,root)
```

### Showing only a specific user's processes

```console
$ pstree -u user
sshd───sshd───bash───pstree
```

### Showing processes for a specific PID

```console
$ pstree -p 2190
bash(2190)───pstree(3422)
```

## Tips

### Find Parent-Child Relationships Quickly

Use `pstree -p` to quickly identify which process spawned another process, helpful for troubleshooting runaway processes or understanding application behavior.

### Compact View for Large Process Trees

By default, `pstree` compacts identical subtrees, showing them only once with a count. Use `-c` to disable this if you need to see every individual process.

### Identify Resource-Intensive Process Hierarchies

Combine with `ps` or `top` to first identify high-resource processes, then use `pstree` to see their relationship to other processes in the system.

## Frequently Asked Questions

#### Q1. How is `pstree` different from `ps`?
A. While `ps` shows a flat list of processes, `pstree` displays processes in a hierarchical tree structure that shows parent-child relationships.

#### Q2. Can I see process arguments with `pstree`?
A. Yes, use the `-a` option to display command line arguments for each process.

#### Q3. How do I find which process started a specific process?
A. Use `pstree -p PID` to see the process and its parent hierarchy.

#### Q4. Does `pstree` show all system processes?
A. By default, it shows all processes. To see only processes for a specific user, use `pstree username`.

## References

https://man7.org/linux/man-pages/man1/pstree.1.html

## Revisions

- 2025/04/30 First revision