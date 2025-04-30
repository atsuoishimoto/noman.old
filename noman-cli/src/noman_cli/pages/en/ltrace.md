# ltrace command

Trace library calls made by a program, showing function calls, arguments, and return values.

## Overview

`ltrace` is a debugging utility that intercepts and records dynamic library calls made by a program, as well as signals received by the program. It's particularly useful for understanding how a program interacts with libraries, troubleshooting issues, or reverse engineering applications when source code is unavailable.

## Options

### **-c**

Count and summarize all function calls

```console
$ ltrace -c ls
% time     seconds  usecs/call     calls      function
------ ----------- ----------- --------- --------------------
 24.45    0.000212          30         7 malloc
 15.67    0.000136          22         6 strlen
 11.53    0.000100          16         6 __ctype_b_loc
  9.94    0.000086          14         6 __cxa_atexit
  8.92    0.000077          15         5 free
  [...]
```

### **-f**

Trace child processes as they are created by the currently traced process

```console
$ ltrace -f ./program
[pid 12345] malloc(32)                                  = 0x55d45e9a12a0
[pid 12345] fork()                                      = 12346
[pid 12346] malloc(64)                                  = 0x55d45e9a1340
[pid 12345] waitpid(12346, 0x7ffd8a7b5a9c, 0)           = 12346
```

### **-e PATTERN**

Filter which library calls to trace using a pattern

```console
$ ltrace -e malloc+free ls
ls->malloc(32)                                         = 0x55d45e9a12a0
ls->malloc(64)                                         = 0x55d45e9a1340
ls->free(0x55d45e9a12a0)                               = <void>
ls->free(0x55d45e9a1340)                               = <void>
```

### **-p PID**

Attach to a running process with the specified PID

```console
$ ltrace -p 1234
[pid 1234] read(5, "data", 1024)                       = 4
[pid 1234] write(1, "data\n", 5)                       = 5
```

### **-S**

Display system calls as well as library calls

```console
$ ltrace -S ls
SYS_brk(0)                                             = 0x55d45e9a1000
SYS_access("/etc/ld.so.preload", 04)                   = -2
ls->malloc(32)                                         = 0x55d45e9a12a0
SYS_write(1, "file.txt\n", 9)                          = 9
```

## Usage Examples

### Tracing a specific program

```console
$ ltrace ./myprogram
myprogram->printf("Hello, world!\n")                   = 14
myprogram->malloc(1024)                                = 0x55d45e9a12a0
myprogram->free(0x55d45e9a12a0)                        = <void>
myprogram->exit(0)                                     = <no return>
```

### Limiting output depth

```console
$ ltrace -L 3 ./myprogram
myprogram->printf("Hello, world!\n") = 14
  -> puts("Hello, world!") = 14
    -> strlen("Hello, world!") = 13
      -> ... <deeper calls not shown>
```

### Saving trace output to a file

```console
$ ltrace -o trace.log ./myprogram
$ cat trace.log
printf("Hello, world!\n")                              = 14
malloc(1024)                                           = 0x55d45e9a12a0
free(0x55d45e9a12a0)                                   = <void>
exit(0)                                                = <no return>
```

## Tips

### Filter Noisy Functions

Use `-e` to filter out noisy functions that aren't relevant to your debugging:
```console
$ ltrace -e '!__cxa_*' ./myprogram
```

### Increase String Length

By default, ltrace truncates string arguments. Use `-s` to increase the displayed length:
```console
$ ltrace -s 100 ./myprogram
```

### Combine with strace

For comprehensive debugging, use both `ltrace` for library calls and `strace` for system calls:
```console
$ ltrace -S ./myprogram
```

### Demangle C++ Names

Use `-C` to demangle C++ function names for better readability when tracing C++ programs.

## Frequently Asked Questions

#### Q1. What's the difference between ltrace and strace?
A. `ltrace` traces library calls (functions from shared libraries), while `strace` traces system calls (interactions with the kernel). `ltrace` is better for understanding application logic, while `strace` is better for understanding OS interactions.

#### Q2. Why doesn't ltrace show all function calls?
A. `ltrace` only shows calls to external libraries, not internal function calls within the program itself. It also can't trace statically linked libraries.

#### Q3. Can ltrace affect program performance?
A. Yes, tracing adds significant overhead. Programs run much slower when being traced, so performance measurements under `ltrace` are not representative of normal execution.

#### Q4. How do I trace a specific set of functions?
A. Use the `-e` option with a pattern: `ltrace -e malloc+free+open ./program` to trace only malloc, free, and open calls.

## References

https://man7.org/linux/man-pages/man1/ltrace.1.html

## Revisions

- 2025/04/30 First revision