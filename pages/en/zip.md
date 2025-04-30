# zip command

Compress files and directories into a ZIP archive.

## Overview

The `zip` command creates compressed archives in the ZIP format, which is widely used across different operating systems. It can compress multiple files and directories into a single file, making it easier to transfer or store data while reducing file size.

## Options

### **-r (Recursive)**

Recursively include files in directories and their subdirectories

```console
$ zip -r backup.zip documents/
  adding: documents/ (stored 0%)
  adding: documents/report.docx (deflated 65%)
  adding: documents/images/ (stored 0%)
  adding: documents/images/photo.jpg (deflated 2%)
```

### **-e (Encrypt)**

Password-protect the ZIP archive

```console
$ zip -e secure.zip confidential.pdf
Enter password: 
Verify password: 
  adding: confidential.pdf (deflated 72%)
```

### **-u (Update)**

Update an existing ZIP file by adding new files or replacing changed files

```console
$ zip -u backup.zip documents/report.docx
updating: documents/report.docx (deflated 65%)
```

### **-j (Junk paths)**

Store just the file names without directory paths

```console
$ zip -j files.zip documents/report.docx documents/images/photo.jpg
  adding: report.docx (deflated 65%)
  adding: photo.jpg (deflated 2%)
```

### **-9 (Compression level)**

Set maximum compression level (1-9, where 9 is highest)

```console
$ zip -9 archive.zip largefile.dat
  adding: largefile.dat (deflated 78%)
```

## Usage Examples

### Creating a basic ZIP archive

```console
$ zip photos.zip *.jpg
  adding: vacation1.jpg (deflated 3%)
  adding: vacation2.jpg (deflated 2%)
  adding: vacation3.jpg (deflated 4%)
```

### Backing up a project with exclusions

```console
$ zip -r project.zip myproject/ -x "*.git*" "*node_modules*"
  adding: myproject/ (stored 0%)
  adding: myproject/index.html (deflated 68%)
  adding: myproject/styles.css (deflated 70%)
  adding: myproject/script.js (deflated 65%)
```

### Creating a split ZIP archive for large files

```console
$ zip -s 100m -r backup.zip large_directory/
  adding: large_directory/ (stored 0%)
  adding: large_directory/video.mp4 (deflated 1%)
  adding: large_directory/dataset.csv (deflated 85%)
```

## Tips:

### Monitor Compression Progress

For large archives, use the `-v` (verbose) option to see detailed progress information during compression.

### Exclude Unwanted Files

Use the `-x` option followed by patterns to exclude certain files or directories from being added to the archive.

### Test Archive Integrity

After creating an important archive, use `unzip -t archive.zip` to verify its integrity without extracting files.

### Preserve Symbolic Links

By default, `zip` follows symbolic links. Use `-y` to store the links themselves rather than the files they point to.

## Frequently Asked Questions

#### Q1. How do I extract a ZIP file?
A. Use the `unzip` command: `unzip archive.zip`. To extract to a specific directory, use `unzip archive.zip -d /path/to/directory`.

#### Q2. How can I see the contents of a ZIP file without extracting it?
A. Use `unzip -l archive.zip` to list the contents without extraction.

#### Q3. How do I create a ZIP file that works on Windows?
A. Standard ZIP files created with the `zip` command are compatible with Windows. For best compatibility with special characters, consider using the `-UN=UTF8` option.

#### Q4. How do I add files to an existing ZIP archive?
A. Use `zip -u archive.zip newfile.txt` to add or update files in an existing archive.

#### Q5. How much compression can I expect?
A. Compression rates vary by file type. Text files typically compress 60-80%, while already-compressed files like JPEGs or MP3s may only reduce by 1-5%.

## References

https://linux.die.net/man/1/zip

## Revisions

- 2025/04/30 First revision