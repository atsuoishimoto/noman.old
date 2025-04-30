# date command

Display or set the system date and time.

## Overview

The `date` command displays the current date and time according to your system clock. It can also format the output in various ways, set the system date and time (with proper permissions), and calculate dates in the past or future.

## Options

### **-d, --date=STRING**

Display the time described by STRING instead of the current time

```console
$ date -d "next Thursday"
Thu May  8 00:00:00 EDT 2025
```

### **-f, --file=DATEFILE**

Display each date specified in DATEFILE

```console
$ date -f dates.txt
Wed Apr 30 12:34:56 EDT 2025
Thu May  1 09:00:00 EDT 2025
```

### **-r, --reference=FILE**

Display the last modification time of FILE

```console
$ date -r document.txt
Wed Apr 30 10:15:23 EDT 2025
```

### **-u, --utc, --universal**

Display or set time in Coordinated Universal Time (UTC)

```console
$ date -u
Wed Apr 30 16:34:56 UTC 2025
```

### **+FORMAT**

Format the output according to the FORMAT string

```console
$ date "+%Y-%m-%d %H:%M:%S"
2025-04-30 12:34:56
```

## Usage Examples

### Displaying current date and time

```console
$ date
Wed Apr 30 12:34:56 EDT 2025
```

### Formatting date output

```console
$ date "+Today is %A, %B %d, %Y"
Today is Wednesday, April 30, 2025
```

### Calculating a date in the future

```console
$ date -d "30 days"
Fri May 30 12:34:56 EDT 2025
```

### Setting the system date (requires root privileges)

```console
$ sudo date 043012342025.56
Wed Apr 30 12:34:56 EDT 2025
```

## Tips

### Common Format Specifiers

- `%Y`: Year (4 digits)
- `%m`: Month (01-12)
- `%d`: Day of month (01-31)
- `%H`: Hour (00-23)
- `%M`: Minute (00-59)
- `%S`: Second (00-60)
- `%a`: Abbreviated weekday name
- `%A`: Full weekday name
- `%b`: Abbreviated month name
- `%B`: Full month name

### Timestamp for Filenames

Generate timestamps for filenames with:
```console
$ date +%Y%m%d_%H%M%S
20250430_123456
```

### Date Calculations

Use the `-d` option with relative time expressions:
```console
$ date -d "yesterday"
$ date -d "last month"
$ date -d "2 years ago"
```

## Frequently Asked Questions

#### Q1. How do I get the Unix timestamp (seconds since epoch)?
A. Use `date +%s` to get the Unix timestamp.

#### Q2. How do I convert a Unix timestamp to a readable date?
A. Use `date -d @1714503296` where the number is the Unix timestamp.

#### Q3. How do I display time in a different timezone?
A. Set the TZ environment variable: `TZ=UTC date` or `TZ=America/New_York date`.

#### Q4. How can I get just the date without the time?
A. Use `date +%F` or `date +%Y-%m-%d`.

## macOS Considerations

On macOS, the `date` command has slightly different syntax:
- The `-d` option is not available; use `-v` for date calculations
- To set the date, use `sudo date MMDDHHmmYY` format
- For formatting, macOS uses the same format specifiers

Examples for macOS:
```console
$ date -v+1d  # tomorrow
$ date -v-1m  # one month ago
$ sudo date 0430123425  # set date to April 30, 12:34, 2025
```

## References

https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html

## Revisions

- 2025/04/30 First revision