# iostat command

Display CPU and input/output statistics for devices and partitions.

## Overview

`iostat` reports CPU statistics and input/output statistics for devices, partitions, and network filesystems. It's particularly useful for monitoring system performance, identifying bottlenecks, and analyzing disk I/O patterns. The command shows how busy your CPU and disks are, helping system administrators diagnose performance issues.

## Options

### **-c**

Display only CPU statistics.

```console
$ iostat -c
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98
```

### **-d**

Display only device statistics.

```console
$ iostat -d
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       141.02       124.53    1250432    1104567
sdb               0.12         3.45         0.00      30567          0
```

### **-h, --human**

Display sizes in human-readable format (e.g., 1.0k, 234M, 2G).

```console
$ iostat -h
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda              5.73       141.0k       124.5k      1.2G      1.1G
sdb              0.12         3.5k         0.0k     30.6M      0.0k
```

### **-k**

Display statistics in kilobytes per second.

```console
$ iostat -k
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       141.02       124.53    1250432    1104567
sdb               0.12         3.45         0.00      30567          0
```

### **-m**

Display statistics in megabytes per second.

```console
$ iostat -m
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device             tps    MB_read/s    MB_wrtn/s    MB_read    MB_wrtn
sda               5.73         0.14         0.12      1221.1    1078.7
sdb               0.12         0.00         0.00        29.8       0.0
```

### **-x**

Display extended statistics, providing more detailed information about device usage.

```console
$ iostat -x
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              3.45    2.28    141.02    124.53     0.12     1.35   3.36  37.25    0.42    2.53   0.01    40.88    54.62   0.25   1.43
sdb              0.12    0.00      3.45      0.00     0.00     0.00   0.00   0.00    0.35    0.00   0.00    28.75     0.00   0.22   0.03
```

### **-p [device]**

Display statistics for block devices and all their partitions that are used by the system.

```console
$ iostat -p sda
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       141.02       124.53    1250432    1104567
sda1              0.25         4.32        12.45      38291     110456
sda2              5.48       136.70       112.08    1212141     994111
```

### **interval [count]**

Specify the interval between reports in seconds and the number of reports to generate.

```console
$ iostat 2 3
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       141.02       124.53    1250432    1104567
sdb               0.12         3.45         0.00      30567          0

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.42    0.00    1.56    0.28    0.00   94.74

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               6.50       152.50       138.00         305         276
sdb               0.00         0.00         0.00           0           0

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.36    0.00    1.48    0.32    0.00   94.84

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.50       132.00       118.50         264         237
sdb               0.50         8.00         0.00          16           0
```

## Usage Examples

### Monitoring disk I/O with extended statistics

```console
$ iostat -xd 2
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              3.45    2.28    141.02    124.53     0.12     1.35   3.36  37.25    0.42    2.53   0.01    40.88    54.62   0.25   1.43
sdb              0.12    0.00      3.45      0.00     0.00     0.00   0.00   0.00    0.35    0.00   0.00    28.75     0.00   0.22   0.03

Device            r/s     w/s     rkB/s     wkB/s   rrqm/s   wrqm/s  %rrqm  %wrqm r_await w_await aqu-sz rareq-sz wareq-sz  svctm  %util
sda              4.00    3.50    164.00    156.00     0.00     2.00   0.00  36.36    0.38    2.43   0.01    41.00    44.57   0.27   2.01
sdb              0.00    0.00      0.00      0.00     0.00     0.00   0.00   0.00    0.00    0.00   0.00     0.00     0.00   0.00   0.00
```

### Displaying human-readable disk statistics

```console
$ iostat -dh
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda              5.73       141.0k       124.5k      1.2G      1.1G
sdb              0.12         3.5k         0.0k     30.6M      0.0k
```

### Monitoring specific partitions

```console
$ iostat -p sda 5
Linux 5.15.0-91-generic (hostname)  05/04/2025  _x86_64_  (8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           3.25    0.00    1.42    0.35    0.00   94.98

Device             tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
sda               5.73       141.02       124.53    1250432    1104567
sda1              0.25         4.32        12.45      38291     110456
sda2              5.48       136.70       112.08    1212141     994111

# Output will repeat every 5 seconds until interrupted
```

## Tips

### Identify I/O Bottlenecks

Look at the `%util` column in the extended statistics (`-x` option) to identify disks that are approaching 100% utilization, which indicates potential bottlenecks.

### Monitor I/O Wait Time

High values in the `r_await` and `w_await` columns indicate that processes are waiting for I/O operations to complete, which could be slowing down your system.

### Continuous Monitoring

Use the interval parameter to continuously monitor disk activity. For example, `iostat 5` will refresh the statistics every 5 seconds.

### Combine with Other Tools

Use `iostat` in conjunction with other monitoring tools like `top`, `vmstat`, and `sar` for a comprehensive view of system performance.

### Focus on Active Devices

When troubleshooting performance issues, focus on devices with high transaction rates (tps) and high utilization percentages.

## Frequently Asked Questions

#### Q1. What does the %iowait value in CPU statistics mean?
A. %iowait represents the percentage of time that the CPU(s) were idle during which the system had pending disk I/O requests. High iowait values indicate that the system is bottlenecked by disk operations.

#### Q2. How do I interpret the extended statistics from iostat -x?
A. Key metrics include: %util (device utilization), r_await/w_await (read/write response times), and aqu-sz (average queue length). High utilization (>80%), long wait times, or large queue sizes indicate potential I/O problems.

#### Q3. What's the difference between tps, r/s, and w/s?
A. tps (transfers per second) is the total number of I/O requests per second. r/s and w/s break this down into read requests and write requests per second, respectively.

#### Q4. How can I monitor NVMe drives with iostat?
A. NVMe drives appear as nvme0n1, nvme1n1, etc. You can use the same iostat commands, for example: `iostat -x nvme0n1`.

#### Q5. Why are my iostat values different between runs?
A. The first report from iostat shows statistics since system boot, while subsequent reports (when using intervals) show statistics for the specified time interval only.

## References

https://man7.org/linux/man-pages/man1/iostat.1.html

## Revisions

- 2025/05/04 First revision