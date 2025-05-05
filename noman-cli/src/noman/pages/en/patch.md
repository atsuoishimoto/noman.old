# patch command

Apply a diff file to an original file or files.

## Overview

The `patch` command applies changes (patches) to files. It reads a patch file (typically created by the `diff` command) and modifies the original file(s) according to the instructions in the patch. This is commonly used for applying bug fixes, updates, or modifications to source code and text files.

## Options

### **-p num, --strip=num**

Strip the smallest prefix containing num leading slashes from each file name found in the patch file.

```console
$ patch -p1 < changes.patch
patching file src/main.c
```

### **-b, --backup**

Create a backup of the original file before applying the patch.

```console
$ patch -b file.txt < changes.patch
patching file file.txt
```

### **-R, --reverse**

Assume that the patch was created with the old and new files swapped, effectively reversing the patch.

```console
$ patch -R file.txt < changes.patch
patching file file.txt
```

### **-i patchfile, --input=patchfile**

Read the patch from the specified file instead of standard input.

```console
$ patch -i changes.patch
patching file file.txt
```

### **-d dir, --directory=dir**

Change to the specified directory before applying the patch.

```console
$ patch -d src/ -i ../changes.patch
patching file main.c
```

### **-u, --unified**

Interpret the patch file as a unified diff (the most common format nowadays).

```console
$ patch -u file.txt < changes.patch
patching file file.txt
```

## Usage Examples

### Basic Patch Application

```console
$ diff -u original.txt modified.txt > changes.patch
$ patch original.txt < changes.patch
patching file original.txt
```

### Applying a Patch to Multiple Files

```console
$ patch -p0 < project.patch
patching file src/main.c
patching file include/header.h
```

### Creating and Applying a Backup

```console
$ patch -b file.txt < changes.patch
patching file file.txt
$ ls
file.txt  file.txt.orig  changes.patch
```

### Dry Run (Check Without Applying)

```console
$ patch --dry-run -p1 < changes.patch
checking file src/main.c
```

## Tips:

### Understanding Patch Levels

The `-p` option (strip level) is crucial when applying patches to projects. If your patch contains paths like `a/src/file.c`, using `-p1` will strip the `a/` prefix, making it look for `src/file.c`.

### Handling Failed Patches

If a patch fails to apply cleanly, patch creates `.rej` files containing the rejected hunks. Examine these files to manually apply the changes that couldn't be applied automatically.

### Testing Patches Before Applying

Always use `--dry-run` to test if a patch will apply cleanly before actually applying it, especially for important files.

### Patch Direction

If you're unsure whether to use `-R` (reverse), try applying the patch normally first. If it fails with "reversed patch detected," then try with `-R`.

## Frequently Asked Questions

#### Q1. What's the difference between a unified diff and a context diff?
A. Unified diffs (`-u` option in diff) show changed lines with context in a single block prefixed with `+` and `-`, while context diffs show before and after blocks separately. Unified diffs are more compact and commonly used today.

#### Q2. How do I reverse an applied patch?
A. Use `patch -R` with the same patch file to undo changes. If you created backups with `-b`, you can also restore from those.

#### Q3. What does "Hunk #1 FAILED" mean?
A. It means that a section (hunk) of the patch couldn't be applied, usually because the target file has been modified since the patch was created. Check the `.rej` file for the failed changes.

#### Q4. How do I apply a patch to multiple files?
A. If the patch file contains changes for multiple files, patch will automatically apply changes to all affected files when you run it.

## References

https://www.gnu.org/software/diffutils/manual/html_node/Invoking-patch.html

## Revisions

- 2025/05/04 First revision