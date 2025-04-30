# split command

Split a file into pieces.

## Overview

The `split` command divides a file into multiple smaller files. It's useful when you need to break up large files for easier handling, transfer, or storage. By default, it creates files named 'xaa', 'xab', etc., each containing a specified number of lines or bytes from the original file.

## Options

### **-b, --bytes=SIZE**

Split by bytes instead of lines. SIZE can be a number followed by a unit (K for kilobytes, M for megabytes, G for gigabytes).

```console
$ split -b 1M largefile.txt chunk_
$ ls chunk_*
chunk_aa  chunk_ab  chunk_ac
```

### **-l, --lines=NUMBER**

Split by a specific number of lines (default is 1000 lines).

```console
$ split -l 100 data.csv data_part_
$ ls data_part_*
data_part_aa  data_part_ab  data_part_ac
```

### **-d, --numeric-suffixes[=FROM]**

Use numeric suffixes instead of alphabetic ones, starting at FROM (default 0).

```console
$ split -d -l 100 report.txt report_
$ ls report_*
report_00  report_01  report_02
```

### **-a, --suffix-length=N**

Use suffixes of length N (default 2).

```console
$ split -a 3 -b 10M backup.tar backup_
$ ls backup_*
backup_aaa  backup_aab  backup_aac
```

## Usage Examples

### Splitting a large log file by size

```console
$ split -b 50M large_log.log log_chunk_
$ ls -lh log_chunk_*
-rw-r--r-- 1 user group 50M Apr 30 10:15 log_chunk_aa
-rw-r--r-- 1 user group 50M Apr 30 10:15 log_chunk_ab
-rw-r--r-- 1 user group 23M Apr 30 10:15 log_chunk_ac
```

### Splitting a CSV file by line count with numeric suffixes

```console
$ split -l 1000 -d customers.csv customer_
$ ls customer_*
customer_00  customer_01  customer_02  customer_03
```

### Splitting a file and specifying output directory

```console
$ split -b 100M backup.img /tmp/backup_parts/part_
$ ls /tmp/backup_parts/
part_aa  part_ab  part_ac
```

## Tips

### Reassembling Split Files

To reassemble split files back into the original, use the `cat` command:

```console
$ cat chunk_* > original_file_restored
```

### Preserving File Extensions

Split doesn't preserve file extensions. If you need to maintain the extension for each part, you'll need to manually rename the files or use a script.

### Estimating Output File Count

To estimate how many files will be created, divide the total file size by the chunk size. For example, a 100MB file split into 10MB chunks will create approximately 10 files.

### Combining with Compression

For large files, consider compressing before splitting:

```console
$ gzip -c largefile > largefile.gz
$ split -b 50M largefile.gz largefile.gz.part_
```

## Frequently Asked Questions

#### Q1. How do I join split files back together?
A. Use the `cat` command with wildcard matching: `cat prefix_* > original_file`

#### Q2. Can I split a file without reading it entirely into memory?
A. Yes, `split` processes the file sequentially and doesn't load the entire file into memory.

#### Q3. How do I split a file into a specific number of parts instead of by size?
A. First determine the total size with `wc -c filename`, then divide by the number of parts you want, and use that value with the `-b` option.

#### Q4. Does split work with binary files?
A. Yes, `split` works with any file type, including binary files.

## References

https://www.gnu.org/software/coreutils/manual/html_node/split-invocation.html

## Revisions

- 2025/04/30 First revision