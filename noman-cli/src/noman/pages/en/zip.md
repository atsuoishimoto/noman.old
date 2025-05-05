# zip command

Package files into a compressed archive.

## Overview

The `zip` command creates compressed archives in ZIP format, which can contain one or more files or directories. It's commonly used for file compression, backup, and sharing files across different operating systems. ZIP is a widely supported format that maintains file attributes and directory structures.

## Options

### **-r, --recurse-paths**

Recursively include files in subdirectories

```console
$ zip -r archive.zip documents/
  adding: documents/ (stored 0%)
  adding: documents/report.txt (deflated 35%)
  adding: documents/images/ (stored 0%)
  adding: documents/images/photo.jpg (deflated 2%)
```

### **-e, --encrypt**

Encrypt the contents of the ZIP archive with a password

```console
$ zip -e secure.zip confidential.txt
Enter password: 
Verify password: 
  adding: confidential.txt (deflated 42%)
```

### **-u, --update**

Update existing entries in the ZIP archive and add new files

```console
$ zip -u archive.zip newfile.txt updated.txt
  adding: newfile.txt (deflated 30%)
  updating: updated.txt (deflated 25%)
```

### **-d, --delete**

Delete entries from a ZIP archive

```console
$ zip -d archive.zip unwanted.txt
deleting: unwanted.txt
```

### **-j, --junk-paths**

Store just the file names without directory paths

```console
$ zip -j flat.zip documents/report.txt documents/images/photo.jpg
  adding: report.txt (deflated 35%)
  adding: photo.jpg (deflated 2%)
```

### **-9, --compress-level**

Set the compression level (0-9, where 9 is maximum compression)

```console
$ zip -9 compressed.zip largefile.dat
  adding: largefile.dat (deflated 68%)
```

## Usage Examples

### Creating a basic ZIP archive

```console
$ zip backup.zip file1.txt file2.txt
  adding: file1.txt (deflated 32%)
  adding: file2.txt (deflated 28%)
```

### Zipping an entire directory with subdirectories

```console
$ zip -r project.zip project/
  adding: project/ (stored 0%)
  adding: project/src/ (stored 0%)
  adding: project/src/main.c (deflated 45%)
  adding: project/docs/ (stored 0%)
  adding: project/docs/readme.md (deflated 38%)
```

### Creating a password-protected ZIP with maximum compression

```console
$ zip -e -9 secure-archive.zip important/*.pdf
Enter password: 
Verify password: 
  adding: important/document1.pdf (deflated 15%)
  adding: important/document2.pdf (deflated 12%)
```

## Tips:

### View ZIP Contents Without Extracting

Use the companion command `unzip -l archive.zip` to list the contents of a ZIP file without extracting it.

### Create Self-Extracting Archives

On some systems, you can create self-extracting archives with `zip -A archive.zip`, though this is primarily useful on Windows systems.

### Exclude Specific Files

Use patterns with the `-x` option to exclude certain files: `zip -r archive.zip directory/ -x "*.tmp" "*.log"`.

### Split Large ZIP Files

For very large archives, use the `-s` option to split the ZIP into smaller parts: `zip -s 100m -r large.zip bigdirectory/`.

## Frequently Asked Questions

#### Q1. How do I extract a ZIP file?
A. Use the companion command `unzip archive.zip` to extract files from a ZIP archive.

#### Q2. Can I add files to an existing ZIP archive?
A. Yes, use `zip -u archive.zip newfiles` to add or update files in an existing archive.

#### Q3. How do I create a ZIP file without compressing the files?
A. Use `zip -0 archive.zip files` to store files without compression (useful for already compressed files like JPEGs).

#### Q4. How can I password-protect a ZIP file?
A. Use `zip -e archive.zip files` to create an encrypted ZIP file. You'll be prompted to enter a password.

#### Q5. How do I preserve file permissions when creating a ZIP archive?
A. On Unix-like systems, use `zip -X archive.zip files` to preserve file permissions and UID/GID information.

## macOS Considerations

On macOS, the built-in Archive Utility creates ZIP files that may not preserve certain Unix file attributes. For more control, use the command-line `zip` utility. Also, be aware that macOS creates hidden `.DS_Store` files in directories, which will be included in your ZIP archives unless explicitly excluded with `-x "*.DS_Store"`.

## References

https://linux.die.net/man/1/zip

## Revisions

- 2025/05/04 First revision