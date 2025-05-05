# tree command

Display directory contents in a tree-like format, showing the hierarchical structure of directories and files.

## Overview

The `tree` command recursively displays the contents of directories in a tree-like format, making it easy to visualize directory structures. It shows files and directories with indentation and connecting lines to represent the hierarchy, providing a clear view of how files are organized.

## Options

### **-a, --all**

Display all files, including hidden files (those starting with a dot)

```console
$ tree -a
.
├── .git
│   ├── HEAD
│   ├── config
│   └── hooks
├── README.md
└── src
    ├── .env
    └── main.js

3 directories, 5 files
```

### **-d, --dirs-only**

List directories only, not files

```console
$ tree -d
.
├── docs
├── node_modules
│   ├── express
│   └── lodash
└── src
    └── components

5 directories
```

### **-L, --level [level]**

Limit the depth of directory recursion to the specified level

```console
$ tree -L 2
.
├── docs
├── node_modules
│   ├── express
│   └── lodash
├── package.json
└── src
    ├── components
    └── index.js

5 directories, 2 files
```

### **-I, --ignore [pattern]**

Ignore files/directories that match the pattern (uses shell glob patterns)

```console
$ tree -I "node_modules"
.
├── docs
├── package.json
└── src
    ├── components
    │   └── Button.js
    └── index.js

3 directories, 3 files
```

### **-C, --color**

Turn on colorized output

```console
$ tree -C
```

### **-F, --classify**

Append indicators to entries (/ for directories, * for executable files, etc.)

```console
$ tree -F
.
├── docs/
├── package.json
└── src/
    ├── components/
    │   └── Button.js
    └── index.js*

3 directories, 3 files
```

### **-h, --human-readable**

Print sizes in human-readable format (e.g., 1K, 234M, 2G)

```console
$ tree -h
.
├── [4.0K]  docs
├── [ 340]  package.json
└── [4.0K]  src
    ├── [4.0K]  components
    │   └── [1.2K]  Button.js
    └── [ 256]  index.js

3 directories, 3 files
```

## Usage Examples

### Basic directory listing

```console
$ tree
.
├── docs
│   └── README.md
├── package.json
└── src
    ├── components
    │   └── Button.js
    └── index.js

3 directories, 3 files
```

### Limiting depth and showing only specific file types

```console
$ tree -L 2 --prune -P "*.js"
.
├── package.json
└── src
    ├── components
    └── index.js

2 directories, 2 files
```

### Showing file sizes with human-readable format

```console
$ tree -h --du
.
├── [4.0K]  docs
│   └── [ 340]  README.md
├── [ 340]  package.json
└── [5.5K]  src
    ├── [4.3K]  components
    │   └── [1.2K]  Button.js
    └── [ 256]  index.js

3 directories, 3 files
```

## Tips

### Save Tree Output to a File

You can redirect the output to a file for documentation purposes:
```console
$ tree > directory_structure.txt
```

### Exclude Multiple Patterns

Use multiple `-I` options or separate patterns with pipes:
```console
$ tree -I "node_modules|*.log|.git"
```

### Find Large Directories

Combine `-h` with `--du` to show directory sizes and identify space-consuming directories:
```console
$ tree -h --du -d
```

### Custom Output Format

Use `-J` for JSON output or `-X` for XML output when you need to process the directory structure programmatically.

## Frequently Asked Questions

#### Q1. How do I install tree on my system?
A. On Debian/Ubuntu: `sudo apt install tree`, on macOS with Homebrew: `brew install tree`, on CentOS/RHEL: `sudo yum install tree`.

#### Q2. How can I limit the depth of directories shown?
A. Use the `-L` option followed by the depth level: `tree -L 2` will show only two levels deep.

#### Q3. How do I exclude certain directories from the output?
A. Use the `-I` option followed by a pattern: `tree -I "node_modules"` will exclude the node_modules directory.

#### Q4. How can I show only directories?
A. Use the `-d` option: `tree -d` will show only directories, not files.

#### Q5. How do I show hidden files?
A. Use the `-a` option: `tree -a` will show all files including hidden ones.

## References

https://linux.die.net/man/1/tree

## Revisions

- 2025/05/04 First revision