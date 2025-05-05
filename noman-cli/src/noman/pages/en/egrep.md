# egrep command

Search for patterns in text using extended regular expressions.

## Overview

`egrep` is a pattern-matching tool that searches for lines in files or standard input that match a specified pattern. It's functionally equivalent to `grep -E`, using extended regular expressions which provide more powerful pattern matching capabilities than basic grep. This command is commonly used for searching through code, logs, and text files.

## Options

### **-i, --ignore-case**

Perform case-insensitive matching

```console
$ egrep -i "error" logfile.txt
ERROR: Connection failed
error: file not found
Warning: Some errors were detected
```

### **-v, --invert-match**

Select non-matching lines

```console
$ egrep -v "success" logfile.txt
ERROR: Connection failed
Warning: operation incomplete
Process terminated unexpectedly
```

### **-c, --count**

Print only a count of matching lines

```console
$ egrep -c "error" logfile.txt
3
```

### **-n, --line-number**

Prefix each line of output with its line number in the input file

```console
$ egrep -n "error" logfile.txt
5:error: file not found
12:error: permission denied
27:error: timeout occurred
```

### **-l, --files-with-matches**

Print only the names of files containing matches

```console
$ egrep -l "error" *.log
app.log
system.log
error.log
```

### **-r, --recursive**

Read all files under each directory, recursively

```console
$ egrep -r "password" /home/user/
/home/user/config.txt:password=12345
/home/user/notes/secret.txt:my password hint
```

## Usage Examples

### Using Extended Regular Expressions

```console
$ egrep "(error|warning)" logfile.txt
error: file not found
warning: disk space low
error: permission denied
```

### Matching Multiple Patterns

```console
$ egrep "user[0-9]+" users.txt
user123 logged in at 14:30
user456 account created
user789 password changed
```

### Combining Options

```console
$ egrep -in "fail(ed|ure)" *.log
app.log:15:Connection failed to server
system.log:42:System failure detected
network.log:7:Authentication failed for user admin
```

## Tips:

### Use Word Boundaries for Precise Matching

Use `\b` to match word boundaries for more precise results:

```console
$ egrep "\berror\b" logfile.txt
```

This matches "error" but not "errors" or "errorless".

### Colorize Matches for Better Visibility

Most modern implementations of egrep automatically colorize matches, but you can ensure this with:

```console
$ egrep --color "pattern" file.txt
```

### Remember egrep is Equivalent to grep -E

`egrep` is deprecated in some systems in favor of `grep -E`. They function identically, but `grep -E` is more portable.

## Frequently Asked Questions

#### Q1. What's the difference between grep and egrep?
A. `egrep` uses extended regular expressions by default, which is equivalent to `grep -E`. Extended regex syntax allows special characters like `+`, `?`, `|`, `()` without escaping them.

#### Q2. How do I search for a pattern in multiple files?
A. Simply list the files after the pattern: `egrep "pattern" file1.txt file2.txt` or use wildcards: `egrep "pattern" *.txt`.

#### Q3. How can I exclude certain patterns from my search?
A. Use the `-v` option: `egrep -v "pattern_to_exclude" file.txt`.

#### Q4. Can egrep search compressed files?
A. No, not directly. For compressed files, use specialized tools like `zgrep` for gzipped files.

## References

https://www.gnu.org/software/grep/manual/grep.html

## Revisions

- 2025/05/04 First revision