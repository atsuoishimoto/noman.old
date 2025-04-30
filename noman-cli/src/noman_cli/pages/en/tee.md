# tee command

Read from standard input and write to both standard output and files.

## Overview

The `tee` command reads from standard input and writes to both standard output and one or more files simultaneously. It's commonly used in command pipelines to capture output while still allowing it to continue through the pipeline. Think of it like a T-shaped pipe fitting in plumbing, where the flow splits in two directions.

## Options

### **-a, --append**

Append to the given files, don't overwrite them

```console
$ echo "Additional line" | tee -a output.txt
Additional line
```

### **-i, --ignore-interrupts**

Ignore interrupt signals (useful for ensuring data is written even if the process is interrupted)

```console
$ long_running_command | tee -i log.txt
[output continues while being saved to log.txt]
```

## Usage Examples

### Basic Usage

```console
$ echo "Hello, world!" | tee output.txt
Hello, world!
```
This writes "Hello, world!" to both the terminal and the file output.txt.

### Writing to Multiple Files

```console
$ echo "Same content in multiple files" | tee file1.txt file2.txt file3.txt
Same content in multiple files
```
This writes the same content to three different files while also displaying it on the terminal.

### Capturing Command Output While Using It

```console
$ ls -la | tee file_listing.txt | grep ".txt"
-rw-r--r--  1 user  staff   15 Apr 30 10:23 file1.txt
-rw-r--r--  1 user  staff   15 Apr 30 10:23 file2.txt
-rw-r--r--  1 user  staff   15 Apr 30 10:23 file3.txt
-rw-r--r--  1 user  staff   28 Apr 30 10:23 file_listing.txt
```
This lists all files, saves the complete listing to file_listing.txt, and then filters to show only .txt files on the screen.

## Tips:

### Use with sudo

When you need to view and save output that requires elevated privileges, `tee` can help:

```console
$ sudo command | tee output.txt
```

This runs the command with sudo but writes the output to a file owned by your user (not root).

### Combining with Other Commands

`tee` works well in complex pipelines. For example, to process data, save an intermediate result, and continue processing:

```console
$ cat data.txt | sort | tee sorted.txt | uniq > unique.txt
```

### Logging and Debugging

Use `tee` to log command output while still seeing it in real-time, which is helpful for debugging:

```console
$ make | tee build.log
```

## Frequently Asked Questions

#### Q1. What does the name "tee" mean?
A. The name comes from the T-shaped pipe fitting in plumbing, which splits flow in two directions, similar to how the command splits output to both the screen and files.

#### Q2. How is `tee` different from redirection with `>`?
A. While `command > file` redirects output only to a file (not showing it on screen), `command | tee file` shows the output on screen while also saving it to a file.

#### Q3. Can I use `tee` with sudo to write to protected files?
A. Yes. `command | sudo tee /protected/file` allows you to write to files that require elevated privileges.

#### Q4. Does `tee` overwrite existing files?
A. By default, yes. Use `tee -a` to append to files instead of overwriting them.

## References

https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html

## Revisions

- 2025/04/30 First revision