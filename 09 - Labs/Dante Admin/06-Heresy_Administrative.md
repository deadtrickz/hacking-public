# Heresy

### Create the vulnerabilities

##### Create minotaur user
```
adduser minotaur
fury
```
```
sudo visudo
username ALL=(ALL) NOPASSWD: /usr/bin/man, /usr/bin/ln
```
##### Modify minotaur profile
```
sudo nano /home/minotaur/.bashrc
echo "RAHHHHHHHHH???"
export PS1='${USER}@07-violence:\w# '
```
##### set sshd_config to port 1
```
Port 1
```
```
reboot
```
##### service
```
nano /etc/systemd/system/ssh-redirect.service
[Unit]
Description=heretic
After=network.target

[Service]
Type=oneshot
ExecStart=/sbin/iptables -t nat -A OUTPUT -p tcp --dport 22 -j DNAT --to-destination 127.0.0.1:1
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```
```
sudo systemctl daemon-reexec
sudo systemctl enable ssh-redirect
sudo systemctl start ssh-redirect
```
```
reboot
```
```
sudo deluser epicurus sudo
```
```
root passwd
never_gonna_give_you_up
```