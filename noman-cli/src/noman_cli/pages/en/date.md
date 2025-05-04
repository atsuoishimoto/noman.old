# date command

Display or set the system date and time.

## Overview

The `date` command displays the current date and time according to your system clock. It can also be used to format the date output in various ways, convert between time zones, or set the system date and time (when run with appropriate permissions).

## Options

### **-d, --date=STRING**

Display the time described by STRING instead of the current time

```console
$ date -d "next Thursday"
Thu May  8 00:00:00 UTC 2025
```

### **-f, --file=DATEFILE**

Display each line in DATEFILE interpreted as a date

```console
$ echo "2023-01-01" > dates.txt
$ echo "tomorrow" >> dates.txt
$ date -f dates.txt
Sun Jan  1 00:00:00 UTC 2023
Mon May  5 00:00:00 UTC 2025
```

### **-I[TIMESPEC], --iso-8601[=TIMESPEC]**

Output date/time in ISO 8601 format. TIMESPEC can be 'date', 'hours', 'minutes', 'seconds', or 'ns'

```console
$ date -I
2025-05-04
$ date -Iseconds
2025-05-04T12:34:56+00:00
```

### **-r, --reference=FILE**

Display the last modification time of FILE

```console
$ touch testfile
$ date -r testfile
Sun May  4 12:34:56 UTC 2025
```

### **-R, --rfc-email**

Output date and time in RFC 5322 format (suitable for email headers)

```console
$ date -R
Sun, 04 May 2025 12:34:56 +0000
```

### **-u, --utc, --universal**

Display or set time in Coordinated Universal Time (UTC)

```console
$ date
Sun May  4 12:34:56 PDT 2025
$ date -u
Sun May  4 19:34:56 UTC 2025
```

### **+FORMAT**

Format the output according to the FORMAT specification

```console
$ date "+%Y-%m-%d %H:%M:%S"
2025-05-04 12:34:56
```

## Usage Examples

### Basic date display

```console
$ date
Sun May  4 12:34:56 PDT 2025
```

### Custom formatting

```console
$ date "+Today is %A, %B %d, %Y"
Today is Sunday, May 04, 2025
```

### Calculating dates

```console
$ date -d "next week"
Sun May 11 12:34:56 PDT 2025
$ date -d "2 months ago"
Fri Mar  4 12:34:56 PST 2025
```

### Setting the system date (requires root privileges)

```console
$ sudo date -s "2025-05-04 12:00:00"
Sun May  4 12:00:00 PDT 2025
```

## Tips

### Common Format Specifiers

- `%Y`: Year (e.g., 2025)
- `%m`: Month (01-12)
- `%d`: Day of month (01-31)
- `%H`: Hour (00-23)
- `%M`: Minute (00-59)
- `%S`: Second (00-60)
- `%A`: Full weekday name (e.g., Sunday)
- `%B`: Full month name (e.g., May)
- `%Z`: Time zone abbreviation (e.g., PDT)

### Timestamp for Filenames

Generate timestamps for unique filenames in scripts:

```console
$ backup_file="backup_$(date +%Y%m%d_%H%M%S).tar.gz"
$ echo $backup_file
backup_20250504_123456.tar.gz
```

### Unix Timestamp

Get the Unix timestamp (seconds since January 1, 1970):

```console
$ date +%s
1746619200
```

## Frequently Asked Questions

#### Q1. How do I display the date in a specific format?
A. Use the `+FORMAT` option with format specifiers. For example: `date "+%Y-%m-%d"` displays the date as 2025-05-04.

#### Q2. How do I get the date for a different time zone?
A. You can use the `TZ` environment variable: `TZ="America/New_York" date` will show the time in New York.

#### Q3. How do I convert a Unix timestamp to a readable date?
A. Use `date -d @TIMESTAMP`. For example: `date -d @1609459200` shows the date for timestamp 1609459200.

#### Q4. How do I calculate dates in the future or past?
A. Use the `-d` option with relative time expressions: `date -d "next Monday"` or `date -d "3 days ago"`.

## macOS Considerations

On macOS, the `date` command has slightly different options. The `-d` option is not available; instead, use `-v` for date adjustments:

```console
$ date -v+1d  # Add one day
Mon May  5 12:34:56 PDT 2025
```

For formatting on macOS, the syntax is the same:

```console
$ date "+%Y-%m-%d"
2025-05-04
```

## References

https://www.gnu.org/software/coreutils/manual/html_node/date-invocation.html

## Revisions

- 2025/05/04 First revision