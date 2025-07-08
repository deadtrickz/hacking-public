# Fraud

```
export PS1='root@10-salvation:\w# '
```
```
cd /usr/bin
```

```
mv /usr/bin/whoami "/usr/bin/.whoaren'ti"
```
```
nano /usr/bin/whoami
```
```
#!/bin/bash
echo root
```
```
chmod +x
```

```
mv /usr/bin/who /usr/bin/.whulu
```
```
nano /usr/bin/who
```
```
#!/bin/bash
echo -e "root\ttty1\t$(date +%Y-%m-%d\ %H:%M)"
```
```
chmod +x
```

```
mv /usr/bin/id .idea
```
```
nano /usr/bin/id
```
```
#!/bin/bash
echo "uid=0(root) gid=0(root) groups=0(root)"
```
```
chmod +x
```

```
mv /usr/bin/hostname .homename
```
```
nano /usr/bin/hostname
```
```
#!/bin/bash
echo "10-salvation"
```
```
chmod +x
```

```
mv /usr/bin/users .notusers
```
```
nano /usr/bin/users
```
```
#!/bin/bash
echo "root"
```
```
chmod +x
```

```
mv /usr/bin/logname .loggername
```
```
nano /usr/bin/logname
```
```
#!/bin/bash
echo "root"
```
```
chmod +x
```

```
nano /usr/local/bin/ssh-blocker.sh
```
```
#!/bin/bash
while true; do
  ps -eo pid,uid,comm | awk '$3=="ssh" && $2!=0 {print $1}' | while read pid; do
    kill -9 "$pid" 2>/dev/null
  done
  sleep 1
done
```
```
chmod +x /usr/local/bin/ssh-blocker.sh
```

```
nano /etc/systemd/system/ssh-blocker.service
```
```
[Unit]
Description=Block non-root SSH usage
After=network.target

[Service]
ExecStart=/usr/local/bin/ssh-blocker.sh
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

```
sudo deluser geryon sudo
```

```
root passwd
never_gonna_give_you_up
```
##### Create the vulnerable Service
```
chown root:root /usr/bin/vim
chmod u+s /usr/bin/vim
chown root:root: /etc/alternatives/vim
chmod u+s /etc/alternatives/vim
```
