# curl command

Transfer data from or to a server using various protocols including HTTP, HTTPS, FTP, and more.

## Overview

`curl` is a command-line tool for transferring data with URLs. It supports numerous protocols including HTTP, HTTPS, FTP, FTPS, SCP, SFTP, LDAP, and more. It's commonly used for downloading files, testing APIs, sending HTTP requests, and debugging network issues. `curl` is non-interactive and designed to work without user intervention, making it ideal for scripts and automation.

## Options

### **-o, --output \<file>**

Save the output to a file instead of displaying it on the screen

```console
$ curl -o example.html https://example.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1256  100  1256    0     0   9664      0 --:--:-- --:--:-- --:--:--  9663
```

### **-O, --remote-name**

Save the output using the remote file name from the URL

```console
$ curl -O https://example.com/sample.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10.2M  100 10.2M    0     0  5.1MB/s      0 --:--:-- 0:00:02 --:--:-- 5.1MB
```

### **-L, --location**

Follow HTTP redirects (3XX responses)

```console
$ curl -L http://github.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   142  100   142    0     0    573      0 --:--:-- --:--:-- --:--:--   573
100  5891    0  5891    0     0  13090      0 --:--:-- --:--:-- --:--:-- 13090
```

### **-s, --silent**

Silent mode; don't show progress meter or error messages

```console
$ curl -s https://example.com > example.html
```

### **-I, --head**

Fetch HTTP headers only (HEAD request)

```console
$ curl -I https://example.com
HTTP/2 200 
content-type: text/html; charset=UTF-8
date: Tue, 04 May 2025 12:00:00 GMT
expires: Tue, 11 May 2025 12:00:00 GMT
cache-control: public, max-age=604800
server: ECS (dcb/7F84)
content-length: 1256
```

### **-X, --request \<command>**

Specify the HTTP request method to use (GET, POST, PUT, DELETE, etc.)

```console
$ curl -X POST https://api.example.com/data
```

### **-H, --header \<header>**

Add a custom header to the request

```console
$ curl -H "Content-Type: application/json" https://api.example.com
```

### **-d, --data \<data>**

Send data in the request body (typically used with POST)

```console
$ curl -X POST -d "name=John&age=30" https://api.example.com/users
```

### **-A, --user-agent \<agent string>**

Specify the User-Agent string to send to the server

```console
$ curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" https://example.com
```

## Usage Examples

### Downloading a file and saving it with a specific name

```console
$ curl -o linux-distro.iso https://example.com/downloads/linux.iso
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 1500M  100 1500M    0     0  10.2M/s      0  0:02:27  0:02:27 --:--:-- 10.5M
```

### Making a POST request with JSON data

```console
$ curl -X POST -H "Content-Type: application/json" -d '{"name":"John","age":30}' https://api.example.com/users
{"id": 123, "status": "created"}
```

### Downloading multiple files with authentication

```console
$ curl -u username:password -O https://example.com/file1.txt -O https://example.com/file2.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1256  100  1256    0     0  12560      0 --:--:-- --:--:-- --:--:-- 12560
100  2048  100  2048    0     0  20480      0 --:--:-- --:--:-- --:--:-- 20480
```

### Uploading a file

```console
$ curl -F "file=@localfile.jpg" https://example.com/upload
{"status": "success", "url": "https://example.com/uploads/image123.jpg"}
```

## Tips

### Use Verbose Mode for Debugging

When troubleshooting, use `-v` (verbose) or `-vv` (very verbose) to see detailed information about the request and response:

```console
$ curl -v https://example.com
```

### Save Cookies and Use Them Later

To handle sessions that require cookies:

```console
$ curl -c cookies.txt https://example.com/login -d "user=name&password=secret"
$ curl -b cookies.txt https://example.com/protected-area
```

### Limit Download Speed

To avoid consuming all available bandwidth:

```console
$ curl --limit-rate 1M -O https://example.com/large-file.zip
```

### Resume Interrupted Downloads

If a download gets interrupted, you can resume it:

```console
$ curl -C - -O https://example.com/large-file.zip
```

### Test API Endpoints Quickly

For quick API testing, combine with tools like `jq` to format JSON responses:

```console
$ curl -s https://api.example.com/users | jq
```

## Frequently Asked Questions

#### Q1. How do I download a file with curl?
A. Use `curl -O URL` to download and save with the original filename, or `curl -o filename URL` to specify a different filename.

#### Q2. How can I make a POST request with curl?
A. Use `curl -X POST -d "key=value" URL` for form data or `curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' URL` for JSON data.

#### Q3. How do I follow redirects with curl?
A. Use the `-L` or `--location` option to follow HTTP redirects.

#### Q4. How can I see the HTTP headers in the response?
A. Use `curl -I URL` to see only headers, or `curl -v URL` to see both headers and body.

#### Q5. How do I authenticate with curl?
A. For basic authentication, use `curl -u username:password URL`. For OAuth or token-based auth, use `curl -H "Authorization: Bearer YOUR_TOKEN" URL`.

## macOS Considerations

On macOS, the default `curl` is typically older than on Linux distributions. Some newer features might not be available. Additionally, macOS's `curl` is built with Secure Transport (Apple's SSL/TLS implementation) rather than OpenSSL, which can occasionally cause subtle differences in behavior, especially with SSL certificates.

If you need the latest version with all features, consider installing `curl` via Homebrew:

```console
$ brew install curl
```

After installation, you may need to use `/usr/local/opt/curl/bin/curl` or add it to your PATH to use the Homebrew version instead of the system version.

## References

https://curl.se/docs/manpage.html

## Revisions

- 2025/05/04 First revision