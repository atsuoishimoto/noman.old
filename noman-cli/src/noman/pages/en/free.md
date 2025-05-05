# free command

Display amount of free and used memory in the system.

## Overview

The `free` command provides information about the system's memory usage, including total, used, and available memory for both physical RAM and swap space. It's a quick way to check memory resources and identify potential memory constraints.

## Options

### **-b, --bytes**

Display the memory amount in bytes.

```console
$ free -b
               total        used        free      shared  buff/cache   available
Mem:     8273514496  3145728000  1073741824   536870912  4053844992  4594966528
Swap:    2147483648   268435456  1879048192
```

### **-k, --kilo**

Display the memory amount in kilobytes (default).

```console
$ free -k
               total        used        free      shared  buff/cache   available
Mem:        8080580     3072000     1048576      524288     3959808     4487272
Swap:       2097152      262144     1835008
```

### **-m, --mega**

Display the memory amount in megabytes.

```console
$ free -m
               total        used        free      shared  buff/cache   available
Mem:           7890        3000        1024         512        3866        4382
Swap:          2048         256        1792
```

### **-g, --giga**

Display the memory amount in gigabytes.

```console
$ free -g
               total        used        free      shared  buff/cache   available
Mem:              7           2           1           0           3           4
Swap:             2           0           1
```

### **-h, --human**

Show all output fields automatically scaled to the shortest three-digit unit and display the units.

```console
$ free -h
               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       3.0Gi       1.0Gi       512Mi       3.7Gi       4.2Gi
Swap:          2.0Gi       256Mi       1.7Gi
```

### **-s, --seconds N**

Continuously display the result with N second delay between updates.

```console
$ free -s 2
               total        used        free      shared  buff/cache   available
Mem:           7890        3000        1024         512        3866        4382
Swap:          2048         256        1792

               total        used        free      shared  buff/cache   available
Mem:           7890        3010        1014         512        3866        4372
Swap:          2048         256        1792
```

### **-c, --count N**

Display the result N times, then exit. Must be used with -s option.

```console
$ free -c 3 -s 1
               total        used        free      shared  buff/cache   available
Mem:           7890        3000        1024         512        3866        4382
Swap:          2048         256        1792

               total        used        free      shared  buff/cache   available
Mem:           7890        3010        1014         512        3866        4372
Swap:          2048         256        1792

               total        used        free      shared  buff/cache   available
Mem:           7890        3020        1004         512        3866        4362
Swap:          2048         256        1792
```

### **-t, --total**

Display a line showing the column totals.

```console
$ free -t
               total        used        free      shared  buff/cache   available
Mem:           7890        3000        1024         512        3866        4382
Swap:          2048         256        1792
Total:         9938        3256        2816
```

### **-w, --wide**

Switch to wide mode. The wide mode produces lines longer than 80 characters.

```console
$ free -w
               total        used        free      shared     buffers       cache   available
Mem:           7890        3000        1024         512         366        3500        4382
Swap:          2048         256        1792
```

## Usage Examples

### Basic memory information

```console
$ free
               total        used        free      shared  buff/cache   available
Mem:           7890        3000        1024         512        3866        4382
Swap:          2048         256        1792
```

### Human-readable memory information with totals

```console
$ free -ht
               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       3.0Gi       1.0Gi       512Mi       3.7Gi       4.2Gi
Swap:          2.0Gi       256Mi       1.7Gi
Total:         9.7Gi       3.2Gi       2.7Gi
```

### Continuous monitoring with 5-second intervals

```console
$ free -h -s 5
               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       3.0Gi       1.0Gi       512Mi       3.7Gi       4.2Gi
Swap:          2.0Gi       256Mi       1.7Gi

               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       3.1Gi       900Mi       512Mi       3.7Gi       4.1Gi
Swap:          2.0Gi       256Mi       1.7Gi
```

## Tips

### Understanding the Output Columns

- **total**: Total installed memory
- **used**: Memory currently in use
- **free**: Unused memory
- **shared**: Memory shared by multiple processes
- **buff/cache**: Memory used by kernel buffers and page cache
- **available**: Estimate of memory available for new applications without swapping

### Focus on Available Memory

The "available" column is more important than "free" as it includes memory that can be reclaimed from buffers and cache if needed by applications.

### Monitoring Memory Over Time

Use `free -s` to monitor memory usage over time, which helps identify memory leaks or usage patterns.

### Combine with Other Commands

Pipe `free` output to other commands for specific information:
```console
$ free -m | grep Mem
Mem:           7890        3000        1024         512        3866        4382
```

## Frequently Asked Questions

#### Q1. What's the difference between "free" and "available" memory?
A. "Free" memory is completely unused, while "available" includes memory that can be reclaimed from buffers and cache for new applications without swapping.

#### Q2. Why is my "free" memory so low?
A. Linux uses available memory for disk caching to improve performance. Look at the "available" column for a better indication of memory that can be used by applications.

#### Q3. How do I check if my system is running out of memory?
A. Monitor the "available" column. If it's consistently low and swap usage is high, your system may be under memory pressure.

#### Q4. What does the "buff/cache" column represent?
A. It shows memory used for kernel buffers and disk caching. This memory can often be reclaimed if needed by applications.

#### Q5. How can I continuously monitor memory usage?
A. Use `free -s N` where N is the number of seconds between updates.

## References

https://www.man7.org/linux/man-pages/man1/free.1.html

## Revisions

- 2025/05/04 First revision