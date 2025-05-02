# Host/Service Enumeration

## SMB
### smbclient
##### List Shares (Anonymous)
```sh
smbclient -L //IP -N
```

##### List Shares (With Creds)
```sh
smbclient -L //IP -U [domain\\user]
```

##### Connect to Share
```sh
smbclient //IP/share -U [domain\\user]
```

### enum4linux-ng
##### Basic Enumeration
```sh
enum4linux-ng -A [IP]
```

##### With Credentials
```sh
enum4linux-ng -A [IP] -u [user] -p [password]
```

### smbmap
##### List Shares with Anonymous Access
```sh
smbmap -H [IP]
```

##### List Shares with Credentials
```sh
smbmap -H [IP] -u [user] -p [password]
```

#### crackmapexec (SMB)
```sh
crackmapexec smb [IP] -u [user] -p [password]
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
rpcclient -U [user] [IP]
```

##### Useful Commands in rpcclient
```text
> enumdomusers
> queryuser [RID]
> getdompwinfo
> enumprivs
```


---
---


## WinRM

##### crackmapexec
```sh
crackmapexec winrm [IP] -u [USER] -p [PASS]
```

##### Evil-WinRM
```sh
evil-winrm -i [IP] -u [USER] -p [PASS]
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
nmap -sC -sV -p- -vv -oA [output_file] [IP]
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
