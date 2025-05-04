# http command

Send arbitrary HTTP requests and display responses from the command line.

## Overview

The `http` command is part of HTTPie, a user-friendly command-line HTTP client designed to make CLI interaction with web services as human-friendly as possible. It provides a simple interface for sending HTTP requests with various methods (GET, POST, PUT, etc.) and displays colorized output for better readability.

## Options

### **-j, --json**

Send JSON data in the request body.

```console
$ http -j POST example.com name=John age:=30
```

### **-f, --form**

Send form-encoded data in the request body.

```console
$ http -f POST example.com name=John age=30
```

### **-a, --auth**

Specify authentication credentials.

```console
$ http -a username:password example.com
```

### **-h, --headers**

Print only the response headers.

```console
$ http -h example.com
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Date: Sat, 04 May 2025 12:00:00 GMT
Server: nginx
Content-Length: 1256
```

### **-v, --verbose**

Print the whole HTTP exchange (request and response).

```console
$ http -v example.com
GET / HTTP/1.1
Host: example.com
User-Agent: HTTPie/3.2.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive

HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Date: Sat, 04 May 2025 12:00:00 GMT
Server: nginx
Content-Length: 1256

<!doctype html>
<html>
...
```

### **--verify**

Control SSL verification. Can be set to `no` to disable verification.

```console
$ http --verify=no https://example.com
```

### **--session**

Create or reuse a session for multiple requests.

```console
$ http --session=mysession -a username:password example.com
$ http --session=mysession example.com/api/resource
```

## Usage Examples

### Basic GET request

```console
$ http example.com
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Date: Sat, 04 May 2025 12:00:00 GMT
Server: nginx
Content-Length: 1256

<!doctype html>
<html>
...
```

### POST with JSON data

```console
$ http POST api.example.com/users name=John age:=30 is_active:=true
HTTP/1.1 201 Created
Content-Type: application/json
Location: /users/123
Content-Length: 42

{
    "id": 123,
    "name": "John",
    "age": 30,
    "is_active": true
}
```

### Download a file

```console
$ http --download https://example.com/file.zip
Downloading to "file.zip"
Done. 15.43 MB in 2.32s (6.65 MB/s)
```

### Custom headers

```console
$ http example.com X-API-Token:abc123 User-Agent:MyApp/1.0
```

## Tips

### Use Shortcuts for Common HTTP Methods

HTTPie provides shortcuts for common HTTP methods, so you can use `http example.com` instead of `http GET example.com`.

### JSON Data Syntax

When sending JSON data, use `:=` for numbers and booleans, and `=` for strings:
- `name=John` becomes `{"name": "John"}`
- `age:=30` becomes `{"age": 30}`
- `active:=true` becomes `{"active": true}`

### Pipe Output to Other Tools

You can pipe the output to tools like `jq` for JSON processing:
```console
$ http api.example.com/users | jq '.[] | select(.active==true)'
```

### Use Output Redirection

Save response bodies to files using standard output redirection:
```console
$ http example.com/image.jpg > image.jpg
```

## Frequently Asked Questions

#### Q1. How do I send a POST request with form data?
A. Use `http -f POST example.com name=value` to send form-encoded data.

#### Q2. How do I include authentication in my request?
A. Use the `-a` or `--auth` option: `http -a username:password example.com`.

#### Q3. How can I see the full HTTP exchange?
A. Use the `-v` or `--verbose` option to see both request and response details.

#### Q4. How do I send a file in my request?
A. Use `@filename` to include file contents: `http POST example.com file@/path/to/file.txt`.

#### Q5. How do I set cookies for my request?
A. Use the `--session` option to maintain cookies between requests, or manually set the Cookie header.

## References

https://httpie.io/docs/cli

## Revisions

- 2025/05/04 First revision