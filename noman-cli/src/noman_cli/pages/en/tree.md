# tree command

Display directory structure in a hierarchical, tree-like format.

## Overview

The `tree` command recursively lists the contents of directories in a tree-like format, making it easy to visualize the structure of your file system. It shows files and directories with indentation and connecting lines to represent the hierarchy.

## Options

### **-L [level]**

Limit the depth of directory recursion

```console
$ tree -L 2
.
├── documents
│   ├── work
│   └── personal
├── images
│   ├── vacation
│   └── screenshots
└── projects
    ├── website
    └── app
```

### **-d**

List directories only, excluding files

```console
$ tree -d
.
├── documents
│   ├── work
│   └── personal
├── images
│   ├── vacation
│   └── screenshots
└── projects
    ├── website
    └── app
```

### **-a**

Show all files, including hidden files (those starting with a dot)

```console
$ tree -a
.
├── .git
│   ├── HEAD
│   ├── config
│   └── hooks
├── documents
│   └── .hidden_file.txt
└── .gitignore
```

### **-I [pattern]**

Exclude files matching the specified pattern

```console
$ tree -I "*.jpg|*.png"
.
├── documents
│   ├── report.pdf
│   └── notes.txt
└── projects
    ├── index.html
    └── script.js
```

### **-p**

Print file permissions

```console
$ tree -p
.
├── [drwxr-xr-x]  documents
│   └── [-rw-r--r--]  report.pdf
└── [drwxr-xr-x]  projects
    └── [-rw-r--r--]  index.html
```

### **-s**

Print file sizes

```console
$ tree -s
.
├── [       4096]  documents
│   └── [      15240]  report.pdf
└── [       4096]  projects
    └── [        1024]  index.html
```

### **-h**

Print file sizes in human-readable format

```console
$ tree -h
.
├── [4.0K]  documents
│   └── [15K]  report.pdf
└── [4.0K]  projects
    └── [1.0K]  index.html
```

## Usage Examples

### Basic directory structure visualization

```console
$ tree
.
├── documents
│   ├── work
│   │   └── report.docx
│   └── personal
│       └── notes.txt
└── projects
    └── website
        ├── index.html
        └── style.css

5 directories, 4 files
```

### Combining multiple options

```console
$ tree -L 2 -h -p
.
├── [drwxr-xr-x 4.0K]  documents
│   ├── [drwxr-xr-x 4.0K]  work
│   └── [drwxr-xr-x 4.0K]  personal
└── [drwxr-xr-x 4.0K]  projects
    └── [drwxr-xr-x 4.0K]  website

5 directories, 0 files
```

### Outputting to a file

```console
$ tree > directory_structure.txt
$ cat directory_structure.txt
.
├── documents
│   ├── work
│   │   └── report.docx
│   └── personal
│       └── notes.txt
└── projects
    └── website
        ├── index.html
        └── style.css

5 directories, 4 files
```

## Tips

### Colorize Output
By default, `tree` often displays colorized output. If colors aren't showing, try using `tree -C` to force colorized output.

### Find Specific Files
Combine with `grep` to find specific files: `tree | grep "\.txt$"` will show the tree but highlight all .txt files.

### Large Directories
For large directories, use `-L` to limit depth and prevent overwhelming output. For example, `tree -L 2 /` shows only the first two levels of the root directory.

### Installation Note
`tree` is not installed by default on many systems. You may need to install it using your package manager (e.g., `apt install tree`, `brew install tree`).

## Frequently Asked Questions

#### Q1. How do I install the `tree` command?
A. On Ubuntu/Debian: `sudo apt install tree`. On macOS with Homebrew: `brew install tree`. On CentOS/RHEL: `sudo yum install tree`.

#### Q2. How can I exclude certain directories from the output?
A. Use the `-I` option followed by a pattern: `tree -I "node_modules|.git"` excludes both node_modules and .git directories.

#### Q3. How do I show only directories of a certain depth?
A. Use `-L` followed by the depth level: `tree -L 2` shows only the first two levels of directories.

#### Q4. Can I save the tree output to a file?
A. Yes, redirect the output: `tree > directory_structure.txt`.

#### Q5. How can I count files and directories?
A. `tree` automatically shows the count at the bottom of its output. For just the count, use `tree --noreport | wc -l`.

## References

https://linux.die.net/man/1/tree

## Revisions

- 2025/04/30 First revision