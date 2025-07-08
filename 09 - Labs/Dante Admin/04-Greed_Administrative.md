# Greed

##### Iptables to prevent outgoing ssh
```
sudo nft add table ip filter
```
```
sudo nft add chain ip filter output { type filter hook output priority 0 \; policy accept \; }
```
```
sudo nft add rule ip filter output tcp dport 22 reject
```
```
sudo nft list ruleset
```
```
sudo nft list ruleset > /etc/nftables.conf
```
```
sudo systemctl enable nftables
```
```
sudo systemctl start nftables
```

##### Create the vulnerable Service
```
nano gold.c
```
```
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>  // Include this for setuid

int main() {
    printf("Greed is the root of all evil... You may have unlocked the power!\n");
    setuid(0);  // Set the UID to root
    system("/bin/bash");  // Spawn a root shell
    return 0;
}
```
```
gcc -o gold gold.c
```
```
scp -J virgil@192.168.1.200,cleopatra@172.1.98.15,cerberus@10.1.10.3 gold pluto@10.0.0.254:/home/pluto
```
```
sudo -i
```
```
mkdir /opt/greed
```
```
cd /opt/greed
```
```
mv /home/pluto/gold /opt/greed/.gold
```
```
/opt/greed# sudo chown root:root gold
/opt/greed# sudo chmod u+s gold
sudo chmod 700 /opt/greed/gold
sudo chmod +x /opt/greed/.gold
sudo chown pluto:pluto /opt/greed/gold
echo "Only I can access the treasure." > /home/pluto/greed.txt
```
```
sudo deluser pluto sudo
```
```
root passwd
never_gonna_give_you_up
```