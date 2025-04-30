# strace command

Trace system calls and signals made by a process.

## Overview

`strace` is a diagnostic and debugging tool that monitors the system calls and signals of a process. It intercepts and records the system calls made by a running process and the signals received by that process, making it invaluable for troubleshooting issues, understanding program behavior, and diagnosing performance problems.

## Options

### **-f**

Trace child processes as they are created by currently traced processes.

```console
$ strace -f ./script.sh
[pid 12345] execve("./script.sh", ["./script.sh"], 0x7ffc8e5b5b50 /* 21 vars */) = 0
[pid 12345] brk(NULL)                  = 0x55a7c1e82000
[pid 12346] clone(child_stack=NULL, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, child_tidptr=0x7f8c9cd29a10) = 12347
```

### **-o file**

Write the trace output to a file instead of stderr.

```console
$ strace -o trace.log ls
$ cat trace.log
execve("/bin/ls", ["ls"], 0x7ffc8e5b5b50 /* 21 vars */) = 0
brk(NULL)                               = 0x55a7c1e82000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT
```

### **-p pid**

Attach to the process with the specified PID and begin tracing.

```console
$ strace -p 1234
strace: Process 1234 attached
read(3, "Hello, world!\n", 4096)        = 14
write(1, "Hello, world!\n", 14)         = 14
```

### **-e expr**

Filter the traced system calls and/or signals. For example, `-e trace=open,read,write` traces only open, read, and write system calls.

```console
$ strace -e trace=open,read,write ls
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\360\25\0\0\0\0\0\0"..., 832) = 832
write(1, "file1.txt  file2.txt  file3.txt\n", 32) = 32
```

### **-c**

Count time, calls, and errors for each system call and report a summary.

```console
$ strace -c ls
file1.txt  file2.txt  file3.txt
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
 25.00    0.000125          21         6           mmap
 20.00    0.000100          25         4           open
 15.00    0.000075          25         3           read
 10.00    0.000050          25         2           write
------ ----------- ----------- --------- --------- ----------------
100.00    0.000500                    42         2 total
```

## Usage Examples

### Tracing a program from start to finish

```console
$ strace ls -l
execve("/bin/ls", ["ls", "-l"], 0x7ffc8e5b5b50 /* 21 vars */) = 0
brk(NULL)                               = 0x55a7c1e82000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
...
```

### Tracing specific system calls in a running process

```console
$ strace -p 1234 -e trace=network
strace: Process 1234 attached
socket(AF_INET, SOCK_STREAM, IPPROTO_TCP) = 3
connect(3, {sa_family=AF_INET, sin_port=htons(80), sin_addr=inet_addr("93.184.216.34")}, 16) = -1 EINPROGRESS
```

### Saving trace output to a file and following child processes

```console
$ strace -f -o mysql_trace.log mysql
$ head mysql_trace.log
12345 execve("/usr/bin/mysql", ["mysql"], 0x7ffc8e5b5b50 /* 21 vars */) = 0
12345 brk(NULL)                         = 0x55a7c1e82000
12345 access("/etc/ld.so.preload", R_OK) = -1 ENOENT
```

## Tips

### Focus on Specific System Calls

When debugging a specific issue, use `-e trace=` to focus on relevant system calls. For example, use `-e trace=file` for file operations or `-e trace=network` for network-related calls.

### Understand Performance Bottlenecks

Use `-c` to get a summary of time spent in each system call, which can help identify performance bottlenecks in your application.

### Reduce Output Verbosity

For large applications, the output can be overwhelming. Use `-e trace=` to filter calls, `-o` to save to a file, and consider `-s` to limit string sizes in the output.

### Attach to Running Processes Carefully

When attaching to production processes with `-p`, be aware that strace adds significant overhead and can slow down the application considerably.

## Frequently Asked Questions

#### Q1. What's the difference between strace and ltrace?
A. `strace` traces system calls (interactions between programs and the kernel), while `ltrace` traces library calls (interactions between programs and libraries).

#### Q2. Can strace affect the performance of the traced program?
A. Yes, strace adds significant overhead to each system call, which can slow down the traced program considerably, especially for I/O-intensive applications.

#### Q3. How can I trace a program that requires root privileges?
A. Run strace with sudo: `sudo strace command`. To attach to a running process owned by root, use `sudo strace -p PID`.

#### Q4. Can strace trace multithreaded applications?
A. Yes, use the `-f` option to follow threads (which are implemented as processes in Linux).

## References

https://man7.org/linux/man-pages/man1/strace.1.html

## Revisions

- 2025/04/30 First revision