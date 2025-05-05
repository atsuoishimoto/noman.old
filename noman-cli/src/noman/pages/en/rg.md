# rg command

Search for patterns in files using regular expressions, with support for recursive directory traversal.

## Overview

`rg` (ripgrep) is a line-oriented search tool that recursively searches the current directory for a regex pattern. It's designed to be faster than other search tools like grep, ag, or ack, while offering similar functionality with sensible defaults. By default, ripgrep respects gitignore rules and automatically skips hidden files/directories and binary files.

## Options

### **-i, --ignore-case**

Makes the search case insensitive.

```console
$ rg -i error
./log.txt:10:ERROR: Connection failed
./log.txt:15:error: timeout occurred
./app.js:42:console.log('error handling');
```

### **-v, --invert-match**

Show lines that don't match the given pattern.

```console
$ rg -v error test.log
./test.log:1:Starting application
./test.log:2:Loading configuration
./test.log:5:Application running
```

### **-w, --word-regexp**

Only show matches surrounded by word boundaries.

```console
$ rg -w log
./app.js:42:console.log('error handling');
./utils.js:15:function log(message) {
```

### **-c, --count**

Only show the count of matching lines for each file.

```console
$ rg -c error logs/
logs/app.log:15
logs/system.log:3
logs/debug.log:0
```

### **-l, --files-with-matches**

Only show the paths with at least one match.

```console
$ rg -l error
logs/app.log
logs/system.log
src/error_handler.js
```

### **--no-ignore**

Don't respect ignore files (.gitignore, .ignore, etc.).

```console
$ rg --no-ignore password
.git/config:3:password=secret123
node_modules/test-lib/passwords.json:5:"default_password": "admin"
```

### **-A, --after-context NUM**

Show NUM lines after each match.

```console
$ rg -A 2 error app.log
app.log:15:error: connection failed
app.log:16:  at line 42 in network.js
app.log:17:  attempted reconnect
```

### **-B, --before-context NUM**

Show NUM lines before each match.

```console
$ rg -B 2 error app.log
app.log:13:attempting connection
app.log:14:using default timeout
app.log:15:error: connection failed
```

## Usage Examples

### Searching in specific file types

```console
$ rg -t js console.log
src/main.js:10:  console.log('Application started');
src/utils.js:25:  console.log('Loading data...');
```

### Searching with multiple patterns

```console
$ rg 'error|warning|critical' logs/app.log
logs/app.log:15:error: connection failed
logs/app.log:23:warning: slow response time
logs/app.log:45:critical: database unavailable
```

### Searching with file name pattern

```console
$ rg TODO -g '*.js'
src/app.js:42:// TODO: Implement error handling
src/utils.js:78:// TODO: Optimize this function
```

## Tips:

### Use Smart Case for Flexible Matching

Use `-S` or `--smart-case` to perform case-insensitive searches when the pattern is all lowercase, but case-sensitive searches when the pattern contains uppercase letters.

### Combine with Other Commands

Pipe `rg` output to other commands for further processing:
```console
$ rg -n 'TODO|FIXME' --no-heading | sort -k1,1
```

### Search in Compressed Files

Use `--search-zip` to search in compressed files like .gz or .zip:
```console
$ rg --search-zip "error" logs/
```

### Exclude Specific Directories

Use `--glob=!{dir}` to exclude specific directories:
```console
$ rg "function" --glob=!{node_modules,dist}
```

## Frequently Asked Questions

#### Q1. How is ripgrep different from grep?
A. Ripgrep is generally faster than grep, automatically recursive, respects .gitignore rules by default, and has built-in support for many file types and encodings.

#### Q2. How do I search for a pattern with spaces?
A. Enclose the pattern in quotes: `rg "search pattern with spaces"`.

#### Q3. How can I make ripgrep search hidden files and directories?
A. Use the `--hidden` flag: `rg --hidden pattern`.

#### Q4. How do I search for a literal string instead of a regex pattern?
A. Use the `-F` or `--fixed-strings` option: `rg -F "string with (special) characters"`.

#### Q5. What does the --no-ignore option do?
A. The `--no-ignore` option tells ripgrep to ignore all ignore files (.gitignore, .ignore, etc.) and search all files, including those that would normally be excluded based on ignore patterns.

## References

https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md

## Revisions

- 2025/05/04 Added explanation for --no-ignore option and expanded FAQs.