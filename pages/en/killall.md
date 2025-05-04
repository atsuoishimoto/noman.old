# killall command

Kill processes by name rather than by process ID.

## Overview

The `killall` command terminates running processes based on their names rather than process IDs (PIDs). It's particularly useful when you need to stop multiple instances of the same program or when you don't know the specific PID of a process.

## Options

### **-e, --exact**

Require an exact match for very long names

```console
$ killall -e firefox
```

### **-I, --ignore-case**

Case insensitive process name match

```console
$ killall -I firefox
```

### **-i, --interactive**

Ask for confirmation before killing

```console
$ killall -i chrome
Kill chrome(1234) ? (y/N) y
Kill chrome(5678) ? (y/N) n
```

### **-l, --list**

List all known signal names

```console
$ killall -l
HUP INT QUIT ILL TRAP ABRT BUS FPE KILL USR1 SEGV USR2 PIPE ALRM TERM STKFLT CHLD CONT STOP TSTP TTIN TTOU URG XCPU XFSZ VTALRM PROF WINCH POLL PWR SYS
```

### **-q, --quiet**

Don't print complaints if no processes were killed

```console
$ killall -q nonexistentprocess
```

### **-s, --signal SIGNAL, -SIGNAL**

Send a specific signal instead of SIGTERM

```console
$ killall -s SIGKILL firefox
$ killall -KILL firefox  # Equivalent
```

### **-u, --user USER**

Kill only processes owned by specified user

```console
$ killall -u username firefox
```

### **-v, --verbose**

Report if the signal was successfully sent

```console
$ killall -v firefox
Killed firefox(1234) with signal 15
```

### **-w, --wait**

Wait for all killed processes to die

```console
$ killall -w firefox
```

## Usage Examples

### Killing a specific application

```console
$ killall firefox
```

### Killing a process with a specific signal

```console
$ killall -9 chrome
```

### Killing processes owned by a specific user

```console
$ killall -u john java
```

### Killing processes and waiting for confirmation

```console
$ killall -i -w firefox
Kill firefox(1234) ? (y/N) y
```

## Tips:

### Use Confirmation for Important Processes

Always use the `-i` (interactive) option when killing critical processes to avoid accidentally terminating the wrong ones.

### Verify Process Names First

Run `ps aux | grep process_name` before using killall to confirm the exact process name you want to terminate.

### Wait for Completion

Use the `-w` option when you need to ensure processes are fully terminated before proceeding with other operations.

### Be Careful with Common Names

Avoid using killall with very generic process names like "http" or "java" without specifying a user (-u) or using interactive mode (-i), as this could terminate important system processes.

## Frequently Asked Questions

#### Q1. What's the difference between `kill` and `killall`?
A. `kill` terminates processes by their PID (Process ID), while `killall` terminates processes by their name.

#### Q2. How do I force kill a stubborn process?
A. Use `killall -9 process_name` or `killall -KILL process_name` to send the SIGKILL signal, which cannot be caught or ignored by the process.

#### Q3. Can I kill multiple different processes at once?
A. Yes, just list all the process names: `killall firefox chrome gedit`

#### Q4. How do I know if killall succeeded?
A. Use the `-v` (verbose) option to see confirmation messages for each process killed.

#### Q5. Is killall available on all Unix systems?
A. No, while common on Linux, some Unix variants like Solaris have a different `killall` command that kills ALL processes, which can be dangerous. Always check the man page on unfamiliar systems.

## References

https://man7.org/linux/man-pages/man1/killall.1.html

## Revisions

- 2025/05/04 First revision