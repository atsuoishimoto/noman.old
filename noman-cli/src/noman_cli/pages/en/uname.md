# uname command

Print system information about the operating system.

## Overview

The `uname` command displays system information about the operating system running on your computer. It can show details such as the kernel name, network hostname, kernel release, kernel version, machine hardware, processor type, and operating system.

## Options

### **-a, --all**

Print all information in the following order: kernel name, network hostname, kernel release, kernel version, machine hardware, processor type, and operating system.

```console
$ uname -a
Linux hostname 5.15.0-91-generic #101-Ubuntu SMP Tue Apr 16 14:15:57 UTC 2024 x86_64 x86_64 GNU/Linux
```

### **-s, --kernel-name**

Print the kernel name. This is the default if no option is specified.

```console
$ uname -s
Linux
```

### **-n, --nodename**

Print the network node hostname.

```console
$ uname -n
hostname
```

### **-r, --kernel-release**

Print the kernel release.

```console
$ uname -r
5.15.0-91-generic
```

### **-v, --kernel-version**

Print the kernel version.

```console
$ uname -v
#101-Ubuntu SMP Tue Apr 16 14:15:57 UTC 2024
```

### **-m, --machine**

Print the machine hardware name.

```console
$ uname -m
x86_64
```

### **-p, --processor**

Print the processor type (or "unknown" if it cannot be determined).

```console
$ uname -p
x86_64
```

### **-o, --operating-system**

Print the operating system.

```console
$ uname -o
GNU/Linux
```

## Usage Examples

### Checking kernel version for compatibility

```console
$ uname -r
5.15.0-91-generic
```

### Getting complete system information

```console
$ uname -a
Linux hostname 5.15.0-91-generic #101-Ubuntu SMP Tue Apr 16 14:15:57 UTC 2024 x86_64 x86_64 GNU/Linux
```

### Checking architecture for software installation

```console
$ uname -m
x86_64
```

## Tips

### Combine with Other Commands

Combine `uname` with other commands like `lsb_release` to get more detailed distribution information:

```console
$ uname -r && lsb_release -a
5.15.0-91-generic
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.3 LTS
Release:        22.04
Codename:       jammy
```

### Use in Scripts

The `uname` command is particularly useful in shell scripts to determine the operating system or architecture before performing system-specific operations.

### macOS Considerations

On macOS, `uname -s` will return "Darwin" instead of "Linux", and some options like `-o` may not be available or may behave differently.

## Frequently Asked Questions

#### Q1. How do I check which Linux kernel version I'm running?
A. Use `uname -r` to display the kernel release version.

#### Q2. How can I tell if my system is 32-bit or 64-bit?
A. Use `uname -m` to show the machine hardware name. "x86_64" indicates a 64-bit system, while "i686" or "i386" indicates a 32-bit system.

#### Q3. What's the difference between `uname -r` and `uname -v`?
A. `uname -r` shows the kernel release (like "5.15.0-91-generic"), while `uname -v` shows the kernel version, which typically includes build information (like "#101-Ubuntu SMP Tue Apr 16 14:15:57 UTC 2024").

#### Q4. Why does `uname -p` sometimes return "unknown"?
A. The processor type might not be determinable on some systems, in which case "unknown" is returned.

## References

https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html

## Revisions

2025/05/04 First revision