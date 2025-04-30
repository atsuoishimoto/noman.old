# pstack command

Print a stack trace of running processes.

## Overview

`pstack` is a diagnostic tool that displays the execution stack trace of a running process. It helps developers and system administrators debug programs by showing the function calls that led to the current execution point. This command is particularly useful for diagnosing hung or misbehaving processes.

## Options

`pstack` is a simple command that doesn't have many options. It primarily takes a process ID (PID) as its argument.

### **Basic Usage**

Simply provide the PID of the process you want to examine:

```console
$ pstack 1234
```

## Usage Examples

### Examining a specific process

```console
$ pstack 3456
#0  0x00007f8e2d72ead3 in __read_nocancel () from /lib64/libc.so.6
#1  0x00007f8e2c8b89c0 in ?? () from /lib64/libpthread.so.0
#2  0x00000000004e472d in read_packet ()
#3  0x00000000004e2d2c in process_input ()
#4  0x000000000046574c in main ()
```

### Examining multiple processes

```console
$ pstack 3456 7890
==> 3456 <==
#0  0x00007f8e2d72ead3 in __read_nocancel () from /lib64/libc.so.6
#1  0x00007f8e2c8b89c0 in ?? () from /lib64/libpthread.so.0
#2  0x00000000004e472d in read_packet ()
#3  0x00000000004e2d2c in process_input ()
#4  0x000000000046574c in main ()

==> 7890 <==
#0  0x00007f4a3c45e923 in poll () from /lib64/libc.so.6
#1  0x000000000045e2fc in wait_for_event ()
#2  0x000000000040a8e3 in main ()
```

## Tips

### Use with sudo for processes owned by other users

If you need to examine a process owned by another user, you'll need to use `sudo`:

```console
$ sudo pstack 1234
```

### Combine with other diagnostic tools

For comprehensive debugging, use `pstack` alongside other tools like `strace`, `ltrace`, or `gdb` to get a complete picture of what a process is doing.

### Alternative commands

On some systems, `pstack` might not be available. You can use equivalent commands:
- `gdb -p PID -batch -ex "thread apply all bt" -ex "quit"`
- On Linux, you can also check `/proc/PID/stack`

## Frequently Asked Questions

#### Q1. What does a stack trace tell me?
A. A stack trace shows the sequence of function calls that led to the current execution point in a process, helping you understand what the program was doing when it was examined.

#### Q2. Why does my pstack output show question marks or missing function names?
A. This typically happens when debugging information is not available for the binary or its libraries. Programs compiled without debugging symbols will show incomplete information.

#### Q3. Is pstack available on all Unix systems?
A. No, `pstack` is not universally available. It's common on Solaris and some Linux distributions, but may be missing on others. On macOS, similar functionality is available through other tools.

#### Q4. Can pstack affect the running process?
A. `pstack` is generally non-intrusive and doesn't modify the target process, making it safe to use on production systems.

## macOS Considerations

`pstack` is not natively available on macOS. Instead, you can use:

- `sample` command: `sample PID 1 -file /dev/stdout`
- `lldb` (the macOS debugger): `lldb -p PID -o "bt all" -o "quit"`

These alternatives provide similar stack trace information on macOS systems.

## References

https://man7.org/linux/man-pages/man1/pstack.1.html

## Revisions

- 2025/04/30 First revision