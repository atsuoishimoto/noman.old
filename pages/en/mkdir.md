# mkdir command

Create directories with specified names.

## Overview

The `mkdir` command creates new directories in the file system. It allows you to create single or multiple directories at once, set permissions, and create parent directories as needed. This is one of the most fundamental commands for organizing files in Unix-like systems.

## Options

### **-p, --parents**

Create parent directories as needed. If you specify a path where some directories don't exist yet, this option creates them automatically.

```console
$ mkdir -p projects/website/css
```

### **-m, --mode=MODE**

Set file permissions for newly created directories. This allows you to specify permissions at creation time rather than changing them afterward.

```console
$ mkdir -m 755 scripts
$ ls -ld scripts
drwxr-xr-x 2 user group 4096 May 4 10:30 scripts
```

### **-v, --verbose**

Print a message for each created directory, showing what's being created.

```console
$ mkdir -v backup
mkdir: created directory 'backup'
```

## Usage Examples

### Creating multiple directories at once

```console
$ mkdir docs images videos
$ ls
docs  images  videos
```

### Creating nested directories with parent creation

```console
$ mkdir -p projects/webapp/src/components
$ ls -R projects
projects:
webapp

projects/webapp:
src

projects/webapp/src:
components
```

### Creating a directory with specific permissions

```console
$ mkdir -m 700 private
$ ls -ld private
drwx------ 2 user group 4096 May 4 10:35 private
```

## Tips:

### Use Tab Completion

When creating directories in existing paths, use tab completion to avoid typing errors and save time.

### Create and Change Directory in One Step

Combine with `cd` to create and navigate to a directory in one step:
```console
$ mkdir new_project && cd new_project
```

### Use Brace Expansion for Related Directories

Create multiple related directories efficiently:
```console
$ mkdir -p project/{src,docs,tests,build}
```
This creates four subdirectories under "project" in a single command.

## Frequently Asked Questions

#### Q1. How do I create a directory with spaces in the name?
A. Use quotes or escape the spaces with backslashes: `mkdir "My Documents"` or `mkdir My\ Documents`.

#### Q2. Can I create multiple nested directories at once?
A. Yes, use the `-p` option: `mkdir -p path/to/new/directory`.

#### Q3. How do I check if a directory exists before creating it?
A. The `-p` option is safe to use even if directories already exist. Alternatively, use `[ -d directory ] || mkdir directory`.

#### Q4. What happens if I try to create a directory that already exists?
A. Without options, `mkdir` will show an error. With `-p`, it will silently continue without creating the existing directory.

## References

https://www.gnu.org/software/coreutils/manual/html_node/mkdir-invocation.html

## Revisions

- 2025/05/04 First revision