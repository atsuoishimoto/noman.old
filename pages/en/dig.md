# dig command

Query DNS name servers for domain information.

## Overview

`dig` (Domain Information Groper) is a flexible DNS lookup utility that allows you to query DNS servers for information about domain names, IP addresses, mail exchanges, and other DNS records. It's commonly used for troubleshooting DNS issues, verifying DNS configurations, and testing DNS changes.

## Options

### **-t, --type=TYPE**

Specify the type of DNS record to query (e.g., A, MX, NS, ANY)

```console
$ dig -t MX google.com
;; ANSWER SECTION:
google.com.		300	IN	MX	10 smtp.google.com.
```

### **-x, --reverse**

Perform a reverse DNS lookup (convert IP address to hostname)

```console
$ dig -x 8.8.8.8
;; ANSWER SECTION:
8.8.8.8.in-addr.arpa.	7200	IN	PTR	dns.google.
```

### **@server**

Query a specific DNS server instead of the default

```console
$ dig @1.1.1.1 example.com
;; ANSWER SECTION:
example.com.		86400	IN	A	93.184.216.34
```

### **+short**

Display a terse answer (only the result, without headers and additional information)

```console
$ dig +short google.com
142.250.190.78
```

### **+noall, +answer**

Control which sections of the response to display

```console
$ dig +noall +answer google.com
google.com.		300	IN	A	142.250.190.78
```

## Usage Examples

### Basic Domain Lookup

```console
$ dig example.com
;; QUESTION SECTION:
;example.com.			IN	A

;; ANSWER SECTION:
example.com.		86400	IN	A	93.184.216.34
```

### Looking Up Multiple Record Types

```console
$ dig example.com ANY
;; ANSWER SECTION:
example.com.		86400	IN	A	93.184.216.34
example.com.		86400	IN	NS	a.iana-servers.net.
example.com.		86400	IN	NS	b.iana-servers.net.
example.com.		86400	IN	SOA	ns.icann.org. noc.dns.icann.org. 2023080794 7200 3600 1209600 3600
```

### Tracing the DNS Resolution Path

```console
$ dig +trace example.com
;; Received 13 bytes from 192.168.1.1#53 in 10 ms

. 			518400	IN	NS	a.root-servers.net.
...
;; Received 811 bytes from 192.5.6.30#53 in 40 ms

com. 			172800	IN	NS	a.gtld-servers.net.
...
;; Received 1173 bytes from 192.41.162.30#53 in 160 ms

example.com.		86400	IN	NS	a.iana-servers.net.
...
;; Received 97 bytes from 199.43.135.53#53 in 100 ms

example.com.		86400	IN	A	93.184.216.34
```

## Tips

### Use +nocomments for Cleaner Output

The `+nocomments` option removes comment lines from the output, making it easier to read when you only need the essential information.

### Check DNS Propagation

When you've made DNS changes, use `dig @server domain.com` with different DNS servers to check if your changes have propagated.

### Specify Multiple Queries in One Command

You can query multiple domains or record types in a single command: `dig example.com mx google.com a`.

### Use +stats for Performance Analysis

The `+stats` option shows query statistics including how long the query took, which is useful for diagnosing slow DNS resolution.

## Frequently Asked Questions

#### Q1. How is `dig` different from `nslookup`?
A. `dig` provides more detailed information and has more options for DNS queries. It's generally preferred by network administrators for its comprehensive output and flexibility.

#### Q2. How do I check if my DNS changes have propagated?
A. Use `dig @different-dns-servers your-domain.com` to query multiple DNS servers and compare the results.

#### Q3. How can I find the authoritative name servers for a domain?
A. Use `dig NS domain.com` to find the name servers responsible for a domain.

#### Q4. How do I check the TTL (Time To Live) for a DNS record?
A. The TTL is shown in the standard output of `dig`. It's the number (in seconds) before the first IN in the answer section.

## References

https://linux.die.net/man/1/dig

## Revisions

- 2025/05/04 First revision