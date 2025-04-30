# vmstat command

Report virtual memory statistics, providing information about system processes, memory, paging, block I/O, traps, and CPU activity.

## Overview

`vmstat` (virtual memory statistics) displays information about system memory, processes, interrupts, paging, block I/O, and CPU utilization. It's particularly useful for monitoring system performance and identifying bottlenecks. The command can provide a snapshot of current system state or continuous monitoring with specified intervals.

## Options

### **-a**

Display active and inactive memory statistics

```console
$ vmstat -a
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free  inact active   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 1456892 1026300 1138752    0    0     0     1   88   79  1  0 99  0  0
```

### **-s**

Display a table of various memory and swap statistics

```console
$ vmstat -s
      4046848 K total memory
      1424804 K used memory
      1138752 K active memory
      1026300 K inactive memory
      1456892 K free memory
            0 K buffer memory
      1165152 K swap cache
      2097148 K total swap
            0 K used swap
      2097148 K free swap
        25128 non-nice user cpu ticks
          103 nice user cpu ticks
        10446 system cpu ticks
      3911130 idle cpu ticks
         1975 IO-wait cpu ticks
            0 IRQ cpu ticks
         1066 softirq cpu ticks
            0 stolen cpu ticks
       279889 pages paged in
       516874 pages paged out
            0 pages swapped in
            0 pages swapped out
      3519838 interrupts
      3341854 CPU context switches
   1619086394 boot time
        13058 forks
```

### **-d**

Display disk statistics

```console
$ vmstat -d
disk- ------------reads------------ ------------writes----------- -----IO------
       total merged sectors      ms  total merged sectors      ms    cur    sec
sda     5082      0  162624   12408   3853      0   30824   20224      0      8
sdb     2134      0   17072    3336    234      0    1872     468      0      0
```

### **Interval and Count**

Monitor system at specified intervals (in seconds)

```console
$ vmstat 2 5
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 1456892      0 1165152    0    0     0     1   88   79  1  0 99  0  0
 0  0      0 1456892      0 1165152    0    0     0     0   85   76  0  0 100  0  0
 0  0      0 1456892      0 1165152    0    0     0     0   83   74  0  0 100  0  0
 0  0      0 1456892      0 1165152    0    0     0     0   84   75  0  0 100  0  0
 0  0      0 1456892      0 1165152    0    0     0     0   86   77  0  0 100  0  0
```

## Usage Examples

### Basic System Overview

```console
$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      0 1456892      0 1165152    0    0     0     1   88   79  1  0 99  0  0
```

### Continuous Monitoring During High Load

```console
$ vmstat 5
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 2  0      0 1423456      0 1165152    0    0     0     1   88   79  1  0 99  0  0
 3  1      0 1398276      0 1165152    0    0   128    64  156  142 15  5 75  5  0
 1  2      0 1387544      0 1165152    0    0   256   128  178  165 25 10 55 10  0
```

## Tips

### Understanding Output Columns

- **procs**: `r` shows runnable processes, `b` shows blocked processes
- **memory**: `swpd` is virtual memory used, `free` is idle memory
- **swap**: `si` is memory swapped in from disk, `so` is memory swapped to disk
- **io**: `bi` is blocks received from a block device, `bo` is blocks sent to a block device
- **cpu**: `us` is user time, `sy` is system time, `id` is idle time, `wa` is I/O wait time

### First Line vs. Subsequent Lines

When using intervals, the first line of output shows averages since the last reboot, while subsequent lines show activity during the specified interval.

### Identifying Performance Issues

- High `wa` (wait) values indicate I/O bottlenecks
- High `r` values (> number of CPUs) suggest CPU bottlenecks
- Consistent `si`/`so` activity indicates memory pressure

## Frequently Asked Questions

#### Q1. What does the `r` column in vmstat output mean?
A. The `r` column shows the number of processes waiting for run time. If this number consistently exceeds the number of CPUs in your system, it indicates CPU contention.

#### Q2. How can I tell if my system is swapping too much?
A. Watch the `si` and `so` columns. Any non-zero values indicate swap activity. Consistent swap activity suggests your system needs more RAM.

#### Q3. What's the difference between `us`, `sy`, and `id` in CPU statistics?
A. `us` shows percentage of CPU time spent running user code, `sy` shows percentage spent in kernel code, and `id` shows percentage of time the CPU was idle.

#### Q4. How do I interpret the memory statistics?
A. `free` is unused memory, `buff` is memory used for buffers, and `cache` is memory used for caching. Low `free` memory isn't necessarily a problem if `cache` is high, as cached memory can be reclaimed when needed.

## References

https://man7.org/linux/man-pages/man8/vmstat.8.html

## Revisions

- 2025/04/30 First revision