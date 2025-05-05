# grep command

Search for patterns in files.

## Overview

`grep` is a powerful text search utility that searches for lines matching a specified pattern in files or standard input. It's commonly used to find specific text within files, filter command output, or search through large datasets. The name comes from "global regular expression print."

## Options

### **-i, --ignore-case**

Perform case-insensitive matching.

```console
$ grep -i "hello" file.txt
Hello World
HELLO everyone
hello there
```

### **-v, --invert-match**

Invert the match, showing lines that don't match the pattern.

```console
$ grep -v "error" log.txt
Starting application
Loading configuration
Application running
Shutting down
```

### **-r, --recursive**

Search recursively through directories.

```console
$ grep -r "TODO" ./src/
./src/main.c:// TODO: Implement error handling
./src/utils.h:/* TODO: Add documentation */
./src/config.c:// TODO: Fix configuration parsing
```

### **-l, --files-with-matches**

Only print filenames of files containing matches.

```console
$ grep -l "function" *.js
utils.js
main.js
helpers.js
```

### **-n, --line-number**

Show line numbers for matching lines.

```console
$ grep -n "import" app.py
3:import os
5:import sys
12:import datetime
```

### **-c, --count**

Print only the count of matching lines per file.

```console
$ grep -c "error" *.log
app.log:15
system.log:3
access.log:0
```

### **-A NUM, --after-context=NUM**

Show NUM lines after each match.

```console
$ grep -A 2 "function main" main.c
function main() {
  int x = 5;
  printf("Starting program\n");
```

### **-B NUM, --before-context=NUM**

Show NUM lines before each match.

```console
$ grep -B 1 "Exception" error.log
2023-05-04 15:30:22 Processing request
2023-05-04 15:30:23 Exception: Invalid input
```

### **-E, --extended-regexp**

Use extended regular expressions.

```console
$ grep -E "(error|warning)" log.txt
System error: disk full
Warning: connection timeout
```

## Usage Examples

### Basic Pattern Search

```console
$ grep "password" config.txt
password=mysecretpassword
# default password is 'admin'
```

### Combining Multiple Options

```console
$ grep -in "todo" --color *.py
utils.py:45:# TODO: Refactor this function
helpers.py:23:# todo: Add error handling
main.py:102:# TODO: Implement caching
```

### Using Regular Expressions

```console
$ grep "^[0-9]" data.txt
123 Main St
456 Oak Ave
789 Pine Rd
```

### Piping Command Output to grep

```console
$ ps aux | grep "firefox"
user     12345  2.5  1.8 3458196 298796 ?      Sl   09:15   0:45 /usr/lib/firefox/firefox
```

## Tips

### Use Context for Better Understanding

Combine `-A`, `-B`, or `-C` (for both before and after context) to see the surrounding lines of a match, which helps understand the context of the match.

### Colorize Matches for Visibility

Use `--color=auto` to highlight matching text in color, making it easier to spot in large outputs. Many systems alias grep to include this by default.

### Exclude Directories

When searching recursively, use `--exclude-dir=PATTERN` to skip directories matching PATTERN, which can significantly speed up searches in large codebases.

### Search for Exact Words

Use `-w` or `--word-regexp` to match only whole words, preventing partial matches within larger words.

### Quiet Mode for Scripts

Use `-q` or `--quiet` in scripts to suppress output and just use the exit status to determine if a match was found.

## Frequently Asked Questions

#### Q1. How do I search for a pattern in multiple files?
A. Simply list the files after the pattern: `grep "pattern" file1.txt file2.txt file3.txt` or use wildcards: `grep "pattern" *.txt`.

#### Q2. How can I search for a pattern that contains spaces?
A. Enclose the pattern in quotes: `grep "hello world" file.txt`.

#### Q3. How do I search for a pattern that includes special characters?
A. Escape special characters with a backslash or use single quotes: `grep 'pattern\*' file.txt` or `grep "pattern\*" file.txt`.

#### Q4. Can grep search for multiple patterns at once?
A. Yes, use the `-e` option multiple times or use extended regex with `-E`: `grep -e "pattern1" -e "pattern2" file.txt` or `grep -E "pattern1|pattern2" file.txt`.

#### Q5. How do I make grep show only the matching part of a line?
A. Use the `-o` or `--only-matching` option: `grep -o "pattern" file.txt`.

## References

https://www.gnu.org/software/grep/manual/grep.html

## Revisions

- 2025/05/04 First revision