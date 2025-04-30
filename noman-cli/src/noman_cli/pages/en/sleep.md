# sleep command

Suspends execution for a specified amount of time.

## Overview

The `sleep` command pauses the execution of a script or command line for a specified duration. It's commonly used in shell scripts to introduce delays between commands, wait for processes to complete, or create timed intervals for repeated tasks.

## Options

### **Duration**

Specify how long to pause execution. By default, the duration is in seconds, but you can use suffixes to specify other units.

```console
$ sleep 5
```
This command pauses execution for 5 seconds.

### **Time Suffixes**

You can use suffixes to specify different time units:
- `s` for seconds (default)
- `m` for minutes
- `h` for hours
- `d` for days

```console
$ sleep 2m
```
This pauses execution for 2 minutes.

## Usage Examples

### Basic delay in a script

```console
$ echo "Starting task..."
Starting task...
$ sleep 3
$ echo "Task resumed after 3 seconds"
Task resumed after 3 seconds
```

### Using multiple time units together

```console
$ sleep 1h 30m 45s
```
This will pause for 1 hour, 30 minutes, and 45 seconds.

### Creating a countdown timer

```console
$ for i in {10..1}; do echo $i; sleep 1; done; echo "Time's up!"
10
9
8
...
1
Time's up!
```

## Tips:

### Interrupt a sleep command

You can interrupt a sleep command by pressing Ctrl+C. This is useful when you've started a long sleep and need to cancel it.

### Use with watch command

Combine with the `watch` command to periodically run a command: `watch -n 5 command` is equivalent to running a command every 5 seconds.

### Fractional sleep times

Most modern versions of sleep support fractional times like `sleep 0.5` for half a second, useful for more precise timing.

## Frequently Asked Questions

#### Q1. Can sleep accept decimal values?
A. Yes, most modern implementations of `sleep` accept decimal values like `sleep 0.5` for half a second.

#### Q2. How accurate is the sleep command?
A. While generally reliable, `sleep` may not be perfectly precise for very short durations (milliseconds) due to system scheduling and load.

#### Q3. Can I combine different time units?
A. Yes, you can combine units like `sleep 1h 30m 15s` to specify hours, minutes, and seconds together.

#### Q4. Does sleep consume significant system resources?
A. No, `sleep` is very lightweight and uses minimal CPU while waiting.

## References

https://www.gnu.org/software/coreutils/manual/html_node/sleep-invocation.html

## Revisions

- 2025/04/30 First revision