# top command

Display and update sorted information about processes.

## Overview

`top` is a real-time system monitoring program that displays a continuously updated list of processes. It shows system summary information and a list of processes or threads currently managed by the Linux kernel. The display is sorted by CPU usage by default, allowing users to monitor system resource usage and identify processes consuming the most resources.

## Options

### **-d, --delay**

Specifies the delay between screen updates in seconds (can include decimal points)

```console
$ top -d 5
top - 14:22:10 up 3 days,  5:10,  2 users,  load average: 0.15, 0.21, 0.28
Tasks: 213 total,   1 running, 212 sleeping,   0 stopped,   0 zombie
%Cpu(s):  2.3 us,  1.2 sy,  0.0 ni, 96.4 id,  0.0 wa,  0.0 hi,  0.1 si,  0.0 st
MiB Mem :  15895.1 total,   7403.2 free,   3265.4 used,   5226.5 buff/cache
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.  12039.3 avail Mem
...
```

### **-n, --iterations**

Specifies the number of iterations before exiting

```console
$ top -n 3
[top will display 3 updates then exit]
```

### **-p, --pid**

Monitor only the processes with specified process IDs

```console
$ top -p 1234,5678
[displays only processes with PIDs 1234 and 5678]
```

### **-u, --user**

Show only processes owned by the specified user

```console
$ top -u username
[displays only processes owned by 'username']
```

### **-b, --batch**

Run in batch mode (useful for sending output to other programs or files)

```console
$ top -b -n 1 > top_output.txt
[saves one iteration of top output to top_output.txt]
```

## Usage Examples

### Basic Usage

```console
$ top
top - 14:22:10 up 3 days,  5:10,  2 users,  load average: 0.15, 0.21, 0.28
Tasks: 213 total,   1 running, 212 sleeping,   0 stopped,   0 zombie
%Cpu(s):  2.3 us,  1.2 sy,  0.0 ni, 96.4 id,  0.0 wa,  0.0 hi,  0.1 si,  0.0 st
MiB Mem :  15895.1 total,   7403.2 free,   3265.4 used,   5226.5 buff/cache
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.  12039.3 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
 1234 user      20   0 3256892 125232  42348 S   2.0   0.8   5:23.02 firefox
 5678 user      20   0  723964  56892  38212 S   1.3   0.4   2:42.15 terminal
```

### Monitoring Specific Processes with Higher Refresh Rate

```console
$ top -d 0.5 -p 1234,5678
[displays only processes 1234 and 5678, updating every 0.5 seconds]
```

## Interactive Commands

While `top` is running, you can use these keyboard commands:

- **h or ?**: Display help
- **q**: Quit the program
- **k**: Kill a process (prompts for PID)
- **r**: Renice a process (change priority)
- **f**: Select fields to display
- **o**: Change sort field
- **1**: Toggle display of individual CPU cores
- **m**: Toggle memory display mode
- **t**: Toggle task/CPU display mode
- **c**: Toggle command line/program name display
- **M**: Sort by memory usage
- **P**: Sort by CPU usage (default)
- **T**: Sort by time/cumulative time

## Tips

### Identify Resource-Intensive Processes

Press `P` to sort by CPU usage or `M` to sort by memory usage to quickly identify which processes are consuming the most resources.

### Save Output to a File

Use batch mode with the `-b` option to save the output to a file for later analysis:
```console
$ top -b -n 1 > system_snapshot.txt
```

### Customize the Display

Press `f` while top is running to select which columns to display, allowing you to focus on the metrics that matter most to you.

### Monitor Multiple CPUs

Press `1` to show individual CPU core usage instead of the combined average, which is useful for identifying if a process is maxing out a single core.

## Frequently Asked Questions

#### Q1. How do I exit top?
A. Press the `q` key to quit the program.

#### Q2. How can I kill a process from within top?
A. Press `k`, then enter the PID of the process you want to terminate, followed by the signal number (9 for SIGKILL).

#### Q3. How do I change the refresh rate?
A. Use the `-d` option followed by the number of seconds (e.g., `top -d 3` for 3-second updates), or press `d` while top is running and enter a new delay.

#### Q4. How can I see only processes for a specific user?
A. Use `top -u username` or press `u` while top is running and enter the username.

#### Q5. What do the load average numbers mean?
A. The three numbers represent the system load average over the last 1, 5, and 15 minutes. Values below your CPU core count generally indicate the system isn't overloaded.

## macOS Considerations

On macOS, the `top` command has different options and output format compared to Linux. Some key differences:

- The `-o` option is used to specify the sort field (e.g., `top -o cpu`)
- Memory is displayed in different units
- Some interactive commands differ
- Use `man top` on macOS to see the specific options available

## References

https://man7.org/linux/man-pages/man1/top.1.html

## Revisions

- 2025/05/04 First revision