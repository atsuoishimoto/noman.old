# ltrace command

Trace library calls of a program.

## Overview

`ltrace` is a debugging utility that displays dynamic library calls made by a program. It can also show system calls and signals received by the process. This tool is particularly useful for debugging programs when source code is unavailable or for understanding how a program interacts with libraries.

## Options

### **-c, --count**

Count time and calls for each library call and report a summary at the end.

```console
$ ltrace -c ls
% time     seconds  usecs/call     calls      function
------ ----------- ----------- --------- --------------------
 21.05    0.000080          2        40 strlen
 15.79    0.000060          2        30 __ctype_b_loc
 10.53    0.000040          2        20 readdir64
  7.89    0.000030          2        15 fwrite
  5.26    0.000020          2        10 malloc
  5.26    0.000020          2        10 free
  5.26    0.000020          2        10 __errno_location
  5.26    0.000020          2        10 __cxa_atexit
  5.26    0.000020         20         1 opendir
  5.26    0.000020         20         1 closedir
  5.26    0.000020         20         1 setlocale
  5.26    0.000020         20         1 isatty
  2.63    0.000010         10         1 bindtextdomain
------ ----------- ----------- --------- --------------------
100.00    0.000380                   150 total
```

### **-f, --follow**

Trace child processes as they are created by the currently traced process.

```console
$ ltrace -f ./program
[pid 12345] malloc(32)                                  = 0x55d7e9fa7260
[pid 12345] fork()                                      = 12346
[pid 12346] malloc(64)                                  = 0x55d7e9fa7290
```

### **-e, --expr=EXPR**

Specify the library calls to trace or filter. Format is [!][?][=][%][/@][+|-]pattern[@arch][:function].

```console
$ ltrace -e malloc+free ls
ls->malloc(32)                                          = 0x55d7e9fa7260
ls->malloc(64)                                          = 0x55d7e9fa7290
ls->free(0x55d7e9fa7260)                                = <void>
ls->free(0x55d7e9fa7290)                                = <void>
```

### **-p, --pid=PID**

Attach to the process with the specified PID and begin tracing.

```console
$ ltrace -p 1234
[pid 1234] read(5, "data", 1024)                        = 4
[pid 1234] write(1, "output", 6)                        = 6
```

### **-S, --summary**

Display a summary of library call usage at the end of the trace.

```console
$ ltrace -S ls
ls->__libc_start_main(0x401670, 1, 0x7ffd2d121768, 0x4017a0 <unfinished ...>
...
+++ exited (status 0) +++
% time     seconds  usecs/call     calls      function
------ ----------- ----------- --------- --------------------
 21.05    0.000080          2        40 strlen
 15.79    0.000060          2        30 __ctype_b_loc
 10.53    0.000040          2        20 readdir64
```

### **-o, --output=FILE**

Write the trace output to FILE instead of stderr.

```console
$ ltrace -o trace.log ls
$ cat trace.log
ls->__libc_start_main(0x401670, 1, 0x7ffd2d121768, 0x4017a0 <unfinished ...>
ls->setlocale(6, "")                                    = "en_US.UTF-8"
ls->bindtextdomain("coreutils", "/usr/share/locale")    = "/usr/share/locale"
```

## Usage Examples

### Basic Usage

```console
$ ltrace ls
ls->__libc_start_main(0x401670, 1, 0x7ffd2d121768, 0x4017a0 <unfinished ...>
ls->setlocale(6, "")                                    = "en_US.UTF-8"
ls->bindtextdomain("coreutils", "/usr/share/locale")    = "/usr/share/locale"
ls->textdomain("coreutils")                             = "coreutils"
ls->__cxa_atexit(0x4014a0, 0, 0, 0x736c6974)            = 0
ls->getenv("QUOTING_STYLE")                             = nil
...
+++ exited (status 0) +++
```

### Tracing Specific Library Calls

```console
$ ltrace -e malloc+free+open ./program
./program->malloc(1024)                                 = 0x55d7e9fa7260
./program->open("/etc/passwd", 0, 0)                    = 3
./program->malloc(2048)                                 = 0x55d7e9fa7660
./program->free(0x55d7e9fa7260)                         = <void>
./program->free(0x55d7e9fa7660)                         = <void>
```

### Tracing with Time Information

```console
$ ltrace -tt ./program
15:30:45.123456 __libc_start_main(0x401670, 1, 0x7ffd2d121768, 0x4017a0 <unfinished ...>
15:30:45.123789 setlocale(6, "")                        = "en_US.UTF-8"
15:30:45.124012 malloc(1024)                            = 0x55d7e9fa7260
15:30:45.124234 free(0x55d7e9fa7260)                    = <void>
```

## Tips

### Filter Out Noise

Use the `-e` option to focus on specific function calls you're interested in. This helps reduce the output volume and makes analysis easier.

### Combine with strace

For comprehensive debugging, use both `ltrace` for library calls and `strace` for system calls. This provides a complete picture of program behavior.

### Redirect Output for Analysis

For complex programs, redirect output to a file with `-o` and then use tools like `grep` or `awk` to analyze the trace data.

### Use with Core Dumps

When debugging crashes, run the program with `ltrace` to see which library calls were made before the crash occurred.

## Frequently Asked Questions

#### Q1. What's the difference between ltrace and strace?
A. `ltrace` traces library calls (functions in shared libraries like libc), while `strace` traces system calls (direct kernel interactions). `ltrace` shows higher-level operations like `printf()`, while `strace` shows lower-level operations like `write()`.

#### Q2. Can ltrace slow down the traced program?
A. Yes, tracing adds significant overhead. Each intercepted call requires context switches, which can slow down the program considerably, especially for programs making many library calls.

#### Q3. How do I trace only specific library functions?
A. Use the `-e` option with a pattern, for example: `ltrace -e malloc+free+fopen ./program` to trace only memory allocation and file operations.

#### Q4. Can ltrace trace statically linked programs?
A. No, `ltrace` primarily works with dynamically linked programs. For statically linked programs, the library calls are compiled into the executable and not made through the dynamic linker.

## References

https://man7.org/linux/man-pages/man1/ltrace.1.html

## Revisions

- 2025/05/04 First revision