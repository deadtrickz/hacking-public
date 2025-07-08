# Gluttony

##### Create the vulnerability
```
sudo nano /etc/vsftpd.conf
```
```
listen=YES
listen_ipv6=NO

anonymous_enable=YES
local_enable=NO
write_enable=NO

anon_root=/srv/ftp
anon_max_rate=0

ftpd_banner=Welcome to Gluttony. Indulge with care.
```
```
sudo mkdir -p /srv/ftp
sudo chown ftp:ftp /srv/ftp
sudo bash -c 'echo "Mammon guards the gate... but he leaves clues behind." > /srv/ftp/clue.txt'
sudo bash -c 'echo "pluto:mammon123" > /srv/ftp/shadow.bak'
sudo bash -c 'echo "ssh pluto@10.0.0.254" > /srv/ftp/.bash_history'
sudo touch /srv/ftp/gluttony.log /srv/ftp/cheesecake.jpg /srv/ftp/leftovers.txt
sudo systemctl restart vsftpd
sudo bash -c 'echo "Welcome, seeker. Feast your eyes... but know the excess may doom you." > /etc/issue.net'
```

##### Files
```
root@03-gluttony:/srv/ftp# ls -al
total 28
dr-xr-xr-x 2 ftp  ftp  4096 May 29 20:44 .
drwxr-xr-x 3 root root 4096 May 29 20:05 ..
-rw-r--r-- 1 root root   21 May 29 20:23 .bash_history
-rw-r--r-- 1 root root    0 May 29 20:24 cheesecake.jpg
-rw-r--r-- 1 root root    3 May 29 20:38 clue.txt
-rw-r--r-- 1 root root  111 May 29 20:44 gluttony.log
-rw-r--r-- 1 root root    0 May 29 20:24 leftovers.txt
-rw-r--r-- 1 root root   13 May 29 20:38 shadow.bak
-rw-r--r-- 1 root root  233 May 29 20:39 ssh_jump.txt
root@03-gluttony:/srv/ftp# pwd
/srv/ftp
root@03-gluttony:/srv/ftp# 
```
##### .bash_history
```
ssh pluto@10.0.0.254
```
##### clue.txt
``` 
HA
```
##### gluttony.log
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
##### shadow.bak
```
pluto:mammon
```
##### ssh_jump.txt
```
ssh -L 4445:72.69.76.2:445 -J virgil@192.168.1.200:22,cleopatra@172.1.98.15:22,cerberus@10.1.10.3:22,pluto@10.0.0.254:22,phlegyas@255.255.255.9:22,epicurus@9.9.9.8:22,minotaur@222.222.222.187:22,geryon@3.3.3.3:22 satan@6.6.6.6 -p 22
```
```
root passwd
never_gonna_give_you_up
```