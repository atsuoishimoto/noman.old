# pstree command

Display a tree of processes showing parent-child relationships.

## Overview

The `pstree` command displays the running processes as a tree, which makes it easy to see the parent-child relationships between processes. It provides a visual representation of how processes are connected, showing which process spawned which other processes.

## Options

### **-a, --arguments**

Show command line arguments for each process.

```console
$ pstree -a
systemd
  ├─ModemManager
  ├─NetworkManager --no-daemon
  ├─accounts-daemon
  ├─avahi-daemon --syslog
  │   └─avahi-daemon --syslog
  └─sshd -D
      └─sshd
          └─sshd
              └─bash
```

### **-p, --show-pids**

Show PIDs (Process IDs) alongside process names.

```console
$ pstree -p
systemd(1)─┬─ModemManager(823)
           ├─NetworkManager(824)
           ├─accounts-daemon(825)
           ├─avahi-daemon(826)───avahi-daemon(845)
           └─sshd(1025)───sshd(1789)───sshd(1823)───bash(1824)
```

### **-h, --highlight-all**

Highlight the current process and its ancestors.

```console
$ pstree -h
systemd─┬─ModemManager
        ├─NetworkManager
        ├─accounts-daemon
        ├─avahi-daemon───avahi-daemon
        └─sshd───sshd───sshd───bash
```

### **-u, --uid-changes**

Show uid transitions (changes in user ID).

```console
$ pstree -u
systemd─┬─ModemManager
        ├─NetworkManager
        ├─accounts-daemon
        ├─avahi-daemon───avahi-daemon
        └─sshd───sshd───sshd───bash(user)
```

### **-n, --numeric-sort**

Sort processes with the same parent by PID instead of by name.

```console
$ pstree -n
systemd─┬─ModemManager
        ├─NetworkManager
        ├─accounts-daemon
        ├─avahi-daemon───avahi-daemon
        └─sshd───sshd───sshd───bash
```

## Usage Examples

### Display the process tree for a specific user

```console
$ pstree username
bash───vim
```

### Display the process tree for a specific PID

```console
$ pstree 1234
bash───firefox───Web Content
```

### Combine multiple options for detailed output

```console
$ pstree -apu
systemd(1)
  ├─ModemManager(823)
  ├─NetworkManager(824) --no-daemon
  ├─accounts-daemon(825)
  ├─avahi-daemon(826) --syslog
  │   └─avahi-daemon(845) --syslog
  └─sshd(1025) -D
      └─sshd(1789)
          └─sshd(1823)
              └─bash(1824)(user)
```

## Tips:

### Find Parent-Child Process Relationships

When troubleshooting, use `pstree -p` to quickly identify which parent process spawned a particular child process. This helps in understanding process hierarchies.

### Identify Resource-Intensive Process Groups

Combine with `ps` to identify not just a resource-intensive process but its entire process family: `pstree -p $(ps -eo pid,pcpu --sort=-pcpu | head -2 | tail -1 | awk '{print $1}')`

### Compact View for Large Systems

For systems with many processes, use `pstree -c` to get a more compact view that doesn't compress identical subtrees.

## Frequently Asked Questions

#### Q1. How is `pstree` different from `ps`?
A. While `ps` lists processes in a flat format, `pstree` displays them in a hierarchical tree structure showing parent-child relationships.

#### Q2. Can I see process IDs with `pstree`?
A. Yes, use `pstree -p` to display PIDs alongside process names.

#### Q3. How do I see the process tree for a specific user?
A. Run `pstree username` to see only processes owned by that user.

#### Q4. Can I see command line arguments in the process tree?
A. Yes, use `pstree -a` to display command line arguments for each process.

## References

https://man7.org/linux/man-pages/man1/pstree.1.html

## Revisions

- 2025/05/04 First revision