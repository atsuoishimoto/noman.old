# host command

DNS lookup utility for querying domain name servers.

## Overview

The `host` command is a simple utility for performing DNS lookups. It's used to convert domain names to IP addresses and vice versa, as well as for querying DNS records. It's simpler than `dig` or `nslookup` and is useful for quick DNS queries.

## Options

### **-a, --all**

Display all available information (equivalent to -v -t ANY)

```console
$ host -a example.com
Trying "example.com"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;example.com.                   IN      ANY

;; ANSWER SECTION:
example.com.            86400   IN      A       93.184.216.34
example.com.            86400   IN      AAAA    2606:2800:220:1:248:1893:25c8:1946
example.com.            86400   IN      NS      a.iana-servers.net.
example.com.            86400   IN      NS      b.iana-servers.net.
example.com.            86400   IN      SOA     ns.icann.org. noc.dns.icann.org. 2023050101 7200 3600 1209600 3600
```

### **-t, --type=TYPE**

Specify the query type (e.g., A, MX, NS, etc.)

```console
$ host -t MX gmail.com
gmail.com mail is handled by 10 alt1.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 20 alt2.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 30 alt3.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 40 alt4.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 5 gmail-smtp-in.l.google.com.
```

### **-v, --verbose**

Enable verbose output with more detailed information

```console
$ host -v example.com
Trying "example.com"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;example.com.                   IN      A

;; ANSWER SECTION:
example.com.            86400   IN      A       93.184.216.34

Received 56 bytes from 8.8.8.8#53 in 28 ms
```

### **-4, -6**

Use IPv4 (-4) or IPv6 (-6) transport only

```console
$ host -4 example.com
example.com has address 93.184.216.34

$ host -6 example.com
example.com has IPv6 address 2606:2800:220:1:248:1893:25c8:1946
```

### **-C, --checking**

Check consistency of the DNS server's responses

```console
$ host -C example.com
Host example.com is consistent
```

## Usage Examples

### Basic Domain Lookup

```console
$ host example.com
example.com has address 93.184.216.34
example.com has IPv6 address 2606:2800:220:1:248:1893:25c8:1946
example.com mail is handled by 0 .
```

### Reverse DNS Lookup

```console
$ host 93.184.216.34
34.216.184.93.in-addr.arpa domain name pointer example.com.
```

### Querying Specific DNS Server

```console
$ host example.com 8.8.8.8
Using domain server:
Name: 8.8.8.8
Address: 8.8.8.8#53
Aliases: 

example.com has address 93.184.216.34
example.com has IPv6 address 2606:2800:220:1:248:1893:25c8:1946
```

### Looking Up Name Servers

```console
$ host -t NS google.com
google.com name server ns1.google.com.
google.com name server ns2.google.com.
google.com name server ns3.google.com.
google.com name server ns4.google.com.
```

## Tips

### Use Short Format for Quick Lookups

For quick lookups, just use `host domain.com` without any options. This gives you the most essential information in a concise format.

### Specify DNS Server for Troubleshooting

When troubleshooting DNS issues, specify a different DNS server (like Google's 8.8.8.8) to check if the problem is with your default DNS server.

### Combine with grep for Filtering

Use `host` with `grep` to filter specific information, like `host -t ANY example.com | grep MX` to see only mail exchange records.

### Use -t ANY for Complete Records

When you need to see all DNS records for a domain, use `host -t ANY domain.com` instead of running multiple queries for different record types.

## Frequently Asked Questions

#### Q1. What's the difference between `host`, `dig`, and `nslookup`?
A. `host` is simpler and more user-friendly than `dig`, which provides more detailed output. `nslookup` is an older interactive tool. For quick lookups, `host` is often preferred, while `dig` is better for detailed DNS troubleshooting.

#### Q2. How do I check if a domain has proper mail server configuration?
A. Use `host -t MX domain.com` to check mail exchange records.

#### Q3. Can I use `host` to check DNS propagation?
A. Yes, use `host domain.com dns-server-ip` with different DNS servers to check if DNS changes have propagated.

#### Q4. How do I look up all DNS records for a domain?
A. Use `host -a domain.com` or `host -t ANY domain.com` to see all available DNS records.

## References

https://linux.die.net/man/1/host

## Revisions

- 2025/05/04 First revision