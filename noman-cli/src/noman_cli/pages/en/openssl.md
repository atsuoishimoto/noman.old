# openssl command

Provides cryptographic functionality for secure communications, certificate management, and various cryptographic operations.

## Overview

OpenSSL is a robust toolkit implementing the Secure Sockets Layer (SSL) and Transport Layer Security (TLS) protocols along with a full-strength general purpose cryptography library. It allows users to create certificates, manage keys, encrypt/decrypt files, generate message digests, and perform many other cryptographic operations from the command line.

## Options

OpenSSL uses a command-based structure where the main command is followed by a subcommand and its options.

### **s_client** - SSL/TLS client

Implements a generic SSL/TLS client which connects to a remote host using SSL/TLS.

```console
$ openssl s_client -connect example.com:443
CONNECTED(00000003)
depth=2 C = US, O = Internet Security Research Group, CN = ISRG Root X1
verify return:1
depth=1 C = US, O = Let's Encrypt, CN = R3
verify return:1
depth=0 CN = example.com
verify return:1
---
Certificate chain
 0 s:CN = example.com
   i:C = US, O = Let's Encrypt, CN = R3
...
```

### **x509** - Certificate display and signing utility

Displays certificate information, converts certificates to various formats, and signs certificate requests.

```console
$ openssl x509 -in certificate.crt -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            04:e5:7b:d2:1d:d5:e5:2c:...
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=US, O=Let's Encrypt, CN=R3
...
```

### **genrsa** - Generate RSA private key

Generates an RSA private key.

```console
$ openssl genrsa -out private.key 2048
Generating RSA private key, 2048 bit long modulus (2 primes)
.....+++++
.....+++++
e is 65537 (0x010001)
```

### **req** - PKCS#10 certificate request and certificate generating utility

Creates and processes certificate requests in PKCS#10 format.

```console
$ openssl req -new -key private.key -out certificate.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:California
...
```

### **enc** - Encoding with ciphers

Encrypts or decrypts using various cipher algorithms.

```console
$ openssl enc -aes-256-cbc -salt -in plaintext.txt -out encrypted.txt
enter aes-256-cbc encryption password:
Verifying - enter aes-256-cbc encryption password:
```

## Usage Examples

### Checking a remote SSL/TLS server

```console
$ openssl s_client -connect example.com:443 -servername example.com
CONNECTED(00000003)
depth=2 C = US, O = Internet Security Research Group, CN = ISRG Root X1
verify return:1
...
```

### Creating a self-signed certificate

```console
$ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
Generating a RSA private key
.....++++
.....++++
writing new private key to 'key.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
...
```

### Verifying certificate chain

```console
$ openssl verify -CAfile ca-bundle.crt certificate.crt
certificate.crt: OK
```

### Generating a random password

```console
$ openssl rand -base64 12
Ew6Y9RzYxAQeFA==
```

## Tips

### Use Proper Key Permissions

Always set restrictive permissions on private keys to prevent unauthorized access:

```console
$ chmod 600 private.key
```

### Verify Certificate Expiration

Check when a certificate expires to avoid unexpected service disruptions:

```console
$ openssl x509 -enddate -noout -in certificate.crt
notAfter=May 15 12:00:00 2026 GMT
```

### Convert Certificate Formats

OpenSSL can convert between different certificate formats (PEM, DER, PKCS#12):

```console
$ openssl x509 -in cert.pem -inform PEM -out cert.der -outform DER
```

### Use -passin and -passout for Automation

When scripting, use these options to provide passwords non-interactively:

```console
$ openssl rsa -in encrypted.key -out decrypted.key -passin file:password.txt
```

## Frequently Asked Questions

#### Q1. How do I create a CSR (Certificate Signing Request)?
A. Use `openssl req -new -key private.key -out request.csr`. You'll be prompted for certificate information.

#### Q2. How can I check the contents of a certificate?
A. Use `openssl x509 -in certificate.crt -text -noout` to display the certificate details.

#### Q3. How do I convert a certificate from PEM to PKCS#12 format?
A. Use `openssl pkcs12 -export -out certificate.pfx -inkey private.key -in certificate.crt -certfile ca-chain.crt`.

#### Q4. How can I test a secure connection to a website?
A. Use `openssl s_client -connect example.com:443 -servername example.com` to establish a connection and view certificate details.

#### Q5. How do I generate a strong random password?
A. Use `openssl rand -base64 16` to generate a 16-byte random string encoded in base64.

## References

https://www.openssl.org/docs/man1.1.1/man1/

## Revisions

- 2025/05/04 First revision