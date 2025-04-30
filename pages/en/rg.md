# rg command

Search for patterns in files using regular expressions, with a focus on speed and usability.

## Overview

`rg` (ripgrep) is a line-oriented search tool that recursively searches the current directory for a regex pattern. It's designed to be faster than other search tools like grep, ag, or ack while respecting gitignore rules by default. Ripgrep automatically skips hidden files, binary files, and files in version control directories unless told otherwise.

## Options

### **-i, --ignore-case**

Perform case insensitive matching

```console
$ rg -i error
config.js:10:function handleError(message) {
log.txt:52:ERROR: Connection refused
```

### **-v, --invert-match**

Show lines that don't match the pattern

```console
$ rg -v import src/
src/utils.js:2:// Helper functions
src/utils.js:3:function formatDate(date) {
```

### **-w, --word-regexp**

Only show matches surrounded by word boundaries

```console
$ rg -w log
logger.js:15:  log(message) {
logger.js:25:  const log = new Logger();
```

### **-c, --count**

Show the number of matching lines per file

```console
$ rg -c function src/
src/app.js:12
src/utils.js:5
src/components/button.js:3
```

### **--no-ignore**

Don't respect ignore files (.gitignore, .ignore, etc.)

```console
$ rg --no-ignore password
node_modules/some-package/test.js:10:const password = 'test123'
.git/config:15:password = hunter2
```

### **-A, --after-context NUM**

Show NUM lines after each match

```console
$ rg -A 2 "class User" src/
src/models/user.js:5:class User {
src/models/user.js:6:  constructor(name, email) {
src/models/user.js:7:    this.name = name;
```

### **-B, --before-context NUM**

Show NUM lines before each match

```console
$ rg -B 1 "throw new Error" src/
src/api.js:24:    if (!response.ok) {
src/api.js:25:      throw new Error('API request failed');
```

## Usage Examples

### Search in specific file types

```console
$ rg -t js "useState" src/
src/components/Counter.js:3:import { useState } from 'react';
src/components/Counter.js:6:  const [count, setCount] = useState(0);
```

### Search and replace (with confirmation)

```console
$ rg -l "http://" | xargs sed -i 's|http://|https://|g'
```

### Search with multiple patterns

```console
$ rg "export|import" src/app.js
src/app.js:1:import React from 'react';
src/app.js:2:import { useState } from 'react';
src/app.js:45:export default App;
```

## Tips:

### Use Fixed Strings for Faster Searches

When searching for literal text (not regex), use `-F` or `--fixed-strings` for better performance:

```console
$ rg -F "useState(" --type js
```

### Combine with Other Commands

Pipe `rg` output to other commands for further processing:

```console
$ rg -l "TODO" | xargs wc -l  # Count lines in files containing TODOs
```

### Search in Compressed Files

Use `--search-zip` to search in compressed files like .zip, .gz, etc.:

```console
$ rg --search-zip "error" logs/
```

## Frequently Asked Questions

#### Q1. How is ripgrep different from grep?
A. Ripgrep is generally faster, respects .gitignore files by default, and has more user-friendly features like colored output and automatic filtering of binary files.

#### Q2. How do I search in hidden files and directories?
A. Use `--hidden` to include hidden files and directories in the search.

#### Q3. How can I search for a pattern in files with specific extensions?
A. Use `-t` or `--type` followed by the file type: `rg -t js "pattern"` to search only in JavaScript files.

#### Q4. Why isn't ripgrep finding matches in files I know contain the pattern?
A. By default, ripgrep respects .gitignore and other ignore files. Use `--no-ignore` to search in ignored files.

## References

https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md

## Revisions

- 2025/04/30 Added explanation for --no-ignore option.
- 2025/04/30 First revision.