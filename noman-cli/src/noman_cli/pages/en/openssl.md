# openssl command

Manage cryptographic functions, certificates, and secure connections.

## Overview

OpenSSL is a powerful toolkit for working with SSL/TLS protocols and cryptography. It allows you to create certificates, encrypt/decrypt files, generate cryptographic keys, hash data, and test secure connections. It's essential for managing secure communications and implementing security protocols.

## Options

### **s_client** - Test SSL/TLS connections

Connect to a secure server to test or debug SSL/TLS connections

```console
$ openssl s_client -connect example.com:443
CONNECTED(00000003)
depth=2 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
verify return:1
...
```

### **req** - Certificate request and certificate generating utility

Create certificate signing requests (CSRs) or self-signed certificates

```console
$ openssl req -new -newkey rsa:2048 -nodes -keyout server.key -out server.csr
Generating a RSA private key
.....+++++
.....+++++
writing new private key to 'server.key'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
...
```

### **x509** - Certificate display and signing utility

Display or modify certificate information

```console
$ openssl x509 -in certificate.crt -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            12:34:56:78:9a:bc:de:f0
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3
...
```

### **genrsa** - Generate RSA private key

Create RSA private keys of specified bit length

```console
$ openssl genrsa -out private.key 2048
Generating RSA private key, 2048 bit long modulus
.......................+++
.......................+++
e is 65537 (0x10001)
```

### **enc** - Encrypt or decrypt using various ciphers

Encrypt or decrypt files using symmetric encryption algorithms

```console
$ openssl enc -aes-256-cbc -salt -in plaintext.txt -out encrypted.txt
enter aes-256-cbc encryption password:
Verifying - enter aes-256-cbc encryption password:
```

## Usage Examples

### Viewing certificate information from a website

```console
$ openssl s_client -connect google.com:443 -showcerts </dev/null | openssl x509 -text
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            33:00:00:00:14:20:0e:99:4f:15:c4:41:8e:f5:16:31:0f:ca
...
```

### Creating a self-signed certificate

```console
$ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
Generating a RSA private key
.................++++
.................++++
writing new private key to 'key.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
...
```

### Generating a secure random password

```console
$ openssl rand -base64 16
dGhpcyBpcyBhIHNlY3JldCE=
```

### Calculating file hash

```console
$ openssl dgst -sha256 file.txt
SHA256(file.txt)= e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

## Tips:

### Check SSL/TLS Configuration of a Server

Use `openssl s_client -connect hostname:port` to check the SSL/TLS configuration of a server, including certificate chain and supported ciphers.

### Verify Certificate Expiration

Use `openssl x509 -enddate -noout -in certificate.crt` to quickly check when a certificate expires without displaying all certificate information.

### Convert Certificate Formats

OpenSSL can convert between different certificate formats (PEM, DER, PKCS#12). For example, to convert from PEM to DER: `openssl x509 -in cert.pem -outform DER -out cert.der`.

### Use Environment Variables for Passwords

Instead of typing passwords in the command line (which might be logged in history), use environment variables: `export OPENSSL_PWD=mypassword` and then `openssl ... -passin env:OPENSSL_PWD`.

## Frequently Asked Questions

#### Q1. How do I check if a website's SSL certificate is valid?
A. Use `openssl s_client -connect website.com:443` to connect and view the certificate chain. Look for "Verify return code: 0 (ok)" to confirm validity.

#### Q2. How do I create a CSR (Certificate Signing Request)?
A. Use `openssl req -new -newkey rsa:2048 -nodes -keyout domain.key -out domain.csr` and follow the prompts.

#### Q3. How do I encrypt a file with OpenSSL?
A. Use `openssl enc -aes-256-cbc -salt -in plaintext.txt -out encrypted.txt` and provide a password when prompted.

#### Q4. How do I generate a random string for use as a password or key?
A. Use `openssl rand -base64 16` for a 16-byte random string encoded in base64.

#### Q5. How do I check what ciphers a server supports?
A. Use `openssl s_client -connect hostname:443 -cipher 'CIPHER-SUITE'` to test specific ciphers, or `nmap --script ssl-enum-ciphers -p 443 hostname` for a comprehensive list.

## References

https://www.openssl.org/docs/

## Revisions

- 2025/04/30 First revision