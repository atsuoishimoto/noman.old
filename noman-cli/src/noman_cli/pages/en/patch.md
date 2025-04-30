# patch command

Apply a diff file to an original file or files.

## Overview

The `patch` command applies changes (patches) to files. It reads a patch file (typically created by the `diff` command) and modifies the original files to incorporate those changes. This is commonly used for applying bug fixes, updates, or modifications to source code and text files.

## Options

### **-p[num]**

Strip the smallest prefix containing `num` leading slashes from each file name in the patch. This helps when patch paths don't match your local directory structure.

```console
$ patch -p1 < changes.patch
patching file src/main.c
```

### **-b, --backup**

Create backup files of the originals before patching.

```console
$ patch -b main.c < fix.patch
patching file main.c
$ ls main.c*
main.c  main.c.orig
```

### **-R, --reverse**

Assume patches were created with old and new files swapped, effectively reversing the patch.

```console
$ patch -R < changes.patch
patching file main.c
```

### **-d dir, --directory=dir**

Change to the specified directory before applying the patch.

```console
$ patch -d src/ < changes.patch
patching file main.c
```

### **--dry-run**

Print the results of applying the patches without actually changing any files.

```console
$ patch --dry-run < changes.patch
patching file main.c
```

## Usage Examples

### Basic Patch Application

```console
$ diff -u original.txt modified.txt > changes.patch
$ patch < changes.patch
patching file original.txt
```

### Applying a Patch to a Different Directory

```console
$ patch -p0 -d project/ < changes.patch
patching file src/main.c
```

### Creating and Applying a Patch for Multiple Files

```console
$ diff -Naur original_dir/ modified_dir/ > project.patch
$ patch -p1 < project.patch
patching file src/main.c
patching file include/header.h
```

## Tips

### Understanding Patch Formats

The most common patch formats are unified (`diff -u`) and context (`diff -c`). Unified format is more compact and readable, showing a few lines of context around each change with `+` for added lines and `-` for removed lines.

### Testing Patches Before Applying

Always use `--dry-run` to test a patch before applying it to important files. This shows what would happen without making actual changes.

### Handling Failed Patches

If a patch fails to apply cleanly, patch will create `.rej` files containing the rejected hunks. Examine these files to manually apply the changes that couldn't be applied automatically.

### Creating Patches

To create a patch file, use the `diff` command with the `-u` option for unified format:
```console
$ diff -u original_file modified_file > changes.patch
```

## Frequently Asked Questions

#### Q1. How do I apply a patch file?
A. Use `patch < patchfile` to apply changes to the files mentioned in the patch file.

#### Q2. How do I reverse a patch I've applied?
A. Use `patch -R < patchfile` to undo changes made by a patch.

#### Q3. What does "Hunk #1 FAILED" mean?
A. It means that a section of the patch couldn't be applied, usually because the target file has been modified since the patch was created. Check the `.rej` file for the failed changes.

#### Q4. How do I handle patches with incorrect file paths?
A. Use the `-p` option to strip path prefixes. For example, `patch -p1` removes the first directory level from paths in the patch file.

#### Q5. Can I preview what a patch will do before applying it?
A. Yes, use `patch --dry-run < patchfile` to see what would happen without making changes.

## References

https://www.gnu.org/software/diffutils/manual/html_node/Invoking-patch.html

## Revisions

- 2025/04/30 First revision