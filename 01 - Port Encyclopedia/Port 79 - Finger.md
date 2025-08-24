# Finger

## Enumeration

##### Finger
```bash
finger [USER]@[HOST]
```

##### Netcat
```bash
nc [IP] 79
[USER]
```

### Metasploit

##### finger_users
```bash
use auxiliary/scanner/finger/finger_users
set RHOSTS [target IP]
set USER_FILE [path to list of usernames]
run
```
