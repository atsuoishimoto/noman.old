# wget command

Download files from the web using HTTP, HTTPS, or FTP protocols.

## Overview

`wget` is a non-interactive command-line utility for downloading files from the web. It supports HTTP, HTTPS, and FTP protocols, and can handle downloads in the background, resume interrupted downloads, and follow links on webpages. It's particularly useful for retrieving content when a browser isn't available or for automating downloads.

## Options

### **-O, --output-document=FILE**

Save downloaded content to a specified file instead of using the name from the URL

```console
$ wget -O custom-name.zip https://example.com/download/archive.zip
--2025-04-30 10:15:20--  https://example.com/download/archive.zip
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1048576 (1.0M) [application/zip]
Saving to: 'custom-name.zip'

custom-name.zip     100%[===================>]   1.00M  1.25MB/s    in 0.8s    

2025-04-30 10:15:22 (1.25 MB/s) - 'custom-name.zip' saved [1048576/1048576]
```

### **-c, --continue**

Resume a partially downloaded file

```console
$ wget -c https://example.com/large-file.iso
--2025-04-30 10:18:45--  https://example.com/large-file.iso
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 206 Partial Content
Length: 1073741824 (1.0G), 536870912 (512M) remaining [application/octet-stream]
Saving to: 'large-file.iso'

large-file.iso      50%[====>           ]   512M  5.25MB/s    eta 1m 38s
```

### **-b, --background**

Run wget in the background after startup

```console
$ wget -b https://example.com/huge-file.zip
Continuing in background, pid 1234.
Output will be written to 'wget-log'.
```

### **-r, --recursive**

Download an entire website recursively

```console
$ wget -r -np -l 2 https://example.com/docs/
--2025-04-30 10:22:30--  https://example.com/docs/
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 8192 (8.0K) [text/html]
Saving to: 'example.com/docs/index.html'

example.com/docs/index.html    100%[===================>]   8.0K  --.-KB/s    in 0.1s    

2025-04-30 10:22:31 (80.0 KB/s) - 'example.com/docs/index.html' saved [8192/8192]

Loading robots.txt; please ignore errors.
--2025-04-30 10:22:31--  https://example.com/robots.txt
Reusing existing connection to example.com:443.
HTTP request sent, awaiting response... 404 Not Found
2025-04-30 10:22:31 ERROR 404: Not Found.

--2025-04-30 10:22:31--  https://example.com/docs/page1.html
Reusing existing connection to example.com:443.
HTTP request sent, awaiting response... 200 OK
Length: 4096 (4.0K) [text/html]
Saving to: 'example.com/docs/page1.html'

example.com/docs/page1.html    100%[===================>]   4.0K  --.-KB/s    in 0.1s    
```

### **-q, --quiet**

Run silently (no output)

```console
$ wget -q https://example.com/file.txt
```

## Usage Examples

### Downloading a file with progress bar

```console
$ wget https://example.com/document.pdf
--2025-04-30 10:30:15--  https://example.com/document.pdf
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 2097152 (2.0M) [application/pdf]
Saving to: 'document.pdf'

document.pdf        100%[===================>]   2.00M  2.50MB/s    in 0.8s    

2025-04-30 10:30:16 (2.50 MB/s) - 'document.pdf' saved [2097152/2097152]
```

### Downloading multiple files listed in a text file

```console
$ cat urls.txt
https://example.com/file1.zip
https://example.com/file2.zip
https://example.com/file3.zip

$ wget -i urls.txt
--2025-04-30 10:35:20--  https://example.com/file1.zip
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 524288 (512K) [application/zip]
Saving to: 'file1.zip'

file1.zip           100%[===================>] 512.00K  1.25MB/s    in 0.4s    

2025-04-30 10:35:21 (1.25 MB/s) - 'file1.zip' saved [524288/524288]

--2025-04-30 10:35:21--  https://example.com/file2.zip
Reusing existing connection to example.com:443.
HTTP request sent, awaiting response... 200 OK
Length: 262144 (256K) [application/zip]
Saving to: 'file2.zip'

file2.zip           100%[===================>] 256.00K  --.-KB/s    in 0.2s    

2025-04-30 10:35:21 (1.28 MB/s) - 'file2.zip' saved [262144/262144]
```

### Mirroring a website

```console
$ wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://example.com/blog/
--2025-04-30 10:40:10--  https://example.com/blog/
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 16384 (16K) [text/html]
Saving to: 'example.com/blog/index.html'

example.com/blog/index.html    100%[===================>]  16.00K  --.-KB/s    in 0.1s    

2025-04-30 10:40:10 (160 KB/s) - 'example.com/blog/index.html' saved [16384/16384]

Loading robots.txt; please ignore errors.
--2025-04-30 10:40:10--  https://example.com/robots.txt
Reusing existing connection to example.com:443.
HTTP request sent, awaiting response... 404 Not Found
2025-04-30 10:40:10 ERROR 404: Not Found.
```

## Tips:

### Rate Limiting Downloads

Use `--limit-rate=RATE` to avoid consuming all available bandwidth. For example, `wget --limit-rate=500k https://example.com/large-file.iso` limits the download speed to 500 KB/s.

### Using a Proxy Server

If you're behind a proxy, use `--proxy=on` and set the environment variables `http_proxy`, `https_proxy`, or specify directly with `--proxy-user` and `--proxy-password`.

### Handling Authentication

For password-protected sites, use `--user=USERNAME --password=PASSWORD` or `wget --http-user=USERNAME --http-password=PASSWORD https://example.com/private/file.zip`.

### Retrying Failed Downloads

Use `--tries=NUMBER` to set the number of retry attempts and `--waitretry=SECONDS` to specify the time between retries.

## Frequently Asked Questions

#### Q1. How do I download a file without showing the progress output?
A. Use `wget -q URL` to run wget in quiet mode.

#### Q2. How can I resume a download that was interrupted?
A. Use `wget -c URL` to continue a partially downloaded file.

#### Q3. How do I download an entire website?
A. Use `wget --mirror --convert-links --adjust-extension --page-requisites --no-parent URL` to create a local copy of a website.

#### Q4. Can wget follow links on a webpage?
A. Yes, use the `-r` (recursive) option along with `-l depth` to specify how many levels of links to follow.

#### Q5. How do I download files that require authentication?
A. Use `wget --user=USERNAME --password=PASSWORD URL` for basic authentication.

## References

https://www.gnu.org/software/wget/manual/wget.html

## Revisions

- 2025/04/30 First revision