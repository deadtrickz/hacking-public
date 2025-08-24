# FTP Transfers

## Server

```
pip install pyftpdlib
```
or
```
sudo apt install vsftpd
```

##### Python
```
python3 -m pyftpdlib -p 21 -w
```
##### Python with Auth
```
python3 -m pyftpdlib --username [USER] --password [PASS] -w
```

##### vsftpd
```
sudo nano /etc/vsftpd.conf
```
```
listen=YES
anonymous_enable=NO         # Set to YES if you want anonymous access
local_enable=YES
write_enable=YES            # Allow uploads
chroot_local_user=YES       # Restrict users to their home dirs
```
```
sudo systemctl restart vsftpd
sudo systemctl enable vsftpd
```


---
---


## Client

##### FTP
```bash
ftp [IP]
```
##### curl
```bash
curl -u username:password ftp://[IP]/[FILE]
```
##### wget
```bash
wget ftp://username:password@<server-ip>/file
```

