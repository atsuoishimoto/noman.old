# mkdir command

Create directories with specified names.

## Overview

The `mkdir` command creates one or more directories (folders) in your file system. If a directory already exists, `mkdir` will typically fail unless you use specific options. It's a fundamental command for organizing files and setting up directory structures.

## Options

### **-p, --parents**

Create parent directories as needed. This allows you to create an entire directory path in one command, even if the parent directories don't exist yet.

```console
$ mkdir -p projects/website/css
```

### **-m, --mode=MODE**

Set file mode (permissions) for the created directories. The mode can be specified as an octal number.

```console
$ mkdir -m 755 secure_folder
```

### **-v, --verbose**

Print a message for each created directory, showing what's being created.

```console
$ mkdir -v new_folder
mkdir: created directory 'new_folder'
```

### **-Z, --context=CONTEXT**

Set the SELinux security context of each created directory to the default type.

```console
$ mkdir -Z secure_data
```

## Usage Examples

### Creating multiple directories at once

```console
$ mkdir docs images videos
```

### Creating a directory with specific permissions

```console
$ mkdir -m 700 private_files
$ ls -ld private_files
drwx------ 2 user user 4096 May 4 10:30 private_files
```

### Creating nested directories with verbose output

```console
$ mkdir -pv projects/webapp/src/components
mkdir: created directory 'projects'
mkdir: created directory 'projects/webapp'
mkdir: created directory 'projects/webapp/src'
mkdir: created directory 'projects/webapp/src/components'
```

## Tips:

### Use Tab Completion

When creating directories in existing paths, use tab completion to avoid typing errors and save time.

### Create and Change Directory in One Step

Combine `mkdir` with `cd` using `&&` to create a directory and immediately navigate into it:
```console
$ mkdir new_project && cd new_project
```

### Use Brace Expansion for Related Directories

Create multiple related directories efficiently with brace expansion:
```console
$ mkdir -p project/{src,docs,tests}/{js,css,img}
```
This creates a structured project with subdirectories for source code, documentation, and tests, each with js, css, and img folders.

## Frequently Asked Questions

#### Q1. How do I create a directory if it doesn't already exist?
A. Use `mkdir -p directory_name`. The `-p` option ensures the command won't fail if the directory already exists.

#### Q2. How do I create multiple nested directories at once?
A. Use `mkdir -p parent/child/grandchild`. The `-p` option creates all directories in the path.

#### Q3. How can I set specific permissions when creating a directory?
A. Use `mkdir -m MODE directory_name`, where MODE is the octal permission value (e.g., `mkdir -m 755 directory_name`).

#### Q4. What happens if I try to create a directory that already exists?
A. Without the `-p` option, `mkdir` will display an error. With `-p`, it will silently continue without error.

## References

https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html

## Revisions

- 2025/05/04 First revision