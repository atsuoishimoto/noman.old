# split command

Split a file into pieces.

## Overview

The `split` command divides a file into multiple smaller files. It's useful when you need to break up large files for easier handling, transfer, or storage. By default, it creates files named 'xaa', 'xab', etc., with each containing a specified number of lines or bytes from the original file.

## Options

### **-b, --bytes=SIZE**

Split by bytes instead of lines. SIZE can be a number followed by a multiplier: k (1024), m (1024²), g (1024³), etc.

```console
$ split -b 1M largefile.dat chunk_
$ ls chunk_*
chunk_aa  chunk_ab  chunk_ac
```

### **-l, --lines=NUMBER**

Split by a specific number of lines per output file (default is 1000 lines).

```console
$ split -l 100 data.csv part_
$ ls part_*
part_aa  part_ab  part_ac  part_ad
```

### **-d, --numeric-suffixes[=FROM]**

Use numeric suffixes instead of alphabetic ones, starting at FROM (default 0).

```console
$ split -d -l 100 data.txt section_
$ ls section_*
section_00  section_01  section_02
```

### **-a, --suffix-length=N**

Generate suffixes of length N (default 2).

```console
$ split -a 3 -l 100 data.txt part_
$ ls part_*
part_aaa  part_aab  part_aac  part_aad
```

### **--additional-suffix=SUFFIX**

Append an additional SUFFIX to file names.

```console
$ split -l 100 --additional-suffix=.txt data.csv part_
$ ls part_*
part_aa.txt  part_ab.txt  part_ac.txt
```

### **-n, --number=CHUNKS**

Split into CHUNKS files based on size or number.

```console
$ split -n 3 largefile.dat chunk_
$ ls chunk_*
chunk_aa  chunk_ab  chunk_ac
```

## Usage Examples

### Splitting a large log file by size

```console
$ split -b 10M large_log.log log_chunk_
$ ls -lh log_chunk_*
-rw-r--r-- 1 user group 10M May 4 10:15 log_chunk_aa
-rw-r--r-- 1 user group 10M May 4 10:15 log_chunk_ab
-rw-r--r-- 1 user group 5.2M May 4 10:15 log_chunk_ac
```

### Splitting a CSV file by line count with numbered output

```console
$ split -d -l 1000 --additional-suffix=.csv large_dataset.csv dataset_
$ ls dataset_*
dataset_00.csv  dataset_01.csv  dataset_02.csv
```

### Splitting a file into equal parts

```console
$ split -n l/4 bigfile.txt equal_part_
$ ls -lh equal_part_*
-rw-r--r-- 1 user group 2.5M May 4 10:20 equal_part_aa
-rw-r--r-- 1 user group 2.5M May 4 10:20 equal_part_ab
-rw-r--r-- 1 user group 2.5M May 4 10:20 equal_part_ac
-rw-r--r-- 1 user group 2.5M May 4 10:20 equal_part_ad
```

## Tips

### Recombining Split Files

To recombine files split with the `split` command, use the `cat` command with the files in the correct order:
```console
$ cat chunk_* > original_file_restored
```

### Choosing Appropriate Split Sizes

When splitting files for transfer (like email attachments), consider the destination's size limits. For example, use `-b 10M` for files that need to be under 10MB.

### Using with Compression

Split after compression for better efficiency:
```console
$ gzip -c largefile > largefile.gz
$ split -b 10M largefile.gz largefile.gz.part_
```

## Frequently Asked Questions

#### Q1. How do I split a file into equal-sized chunks?
A. Use `split -n l/N filename`, where N is the number of equal parts you want.

#### Q2. How can I split a file and maintain the original file extension?
A. Use the `--additional-suffix` option: `split -l 1000 file.csv part_ --additional-suffix=.csv`

#### Q3. What's the difference between `-b` and `-n`?
A. `-b` splits by exact byte size, while `-n` splits into a specific number of chunks, potentially of different sizes.

#### Q4. Can I preview what split would do without actually splitting the file?
A. No, `split` doesn't have a preview or dry-run option. You can use `wc -l` to count lines first to help plan your split.

## References

https://www.gnu.org/software/coreutils/manual/html_node/split-invocation.html

## Revisions

- 2025/05/04 First revision