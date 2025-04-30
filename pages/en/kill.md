# kill command

Terminate or send signals to processes.

## Overview

The `kill` command sends signals to processes, most commonly used to terminate unwanted or unresponsive programs. While its name suggests termination, `kill` can actually send various signals to control process behavior, including pausing, resuming, or requesting graceful shutdown.

## Options

### **-l (List signals)**

Displays all available signals that can be sent to processes.

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

### **-s (Specify signal)**

Sends a specific signal to a process by name instead of number.

```console
$ kill -s TERM 1234
```

### **-9 (SIGKILL)**

Forcefully terminates a process without allowing it to clean up.

```console
$ kill -9 1234
```

### **-15 (SIGTERM)**

Gracefully terminates a process (this is the default signal).

```console
$ kill -15 1234
```

## Usage Examples

### Terminating a process by PID

```console
$ kill 1234
```

### Forcefully terminating a stubborn process

```console
$ kill -9 1234
```

### Sending a custom signal

```console
$ kill -s HUP 1234
```

### Terminating multiple processes at once

```console
$ kill 1234 5678 9012
```

## Tips

### Find Process IDs First

Use `ps` or `pgrep` to find the PID before using kill:

```console
$ ps aux | grep firefox
user     1234  2.0  1.5 3521404 124540 ?      Sl   09:30   0:45 /usr/lib/firefox/firefox
$ kill 1234
```

### Use SIGTERM Before SIGKILL

Try using the default signal (SIGTERM, -15) before resorting to SIGKILL (-9). SIGTERM allows the process to clean up resources and exit gracefully.

### Process Groups

You can kill entire process groups by prefixing the PID with a minus sign:

```console
$ kill -15 -1234  # Kills process group 1234
```

### Signals Have Different Effects

Different signals do different things:
- SIGTERM (15): Request graceful termination
- SIGKILL (9): Force immediate termination
- SIGHUP (1): Often used to reload configuration
- SIGSTOP (19): Pause a process
- SIGCONT (18): Resume a paused process

## Frequently Asked Questions

#### Q1. What's the difference between kill, pkill, and killall?
A. `kill` terminates processes by PID, `pkill` by name or other attributes, and `killall` terminates all processes with a given name.

#### Q2. Why doesn't kill -9 work sometimes?
A. Processes in uninterruptible sleep (D state) or zombie processes can't be killed even with SIGKILL. Zombie processes will remain until the parent process handles them.

#### Q3. How do I kill a process by name instead of PID?
A. Use `pkill` or `killall` instead: `pkill firefox` or `killall firefox`.

#### Q4. What signal does kill send by default?
A. SIGTERM (signal 15), which requests graceful termination.

## References

https://www.gnu.org/software/coreutils/manual/html_node/kill-invocation.html

## Revisions

- 2025/04/30 First revision