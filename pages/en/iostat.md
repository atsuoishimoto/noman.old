# iostat command

Display CPU and input/output statistics for devices and partitions.

## Overview

`iostat` reports system input/output device loading statistics, CPU utilization, and throughput information. It helps monitor system performance by showing how busy the CPU and disk devices are, making it useful for identifying bottlenecks and performance issues.

## Options

### **-c**

Display only CPU statistics.

```console
$ iostat -c
Linux 5.15.0-91-generic (hostname)  04/30/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.32    0.00   95.01
```

### **-d**

Display only device statistics.

```console
$ iostat -d
Linux 5.15.0-91-generic (hostname)  04/30/2025  _x86_64_  (8 CPU)

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       112.73        45.12    9876324    3954321
nvme0n1          12.45       234.56       123.45   20543211   10876543
```

### **-x**

Display extended statistics for devices.

```console
$ iostat -x
Linux 5.15.0-91-generic (hostname)  04/30/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.32    0.00   95.01

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %util
sda              3.45    2.28    112.73     45.12     0.12     1.32  12.34
nvme0n1          8.23    4.22    234.56    123.45     0.05     0.87   8.76
```

### **-k**

Display statistics in kilobytes per second.

```console
$ iostat -k
Linux 5.15.0-91-generic (hostname)  04/30/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.32    0.00   95.01

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       112.73        45.12    9876324    3954321
nvme0n1          12.45       234.56       123.45   20543211   10876543
```

### **-m**

Display statistics in megabytes per second.

```console
$ iostat -m
Linux 5.15.0-91-generic (hostname)  04/30/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.32    0.00   95.01

Device             tps    MB_read/s    MB_wrtn/s    MB_read    MB_wrtn
sda               5.73         0.11         0.04      9643      3861
nvme0n1          12.45         0.23         0.12     20062     10621
```

### **-p [device]**

Display statistics for a specific device and its partitions.

```console
$ iostat -p sda
Linux 5.15.0-91-generic (hostname)  04/30/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.32    0.00   95.01

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       112.73        45.12    9876324    3954321
sda1              2.34        45.67        23.45    3987654    2054321
sda2              3.39        67.06        21.67    5888670    1900000
```

### **[interval] [count]**

Specify the reporting interval in seconds and the number of reports.

```console
$ iostat 2 3
Linux 5.15.0-91-generic (hostname)  04/30/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.32    0.00   95.01

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       112.73        45.12    9876324    3954321
nvme0n1          12.45       234.56       123.45   20543211   10876543

[...repeats 2 more times with updated statistics...]
```

## Usage Examples

### Monitoring disk I/O in real-time

```console
$ iostat -dx 2
Linux 5.15.0-91-generic (hostname)  04/30/2025  _x86_64_  (8 CPU)

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %util
sda              3.45    2.28    112.73     45.12     0.12     1.32  12.34
nvme0n1          8.23    4.22    234.56    123.45     0.05     0.87   8.76

[...updates every 2 seconds...]
```

### Checking CPU and disk statistics in megabytes

```console
$ iostat -cm 5
Linux 5.15.0-91-generic (hostname)  04/30/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.32    0.00   95.01

Device             tps    MB_read/s    MB_wrtn/s    MB_read    MB_wrtn
sda               5.73         0.11         0.04      9643      3861
nvme0n1          12.45         0.23         0.12     20062     10621

[...updates every 5 seconds...]
```

### Monitoring specific partitions

```console
$ iostat -p sda -x 3
Linux 5.15.0-91-generic (hostname)  04/30/2025  _x86_64_  (8 CPU)

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %util
sda              3.45    2.28    112.73     45.12     0.12     1.32  12.34
sda1             1.23    1.11     45.67     23.45     0.05     0.76   5.43
sda2             2.22    1.17     67.06     21.67     0.07     0.56   6.91

[...updates every 3 seconds...]
```

## Tips

### Understanding %util

The %util metric shows the percentage of CPU time during which I/O requests were issued to the device. A value close to 100% indicates the device is saturated, which may cause performance bottlenecks.

### Identifying I/O Wait Issues

High %iowait values in the CPU statistics indicate that the processor is waiting for disk I/O operations to complete. This often points to disk performance issues.

### Continuous Monitoring

For troubleshooting performance issues, run iostat with an interval (e.g., `iostat -x 2`) to see how the system behaves over time rather than just taking a single snapshot.

### Combining with Other Tools

Use iostat alongside tools like top, vmstat, and sar for a comprehensive view of system performance. This helps identify whether bottlenecks are CPU, memory, or I/O related.

## Frequently Asked Questions

#### Q1. What does the tps column mean?
A. tps stands for "transfers per second," which represents the number of I/O requests to the device per second.

#### Q2. How do I interpret the r/s and w/s columns?
A. r/s shows reads per second, and w/s shows writes per second to the device. These metrics help identify read-heavy or write-heavy workloads.

#### Q3. What's the difference between iostat and vmstat?
A. iostat focuses on I/O statistics for devices and partitions, while vmstat provides a broader view of system performance including memory, processes, and I/O.

#### Q4. How can I see statistics for a specific disk only?
A. Use `iostat -d [device]`, for example: `iostat -d sda` to show statistics only for the sda device.

#### Q5. What does rrqm/s and wrqm/s mean?
A. These represent read and write requests merged per second. Merging occurs when adjacent I/O operations are combined into a single request, improving efficiency.

## References

https://man7.org/linux/man-pages/man1/iostat.1.html

## Revisions

- 2025/04/30 First revision