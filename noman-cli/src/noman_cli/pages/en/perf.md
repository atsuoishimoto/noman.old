# perf command

Performance analysis tool for Linux, providing hardware counter statistics and tracing capabilities.

## Overview

`perf` is a powerful Linux profiling and performance analysis tool that accesses the performance monitoring hardware counters of the CPU to gather statistics about program execution. It can monitor CPU performance events, trace system calls, and analyze application performance with minimal overhead. Part of the Linux kernel tools, `perf` helps developers identify bottlenecks and optimize code.

## Options

### **-e, --event**

Specify the performance event to count or sample

```console
$ perf stat -e cycles,instructions ./myprogram
 Performance counter stats for './myprogram':

       1,234,567      cycles
       2,345,678      instructions             #    1.90  insn per cycle
       
       0.123456789 seconds time elapsed
```

### **-p, --pid**

Profile events on existing process by process ID

```console
$ perf record -p 1234 -g
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.452 MB perf.data (5093 samples) ]
```

### **-a, --all-cpus**

System-wide monitoring of all CPUs

```console
$ perf stat -a sleep 5
 Performance counter stats for 'system wide':

       12,345,678      cpu-cycles           
        5,678,901      instructions              #    0.46  insn per cycle
          123,456      cache-misses

       5.000621884 seconds time elapsed
```

### **-g, --call-graph**

Enable call-graph (stack chain/backtrace) recording

```console
$ perf record -g ./myprogram
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.452 MB perf.data (5093 samples) ]
```

## Usage Examples

### Basic CPU statistics

```console
$ perf stat ./myprogram
 Performance counter stats for './myprogram':

          0.086283      task-clock (msec)         #    0.733 CPUs utilized
                 2      context-switches          #    0.023 M/sec
                 0      cpu-migrations            #    0.000 K/sec
               108      page-faults               #    0.001 M/sec
           235,538      cycles                    #    2.731 GHz
           580,716      instructions              #    2.47  insn per cycle
           116,931      branches                  #    1.356 M/sec
             3,468      branch-misses             #    2.97% of all branches

       0.117743392 seconds time elapsed
```

### Recording and analyzing performance data

```console
$ perf record -g ./myprogram
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.452 MB perf.data (5093 samples) ]

$ perf report
# Samples: 5K of event 'cycles'
# Event count (approx.): 2345678901
#
# Overhead  Command      Shared Object        Symbol
# ........  .......  .................  ..............
#
    14.59%  myprogram  myprogram           [.] process_data
    10.21%  myprogram  myprogram           [.] calculate_result
     8.45%  myprogram  libc-2.31.so        [.] malloc
```

### Tracing system calls

```console
$ perf trace -p 1234
     0.000 ( 0.000 ms): myprogram/1234 write(fd: 1, buf: 0x7f9876543210, count: 16) = 16
     0.223 ( 0.019 ms): myprogram/1234 read(fd: 0, buf: 0x7f9876543210, count: 1024) = 64
     0.415 ( 0.021 ms): myprogram/1234 open(filename: 0x7f9876543210, flags: RDONLY) = 3
```

## Tips

### Use Flame Graphs for Visualization

Convert perf data to flame graphs using tools like FlameGraph to visualize call stacks and quickly identify hot spots in your code.

```console
$ perf record -g -F 99 ./myprogram
$ perf script | ./FlameGraph/stackcollapse-perf.pl | ./FlameGraph/flamegraph.pl > profile.svg
```

### Focus on Specific Events

Instead of collecting all events, focus on specific ones like cache-misses or branch-misses to diagnose particular performance issues.

```console
$ perf stat -e cache-misses,branch-misses ./myprogram
```

### Reduce Overhead with Sampling

For production environments, use sampling to reduce overhead by specifying a frequency:

```console
$ perf record -F 99 -g ./myprogram
```

## Frequently Asked Questions

#### Q1. What's the difference between `perf stat` and `perf record`?
A. `perf stat` provides a summary of performance counters, while `perf record` captures detailed samples for later analysis with `perf report`.

#### Q2. How do I profile a running application?
A. Use `perf record -p PID` where PID is the process ID of your running application.

#### Q3. Can I use perf on a virtual machine?
A. Yes, but with limitations. Some hardware counters may not be available or accurate in virtualized environments.

#### Q4. How do I see which functions are using the most CPU?
A. Use `perf top` for real-time function monitoring or `perf record` followed by `perf report` for detailed analysis.

#### Q5. Does perf work on all Linux distributions?
A. Most modern distributions support perf, but functionality may vary based on kernel version and configuration.

## References

https://perf.wiki.kernel.org/index.php/Main_Page

## Revisions

- 2025/05/04 First revision