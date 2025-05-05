# pstack command

Print a stack trace of running processes.

## Overview

`pstack` is a utility that attaches to a running process and prints a stack trace of all threads in that process. It's useful for debugging programs, especially when they're hung or consuming excessive resources, as it shows what functions are currently being executed.

## Options

`pstack` is a simple command that doesn't have many options. It primarily takes a process ID (PID) as its argument.

### **Basic Usage**

```console
$ pstack PID
```

Where `PID` is the process ID of the target process.

## Usage Examples

### Examining a running process

```console
$ pstack 1234
Thread 1 (process 1234):
#0  0x00007f8e2e2b7550 in poll () from /lib64/libc.so.6
#1  0x00007f8e2d8c3432 in ?? () from /lib64/libpthread.so.0
#2  0x000055c6a12b4e6a in main () at myprogram.c:42
```

### Examining multiple processes

```console
$ pstack 1234 5678
==> 1234 <==
Thread 1 (process 1234):
#0  0x00007f8e2e2b7550 in poll () from /lib64/libc.so.6
#1  0x00007f8e2d8c3432 in ?? () from /lib64/libpthread.so.0
#2  0x000055c6a12b4e6a in main () at myprogram.c:42

==> 5678 <==
Thread 1 (process 5678):
#0  0x00007f8e2e2b7550 in read () from /lib64/libc.so.6
#1  0x000055c6a12b4e6a in process_data () at otherprogram.c:123
#2  0x000055c6a12b4f2b in main () at otherprogram.c:45
```

## Tips

### Root Privileges May Be Required

You might need root privileges to examine processes that don't belong to your user. Use `sudo pstack PID` in such cases.

### Alternative Commands

On some systems, `pstack` might not be available. You can use `gdb -p PID -ex "thread apply all bt" -ex "quit"` as an alternative.

### Combine with Other Diagnostic Tools

Use `pstack` alongside other diagnostic tools like `top`, `ps`, and `strace` for comprehensive debugging.

### Finding Process IDs

Use `ps aux | grep program_name` to find the PID of a specific program before using `pstack`.

## Frequently Asked Questions

#### Q1. What does `pstack` actually do?
A. `pstack` attaches to a running process and uses debugging information to generate a stack trace showing the call hierarchy of functions currently being executed in each thread.

#### Q2. Why does `pstack` show "??" for some function names?
A. This typically happens when debugging symbols are missing. The program may have been compiled without debug information, or the symbols might be in a separate file that `pstack` can't locate.

#### Q3. Can I use `pstack` on any process?
A. You can use `pstack` on any process for which you have appropriate permissions. Typically, you can examine your own processes, but you'll need root privileges to examine processes owned by other users.

#### Q4. Is `pstack` available on all Unix systems?
A. No, `pstack` is not a standard Unix utility. It's commonly found on Linux systems, particularly those derived from Red Hat. On other systems, you might need to use alternatives like `gdb` commands.

## References

https://man7.org/linux/man-pages/man1/pstack.1.html

## Revisions

2025/05/04 First revision