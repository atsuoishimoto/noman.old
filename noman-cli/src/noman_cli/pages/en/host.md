# host command

Look up DNS information for domain names and IP addresses.

## Overview

The `host` command is a DNS lookup utility that converts domain names to IP addresses and vice versa. It's simpler than `dig` or `nslookup` and is useful for quick DNS queries, checking domain information, and basic network troubleshooting.

## Options

### **-t type**

Specify the DNS record type to look up (A, MX, NS, etc.)

```console
$ host -t MX gmail.com
gmail.com mail is handled by 10 alt1.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 20 alt2.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 30 alt3.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 40 alt4.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 5 gmail-smtp-in.l.google.com.
```

### **-a**

Display all available information about a domain (equivalent to -t ANY)

```console
$ host -a example.com
Trying "example.com"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;example.com.                   IN      ANY

;; ANSWER SECTION:
example.com.            86400   IN      A       93.184.216.34
```

### **-v**

Enable verbose output, showing more detailed information

```console
$ host -v google.com
Trying "google.com"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 39508
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;google.com.                    IN      A

;; ANSWER SECTION:
google.com.             299     IN      A       142.250.190.78
```

### **-4**

Use IPv4 queries only

```console
$ host -4 example.com
example.com has address 93.184.216.34
```

### **-6**

Use IPv6 queries only

```console
$ host -6 google.com
google.com has IPv6 address 2a00:1450:4001:830::200e
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
$ host 8.8.8.8
8.8.8.8.in-addr.arpa domain name pointer dns.google.
```

### Looking up Name Server Records

```console
$ host -t NS github.com
github.com name server ns-1707.awsdns-21.co.uk.
github.com name server ns-421.awsdns-52.com.
github.com name server ns-520.awsdns-01.net.
github.com name server ns-1283.awsdns-32.org.
```

### Querying a Specific DNS Server

```console
$ host example.com 8.8.8.8
Using domain server:
Name: 8.8.8.8
Address: 8.8.8.8#53
Aliases: 

example.com has address 93.184.216.34
example.com has IPv6 address 2606:2800:220:1:248:1893:25c8:1946
```

## Tips

### Use Short Form for Common Queries

For quick lookups, you can omit the `-t` option and just specify the record type: `host -t MX example.com` can be shortened to `host MX example.com`.

### Troubleshoot Email Delivery

Check MX records when troubleshooting email delivery issues: `host -t MX domain.com` shows mail servers for a domain.

### Verify DNS Propagation

When you've updated DNS records, use `host` with different DNS servers to check if changes have propagated: `host example.com 8.8.8.8` and `host example.com 1.1.1.1`.

### Combine with Other Tools

Pipe `host` output to other commands for further processing: `host -t A example.com | grep "has address" | cut -d' ' -f4`.

## Frequently Asked Questions

#### Q1. What's the difference between `host`, `dig`, and `nslookup`?
A. `host` is simpler and more concise, `dig` provides comprehensive DNS information in a structured format, and `nslookup` is an interactive tool. `host` is best for quick lookups, while `dig` is better for detailed DNS troubleshooting.

#### Q2. How do I check if a domain exists?
A. Run `host domain.com`. If it returns "not found", the domain either doesn't exist or doesn't have DNS records configured.

#### Q3. Can I use `host` to check if a website is down?
A. Not directly. `host` only checks DNS records, not if a website is operational. It can tell you if DNS is resolving correctly, which is one potential cause of website unavailability.

#### Q4. How do I find all subdomains of a domain?
A. `host` doesn't have a built-in feature for this. You'd need to use a zone transfer (`host -l domain.com nameserver`) if allowed, or use specialized tools like `dnsrecon`.

## References

https://linux.die.net/man/1/host

## Revisions

- 2025/04/30 First revision