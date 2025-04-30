# http command

Send HTTP requests from the command line and display responses.

## Overview

The `http` command is a user-friendly HTTP client for the command line, provided by HTTPie. It allows you to make HTTP requests, test APIs, and interact with web services using a simple syntax. HTTPie is designed to be more intuitive than curl, with colorized output and JSON support built-in.

## Options

### **-f, --form**

Send data as form-encoded (similar to browser form submission)

```console
$ http -f POST example.com name=John age=30
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "Form data received",
    "form": {
        "name": "John",
        "age": "30"
    }
}
```

### **-j, --json**

Send data as JSON (default for sending data)

```console
$ http -j POST example.com name=John age:=30
HTTP/1.1 200 OK
Content-Type: application/json

{
    "message": "JSON data received",
    "json": {
        "name": "John",
        "age": 30
    }
}
```

### **-v, --verbose**

Show the full HTTP exchange (request and response headers)

```console
$ http -v example.com
GET / HTTP/1.1
Host: example.com
User-Agent: HTTPie/3.2.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive

HTTP/1.1 200 OK
Age: 595934
Cache-Control: max-age=604800
Content-Type: text/html; charset=UTF-8
Date: Fri, 30 Apr 2025 12:34:56 GMT
Etag: "3147526947+ident"
Expires: Fri, 07 May 2025 12:34:56 GMT
Last-Modified: Thu, 17 Oct 2024 07:18:26 GMT
Server: ECS (dcb/7F83)
Vary: Accept-Encoding
X-Cache: HIT
Content-Length: 1256

<!doctype html>
<html>
...
```

### **-a, --auth**

Add authentication to the request

```console
$ http -a username:password example.com/api/protected
HTTP/1.1 200 OK
Content-Type: application/json

{
    "authenticated": true,
    "user": "username"
}
```

### **-h, --headers**

Show only the response headers

```console
$ http -h example.com
HTTP/1.1 200 OK
Age: 595934
Cache-Control: max-age=604800
Content-Type: text/html; charset=UTF-8
Date: Fri, 30 Apr 2025 12:34:56 GMT
Etag: "3147526947+ident"
Expires: Fri, 07 May 2025 12:34:56 GMT
Last-Modified: Thu, 17 Oct 2024 07:18:26 GMT
Server: ECS (dcb/7F83)
Vary: Accept-Encoding
X-Cache: HIT
Content-Length: 1256
```

## Usage Examples

### Basic GET request

```console
$ http example.com
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 1256

<!doctype html>
<html>
...
```

### POST request with JSON data

```console
$ http POST api.example.com/users name=John email=john@example.com
HTTP/1.1 201 Created
Content-Type: application/json

{
    "id": 123,
    "name": "John",
    "email": "john@example.com",
    "created_at": "2025-04-30T12:34:56Z"
}
```

### Adding custom headers

```console
$ http example.com/api X-API-Token:abc123 Accept:application/json
HTTP/1.1 200 OK
Content-Type: application/json

{
    "status": "success",
    "data": { ... }
}
```

### Downloading a file

```console
$ http --download https://example.com/file.zip
Downloading to "file.zip"
Done. 15.43 MB in 2.32s (6.65 MB/s)
```

## Tips

### JSON Data Types

When sending JSON data, use `:=` for numbers, booleans, and null: `count:=42 active:=true data:=null`

### URL Parameters

Add URL parameters with `==`: `http example.com/search q==httpie`

### File Upload

Upload files using `@` symbol: `http POST example.com/upload file@/path/to/file.txt`

### Session Support

Use `--session=NAME` to maintain cookies between requests: `http --session=logged-in -a user:pass example.com`

### Redirect Output

Save response body to a file: `http example.com/file.pdf > file.pdf`

## Frequently Asked Questions

#### Q1. How is HTTPie different from curl?
A. HTTPie has a more intuitive syntax, colorized output, and built-in JSON support. It's designed to be more user-friendly for API testing and development.

#### Q2. How do I install HTTPie?
A. You can install it via pip (`pip install httpie`), Homebrew on macOS (`brew install httpie`), or apt on Ubuntu/Debian (`apt install httpie`).

#### Q3. How do I send form data vs. JSON data?
A. Use `-f` or `--form` for form data, and `-j` or `--json` for JSON data (JSON is the default when sending data).

#### Q4. How can I see the full HTTP request being sent?
A. Use the `-v` or `--verbose` flag to see the complete HTTP exchange, including all request and response headers.

#### Q5. How do I set cookies for a request?
A. Use the `Cookie:` header: `http example.com Cookie:'name=value; another=value2'`

## References

https://httpie.io/docs/cli

## Revisions

- 2025/04/30 First revision