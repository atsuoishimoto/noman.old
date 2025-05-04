# basename command

Extract the filename or directory name from a pathname.

## Overview

The `basename` command strips directory components and a specified suffix from a given path, leaving just the filename or the final directory name. It's commonly used in shell scripts to extract filenames from full paths or to remove file extensions.

## Options

### **-a, --multiple**

Process multiple arguments, treating each as a NAME.

```console
$ basename -a /usr/bin/sort /usr/bin/cut
sort
cut
```

### **-s, --suffix=SUFFIX**

Remove a trailing SUFFIX from each NAME.

```console
$ basename -s .txt file.txt
file
```

### **-z, --zero**

End each output line with NUL, not newline.

```console
$ basename -z file.txt | hexdump -C
00000000  66 69 6c 65 2e 74 78 74  00                       |file.txt.|
00000009
```

## Usage Examples

### Basic filename extraction

```console
$ basename /usr/local/bin/example.sh
example.sh
```

### Removing file extension

```console
$ basename /home/user/documents/report.pdf .pdf
report
```

### Using in shell scripts

```console
$ filename=$(basename "$path")
$ echo "The filename is: $filename"
The filename is: example.txt
```

### Processing multiple paths

```console
$ basename -a /var/log/syslog /etc/passwd /usr/bin/bash
syslog
passwd
bash
```

## Tips:

### Combine with dirname

Use `basename` with `dirname` to split a path into its components:

```console
$ path="/home/user/documents/report.pdf"
$ dir=$(dirname "$path")
$ file=$(basename "$path")
$ echo "Directory: $dir, File: $file"
Directory: /home/user/documents, File: report.pdf
```

### Quote your arguments

Always quote your arguments to handle filenames with spaces or special characters:

```console
$ basename "/path/to/my file.txt"
my file.txt
```

### Use with parameter expansion

In Bash, you can often use parameter expansion instead of `basename`:

```console
$ path="/home/user/documents/report.pdf"
$ echo "${path##*/}"
report.pdf
```

## Frequently Asked Questions

#### Q1. What's the difference between `basename` and `dirname`?
A. `basename` extracts the final component (filename or directory name) from a path, while `dirname` extracts the directory portion of the path.

#### Q2. How do I remove multiple extensions (like .tar.gz)?
A. `basename` only removes one suffix at a time. For multiple extensions, you'll need to use it multiple times or use shell parameter expansion.

#### Q3. Does `basename` work with relative paths?
A. Yes, it works with both absolute and relative paths, always returning the final component.

#### Q4. Can `basename` handle paths with spaces?
A. Yes, but you need to quote the arguments to prevent the shell from interpreting spaces as argument separators.

## References

https://www.gnu.org/software/coreutils/manual/html_node/basename-invocation.html

## Revisions

- 2025/05/04 First revision