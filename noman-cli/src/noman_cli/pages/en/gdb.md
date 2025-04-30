# gdb command

Debug and analyze programs at runtime with the GNU Debugger.

## Overview

GDB (GNU Debugger) is a powerful debugging tool that allows developers to monitor and control the execution of programs. It helps find and fix bugs by letting you pause execution, examine variables, set breakpoints, and step through code line by line. GDB works with many programming languages including C, C++, and Fortran.

## Options

### **-q, --quiet, --silent**

Start GDB in quiet mode, suppressing the introductory and copyright messages

```console
$ gdb -q ./myprogram
(gdb) 
```

### **--args**

Pass command line arguments to the program being debugged

```console
$ gdb --args ./myprogram arg1 arg2
(gdb) run
Starting program: ./myprogram arg1 arg2
```

### **-x FILE**

Execute GDB commands from a file

```console
$ gdb -x commands.gdb ./myprogram
```

### **-c FILE**

Debug a core dump file

```console
$ gdb ./myprogram -c core.dump
```

## Usage Examples

### Basic debugging session

```console
$ gdb ./myprogram
(gdb) break main
Breakpoint 1 at 0x1149: file main.c, line 5.
(gdb) run
Starting program: /path/to/myprogram

Breakpoint 1, main () at main.c:5
5       int x = 10;
(gdb) next
6       printf("x = %d\n", x);
(gdb) print x
$1 = 10
(gdb) continue
Continuing.
x = 10
[Inferior 1 (process 12345) exited normally]
(gdb) quit
```

### Attaching to a running process

```console
$ gdb -p 12345
(gdb) backtrace
#0  0x00007f8b4c5fe4e0 in __read_nocancel () from /lib64/libc.so.6
#1  0x000000000040125c in main () at program.c:15
(gdb) detach
Detaching from program: /path/to/program, process 12345
(gdb) quit
```

## Tips

### Use TUI Mode for a Better Interface

Enable the Text User Interface mode with `tui enable` or start GDB with `gdb -tui`. This splits the screen to show source code alongside the GDB prompt.

### Set Breakpoints on Conditions

Create conditional breakpoints with `break [location] if [condition]`. For example: `break main.c:25 if x > 10` only stops when x exceeds 10.

### Use Watchpoints to Monitor Variables

Set watchpoints with `watch [variable]` to pause execution whenever a variable's value changes, helping identify unexpected modifications.

### Save Common Commands in .gdbinit

Create a `.gdbinit` file in your home directory with frequently used commands. GDB runs these automatically at startup.

### Use Reverse Debugging

If your GDB version supports it, use `record` and then `reverse-step` or `reverse-continue` to move backward through program execution.

## Frequently Asked Questions

#### Q1. How do I print the value of a variable?
A. Use the `print` or `p` command followed by the variable name: `p variable_name`.

#### Q2. How do I set a breakpoint?
A. Use `break` or `b` followed by a function name, line number, or file:line combination: `b main`, `b 42`, or `b file.c:42`.

#### Q3. How do I step through my program?
A. Use `next` (or `n`) to execute the current line and stop at the next line. Use `step` (or `s`) to step into function calls.

#### Q4. How do I examine memory?
A. Use `x` command with format and address: `x/10x &variable` shows 10 memory locations in hex format.

#### Q5. How do I run my program with arguments?
A. Use `run arg1 arg2` or start GDB with `gdb --args ./program arg1 arg2`.

## References

https://sourceware.org/gdb/current/onlinedocs/gdb/

## Revisions

- 2025/04/30 First revision