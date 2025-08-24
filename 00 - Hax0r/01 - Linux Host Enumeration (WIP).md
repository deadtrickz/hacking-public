# Nix* Post-Exploitation Checklist

- [ ] Check Running Processes
```sh
ps
```
```sh
ps aux
```
```
ss -lntp
```

- [ ] System Information
```ps
sysinfo
```
```sh
uname -a
```
```sh
hostnamectl
```
```sh
cat /etc/os-release
```
```sh
lsb_release
```

- [ ] Identify/Verify User
```sh
whoami
```
```sh
id
```

- [ ] Identify User Permissions
```sh
whoami /priv
```
```
sudo -l
```

- [ ] Identify/Verify IP Configuration
```sh
ip a
```
```sh
ifconfig -a
```

- [ ] Network Information
```sh
arp -a
```
```sh
route print
```

- [ ] Firewall Information
```sh

```

- [ ] List Network Connections
```sh
netstat -anto
```
```sh
netstat -panto
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
```

```

- [ ] Environmental Variables
```sh
set
```

- [ ] Service Query
```sh
sc query
```

- [ ] List Tasks
```sh
cat /etc/crontab
```
```
```sh
crontab -l
```

- [ ] List Startup Applications
```sh

```

## File Search

- [ ] Linux
```sh
find / -perm /4000 -exec ls -l {} \; 2>/dev/null
```
```sh
find / -username -exec ls -l {} \; 2>/dev/null
```

## File Permissions

- [ ] Linux
```sh
find / -perm /4000 -exec ls -l {} \; 2>/dev/null
```
```sh
find / -username -exec ls -l {} \; 2>/dev/null
```


- [ ] 10
```sh

```