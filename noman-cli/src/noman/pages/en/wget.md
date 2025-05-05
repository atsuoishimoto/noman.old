# wget command

Download files from the web using HTTP, HTTPS, or FTP protocols.

## Overview

`wget` is a non-interactive command-line utility for downloading files from the web. It supports HTTP, HTTPS, and FTP protocols, and can work in the background, resume interrupted downloads, and follow links on webpages. It's particularly useful for retrieving content when a browser isn't available or when you need to automate downloads.

## Options

### **-O, --output-document=FILE**

Specify a different filename for the downloaded file

```console
$ wget -O custom-name.zip https://example.com/download/file.zip
--2025-05-04 10:15:30--  https://example.com/download/file.zip
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1024000 (1000K) [application/zip]
Saving to: 'custom-name.zip'

custom-name.zip     100%[===================>]  1000K  1.2MB/s    in 0.8s    

2025-05-04 10:15:31 (1.2 MB/s) - 'custom-name.zip' saved [1024000/1024000]
```

### **-c, --continue**

Resume a partially downloaded file

```console
$ wget -c https://example.com/large-file.iso
--2025-05-04 10:20:45--  https://example.com/large-file.iso
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 206 Partial Content
Length: 1073741824 (1.0G), 536870912 (512M) remaining [application/octet-stream]
Saving to: 'large-file.iso'

large-file.iso      50%[====>           ]  512M  5.2MB/s    eta 1m 40s
```

### **-b, --background**

Run wget in the background after startup

```console
$ wget -b https://example.com/large-file.iso
Continuing in background, pid 12345.
Output will be written to 'wget-log'.
```

### **-r, --recursive**

Download recursively (useful for website mirroring)

```console
$ wget -r -np https://example.com/docs/
--2025-05-04 10:30:15--  https://example.com/docs/
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5120 (5.0K) [text/html]
Saving to: 'example.com/docs/index.html'

example.com/docs/index.html    100%[===================>]   5.0K  --.-KB/s    in 0.001s  

2025-05-04 10:30:16 (5.0 MB/s) - 'example.com/docs/index.html' saved [5120/5120]

--2025-05-04 10:30:16--  https://example.com/docs/page1.html
Reusing existing connection to example.com:443.
HTTP request sent, awaiting response... 200 OK
Length: 4096 (4.0K) [text/html]
Saving to: 'example.com/docs/page1.html'

example.com/docs/page1.html    100%[===================>]   4.0K  --.-KB/s    in 0.001s  
```

### **-np, --no-parent**

Don't ascend to the parent directory when retrieving recursively

```console
$ wget -r -np https://example.com/docs/
```

### **-q, --quiet**

Quiet mode (no output)

```console
$ wget -q https://example.com/file.txt
```

### **-P, --directory-prefix=PREFIX**

Save files to the specified directory

```console
$ wget -P downloads/ https://example.com/file.txt
--2025-05-04 10:40:20--  https://example.com/file.txt
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2048 (2.0K) [text/plain]
Saving to: 'downloads/file.txt'

downloads/file.txt  100%[===================>]   2.0K  --.-KB/s    in 0.001s  

2025-05-04 10:40:21 (2.0 MB/s) - 'downloads/file.txt' saved [2048/2048]
```

## Usage Examples

### Downloading a file with progress bar

```console
$ wget https://example.com/file.zip
--2025-05-04 10:45:30--  https://example.com/file.zip
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 10485760 (10M) [application/zip]
Saving to: 'file.zip'

file.zip            100%[===================>]  10.0M  1.5MB/s    in 6.7s    

2025-05-04 10:45:37 (1.5 MB/s) - 'file.zip' saved [10485760/10485760]
```

### Mirroring a website

```console
$ wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://example.com/docs/
--2025-05-04 10:50:15--  https://example.com/docs/
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5120 (5.0K) [text/html]
Saving to: 'example.com/docs/index.html'

example.com/docs/index.html    100%[===================>]   5.0K  --.-KB/s    in 0.001s  

2025-05-04 10:50:16 (5.0 MB/s) - 'example.com/docs/index.html' saved [5120/5120]
```

### Downloading with authentication

```console
$ wget --user=username --password=password https://example.com/protected/file.pdf
--2025-05-04 10:55:45--  https://example.com/protected/file.pdf
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 401 Unauthorized
Authentication selected: Basic realm="Restricted Area"
Reusing existing connection to example.com:443.
HTTP request sent, awaiting response... 200 OK
Length: 1048576 (1.0M) [application/pdf]
Saving to: 'file.pdf'

file.pdf            100%[===================>]   1.0M  1.2MB/s    in 0.8s    

2025-05-04 10:55:46 (1.2 MB/s) - 'file.pdf' saved [1048576/1048576]
```

## Tips:

### Rate Limiting Downloads

Use `--limit-rate=RATE` to restrict download speed (e.g., `--limit-rate=200k` for 200 KB/s). This is useful when you don't want wget to consume all available bandwidth.

### Handling Timeouts

For unstable connections, increase timeout values with `--timeout=SECONDS` and `--tries=NUMBER` to make wget more persistent in completing downloads.

### Using a User Agent

Some websites block wget's default user agent. Use `--user-agent="Mozilla/5.0"` to mimic a browser and avoid being blocked.

### Creating a Log File

Use `--output-file=logfile.txt` to save wget's output to a file instead of displaying it on the screen, useful for tracking long downloads.

## Frequently Asked Questions

#### Q1. How do I download multiple files at once?
A. Create a text file with URLs (one per line) and use `wget -i urls.txt`.

#### Q2. How can I download a file without showing the progress output?
A. Use `wget -q URL` for quiet mode or `wget -b URL` to run in the background.

#### Q3. How do I resume a download that was interrupted?
A. Use `wget -c URL` to continue a partially downloaded file from where it left off.

#### Q4. Can wget download an entire website?
A. Yes, use `wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://example.com/` to create a local copy of a website.

#### Q5. How do I download files from an FTP server?
A. Use `wget ftp://username:password@ftp.example.com/path/to/file` or `wget --ftp-user=username --ftp-password=password ftp://ftp.example.com/path/to/file`.

## References

https://www.gnu.org/software/wget/manual/wget.html

## Revisions

- 2025/05/04 First revision