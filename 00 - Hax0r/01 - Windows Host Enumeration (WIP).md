# Windows Post-Exploitation Checklist

- [ ] Check Running Processes
```sh
wmic processlist
```
```sh
tasklist
```
```ps
tasklist /svc
```

- [ ] System Information
```ps
systeminfo
```

- [ ] Identify/Verify User
```sh
whoami
```

- [ ] Identify User Permissions
```sh
whoami /priv
```

- [ ] Identify/Verify IP Configuration
```sh
ipconfig /all
```

- [ ] Network Information
```sh
arp -a
```
```sh
route print
```
```sh
type c:\windows\system32\drivers\etc\hosts
```
```sh
ipconfig /displaydns
```

- [ ] Firewall Information
```sh
netsh advfirewall firewall show rule name=all
```

- [ ] List Pipes
```shell
dir /b \\.\pipe\\
```
```PowerShell
(get-childitem \\.\pipe\).FullName
```
```powershell
get-childitem \\.\pipe\
```
```sh
ls \\.\pipe\
```

- [ ] List Network Connections
```sh
netstat -anto
```
```sh
netstat -banto
```

- [ ] Print All User Accounts for the Local System
```sh
net user
```

- [ ] List Shared Folder
```
net share
```

- [ ] List Network Connections
```
net session
```

- [ ] List Drives
```powershell
Get-PSDrive | where {$_.provider -like "Microsoft.PowerShell.Core\FileSystem"}|ft name, root
```
```powershell
get-psdrive -psprovider filesystem
```

- [ ] Environmental Variables
```powershell
get-childitem env: | ft key,value
```

- [ ] Service Query
```sh
net start
```

- [ ] List Tasks
```sh
schtasks /query /fo LIST 2>nul | findstr TaskName
```

- [ ] List Startup Applications
```sh
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
```
```sh
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce
```
```sh
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```
```sh
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce
```
```sh
dir "C:\Documents and Settings\%username%\Start Menu\Programs\Startup"
```

- [ ] File Search
```sh
dir c:\
```
```sh
dir c:\Users\[USER]\documents
```
```sh
dir c:\Users\[USER]\Downloads
```
```sh
dir /a c:\Users\[USER]
```
```sh
dir c:\Users\[USER]\AppData\Roaming\Microsoft\Windows\Recent
```
```sh
type c:\Users\[USER]\AppData\Roaming\Microsoft\Windows\Recent\[FILE].lnk
```
```sh
dir c:\Users\[USER]\Desktop
```

- [ ] Linux
```sh
find / -perm /4000 -exec ls -l {} \; 2>/dev/null
```
```sh
find / -username -exec ls -l {} \; 2>/dev/null
```

- [ ] File Permissions
```sh
icacls "C:\Program Files\*" 2>nul | findstr "(F)" | findstr "Everyone"
```
```sh
icacls "C:\Program Files (x86)\*" 2>nul | findstr "(F)" | findstr "Everyone"
```
```sh
icacls "C:\Program Files\*" 2>nul | findstr "(F)" | findstr "BUILTIN\Users"
```
```sh
icacls "C:\Program Files (x86)\*" 2>nul | findstr "(F)" | findstr "BUILTIN\Users"
```
```sh
icacls "C:\Program Files\*" 2>nul | findstr "(M)" | findstr "Everyone"
```
```sh
icacls "C:\Program Files (x86)\*" 2>nul | findstr "(M)" | findstr "Everyone"
```
```sh
icacls "C:\Program Files\*" 2>nul | findstr "(M)" | findstr "BUILTIN\Users"
```
```sh
icacls "C:\Program Files (x86)\*" 2>nul | findstr "(M)" | findstr "BUILTIN\Users"
```

## Basic Host Enumeration
```bash
systeminfo
ipconfig /all
netstat -anop tcp
```

## Common Directories to Search
```bash
dir c:\
```
```bash
dir c:\Users\[USER]\documents
```
```bash
dir c:\Users\[USER]\Downloads
```
```bash
dir /a c:\Users\[USER]
dir c:\Users\[USER]\AppData\Roaming\Microsoft\Windows\Recent
type c:\Users\[USER]\AppData\Roaming\Microsoft\Windows\Recent\[FILE].lnk
```
```bash
dir c:\Users\[USER]\Desktop
```

## Net Commands
```shell
net localgroup administrators
net localgroup administrators /domain
net use
net user [USER] /domain
net view \\[COMPUTER NAME] /all
net session
```

## nslookup
- sometimes requires FQDN
```bash
nslookup [HOSTNAME]
```

## Passwords
```bash
hashdump
wdigest
logonpasswords
```
