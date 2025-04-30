# dig command

Query DNS name servers for domain information.

## Overview

`dig` (Domain Information Groper) is a flexible tool for interrogating DNS name servers. It performs DNS lookups and displays the answers returned from the queried name servers. System administrators and network troubleshooters commonly use it to verify DNS records and diagnose DNS problems.

## Options

### **-t (type)**

Specify the type of DNS record to query (A, MX, NS, etc.)

```console
$ dig -t MX google.com
;; ANSWER SECTION:
google.com.		600	IN	MX	10 smtp.google.com.
```

### **-x (reverse lookup)**

Perform a reverse DNS lookup to find the hostname associated with an IP address

```console
$ dig -x 8.8.8.8
;; ANSWER SECTION:
8.8.8.8.in-addr.arpa.	7200	IN	PTR	dns.google.
```

### **+short**

Display a terse answer, showing only the requested information

```console
$ dig +short google.com
142.250.190.78
```

### **@server**

Query a specific DNS server instead of the default

```console
$ dig @1.1.1.1 google.com
;; ANSWER SECTION:
google.com.		300	IN	A	142.250.190.78
```

## Usage Examples

### Looking up A records (IP addresses)

```console
$ dig google.com
;; ANSWER SECTION:
google.com.		300	IN	A	142.250.190.78
```

### Finding name servers for a domain

```console
$ dig -t NS example.com
;; ANSWER SECTION:
example.com.		86400	IN	NS	a.iana-servers.net.
example.com.		86400	IN	NS	b.iana-servers.net.
```

### Tracing the entire DNS resolution path

```console
$ dig +trace google.com
;; Received 13 records from 198.41.0.4 in 40 ms

;; Received 6 records from 192.12.94.30 in 160 ms

;; Received 4 records from 216.239.34.10 in 40 ms

google.com.		300	IN	A	142.250.190.78
;; Received 1 records from 216.239.38.10 in 40 ms
```

## Tips

### Use +noall +answer for Clean Output

The `+noall +answer` options remove all the extra information and only show the answer section, making output easier to read:

```console
$ dig +noall +answer google.com
google.com.		300	IN	A	142.250.190.78
```

### Check DNS Propagation

When you've updated DNS records, use dig with different DNS servers to check if changes have propagated:

```console
$ dig @8.8.8.8 example.com
$ dig @1.1.1.1 example.com
```

### Use +stats for Query Statistics

Add `+stats` to see how long the query took and which server responded:

```console
$ dig +stats google.com
;; Query time: 28 msec
;; SERVER: 192.168.1.1#53(192.168.1.1)
;; WHEN: Wed Apr 30 10:00:00 EDT 2025
;; MSG SIZE  rcvd: 55
```

## Frequently Asked Questions

#### Q1. What's the difference between `dig` and `nslookup`?
A. Both query DNS servers, but `dig` provides more detailed output and has more options for advanced DNS troubleshooting. `nslookup` is simpler but less powerful.

#### Q2. How do I check if my domain's DNS is properly configured?
A. Use `dig -t ANY yourdomain.com` to see all record types, or check specific records with `dig -t A`, `dig -t MX`, etc.

#### Q3. How can I find which DNS server is being used for a query?
A. Use `dig +trace domain.com` to see the full resolution path, or add `+stats` to see which server answered your query.

#### Q4. How do I check DNS propagation globally?
A. Query multiple DNS servers around the world using `@server` option with different public DNS servers.

## References

https://linux.die.net/man/1/dig

## Revisions

- 2025/04/30 First revision