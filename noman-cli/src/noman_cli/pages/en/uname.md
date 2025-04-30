# uname command

Print system information about the operating system.

## Overview

The `uname` command displays information about the system, including the operating system name, hostname, kernel version, and hardware architecture. It's commonly used in shell scripts to determine the operating system type or version for compatibility checks.

## Options

### **-a, --all**

Print all available system information (combination of all options)

```console
$ uname -a
Darwin MacBook-Pro.local 22.5.0 Darwin Kernel Version 22.5.0: Mon Apr 24 20:52:24 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T6000 arm64
```

### **-s, --kernel-name**

Print the kernel name (default option if none specified)

```console
$ uname -s
Darwin
```

### **-n, --nodename**

Print the network node hostname

```console
$ uname -n
MacBook-Pro.local
```

### **-r, --kernel-release**

Print the kernel release

```console
$ uname -r
22.5.0
```

### **-v, --kernel-version**

Print the kernel version

```console
$ uname -v
Darwin Kernel Version 22.5.0: Mon Apr 24 20:52:24 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T6000
```

### **-m, --machine**

Print the machine hardware name (architecture)

```console
$ uname -m
arm64
```

## Usage Examples

### Checking OS type in a script

```console
$ if [ "$(uname)" = "Darwin" ]; then
>   echo "This is macOS"
> else
>   echo "This is not macOS"
> fi
This is macOS
```

### Getting kernel version and architecture

```console
$ uname -rv
Darwin Kernel Version 22.5.0: Mon Apr 24 20:52:24 PDT 2023; root:xnu-8796.121.2~5/RELEASE_ARM64_T6000 22.5.0
```

## Tips

### Use in Shell Scripts for Cross-Platform Compatibility

The `uname` command is particularly useful in shell scripts that need to run on multiple platforms. You can use it to detect the operating system and execute platform-specific commands.

### Combine with Other Commands

Pair `uname` with commands like `sw_vers` on macOS to get more detailed system information:

```console
$ uname -m && sw_vers
arm64
ProductName:		macOS
ProductVersion:		13.4
BuildVersion:		22F66
```

### Remember Platform Differences

Output format varies between Unix-like systems. For example, Linux systems will show "Linux" as the kernel name, while macOS shows "Darwin".

## Frequently Asked Questions

#### Q1. What's the difference between `uname -s` and `uname`?
A. There is no difference. When run without options, `uname` defaults to the `-s` option, displaying just the kernel name.

#### Q2. How can I tell if I'm on a 32-bit or 64-bit system?
A. Use `uname -m`. On 64-bit systems, you'll typically see "x86_64" for Intel/AMD processors or "arm64" for ARM processors.

#### Q3. Why does macOS show "Darwin" instead of "macOS"?
A. Darwin is the name of the core Unix-based operating system that underlies macOS. The `uname` command reports the kernel name, not the commercial product name.

#### Q4. How can I get the macOS version instead of kernel version?
A. Use the `sw_vers` command, which is specific to macOS and shows the product name, version, and build.

## References

https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html

## Revisions

- 2025/04/30 First revision