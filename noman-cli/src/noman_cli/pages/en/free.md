# free command

Display amount of free and used memory in the system.

## Overview

The `free` command shows the total amount of free and used physical memory (RAM) and swap space in the system, as well as the buffers and caches used by the kernel. It helps users monitor system memory usage and identify potential memory-related issues.

## Options

### **-h, --human**

Display memory sizes in human-readable format (e.g., MB, GB) instead of bytes

```console
$ free -h
               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       3.2Gi       1.2Gi       264Mi       3.3Gi       3.9Gi
Swap:          2.0Gi       156Mi       1.8Gi
```

### **-s, --seconds**

Continuously display the memory usage, updating every specified number of seconds

```console
$ free -s 5
               total        used        free      shared  buff/cache   available
Mem:        8033016     3342104     1245708      270336     3445204     4110292
Swap:       2097148      159744     1937404
[Updates every 5 seconds...]
```

### **-t, --total**

Display a line showing the column totals (RAM + swap)

```console
$ free -t
               total        used        free      shared  buff/cache   available
Mem:        8033016     3342104     1245708      270336     3445204     4110292
Swap:       2097148      159744     1937404
Total:     10130164     3501848     3183112
```

### **-w, --wide**

Switch to wide output format, showing buffers and cache separately

```console
$ free -w
               total        used        free      shared     buffers       cache   available
Mem:        8033016     3342104     1245708      270336      345204     3100000     4110292
Swap:       2097148      159744     1937404
```

## Usage Examples

### Combining human-readable format with total

```console
$ free -ht
               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       3.2Gi       1.2Gi       264Mi       3.3Gi       3.9Gi
Swap:          2.0Gi       156Mi       1.8Gi
Total:         9.7Gi       3.4Gi       3.0Gi
```

### Monitoring memory usage continuously with wide format

```console
$ free -ws 10 -h
               total        used        free      shared     buffers       cache   available
Mem:           7.7Gi       3.2Gi       1.2Gi       264Mi       336Mi       3.0Gi       3.9Gi
Swap:          2.0Gi       156Mi       1.8Gi
[Updates every 10 seconds...]
```

## Tips:

### Understanding Memory Output

The "available" column shows memory that can be allocated to processes without swapping. It's often more useful than the "free" column, which only shows completely unused memory.

### Interpreting Buffers and Cache

High values in buff/cache are normal and beneficial. Linux uses unused memory for disk caching to improve performance and will free this memory when applications need it.

### Monitoring for Memory Issues

If the "free" and "available" values are consistently low and swap usage is high, your system might be experiencing memory pressure, which can cause performance issues.

## Frequently Asked Questions

#### Q1. What's the difference between "free" and "available" memory?
A. "Free" memory is completely unused, while "available" includes memory that can be reclaimed from buffers and cache for new applications without swapping.

#### Q2. Is high buffer/cache usage a problem?
A. No, it's actually beneficial. Linux uses otherwise unused memory to cache disk data, improving performance. This memory is automatically freed when applications need it.

#### Q3. How do I know if my system is running out of memory?
A. Look for low "available" memory, high swap usage, and check if the system is actively swapping (using tools like `vmstat` or `top`).

#### Q4. What does the "shared" column represent?
A. It shows memory that may be used by multiple processes, typically through shared memory segments or tmpfs filesystems.

## References

https://www.man7.org/linux/man-pages/man1/free.1.html

## Revisions

- 2025/04/30 First revision