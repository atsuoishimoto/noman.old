# top command

Display and update sorted information about processes.

## Overview

`top` is a real-time system monitoring program that displays a continuously updated list of processes. It shows CPU usage, memory consumption, running time, and other process-related information. The display refreshes periodically, allowing users to monitor system performance and identify resource-intensive processes.

## Options

### **-o field**

Sort the process list according to the specified field.

```console
$ top -o cpu
Processes: 383 total, 2 running, 381 sleeping, 1763 threads            23:15:30
Load Avg: 1.83, 1.91, 1.87  CPU usage: 9.25% user, 5.37% sys, 85.37% idle
SharedLibs: 269M resident, 46M data, 16M linkedit.
MemRegions: 95609 total, 1966M resident, 70M private, 1004M shared.
PhysMem: 8192M used (1995M wired), 24M unused.
VM: 2229G vsize, 1798M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 2778/430K in, 2778/430K out.
Disks: 0/0B read, 0/0B written.

PID    COMMAND      %CPU TIME     #TH   #WQ  #PORT MEM    PURG   CMPRS  PGRP
86753  Google Chrome 25.0 00:42.31 15    1    165   264M   0B     0B     86753
```

### **-u username**

Display only processes owned by the specified user.

```console
$ top -u john
Processes: 27 total, 2 running, 25 sleeping, 162 threads               23:16:45
Load Avg: 1.75, 1.88, 1.86  CPU usage: 8.12% user, 4.25% sys, 87.62% idle
SharedLibs: 269M resident, 46M data, 16M linkedit.
MemRegions: 8562 total, 412M resident, 22M private, 104M shared.
PhysMem: 7892M used (1895M wired), 324M unused.
VM: 1229G vsize, 798M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 278/43K in, 278/43K out.
Disks: 0/0B read, 0/0B written.

PID    COMMAND      %CPU TIME     #TH   #WQ  #PORT MEM    PURG   CMPRS  PGRP
12345  firefox      12.0 01:23.45 8     2    78    156M   0B     0B     12345
```

### **-n number**

Set the maximum number of processes to display.

```console
$ top -n 5
Processes: 383 total, 2 running, 381 sleeping, 1763 threads            23:18:10
Load Avg: 1.80, 1.85, 1.85  CPU usage: 8.75% user, 5.12% sys, 86.13% idle
SharedLibs: 269M resident, 46M data, 16M linkedit.
MemRegions: 95609 total, 1966M resident, 70M private, 1004M shared.
PhysMem: 8192M used (1995M wired), 24M unused.
VM: 2229G vsize, 1798M framework vsize, 0(0) swapins, 0(0) swapouts.
Networks: packets: 2778/430K in, 2778/430K out.
Disks: 0/0B read, 0/0B written.

PID    COMMAND      %CPU TIME     #TH   #WQ  #PORT MEM    PURG   CMPRS  PGRP
86753  Google Chrome 25.0 00:42.31 15    1    165   264M   0B     0B     86753
1234   WindowServer  15.2 12:45.67 12    3    342   312M   0B     0B     1234
5678   kernel_task   10.5 35:12.89 120   0    0     128M   0B     0B     0
9012   Finder        8.3  02:34.56 8     2    256   186M   0B     0B     9012
3456   Safari        7.1  01:23.45 25    4    198   275M   0B     0B     3456
```

## Usage Examples

### Interactive Mode Commands

While top is running, you can use these keyboard commands:

```console
$ top
# Press 'q' to quit
# Press 'o' and type a field name to change sort order
# Press 'k' followed by PID to kill a process
# Press 'h' or '?' for help
```

### Displaying Processes with Specific Sorting and Refresh Rate

```console
$ top -o mem -s 5
# Sorts processes by memory usage and refreshes every 5 seconds
```

### Running Top in Batch Mode

```console
$ top -l 3 -n 10 > system_snapshot.txt
# Captures 3 iterations of the top 10 processes and saves to a file
```

## Tips

### Changing Sort Order on the Fly

Press 'o' while top is running, then type the field name (like 'cpu', 'mem', 'time') to instantly change the sort order without restarting the command.

### Monitoring Specific Processes

Use `top -pid PID1,PID2,PID3` to monitor only specific processes of interest, which helps focus on particular applications.

### Understanding Memory Columns

In top's output, 'MEM' shows physical memory usage, while 'VIRT' (or similar column depending on OS) shows virtual memory allocation. Focus on physical memory (MEM) for actual resource usage.

### macOS Specific Information

On macOS, top shows additional columns like PURG (purgeable memory) and CMPRS (compressed memory) that aren't present in other Unix variants. The memory reporting also differs slightly from Linux versions.

## Frequently Asked Questions

#### Q1. How do I exit the top command?
A. Press the 'q' key to quit top.

#### Q2. How can I change how frequently top updates?
A. Use the -s option followed by the number of seconds (e.g., `top -s 10` for 10-second updates) or press 's' while top is running.

#### Q3. How do I kill a process from within top?
A. Press 'k', then enter the PID of the process you want to terminate.

#### Q4. Why does top show different information on macOS compared to Linux?
A. macOS and Linux versions of top have different implementations with varying columns and metrics. macOS top focuses on additional memory statistics like compressed memory that aren't present in Linux.

## References

https://ss64.com/osx/top.html

## Revisions

- 2025/04/30 First revision