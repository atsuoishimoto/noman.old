# grep command

Search for patterns in files or text streams.

## Overview

`grep` is a powerful text search tool that finds lines matching a specified pattern in files or input streams. It's commonly used to filter output, search through code, or find specific content in text files. The name comes from "global regular expression print."

## Options

### **-i** (Ignore case)

Performs a case-insensitive search, matching both uppercase and lowercase letters.

```console
$ grep -i "error" log.txt
Error: Connection failed
error: file not found
WARNING: Some errors were detected
```

### **-r** or **-R** (Recursive)

Searches through all files in the specified directory and its subdirectories.

```console
$ grep -r "function" /path/to/project
/path/to/project/main.js:function initialize() {
/path/to/project/utils/helpers.js:const function calculateTotal() {
```

### **-v** (Invert match)

Shows lines that do NOT match the pattern.

```console
$ grep -v "success" log.txt
Error: Connection failed
Warning: Low disk space
Info: Process started
```

### **-n** (Line numbers)

Displays the line number before each matching line.

```console
$ grep -n "TODO" *.js
main.js:15:// TODO: Implement error handling
utils.js:42:// TODO: Optimize this algorithm
```

### **-c** (Count)

Shows only the count of matching lines for each file.

```console
$ grep -c "error" *.log
app.log:5
system.log:2
access.log:0
```

### **-A**, **-B**, and **-C** (Context)

Shows lines before (-B), after (-A), or both (-C) around each match.

```console
$ grep -A 2 "error" log.txt
error: file not found
  at line 42
  in module loader.js
```

## Usage Examples

### Basic pattern matching

```console
$ grep "password" config.txt
default_password=admin123
# password settings below
```

### Using regular expressions

```console
$ grep "^[0-9]" data.txt
123 Main Street
456 Oak Avenue
789 Pine Road
```

### Combining multiple options

```console
$ grep -in "warning" --color=auto *.log
app.log:15:Warning: Connection unstable
system.log:42:warning: low memory detected
```

### Piping output from another command

```console
$ ps aux | grep "firefox"
user     12345  2.5  1.8 3458196 298796 ?      Sl   09:15   0:45 /usr/lib/firefox/firefox
```

## Tips

### Use Color Highlighting
Enable color highlighting with `--color=auto` to make matches stand out. Add this to your shell profile as an alias: `alias grep='grep --color=auto'`.

### Understand Basic Regular Expressions
Learn basic regex patterns to make searches more powerful. For example, `^` matches the start of a line, `$` matches the end, and `[0-9]` matches any digit.

### Exclude Directories
When searching recursively, exclude directories with `--exclude-dir=PATTERN`: `grep -r "TODO" --exclude-dir=node_modules .`

### Search for Multiple Patterns
Use the `-e` option multiple times or the `-f` option with a file containing patterns: `grep -e "error" -e "warning" log.txt`

## Frequently Asked Questions

#### Q1. What's the difference between `grep`, `egrep`, and `fgrep`?
A. `egrep` is equivalent to `grep -E` (extended regex), and `fgrep` is equivalent to `grep -F` (fixed strings, no regex). Modern systems typically implement these as links to `grep` with the appropriate option.

#### Q2. How do I search for a pattern that contains spaces?
A. Enclose the pattern in quotes: `grep "search term with spaces" file.txt`

#### Q3. How can I make grep show only the matching part of a line?
A. Use the `-o` option: `grep -o "pattern" file.txt`

#### Q4. How do I search for a pattern in all files of a specific type?
A. Combine with find or use globbing: `grep "pattern" *.txt` or `find . -name "*.txt" -exec grep "pattern" {} \;`

## References

https://www.gnu.org/software/grep/manual/grep.html

## Revisions

- 2025/04/30 First revision