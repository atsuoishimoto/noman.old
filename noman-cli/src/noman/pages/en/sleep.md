# sleep command

Suspends execution for a specified amount of time.

## Overview

The `sleep` command pauses the execution of a script or command line for a specified duration. It's commonly used in shell scripts to introduce delays between commands, wait for resources to become available, or create timed operations.

## Options

### **-s, --suffix=SUFFIX**

Specifies the unit of time (s for seconds, m for minutes, h for hours, d for days).

```console
$ sleep 5s
[pauses for 5 seconds]
```

### **--help**

Displays help information and exits.

```console
$ sleep --help
Usage: sleep NUMBER[SUFFIX]...
  or:  sleep OPTION
Pause for NUMBER seconds.  SUFFIX may be 's' for seconds (the default),
'm' for minutes, 'h' for hours or 'd' for days.  NUMBER may be an
arbitrary floating point number.  Given two or more arguments, pause for
the sum of their values.

      --help     display this help and exit
      --version  output version information and exit
```

### **--version**

Outputs version information and exits.

```console
$ sleep --version
sleep (GNU coreutils) 9.0
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Jim Meyering and Paul Eggert.
```

## Usage Examples

### Basic usage

```console
$ sleep 5
[pauses for 5 seconds]
```

### Using different time units

```console
$ sleep 1m
[pauses for 1 minute]

$ sleep 2h
[pauses for 2 hours]

$ sleep 1d
[pauses for 1 day]
```

### Using decimal values

```console
$ sleep 0.5
[pauses for half a second]
```

### Combining multiple values

```console
$ sleep 1m 30s
[pauses for 1 minute and 30 seconds]
```

### Using in a script

```console
$ echo "Starting task..."
Starting task...
$ sleep 2
$ echo "Task completed after 2 seconds"
Task completed after 2 seconds
```

## Tips

### Interrupt a Sleep Command

You can interrupt a running sleep command by pressing Ctrl+C.

### Background Sleep

Run sleep in the background with `&` to continue using the terminal:
```console
$ sleep 60 &
[1] 12345
```

### Combine with Other Commands

Use sleep with other commands to create timed operations:
```console
$ (sleep 5; echo "Message after 5 seconds") &
```

### Use in Loops

Sleep is useful in loops to prevent excessive resource usage:
```console
$ for i in {1..5}; do echo "Iteration $i"; sleep 1; done
Iteration 1
Iteration 2
Iteration 3
Iteration 4
Iteration 5
```

## Frequently Asked Questions

#### Q1. What happens if I don't specify a unit?
A. If no unit is specified, sleep uses seconds as the default unit.

#### Q2. Can I use decimal values with sleep?
A. Yes, sleep accepts decimal values like `0.5` for half a second.

#### Q3. How do I make a script wait for a specific time?
A. Use sleep with the appropriate time value, e.g., `sleep 10m` to wait for 10 minutes.

#### Q4. Can I combine different time units?
A. Yes, you can provide multiple arguments that will be added together, e.g., `sleep 1h 30m` for 1.5 hours.

#### Q5. Does sleep consume a lot of system resources?
A. No, sleep is very lightweight and uses minimal CPU resources while waiting.

## References

https://www.gnu.org/software/coreutils/manual/html_node/sleep-invocation.html

## Revisions

- 2025/05/04 First revision