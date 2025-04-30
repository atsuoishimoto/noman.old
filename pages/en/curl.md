# curl command

Transfer data from or to a server using various protocols including HTTP, HTTPS, FTP, and more.

## Overview

`curl` is a command-line tool for transferring data with URLs. It supports numerous protocols including HTTP, HTTPS, FTP, FTPS, SCP, SFTP, SMTP, and more. It's commonly used for downloading files, testing APIs, sending HTTP requests, and debugging network issues. `curl` is highly versatile and can be used with or without user interaction.

## Options

### **-o, --output \<file\>**

Save the output to a file instead of displaying it on the screen

```console
$ curl -o example.html https://example.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1256  100  1256    0     0  12560      0 --:--:-- --:--:-- --:--:-- 12560
```

### **-O, --remote-name**

Save the output using the remote file name

```console
$ curl -O https://example.com/sample.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10.5M  100 10.5M    0     0  5.2M      0  0:00:02  0:00:02 --:--:-- 5.2M
```

### **-I, --head**

Fetch HTTP headers only (HEAD request)

```console
$ curl -I https://example.com
HTTP/2 200 
content-type: text/html; charset=UTF-8
date: Tue, 30 Apr 2025 12:00:00 GMT
expires: Tue, 07 May 2025 12:00:00 GMT
cache-control: public, max-age=604800
server: ECS (dcb/7F83)
content-length: 1256
```

### **-X, --request \<method\>**

Specify the request method to use (GET, POST, PUT, DELETE, etc.)

```console
$ curl -X POST https://api.example.com/data
{"status":"success","message":"Data received"}
```

### **-H, --header \<header\>**

Add custom headers to the request

```console
$ curl -H "Content-Type: application/json" -H "Authorization: Bearer token123" https://api.example.com
{"data":"This is protected content"}
```

### **-d, --data \<data\>**

Send data in the request body (typically for POST requests)

```console
$ curl -X POST -d "name=John&age=30" https://api.example.com/users
{"id":123,"name":"John","age":30}
```

### **-s, --silent**

Silent mode (don't show progress meter or error messages)

```console
$ curl -s https://example.com
<!doctype html>
<html>
<head>
    <title>Example Domain</title>
    ...
</html>
```

## Usage Examples

### Downloading a file and showing progress

```console
$ curl -# -o firefox.dmg "https://download.mozilla.org/?product=firefox-latest"
######################################################################## 100.0%
```

### Sending JSON data in a POST request

```console
$ curl -X POST -H "Content-Type: application/json" -d '{"name":"Alice","email":"alice@example.com"}' https://api.example.com/users
{"id":456,"name":"Alice","email":"alice@example.com","status":"created"}
```

### Following redirects

```console
$ curl -L http://github.com
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>GitHub: Let's build from here · GitHub</title>
    ...
```

### Uploading a file

```console
$ curl -F "file=@photo.jpg" https://upload.example.com
{"success":true,"url":"https://cdn.example.com/uploads/photo123.jpg"}
```

## Tips

### Use `-v` for Debugging

The verbose flag (`-v`) shows the complete request and response headers, which is invaluable for debugging API calls or network issues.

```console
$ curl -v https://example.com
```

### Save Cookies and Use Them Later

Use `--cookie-jar` to save cookies and `--cookie` to use them in subsequent requests, which helps with authenticated sessions.

```console
$ curl --cookie-jar cookies.txt https://login.example.com
$ curl --cookie cookies.txt https://protected.example.com
```

### Set Timeouts for Unreliable Connections

Use `--connect-timeout` and `--max-time` to prevent curl from hanging indefinitely on slow or unresponsive servers.

```console
$ curl --connect-timeout 10 --max-time 30 https://slow-server.example.com
```

### Use `-k` with Caution

The `-k` (or `--insecure`) option allows connections to SSL sites without certificates, but should only be used for testing as it bypasses security checks.

## Frequently Asked Questions

#### Q1. How do I download a file with curl?
A. Use `curl -o filename URL` to save to a specific filename or `curl -O URL` to use the remote filename.

#### Q2. How can I send a POST request with curl?
A. Use `curl -X POST -d "key=value" URL` or `curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' URL` for JSON data.

#### Q3. How do I follow redirects with curl?
A. Use the `-L` or `--location` option to make curl follow HTTP redirects.

#### Q4. How can I see detailed information about the request and response?
A. Use the `-v` or `--verbose` option to see the complete HTTP transaction.

#### Q5. How do I upload a file with curl?
A. Use `curl -F "file=@path/to/file" URL` for form-based uploads or `curl -T filename URL` for direct uploads.

## References

https://curl.se/docs/manpage.html

## Revisions

- 2025/04/30 First revision