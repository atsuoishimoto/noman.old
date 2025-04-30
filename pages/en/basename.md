# basename command

Extract the filename or directory name from a pathname.

## Overview

`basename` strips directory components and suffixes from file paths. It's commonly used in shell scripts to extract just the filename from a full path, or to remove file extensions.

## Options

### **-a, --multiple**

Process multiple arguments, treating each as a NAME

```console
$ basename -a /usr/bin/zip /usr/bin/unzip
zip
unzip
```

### **-s, --suffix=SUFFIX**

Remove a trailing SUFFIX from each NAME

```console
$ basename -s .txt file.txt
file
```

### **-z, --zero**

End each output line with NUL, not newline

```console
$ basename -z /usr/bin/zip | hexdump -C
00000000  7a 69 70 00                                       |zip.|
00000004
```

## Usage Examples

### Basic filename extraction

```console
$ basename /home/user/documents/report.pdf
report.pdf
```

### Removing file extension

```console
$ basename /home/user/documents/report.pdf .pdf
report
```

### Using in shell scripts

```console
$ filename=$(basename "$filepath")
$ echo "Working with file: $filename"
Working with file: report.pdf
```

### Processing multiple paths

```console
$ basename -a /var/log/syslog /etc/hosts /usr/bin/python3
syslog
hosts
python3
```

## Tips:

### Combine with dirname

Use `basename` with `dirname` to split a path into its components:
```console
$ path="/home/user/documents/report.pdf"
$ dirname "$path"
/home/user/documents
$ basename "$path"
report.pdf
```

### Alternative in Bash

In Bash, you can use parameter expansion instead of `basename`:
```console
$ path="/home/user/documents/report.pdf"
$ echo "${path##*/}"
report.pdf
```

### Handling Paths with Spaces

Always quote your variables when using `basename` to handle paths with spaces:
```console
$ basename "/path/with spaces/file.txt"
file.txt
```

## Frequently Asked Questions

#### Q1. What's the difference between `basename` and `dirname`?
A. `basename` extracts the final component (filename) from a path, while `dirname` extracts the directory portion of the path.

#### Q2. How do I remove multiple extensions (like .tar.gz)?
A. `basename` only removes one suffix at a time. For multiple extensions, you'll need to use it multiple times or use shell parameter expansion.

#### Q3. Does `basename` work with relative paths?
A. Yes, it works with both absolute and relative paths, extracting the final component in either case.

#### Q4. Can `basename` handle paths with spaces?
A. Yes, but you need to quote the path arguments to prevent the shell from splitting them.

## References

https://www.gnu.org/software/coreutils/manual/html_node/basename-invocation.html

## Revisions

- 2025/04/30 First revision