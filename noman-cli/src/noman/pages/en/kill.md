# kill command

Send a signal to a process, usually to terminate it.

## Overview

The `kill` command sends signals to processes, most commonly used to terminate running processes. While its name suggests termination, `kill` can actually send various signals to processes, allowing for different types of control beyond just stopping them. Each signal has a specific purpose, with SIGTERM (15) being the default signal that requests graceful termination.

## Options

### **-s, --signal [signal]**

Specify the signal to send (either as a name or number)

```console
$ kill -s TERM 1234
```

### **-l, --list [signal]**

List available signal names or convert signal names to/from numbers

```console
$ kill -l
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX
```

### **-9, -KILL, -SIGKILL**

Send SIGKILL signal, which forces immediate termination (cannot be caught or ignored)

```console
$ kill -9 1234
```

### **-15, -TERM, -SIGTERM**

Send SIGTERM signal (default), which requests graceful termination

```console
$ kill -15 1234
```

## Usage Examples

### Terminating a process by PID

```console
$ kill 1234
```

### Forcefully terminating a process that won't respond

```console
$ kill -9 1234
```

### Sending a custom signal to a process

```console
$ kill -s USR1 1234
```

### Terminating multiple processes at once

```console
$ kill 1234 5678 9012
```

## Tips:

### Find Process IDs First

Use `ps` or `pgrep` to find the process ID before using kill:

```console
$ ps aux | grep firefox
user     1234  2.0  1.5 3245676 124548 ?      Sl   09:15   0:45 /usr/lib/firefox/firefox
$ kill 1234
```

### Use Signal Names for Clarity

Signal names are often clearer than numbers:

```console
$ kill -TERM 1234  # Same as kill -15 1234
```

### Common Signals and Their Uses

- SIGTERM (15): Standard termination signal, allows cleanup
- SIGKILL (9): Force termination, use when process is unresponsive
- SIGHUP (1): Often used to reload configuration files
- SIGINT (2): Interrupt signal (same as pressing Ctrl+C)

## Frequently Asked Questions

#### Q1. What's the difference between `kill -9` and regular `kill`?
A. Regular `kill` (equivalent to `kill -15`) sends SIGTERM, requesting graceful termination and allowing the process to clean up. `kill -9` sends SIGKILL, which forces immediate termination without cleanup and cannot be caught or ignored by the process.

#### Q2. How do I kill a process by name instead of PID?
A. `kill` itself requires PIDs, but you can use `pkill` or `killall` to kill processes by name: `pkill firefox` or `killall firefox`.

#### Q3. Why doesn't `kill -9` work on some processes?
A. Processes in uninterruptible sleep states (usually waiting for I/O) or zombie processes cannot be killed with any signal. Also, processes with PID 1 (init/systemd) handle signals differently.

#### Q4. How can I kill all processes of a specific user?
A. Use `pkill -u username` to kill all processes owned by a specific user.

## References

https://man7.org/linux/man-pages/man1/kill.1.html

## Revisions

- 2025/05/04 First revision