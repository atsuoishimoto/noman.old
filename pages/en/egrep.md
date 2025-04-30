# egrep command

Search for patterns in text using extended regular expressions.

## Overview

`egrep` is a pattern-matching tool that searches for text patterns in files using extended regular expressions. It's functionally equivalent to `grep -E` and provides more powerful pattern matching capabilities than standard `grep`. When a match is found, `egrep` prints the matching lines.

## Options

### **-i** (ignore case)

Performs case-insensitive matching

```console
$ egrep -i "error" logfile.txt
ERROR: Connection failed
error: file not found
Warning: Some errors were detected
```

### **-v** (invert match)

Shows lines that do NOT match the pattern

```console
$ egrep -v "success" logfile.txt
ERROR: Connection failed
Warning: operation incomplete
Process terminated unexpectedly
```

### **-n** (line numbers)

Displays line numbers along with matching lines

```console
$ egrep -n "warning" logfile.txt
3:Warning: disk space low
7:warning: connection unstable
15:Warning: operation timed out
```

### **-c** (count)

Shows only the count of matching lines

```console
$ egrep -c "error" logfile.txt
5
```

### **-l** (files with matches)

Lists only the names of files containing matches

```console
$ egrep -l "error" *.log
system.log
application.log
```

### **-r** (recursive)

Searches directories recursively

```console
$ egrep -r "password" /home/user/documents/
/home/user/documents/config.txt:password=123456
/home/user/documents/notes/credentials.md:temporary password: admin123
```

## Usage Examples

### Basic Pattern Matching

```console
$ egrep "apple|orange" fruits.txt
apple
orange
mixed apple juice
fresh orange
```

### Using Extended Regular Expressions

```console
$ egrep "Feb(ruary)? [0-9]{1,2}" calendar.txt
February 14 - Valentine's Day
Feb 29 - Leap Day
```

### Combining Multiple Options

```console
$ egrep -in "error|warning|critical" --color=auto system.log
12:ERROR: system failure detected
45:warning: memory usage high
67:CRITICAL: service unavailable
```

## Tips

### Use Color Highlighting
Add `--color=auto` to highlight matching text in color, making it easier to spot matches in large outputs.

### Understand Basic Regex Patterns
- `|` means "OR" (match either pattern)
- `?` means the preceding character is optional
- `+` means one or more of the preceding character
- `*` means zero or more of the preceding character
- `[0-9]` matches any digit, `[a-z]` matches any lowercase letter
- `{n}` specifies exactly n occurrences of the preceding character

### Pipe with Other Commands
Combine `egrep` with other commands using pipes for powerful text processing:
```console
$ ps aux | egrep "(nginx|apache)"
```

## Frequently Asked Questions

#### Q1. What's the difference between `grep` and `egrep`?
A. `egrep` is equivalent to `grep -E`, which uses extended regular expressions. Extended regex provides more powerful pattern matching with special characters like `+`, `?`, `|`, and parentheses without needing to escape them.

#### Q2. How do I search for a pattern in multiple files?
A. Simply list the files after your pattern: `egrep "pattern" file1.txt file2.txt`. You can also use wildcards: `egrep "pattern" *.txt`.

#### Q3. How can I exclude certain patterns?
A. Use the `-v` option: `egrep -v "pattern"` shows lines that don't match the pattern.

#### Q4. Can I search for whole words only?
A. Yes, use the `-w` option: `egrep -w "word"` matches only when "word" appears as a complete word, not as part of another word.

## References

https://www.gnu.org/software/grep/manual/grep.html

## Revisions

- 2025/04/30 First revision