# tar

`tar` is a command-line utility used to create, maintain, modify, and extract files from archive files (commonly called tarballs). It's frequently used for file backup and distribution.

## Options

### **-c (create)**

Creates a new archive file.

```bash
$ tar -cf archive.tar file1 file2 directory/
```

### **-x (extract)**

Extracts files from an archive.

```bash
$ tar -xf archive.tar
```

### **-f (file)**

Specifies the archive file name (must be used with other operations).

```bash
$ tar -cf archive.tar files/
```

### **-v (verbose)**

Shows the files being processed.

```bash
$ tar -cvf archive.tar files/
files/
files/document1.txt
files/document2.txt
```

### **-z (gzip)**

Compresses the archive with gzip.

```bash
$ tar -czf archive.tar.gz files/
```

### **-j (bzip2)**

Compresses the archive with bzip2 (better compression but slower).

```bash
$ tar -cjf archive.tar.bz2 files/
```

### **-t (list)**

Lists the contents of an archive without extracting.

```bash
$ tar -tf archive.tar
files/
files/document1.txt
files/document2.txt
```

### **-C (directory)**

Changes to the specified directory before performing operations.

```bash
$ tar -xf archive.tar -C /path/to/extract/
```

## Usage Examples

### Creating a compressed archive

```bash
$ tar -czf backup.tar.gz ~/Documents ~/Pictures
```

### Extracting a compressed archive

```bash
$ tar -xzf backup.tar.gz
```

### Viewing archive contents without extracting

```bash
$ tar -tvf archive.tar
-rw-r--r-- user/group   4096 2023-04-10 15:30 files/document1.txt
-rw-r--r-- user/group   2048 2023-04-09 14:22 files/document2.txt
```

### Extracting a single file from an archive

```bash
$ tar -xf archive.tar files/document1.txt
```

## Frequently Asked Questions

### Q1. What's the difference between .tar, .tar.gz, and .tar.bz2?
A. `.tar` is an uncompressed archive, `.tar.gz` is compressed with gzip (good balance of speed and compression), and `.tar.bz2` is compressed with bzip2 (better compression but slower).

### Q2. How do I extract a specific file from an archive?
A. Use `tar -xf archive.tar path/to/specific/file`.

### Q3. How can I see what's in a tar archive without extracting it?
A. Use `tar -tf archive.tar` to list contents, or add the `v` option (`tar -tvf`) for more details.

### Q4. How do I update files in an existing archive?
A. Use the `-u` option: `tar -uf archive.tar newfile.txt`.

## Additional Notes

- The order of options matters in `tar` commands. The `-f` option should be followed immediately by the archive filename.
- Modern versions of `tar` can automatically detect compression types, so you often don't need to specify `-z` or `-j` when extracting.
- On macOS, the BSD version of `tar` has some slight differences from GNU tar, but the core options work the same way.
- A common mnemonic for remembering tar options: "**c**reate **f**ile **v**erbosely **z**ipped" for `tar -cfvz`.

## References

https://www.gnu.org/software/tar/manual/