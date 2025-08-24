# DNS

## Enumeration

### Identify DNS and Mail Servers

##### host (Name Server)
```bash
host -t ns [domain name]
```

##### host (Mail Server)
```bash
host -t mx [domain name]
```

### Forward DNS Lookup  
- Find the IP address of a domain name
##### host
```bash
host [domain]
```

### Reverse DNS Lookup  
- Find the domain name associated with an IP

##### host
```bash
host [IP]
```

##### nslookup
```bash
nslookup
```
```bash
server [DNS_IP]
```
```bash
[IP]
```

### Zone Transfers  
*Attempt to dump all DNS records from a misconfigured DNS server*

##### host
```bash
host -l [DOMAIN] [DNS_IP]
```

##### dnsrecon
```bash
dnsrecon -d [DOMAIN] -t axfr
```

##### dig
```bash
dig @[DNS_IP] [DOMAIN] AXFR
```

### Metasploit

##### enum_dns
```bash
use auxiliary/gather/enum_dns
set DOMAIN [domain]
run
```

##### dns_enum (Subdomain Brute Forcing)
```bash
use auxiliary/gather/dns_enum
set DOMAIN [domain]
run
```


---
---


## Exploitation

### Metasploit

##### dns_amp (DNS Amplification DDoS Testing)
```bash
use auxiliary/amplification/dns/dns_amp
set RHOSTS [IP]
set SHOST [spoofed_IP]
run
```

##### dns_bindshell (Bind shell exploit over DNS)

```bash
use exploit/windows/dns/dns_bindshell
set RHOST [IP]
run
```

### Nmap

##### DNS-related NSE scripts
```bash
nmap -p 53 --script=dns-brute,dns-cache-snoop,dns-nsid,dns-zone-transfer [IP]
```

### dnsenum

##### dnsenum (Brute force and enumerate DNS info)
```bash
dnsenum [domain]
```

### fierce

##### fierce (Subdomain/host brute forcing)
```bash
fierce --domain [domain]
```

### dig (Brute force with a wordlist)
```bash
for sub in $(cat wordlist.txt); do dig $sub.[domain] @target_dns_server; done
```
