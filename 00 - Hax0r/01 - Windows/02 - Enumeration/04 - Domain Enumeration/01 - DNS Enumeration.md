# DNS Enumeration

### Retrieve DNS Records
```
dig @[SERVER] [DOMAIN] -[flag(s)]
```

### Zone Transfer
```
dig @[SERVER] [DOMAIN] -t AXFR
```

### Incremental Zone Transfer
```
dig @[SERVER] [DOMAIN] AXFR +ixfr=[SERIAL]
```
- zone transfer which pulls only recently updated records (all records that have changed since that SOA serial number)

##### Flags
| Flag   | Description                          |
|--------|--------------------------------------|
| NS     | Nameserver for the domain            |
| A      | Maps domain to IPv4 address          |
| AAAA   | Maps domain to IPv6 address          |
| HINFO  | Host/system info (rarely used)       |
| MX     | Mail server for the domain           |
| TXT    | Freeform text data                   |
| CNAME  | Domain alias                         |
| SOA    | Authoritative DNS zone info          |
| RP     | Responsible person (rarely used)     |
| PTR    | Reverse lookup (IP to domain)        |
| SRV    | Service info (hostname and port)     |
