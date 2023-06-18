# Enumeration
---
## Basic Enumeration
```bash
ps
shell ipconfig /all
shell netstat -anop tcp
```
## Common Places
```bash
shell dir c:\
```
```bash
shell dir c:\Users\[USER]\documents
```
```bash
shell dir c:\Users\[USER]\Downloads
```
```bash
shell dir /a c:\Users\[USER]
shell dir c:\Users\[USER]\AppData\Roaming\Microsoft\Windows\Recent
shell type c:\Users\[USER]\AppData\Roaming\Microsoft\Windows\Recent\[FILE].lnk
```
```bash
shell dir c:\Users\[USER]\Desktop
```

## nmap
```bash
nmap -sT -Pn -n 192.168.1.1/24 --top-ports=100
```

## Net
```
shell net localgroup administrators
shell net group "Domain Admins" /domain
shell net localgroup administrators /domain
shell net use
shell net user [USER] /domain
shell net view \\[COMPUTER NAME] /all
shell net session
```

## nslookup
- sometimes requires FQDN
```bash
shell nslookup [HOSTNAME]
```

## Passwords
```bash
hashdump
wdigest
logonpasswords
```

## wevtutil
```bash
shell wevtutil qe security /rd:true /f:text /q:"*[System/EventID=4624] and *[EventData/Data[@Name='TargetUserName']='target_group']" /c:20
```

