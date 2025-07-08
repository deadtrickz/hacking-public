# Lust

##### Create the vulnerable Service
```
nano /etc/systemd/system/desire.service
```
```
[Unit]
Description="reaching out"
After=network.target

[Service]
user=root
ExecStart=/bin/bash -c 'while true; do /bin/cat /etc/shadow | /usr/bin/nc -l -p 80 -q 1; done'
Restart=always

[Install]
WantedBy=multi-user.target
```
```
sudo systemctl daemon-reload
```
```
sudo systemctl desire.service enable
```
```
root passwd
N/A
```
```
modify root hash in /etc/shadow to be "desire"
```

