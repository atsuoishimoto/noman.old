# strace command

Trace system calls and signals made by a process.

## Overview

`strace` is a diagnostic and debugging tool for Linux that monitors the system calls and signals of a specified program. It intercepts and records the system calls made by a process and the signals received by the process. This tool is invaluable for troubleshooting issues, understanding how programs interact with the operating system, and analyzing performance problems.

## Options

### **-f, --follow-forks**

Trace child processes as they are created by currently traced processes.

```console
$ strace -f ./my_program
[pid 12345] execve("./my_program", ["./my_program"], 0x7ffc123456) = 0
[pid 12345] brk(NULL)                  = 0x55555555
[pid 12345] clone(...)                 = 12346
[pid 12346] open("file.txt", O_RDONLY) = 3
```

### **-o, --output=FILE**

Write the trace output to FILE instead of stderr.

```console
$ strace -o trace.log ls
$ cat trace.log
execve("/bin/ls", ["ls"], 0x7ffc123456) = 0
brk(NULL)                               = 0x55555555
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT
```

### **-p, --attach=PID**

Attach to the process with the specified PID and begin tracing.

```console
$ strace -p 1234
Process 1234 attached
read(3, "Hello World", 1024)            = 11
write(1, "Hello World", 11)             = 11
```

### **-e, --expr=EXPR**

A qualifier to specify which events to trace or how to trace them.

```console
$ strace -e open,close ls
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
close(3)                                = 0
open("/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
close(3)                                = 0
```

### **-c, --summary-only**

Count time, calls, and errors for each system call and report a summary.

```console
$ strace -c ls
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
 25.91    0.000091          5        18           mmap
 17.66    0.000062          6        10           openat
 11.08    0.000039          3        12           close
  9.12    0.000032          5         6           read
  8.83    0.000031          5         6           fstat
  ...
------ ----------- ----------- --------- --------- ----------------
100.00    0.000351                   98         5 total
```

### **-t, --relative-timestamps**

Prefix each line of output with the time of day.

```console
$ strace -t ls
14:15:32 execve("/bin/ls", ["ls"], 0x7ffc123456) = 0
14:15:32 brk(NULL)                      = 0x55555555
14:15:32 access("/etc/ld.so.preload", R_OK) = -1 ENOENT
```

## Usage Examples

### Tracing a program from start to finish

```console
$ strace ls -l
execve("/bin/ls", ["ls", "-l"], 0x7ffc123456) = 0
brk(NULL)                               = 0x55555555
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT
...
write(1, "total 20\n-rw-r--r-- 1 user user...", 612) = 612
exit_group(0)                           = ?
+++ exited with 0 +++
```

### Tracing specific system calls

```console
$ strace -e trace=open,read,write echo "Hello World"
execve("/bin/echo", ["echo", "Hello World"], 0x7ffc123456) = 0
write(1, "Hello World\n", 12)           = 12
+++ exited with 0 +++
```

### Analyzing file access patterns

```console
$ strace -e trace=file ls
execve("/bin/ls", ["ls"], 0x7ffc123456) = 0
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
stat(".", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
+++ exited with 0 +++
```

## Tips

### Filter Noise with Specific Syscalls

When debugging, focus on relevant system calls using `-e trace=` followed by the syscall names. For example, use `strace -e trace=open,read,write` to only see file operations.

### Redirect Output to a File

For long-running processes, redirect output to a file with `-o filename.log` to avoid cluttering your terminal and to allow for later analysis.

### Trace Running Processes

You can attach to an already running process using `-p PID`. This is useful when a program is already experiencing issues and you don't want to restart it.

### Measure System Call Time

Use `-T` to show the time spent in each system call, which helps identify performance bottlenecks.

### Trace Network Activity

Use `-e trace=network` to focus on network-related system calls, which is useful for debugging connectivity issues.

## Frequently Asked Questions

#### Q1. What's the difference between strace and ltrace?
A. `strace` traces system calls (interactions between programs and the kernel), while `ltrace` traces library calls (interactions between programs and libraries).

#### Q2. How can I reduce the verbosity of strace output?
A. Use `-e trace=` to specify only the system calls you're interested in, or use `-c` to get a summary count instead of detailed output.

#### Q3. Can strace slow down the traced program?
A. Yes, `strace` adds significant overhead as it intercepts every system call. For performance-sensitive applications, use it sparingly or with specific filters.

#### Q4. How do I trace a program that creates child processes?
A. Use the `-f` option to follow forks and trace child processes as well.

#### Q5. Can I use strace on macOS?
A. No, `strace` is specific to Linux. On macOS, you can use `dtruss` or `dtrace` for similar functionality, though they require root privileges.

## References

https://man7.org/linux/man-pages/man1/strace.1.html

## Revisions

2025/05/04 First revision