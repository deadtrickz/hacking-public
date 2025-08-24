# Host/Service Enumeration

## SMB
### smbclient
##### List Shares (Anonymous)
```sh
smbclient -L //[IP] -N
```

##### List Shares (With Creds)
```sh
smbclient -L //[IP] -U [DOMAIN\\USER]
```

##### Connect to Share
```sh
smbclient //[IP]/[SHARE] -U [DOMAIN\\USER]
```

### smbmap
##### List Shares with Anonymous Access
```sh
smbmap -H [IP]
```

##### List Shares with Credentials
```sh
smbmap -H [IP] -u [USER] -p [PASSWORD]
```

#### crackmapexec (SMB)
```sh
crackmapexec smb [IP] -u [USER] -p [PASSWORD]
```


---
---


## RPC 
### rpcclient
##### Anonymous Connection
```sh
rpcclient -U "" [IP]
```

##### With Credentials
```sh
rpcclient -U [USER] [IP]
```

##### Useful Commands in rpcclient
```text
enumdomusers
queryuser [RID]
getdompwinfo
enumprivs
```


---
---


## WinRM

##### crackmapexec
```sh
crackmapexec winrm [IP] -u [USER] -p [PASSWORD]
```

##### Evil-WinRM
```sh
evil-winrm -i [IP] -u [USER] -p [PASSWORD]
```


---
---


## RDP

##### Check if RDP is Open
```sh
nmap -p 3389 [IP]
```

##### RDP Banner
```sh
nmap -sV -p 3389 [IP]
```


---
---


### Service Enumeration

**CHECK PORT ENCYCLOPEDIA**


---
---


### Nmap for Service Enumeration

#### Full TCP Scan with Scripts
```sh
nmap -sC -sV -p- -vv -oA [OUTPUT_FILE] [IP]
```

#### SMB Scripts
```sh
nmap --script "smb-*" -p 445 [IP]
```

#### RPC, RDP, WinRM Scripts
```sh
nmap --script=rdp-enum-encryption -p 3389 [IP]
nmap --script=msrpc-enum -p 135 [IP]
nmap --script=http-winrm-enum -p 5985 [IP]
```
