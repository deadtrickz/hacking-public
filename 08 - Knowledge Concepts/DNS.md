# DNS Concepts

## Overview

**DNS (Domain Name System)** is a decentralized system used to translate human-readable domain names (like `www.example.com`) into machine-readable IP addresses (like `192.0.2.1`). DNS is an essential part of the internet infrastructure, enabling users to access websites without needing to remember numeric IP addresses.


## Key Components

| Component                    | Description                                                                                    |
| ---------------------------- | ---------------------------------------------------------------------------------------------- |
| **Domain Name**              | The human-readable address that is mapped to an IP address (`example.com`).                    |
| **DNS Resolver**             | A client that queries DNS servers to resolve domain names into IP addresses.                   |
| **DNS Server**               | A server that holds and provides domain name records to clients.                               |
| **DNS Records**              | Entries in DNS servers that map domain names to IP addresses and other data (`A`, `MX`, `NS`). |
| **Root DNS Servers**         | The highest-level DNS servers, which direct queries to other DNS servers in the hierarchy.     |
| **Authoritative DNS Server** | The server that provides the definitive answer for a domain name query.                        |


## How DNS Works

1. **DNS Query Initiation**: When a user attempts to visit a website, their device checks local caches before sends a DNS query to a DNS resolver.
2. **Resolver Search**: The DNS resolver checks if it has a cached copy of the domain’s IP address.
3. **Root DNS Server**: If the resolver doesn’t have the IP, it queries a root DNS server for the top-level domain (TLD), like `.com` or `.org`.
4. **TLD DNS Server**: The TLD DNS server returns the address of the authoritative DNS server for the specific domain.
5. **Authoritative DNS Server**: The authoritative DNS server provides the IP address for the requested domain, which is returned to the resolver.
6. **Caching**: The resolver caches the IP address to speed up future queries for the same domain.
	- Browser Cache/Host Cache 


## DNS Records

| Record Type      | Description                                                                                    |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| **A Record**     | Maps a domain name to an IPv4 address (e.g., `example.com` -> `192.0.2.1`).                    |
| **AAAA Record**  | Maps a domain name to an IPv6 address.                                                         |
| **MX Record**    | Specifies mail servers responsible for receiving email for a domain.                           |
| **CNAME Record** | An alias record that points to another domain name (e.g., `www.example.com` -> `example.com`). |
| **NS Record**    | Indicates which name servers are authoritative for the domain.                                 |
| **PTR Record**   | Used for reverse DNS lookups, mapping an IP address to a domain name.                          |
| **TXT Record**   | Allows for arbitrary text entries, often used for verification (e.g., SPF or DKIM).            |
| **SOA Record**   | Start of Authority, providing administrative information about the domain.                     |


## Types of DNS Servers

| Server Type               | Description |
|---------------------------|-------------|
| **DNS Resolver**           | A client-side server that queries other DNS servers to resolve domain names. |
| **Root DNS Server**        | A top-level server that directs queries to the correct TLD server. |
| **TLD DNS Server**         | A server responsible for a top-level domain (e.g., `.com`, `.net`, `.org`). |
| **Authoritative DNS Server** | A DNS server that provides the definitive answer for a domain name query. |
| **Caching DNS Server**     | A server that temporarily stores DNS query results to improve performance. |


## DNS Caching

- **TTL (Time To Live)**: The amount of time a DNS record is cached by a resolver before it expires and a new query is made.
- **Benefits of Caching**: Reduces DNS query load, improves resolution times, and reduces internet traffic.
- **DNS Cache Poisoning**: An attack where malicious DNS records are inserted into a DNS cache, potentially redirecting users to malicious websites.


## Common DNS Tools

| Tool            | Description |
|-----------------|-------------|
| **nslookup**    | A command-line tool for querying DNS records. |
| **dig**         | A more powerful command-line tool for querying DNS information and debugging DNS issues. |
| **host**        | A simple command-line tool for querying DNS records. |
| **dnsrecon**    | A Python-based DNS reconnaissance tool used for DNS enumeration. |
| **whois**       | A command-line tool to get information about domain registration and ownership. |


## DNS Security

| Concept            | Description |
|--------------------|-------------|
| **DNSSEC**         | DNS Security Extensions, a set of protocols that provide security to DNS by enabling DNS responses to be verified as authentic. |
| **DNS Spoofing**   | A form of attack where an attacker falsifies DNS responses to redirect users to malicious sites. |
| **DDoS Attacks**   | Distributed Denial of Service attacks targeting DNS servers to overwhelm them with traffic, causing downtime. |


## Common DNS Commands

| Command                        | Description                               |
| ------------------------------ | ----------------------------------------- |
| **nslookup [domain]**          | Look up DNS information for a domain.     |
| **dig [domain]**               | Query DNS records for a domain.           |
| **dig @[DNS_SERVER] [domain]** | Query a specific DNS server for a domain. |
| **host [domain]**              | Perform a simple DNS lookup.              |
| **dnsrecon -d [domain]**       | Perform DNS reconnaissance for a domain.  |

