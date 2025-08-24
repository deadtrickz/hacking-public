# SSH

## Enumeration

### netcat
```bash
nc [IP] 22
```

### telnet
```bash
telnet [IP] 22
```

### nmap
```bash
nmap -sV -p 22 [IP]
```


---
---

## Exploitation

##### Password Guessing
```sh
ssh [User]@[IP]
```

### Brute Force

##### Hydra
-  -oKexAlgorithms=+[Algorithm]
```sh
hydra -s 22 -L [UserList] -P [PassList] [IP] ssh -e ns -w 5 -W 1
```
