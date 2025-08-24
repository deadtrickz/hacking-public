# Passive Reconnaissance
---
---

## Banner Grabbing
---
- ##### netcat
```
nc -vv [IP] [port]
```

## Host Discovery
---
- ##### netdiscover
	- p means passive; only receives traffic and does not send
```sh
sudo netdiscover -p
```

## WHOIS Enumeration
```
whois domain.com | less
```
- registrant name
- name servers

##### Reverse Lookup (IP Lookup)
- using an IP
```
whois [IP] | less
```


### DNS Records
```
dig @[server] [domain] -[flag(s)]
```

Flags
```
- NS - a nameserver record, this indicates the name servers that are associated with a given domain.
- A - address record, this maps a domain name to an IPv4 address
- AAAA - "Quad-A" record, this maps a domain name to an IPv6 address
- HINFO - Host Information record, this associates an arbitrary set of information with a domain name. It is formerly used to indicate system types.
- MX - mail exchange record, this identifies the mail servers associated with a given domain.
- TXT - text record, this includes an arbitrary text string for the domain.
- CNAME - a canonical name record, this indicates an alias or alternative name for a given host.
- SOA - start of authority record, which indicates that a server is the authoritative server for a given DNS zone.
- RP - responsible person records, these are informational and not functional. They indicate the person responsible for a given domain, and it is not used very often.
- PTR - pointer record, for inverse lookups (also called a reverse record). It indicates an IP address to domain name mapping.
- SRV - service location records, which provides information about available services, including the port and hostname, also not used very often.
```

#### Zone Transfer
```
dig @[server] [domain] -t AXFR
```

##### Incremental Zone Transfer
- Perform a zone transfer which pulls only recently updated records (all records that have changed since the SOA serial number was [N]).
```
dig @[server] [domain] -t IXFR=[N]
```
