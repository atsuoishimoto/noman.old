# tee command

Read from standard input and write to both standard output and files.

## Overview

The `tee` command reads from standard input and writes to both standard output and one or more files simultaneously. This allows you to view command output in the terminal while also saving it to a file. It's commonly used in pipelines to capture intermediate results.

## Options

### **-a, --append**

Append to the given files, don't overwrite them

```console
$ echo "Additional line" | tee -a output.txt
Additional line
```

### **-i, --ignore-interrupts**

Ignore interrupt signals (SIGINT)

```console
$ long_running_command | tee -i output.log
```

### **--help**

Display help information and exit

```console
$ tee --help
Usage: tee [OPTION]... [FILE]...
Copy standard input to each FILE, and also to standard output.

  -a, --append              append to the given FILEs, do not overwrite
  -i, --ignore-interrupts   ignore interrupt signals
  -p                        diagnose errors writing to non pipes
      --output-error[=MODE]   set behavior on write error.  See MODE below
      --help     display this help and exit
      --version  output version information and exit

MODE determines behavior with write errors on the outputs:
  'warn'         diagnose errors writing to any output
  'warn-nopipe'  diagnose errors writing to any output not a pipe
  'exit'         exit on error writing to any output
  'exit-nopipe'  exit on error writing to any output not a pipe
The default MODE for the -p option is 'warn-nopipe'.
The default operation when --output-error is not specified, is to
exit immediately on error writing to a pipe, and diagnose errors
writing to non pipe outputs.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/tee>
or available locally via: info '(coreutils) tee invocation'
```

### **--version**

Output version information and exit

```console
$ tee --version
tee (GNU coreutils) 9.0
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Mike Parker, Richard M. Stallman, and David MacKenzie.
```

## Usage Examples

### Basic Usage

```console
$ ls -l | tee file_list.txt
total 16
-rw-r--r-- 1 user group 1024 May 4 10:30 document.txt
drwxr-xr-x 2 user group 4096 May 3 15:45 projects
```

### Writing to Multiple Files

```console
$ echo "Hello, World!" | tee file1.txt file2.txt file3.txt
Hello, World!
```

### Combining with sudo

```console
$ cat config.txt | sudo tee /etc/app/config.txt > /dev/null
```

### Capturing Command Output While Viewing It

```console
$ make | tee build.log
[compilation output appears here and is also saved to build.log]
```

## Tips:

### Use with sudo to Edit Protected Files

When you need to edit a file that requires elevated privileges, you can use `tee` with `sudo` to write to the file:

```console
$ echo "new content" | sudo tee /etc/protected_file.txt
```

### Discard Standard Output

If you only want to write to files without seeing the output in the terminal, redirect standard output to `/dev/null`:

```console
$ command | tee output.txt > /dev/null
```

### Capture Both stdout and stderr

To capture both standard output and standard error:

```console
$ command 2>&1 | tee output.log
```

## Frequently Asked Questions

#### Q1. What's the difference between `tee` and simple redirection (`>`)?
A. While redirection (`>`) only writes output to a file, `tee` writes to both the file and standard output, allowing you to see the output in the terminal while saving it.

#### Q2. How do I append to a file instead of overwriting it?
A. Use the `-a` option: `command | tee -a file.txt`

#### Q3. Can I write to multiple files at once?
A. Yes, simply list all the files: `command | tee file1.txt file2.txt file3.txt`

#### Q4. How do I use `tee` to write to a file that requires root permissions?
A. Combine with sudo: `command | sudo tee /path/to/file > /dev/null`

## References

https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html

## Revisions

- 2025/05/04 First revision