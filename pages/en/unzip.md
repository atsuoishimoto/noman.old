# unzip command

Extract files from a ZIP archive.

## Overview

The `unzip` command extracts files from ZIP archives. It supports various compression methods and can handle password-protected archives, display archive contents without extraction, and selectively extract specific files. It's the standard tool for working with ZIP files on Unix-like systems.

## Options

### **-l (--list)**

List the contents of a ZIP archive without extracting

```console
$ unzip -l archive.zip
Archive:  archive.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
     1234  2025-01-01 12:34   file1.txt
      567  2025-01-02 15:45   file2.txt
---------                     -------
     1801                     2 files
```

### **-t (--test)**

Test the integrity of a ZIP archive without extracting

```console
$ unzip -t archive.zip
Archive:  archive.zip
    testing: file1.txt               OK
    testing: file2.txt               OK
No errors detected in compressed data of archive.zip.
```

### **-o (--overwrite)**

Overwrite existing files without prompting

```console
$ unzip -o archive.zip
Archive:  archive.zip
  inflating: file1.txt
  inflating: file2.txt
```

### **-n (--never-overwrite)**

Never overwrite existing files (skip extraction of files that already exist)

```console
$ unzip -n archive.zip
Archive:  archive.zip
 extracting: file1.txt
 extracting: file2.txt
```

### **-d (--directory)**

Extract files to a specified directory

```console
$ unzip archive.zip -d extracted_files/
Archive:  archive.zip
   creating: extracted_files/
  inflating: extracted_files/file1.txt
  inflating: extracted_files/file2.txt
```

### **-P (--password)**

Specify password for encrypted archives

```console
$ unzip -P mypassword protected.zip
Archive:  protected.zip
  inflating: secret.txt
```

### **-j (--junk-paths)**

Extract files without creating directories (junk the paths)

```console
$ unzip -j archive.zip
Archive:  archive.zip
  inflating: file1.txt
  inflating: file2.txt
```

## Usage Examples

### Extracting specific files from an archive

```console
$ unzip archive.zip file1.txt
Archive:  archive.zip
  inflating: file1.txt
```

### Extracting files with wildcard patterns

```console
$ unzip archive.zip "*.txt"
Archive:  archive.zip
  inflating: file1.txt
  inflating: file2.txt
```

### Extracting with verbose output

```console
$ unzip -v archive.zip
Archive:  archive.zip
 Length   Method    Size  Cmpr    Date    Time   CRC-32   Name
--------  ------  ------- ---- ---------- ----- --------  ----
    1234  Defl:N      567  54% 2025-01-01 12:34 a1b2c3d4  file1.txt
     567  Defl:N      234  59% 2025-01-02 15:45 e5f6g7h8  file2.txt
--------          -------  ---                            -------
    1801              801  56%                            2 files
```

## Tips

### Preview Archive Contents Before Extracting

Always use `unzip -l archive.zip` to preview the contents before extraction. This helps avoid accidentally extracting files that might overwrite existing ones.

### Handle Path Traversal Safely

Be cautious with archives from untrusted sources. Some ZIP files may contain entries with "../" paths that could overwrite files outside the extraction directory. Use the `-d` option to specify a dedicated extraction directory.

### Extract to a Temporary Directory

When working with unfamiliar archives, extract to a temporary directory first using `unzip archive.zip -d temp/` to inspect the contents before moving them to their final location.

### Handling Large Archives

For large archives, use `unzip -q` (quiet mode) to reduce output and speed up extraction, or use `unzip -n` to avoid overwriting existing files if you're resuming a previous extraction.

## Frequently Asked Questions

#### Q1. How do I extract a password-protected ZIP file?
A. Use `unzip -P password archive.zip`. If you don't want to expose the password in command history, omit the -P option and unzip will prompt for the password.

#### Q2. How can I extract only specific files from a ZIP archive?
A. Use `unzip archive.zip filename1 filename2` to extract only the specified files. You can also use wildcards like `unzip archive.zip "*.txt"`.

#### Q3. How do I extract a ZIP file without creating its directory structure?
A. Use `unzip -j archive.zip` to extract all files to the current directory without creating subdirectories.

#### Q4. How can I check if a ZIP file is valid without extracting it?
A. Use `unzip -t archive.zip` to test the integrity of the archive without extracting any files.

#### Q5. How do I handle filename encoding issues?
A. If filenames appear garbled, try using the `-O` option to specify the encoding, like `unzip -O CP936 archive.zip` for Chinese Windows archives.

## References

https://linux.die.net/man/1/unzip

## Revisions

- 2025/05/04 First revision