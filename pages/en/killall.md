# killall command

Kill processes by name rather than by process ID (PID).

## Overview

The `killall` command terminates running processes based on their names rather than their process IDs. It's particularly useful when you need to stop multiple instances of the same program or when you don't know the specific PID of a process.

## Options

### **-s, --signal SIGNAL**

Specify the signal to send to processes (default is TERM)

```console
$ killall -s KILL firefox
```

### **-i, --interactive**

Ask for confirmation before killing each process

```console
$ killall -i chrome
Kill chrome(1234)? (y/N) y
Kill chrome(5678)? (y/N) n
```

### **-u, --user USER**

Kill only processes owned by the specified user

```console
$ killall -u john firefox
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
$ killall -u john bash
```

### Killing processes with confirmation

```console
$ killall -i spotify
Kill spotify(1234)? (y/N) y
```

## Tips

### Use the Correct Process Name

The process name must match exactly what appears in the process list. Use `ps aux` to see the exact process names.

### Force Kill Stubborn Processes

If a process doesn't respond to the default TERM signal, use `-9` (SIGKILL) to force termination: `killall -9 processname`. Be cautious as this doesn't allow the process to clean up.

### Verify Before Killing

When dealing with critical processes, use the `-i` option to confirm each kill action or `-v` to see which processes are being terminated.

### Specify Signal by Name or Number

You can specify signals by name (TERM, KILL, HUP) or by number (15, 9, 1).

## Frequently Asked Questions

#### Q1. What's the difference between `kill` and `killall`?
A. `kill` terminates processes by their PID, while `killall` terminates processes by their name.

#### Q2. How do I kill all instances of a program?
A. Simply run `killall programname` to terminate all instances of that program.

#### Q3. What if `killall` doesn't work?
A. Try using the `-9` option (`killall -9 programname`) to send a SIGKILL signal, which forces termination. If that fails, the process might be in an uninterruptible state or you might need root privileges.

#### Q4. Is there a way to test without actually killing processes?
A. Yes, use `killall -l` to list all available signals or `killall -s 0 processname` to test if processes exist without sending a kill signal.

## macOS Considerations

On macOS, the `killall` command behaves slightly differently than on Linux. It doesn't support all the same options, and the syntax may vary. For example, the `-u` option to specify a user isn't available on macOS. Also, macOS's `killall` is generally less flexible with pattern matching for process names.

## References

https://man7.org/linux/man-pages/man1/killall.1.html

## Revisions

- 2025/04/30 First revision