# xargs command

Executes commands using arguments from standard input.

## Overview

`xargs` is a command-line utility that builds and executes commands from standard input. It reads items from standard input, delimited by blanks or newlines, and executes a command (by default `/bin/echo`) using those items as arguments. This is particularly useful for processing output from other commands and applying operations to multiple files or data streams.

## Options

### **-0, --null**

Input items are terminated by a null character instead of whitespace, useful when input might contain spaces or newlines.

```console
$ find . -name "*.txt" -print0 | xargs -0 grep "example"
./file1.txt:example text here
./path with spaces/file2.txt:another example
```

### **-I, --replace[=REPLACE]**

Replace occurrences of REPLACE (default is {}) in the initial arguments with names read from standard input.

```console
$ echo "file1.txt file2.txt" | xargs -I {} cp {} backup/
```

### **-n, --max-args=MAX-ARGS**

Use at most MAX-ARGS arguments per command line.

```console
$ echo "1 2 3 4" | xargs -n 2 echo
1 2
3 4
```

### **-P, --max-procs=MAX-PROCS**

Run up to MAX-PROCS processes simultaneously.

```console
$ find . -name "*.jpg" | xargs -P 4 -I {} convert {} {}.png
```

### **-t, --verbose**

Print the command to be executed before running it.

```console
$ echo "file1.txt file2.txt" | xargs -t rm
rm file1.txt file2.txt
```

### **-p, --interactive**

Prompt the user before executing each command.

```console
$ echo "file1.txt file2.txt" | xargs -p rm
rm file1.txt file2.txt ?...
```

## Usage Examples

### Processing files with spaces in names

```console
$ find . -name "*.txt" -print0 | xargs -0 grep "pattern"
./document.txt:pattern found here
./notes with spaces.txt:another pattern example
```

### Batch processing files

```console
$ find . -name "*.jpg" | xargs -P 4 -I {} convert {} {}.png
```

### Deleting files listed in a file

```console
$ cat files_to_delete.txt | xargs rm
```

### Running multiple commands on each input

```console
$ echo "file1 file2" | xargs -I {} sh -c 'echo {}; wc -l {}'
file1
      42 file1
file2
      18 file2
```

## Tips

### Use -0 with find -print0

When dealing with filenames that contain spaces, newlines, or other special characters, always pair `find -print0` with `xargs -0` to ensure proper handling.

### Prevent Command Injection

Be careful when using user-supplied input with xargs. Use the `-I` option with a placeholder to avoid command injection vulnerabilities.

### Preview Commands with -t

Use the `-t` option to see what commands will be executed before they run, especially when working with destructive operations like `rm`.

### Control Parallelism

For CPU-intensive tasks, use `-P` with the number of CPU cores to optimize performance without overloading your system.

## Frequently Asked Questions

#### Q1. What's the difference between piping to a command and using xargs?
A. Piping (`|`) sends the output of one command as input to another command, while `xargs` converts input into arguments for a command. Many commands don't accept input from stdin for filenames, which is where xargs becomes necessary.

#### Q2. How do I use xargs to handle filenames with spaces?
A. Use `find -print0` with `xargs -0` to properly handle filenames with spaces, newlines, or other special characters.

#### Q3. Can xargs run multiple commands for each input?
A. Yes, use the `-I` option with `sh -c` to run multiple commands: `xargs -I {} sh -c 'command1 {}; command2 {}'`

#### Q4. How can I limit the number of arguments per command?
A. Use the `-n` option followed by the maximum number of arguments: `xargs -n 5 command`

## References

https://www.gnu.org/software/findutils/manual/html_node/find_html/xargs-options.html

## Revisions

- 2025/05/04 First revision