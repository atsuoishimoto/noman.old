# perf command

Performance analysis tool for Linux systems that collects and analyzes performance data.

## Overview

`perf` is a powerful Linux profiling tool that accesses the performance monitoring hardware counters of the CPU to gather information about the behavior of user code, kernel, and hardware events. It helps identify performance bottlenecks, analyze CPU usage, track memory access patterns, and debug system performance issues.

## Options

### **stat**

Runs a command and gathers performance counter statistics

```console
$ perf stat ls
Documents  Downloads  Pictures  Videos

 Performance counter stats for 'ls':

              0.93 msec task-clock                #    0.076 CPUs utilized
                 0      context-switches          #    0.000 K/sec
                 0      cpu-migrations            #    0.000 K/sec
                89      page-faults               #    0.096 M/sec
           1,597,086      cycles                  #    1.723 GHz
           1,221,363      instructions            #    0.76  insn per cycle
             245,931      branches                #  265.249 M/sec
              10,764      branch-misses           #    4.38% of all branches

       0.012249350 seconds time elapsed

       0.001349000 seconds user
       0.000000000 seconds sys
```

### **record**

Records performance data for later analysis

```console
$ perf record -g ./myprogram
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.086 MB perf.data (1093 samples) ]
```

### **report**

Analyzes and displays the data collected by perf record

```console
$ perf report
# Samples: 1K of event 'cycles:ppp'
# Event count (approx.): 1597086
#
# Overhead  Command      Shared Object        Symbol
# ........  .......  .................  ..............
#
    14.29%  myprogram  myprogram           [.] process_data
    10.53%  myprogram  libc-2.31.so        [.] malloc
     8.76%  myprogram  myprogram           [.] calculate_result
```

### **top**

System profiling tool similar to top, but showing performance counter information

```console
$ perf top
Samples: 42K of event 'cycles', 4000 Hz, Event count (approx.): 9857399138
Overhead  Shared Object                       Symbol
  10.95%  [kernel]                            [k] _raw_spin_unlock_irqrestore
   3.62%  [kernel]                            [k] finish_task_switch
   2.40%  [kernel]                            [k] __schedule
   2.11%  libcrypto.so.1.1                    [.] 0x000000000012b8d6
```

## Usage Examples

### Profiling CPU usage of a specific command

```console
$ perf stat -e cycles,instructions,cache-references,cache-misses ./myprogram
[output shows CPU performance metrics for myprogram]
```

### Recording call graph information

```console
$ perf record -g ./myprogram
[perf data recorded to perf.data]
$ perf report --sort comm,dso,symbol
[displays hierarchical call graph with hotspots]
```

### Analyzing specific events

```console
$ perf list
[lists available events]
$ perf stat -e cache-misses,branch-misses ./myprogram
[shows cache and branch miss statistics]
```

## Tips:

### Run with Elevated Privileges

Many perf features require root access. Use `sudo perf` to access hardware counters and kernel events.

### Focus on Hotspots

When analyzing performance reports, focus on functions with the highest overhead percentages first. These "hotspots" offer the greatest potential for optimization.

### Use Flame Graphs

Convert perf data to flame graphs for better visualization:
```console
$ perf record -g ./myprogram
$ perf script | FlameGraph/stackcollapse-perf.pl | FlameGraph/flamegraph.pl > flamegraph.svg
```

### Limit Data Collection

For long-running programs, use `-F` to reduce sampling frequency and `-g` to collect call graphs:
```console
$ perf record -F 99 -g ./myprogram
```

## Frequently Asked Questions

#### Q1. What's the difference between perf stat and perf record?
A. `perf stat` provides a summary of performance metrics after a command completes, while `perf record` captures detailed performance data that can be analyzed later with `perf report`.

#### Q2. How do I profile a running process?
A. Use `perf record -p PID` to attach to an already running process with the specified PID.

#### Q3. Why do I get "Permission denied" errors?
A. Many perf features require root privileges. Try running with `sudo` or adjust the `/proc/sys/kernel/perf_event_paranoid` setting.

#### Q4. How can I reduce the size of perf.data files?
A. Use `-F` to lower the sampling frequency (e.g., `perf record -F 99`) or limit the events you're recording with the `-e` option.

## References

https://perf.wiki.kernel.org/index.php/Main_Page

## Revisions

- 2025/04/30 First revision