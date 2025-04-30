# unzip command

Extract files from a ZIP archive.

## Overview

`unzip` extracts files and directories from ZIP archives. It supports various compression methods and can handle password-protected archives. The command can list, test, or extract the contents of ZIP files, making it essential for working with compressed data.

## Options

### **-l (List)**

Lists the contents of a ZIP archive without extracting them

```console
$ unzip -l archive.zip
Archive:  archive.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
     1024  2025-04-20 15:30   document.txt
      512  2025-04-19 14:22   notes.md
---------                     -------
     1536                     2 files
```

### **-t (Test)**

Tests the integrity of a ZIP archive without extracting files

```console
$ unzip -t archive.zip
Archive:  archive.zip
    testing: document.txt            OK
    testing: notes.md                OK
No errors detected in compressed data of archive.zip.
```

### **-o (Overwrite)**

Overwrites existing files without prompting

```console
$ unzip -o archive.zip
Archive:  archive.zip
  inflating: document.txt
  inflating: notes.md
```

### **-d (Directory)**

Extracts files to a specified directory

```console
$ unzip archive.zip -d extracted_files
Archive:  archive.zip
   creating: extracted_files/
  inflating: extracted_files/document.txt
  inflating: extracted_files/notes.md
```

### **-P (Password)**

Provides a password for encrypted ZIP archives

```console
$ unzip -P secretpassword protected.zip
Archive:  protected.zip
  inflating: confidential.txt
```

## Usage Examples

### Extracting specific files from an archive

```console
$ unzip archive.zip document.txt
Archive:  archive.zip
  inflating: document.txt
```

### Extracting all files but excluding certain ones

```console
$ unzip archive.zip -x "*.log"
Archive:  archive.zip
  inflating: document.txt
  inflating: notes.md
```

### Extracting with verbose output

```console
$ unzip -v archive.zip
Archive:  archive.zip
 Length   Method    Size  Cmpr    Date    Time   CRC-32   Name
--------  ------  ------- ---- ---------- ----- --------  ----
    1024  Defl:N      512  50% 2025-04-20 15:30 a1b2c3d4  document.txt
     512  Defl:N      256  50% 2025-04-19 14:22 e5f6g7h8  notes.md
--------          -------  ---                            -------
    1536              768  50%                            2 files
```

## Tips

### Handle Spaces in Filenames

When extracting files with spaces in their names, use quotes around the filename:

```console
$ unzip archive.zip "my document.txt"
```

### Preview Before Extracting

Always use `unzip -l` to preview the contents before extracting, especially when working with unfamiliar archives.

### Handle Character Encoding Issues

If you encounter character encoding issues with filenames, try using the `-O` option to specify the encoding:

```console
$ unzip -O UTF-8 archive.zip
```

### Dealing with Nested Archives

For ZIP files containing other ZIP files, you may need to run unzip multiple times:

```console
$ unzip outer.zip
$ cd extracted_folder
$ unzip inner.zip
```

## Frequently Asked Questions

#### Q1. How do I extract a password-protected ZIP file?
A. Use `unzip -P password archive.zip`. If you don't know the password, you'll need specialized tools to attempt recovery.

#### Q2. How can I extract a ZIP file without overwriting existing files?
A. Use `unzip -n archive.zip`. This will skip extraction of files that already exist.

#### Q3. How do I extract a ZIP file to a different directory?
A. Use `unzip archive.zip -d /path/to/directory` to specify the destination directory.

#### Q4. Can unzip handle .rar or .7z files?
A. No, `unzip` only works with ZIP archives. For RAR files, use `unrar`, and for 7z files, use `7z`.

#### Q5. How do I view the contents of a ZIP file without extracting it?
A. Use `unzip -l archive.zip` to list all files in the archive without extracting them.

## References

https://linux.die.net/man/1/unzip

## Revisions

- 2025/04/30 First revision