# Anger
##### Create the messages
##### anger21.service
```
nano /etc/systemd/system/anger21.service
```
```
[Unit]
Description="Angry FTP on Port 21"
After=network.target

[Service]
User=root
ExecStart=/bin/bash -c 'while true; do echo "STOP TRYING TO LOGIN! I’M DONE! 65536 MORE" | /usr/bin/nc -l -p 21 -q 1; done'
Restart=always

[Install]
WantedBy=multi-user.target
```
##### anger23.service
```
nano /etc/systemd/system/anger23.service
```
```
[Unit]
Description="Angry Telnet on Port 23"
After=network.target

[Service]
User=root
ExecStart=/bin/bash -c 'while true; do echo "NO! I WON’T TALK TO YOU! 65536 MORE" | /usr/bin/nc -l -p 23 -q 1; done'
Restart=always

[Install]
WantedBy=multi-user.target
```
##### anger25.service
```
nano /etc/systemd/system/anger25.service
```
```
[Unit]
Description="Angry SMTP on Port 25"
After=network.target

[Service]
User=root
ExecStart=/bin/bash -c 'while true; do echo "I WON\'T SEND YOUR EMAILS, NO MATTER WHAT! 65536 MORE" | /usr/bin/nc -l -p 25 -q 1; done'
Restart=always

[Install]
WantedBy=multi-user.target
```
##### anger79.service
```
nano /etc/systemd/system/anger79.service
```
```
Description="Angry on Port 79"
After=network.target

[Service]
User=root
ExecStart=/bin/bash -c 'while true; do echo "NO, WHY WOULD YOU THINK THIS IS OK? ...NO NO NONONO" | /usr/bin/nc -l -p 79 -q 1; done'
Restart=always

[Install]
WantedBy=multi-user.target
```
##### anger80.service
```
nano /etc/systemd/system/anger80.service
```
```
[Unit]
Description="Angry HTTP on Port 80"
After=network.target

[Service]
User=root
ExecStart=/bin/bash -c 'while true; do echo "ANGER 404 - THIS ISN\'T YOUR WEBSITE! 65536 MORE" | /usr/bin/nc -l -p 80 -q 1; done'
Restart=always

[Install]
WantedBy=multi-user.target
```
##### anger443.service
```
nano /etc/systemd/system/anger443.service
```
```
[Unit]
Description="Angry HTTPS on Port 443"
After=network.target

[Service]
User=root
ExecStart=/bin/bash -c 'while true; do echo "YOU WANT ENCRYPTION? TRY SOMEWHERE ELSE! 65536 MORE" | /usr/bin/nc -l -p 443 -q 1; done'
Restart=always

[Install]
WantedBy=multi-user.target
```
##### anger5900.service
```
nano /etc/systemd/system/anger5900.service
```
```
[Unit]
Description="Angry VNC on Port 5900"
After=network.target

[Service]
User=root
ExecStart=/bin/bash -c 'while true; do echo "YOU CAN\'T REMOTELY CONTROL ME! 65536 MORE" | /usr/bin/nc -l -p 5900 -q 1; done'
Restart=always

[Install]
WantedBy=multi-user.target
```
##### anger8080.service
```
nano /etc/systemd/system/anger8080.service
```
```
[Unit]
Description="Angry HTTP on Port 8080"
After=network.target

[Service]
User=root
ExecStart=/bin/bash -c 'while true; do echo "TRY THE LAST PORT! 65536 MORE" | /usr/bin/nc -l -p 8080 -q 1; done'
Restart=always

[Install]
WantedBy=multi-user.target
```
##### Create the vulnerable Service
```
nano /etc/systemd/system/wrath.service
```
```
[Unit]
Description="Angry answer on Port 65535"
After=network.target

[Service]
User=root
ExecStart=/bin/bash -c 'while true; do echo "YOU WILL FEEL MY wrath AS YOU DESCEND TO THE BOTTOM!" | /usr/bin/nc -l -p 65535 -q 1; done'
Restart=always

[Install]
WantedBy=multi-user.target
```

##### Start the services
```
sudo systemctl daemon-reload
```
```
sudo systemctl enable anger21.service anger23.service anger25.service anger79.service anger80.service anger443.service anger5900.service anger8080.service wrath.service && sudo systemctl start anger21.service anger23.service anger25.service anger79.service anger80.service anger443.service anger5900.service anger8080.service wrath.service
```

##### anger.txt
```
EPICURUS AND ALL THE denial
THE MINOTAUR'S MINDLESS fury
GERYON'S HORROR IS THE ULTIMATE deception
disgusting horror torment betrayal malcontent monstrous faces treacherous traitor frozen powerless punishment judas brutus cassius nine treason
```
```
root passwd
never_gonna_give_you_up
```