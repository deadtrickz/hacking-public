# Telnet

## Enumeration

### Banner Grabbing

##### telnet
```bash
telnet [IP]
```


---
---


## Exploitation

### Metasploit

##### telnet_login
```bash
use auxiliary/scanner/telnet/telnet_login
set RHOSTS [IP]
set USER_FILE [e.g., /usr/share/wordlists/usernames.txt]
set PASS_FILE [e.g., /usr/share/wordlists/rockyou.txt]
run
```
