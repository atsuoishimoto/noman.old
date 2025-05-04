# vmstat command

Report virtual memory statistics, providing information about system processes, memory, paging, block I/O, traps, and CPU activity.

## Overview

`vmstat` (virtual memory statistics) displays information about system memory, processes, interrupts, paging, block I/O, and CPU utilization. It's particularly useful for monitoring system performance and identifying bottlenecks. The command can provide a snapshot of current system state or continuous monitoring with specified intervals.

## Options

### **-a, --active**

Display active and inactive memory

```console
$ vmstat -a
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free  inact active   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 6291456 1048576 2097152    0    0     0     2    9   10  1  1 98  0  0
```

### **-d, --disk**

Report disk statistics

```console
$ vmstat -d
disk- ------------reads------------ ------------writes----------- -----IO------
       total merged sectors      ms  total merged sectors      ms    cur    sec
sda    12687   2713  972490   13002  15748  23182  313544   62692      0     19
sdb     1044      0   33512     708   2106      0   16848     308      0      0
```

### **-s, --stats**

Display a table of various event counters and memory statistics

```console
$ vmstat -s
      8167848 K total memory
      1872016 K used memory
      1224268 K active memory
       525148 K inactive memory
      6295832 K free memory
       226748 K buffer memory
      1654304 K swap cache
      8388604 K total swap
            0 K used swap
      8388604 K free swap
        24818 non-nice user cpu ticks
          226 nice user cpu ticks
        18911 system cpu ticks
      2137707 idle cpu ticks
         2660 IO-wait cpu ticks
            0 IRQ cpu ticks
         1367 softirq cpu ticks
            0 stolen cpu ticks
       772844 pages paged in
      1492454 pages paged out
            0 pages swapped in
            0 pages swapped out
      2838484 interrupts
      6547301 CPU context switches
   1588876743 boot time
        16793 forks
```

### **-t, --timestamp**

Append timestamp to each line

```console
$ vmstat -t 1 3
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu----- -----timestamp-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st                 EDT
 0  0      0 6295832 226748 1654304    0    0     0     2    9   10  1  1 98  0  0 2025-05-04 10:15:01
 0  0      0 6295832 226748 1654304    0    0     0     0  104  168  0  0 100  0  0 2025-05-04 10:15:02
 0  0      0 6295832 226748 1654304    0    0     0     0  104  167  0  0 100  0  0 2025-05-04 10:15:03
```

### **-S, --unit [k|K|m|M]**

Switch output between 1000 (k), 1024 (K), 1000000 (m), or 1048576 (M) bytes

```console
$ vmstat -S M
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      0   6002    216   1578    0    0     0     2    9   10  1  1 98  0  0
```

## Usage Examples

### Basic usage with interval and count

```console
$ vmstat 2 5
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 6295832 226748 1654304    0    0     0     2    9   10  1  1 98  0  0
 0  0      0 6295832 226748 1654304    0    0     0     0  104  168  0  0 100  0  0
 0  0      0 6295832 226748 1654304    0    0     0     0  103  166  0  0 100  0  0
 0  0      0 6295832 226748 1654304    0    0     0     0  105  169  0  0 100  0  0
 0  0      0 6295832 226748 1654304    0    0     0    12  106  171  0  0 100  0  0
```

### Monitoring disk activity

```console
$ vmstat -d 1 3
disk- ------------reads------------ ------------writes----------- -----IO------
       total merged sectors      ms  total merged sectors      ms    cur    sec
sda    12687   2713  972490   13002  15748  23182  313544   62692      0     19
sdb     1044      0   33512     708   2106      0   16848     308      0      0

disk- ------------reads------------ ------------writes----------- -----IO------
       total merged sectors      ms  total merged sectors      ms    cur    sec
sda    12687   2713  972490   13002  15748  23182  313544   62692      0     19
sdb     1044      0   33512     708   2106      0   16848     308      0      0

disk- ------------reads------------ ------------writes----------- -----IO------
       total merged sectors      ms  total merged sectors      ms    cur    sec
sda    12687   2713  972490   13002  15749  23182  313552   62692      0     19
sdb     1044      0   33512     708   2106      0   16848     308      0      0
```

### Displaying memory statistics

```console
$ vmstat -s | grep memory
      8167848 K total memory
      1872016 K used memory
      1224268 K active memory
       525148 K inactive memory
      6295832 K free memory
       226748 K buffer memory
```

## Tips

### Understanding the Output Fields

- **procs**: 'r' shows runnable processes (running or waiting for run time), 'b' shows processes in uninterruptible sleep
- **memory**: 'swpd' is virtual memory used, 'free' is idle memory, 'buff' is memory used as buffers, 'cache' is memory used as cache
- **swap**: 'si' is memory swapped in from disk, 'so' is memory swapped to disk
- **io**: 'bi' is blocks received from a block device, 'bo' is blocks sent to a block device
- **system**: 'in' is the number of interrupts per second, 'cs' is the number of context switches per second
- **cpu**: percentages of total CPU time in user mode ('us'), system mode ('sy'), idle ('id'), waiting for I/O ('wa'), and stolen from a virtual machine ('st')

### First Line vs. Subsequent Lines

The first line of output shows averages since the last reboot, while subsequent lines show information for the sampling period. Always look at the second line onward for current statistics.

### Identifying Memory Bottlenecks

High 'si' and 'so' values indicate excessive swapping, which suggests your system needs more RAM or memory usage optimization.

### Detecting I/O Problems

High 'wa' (I/O wait) percentages in the CPU section indicate that your system is spending too much time waiting for disk operations to complete.

## Frequently Asked Questions

#### Q1. What does the 'r' column in vmstat output mean?
A. The 'r' column shows the number of processes waiting for run time. High numbers (greater than the number of CPU cores) indicate CPU contention.

#### Q2. How can I monitor memory usage with vmstat?
A. Use `vmstat -s` to see detailed memory statistics or `vmstat -a` to see active/inactive memory. For continuous monitoring, add an interval: `vmstat 5`.

#### Q3. What's the difference between buffer and cache memory?
A. Buffer memory ('buff') is used for disk block operations, while cache memory ('cache') is used for file system data. Both can be reclaimed when applications need memory.

#### Q4. How do I interpret high 'wa' (I/O wait) values?
A. High I/O wait percentages (over 10%) indicate that your CPU is waiting for disk operations to complete. This suggests disk I/O bottlenecks that might be resolved with faster storage or I/O optimization.

## References

https://man7.org/linux/man-pages/man8/vmstat.8.html

## Revisions

- 2025/05/04 First revision