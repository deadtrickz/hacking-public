# URL Scanning


## gobuster

##### Standard scan
```
gobuster dir -u http://[IP]:[PORT] -w /usr/share/wordlists/dirb/common.txt -t 5 -b 301
```

|Option |Description |
|:---|:---|
|-u| URL address|
|-w| Wordlist to use|
|-t| Threads to use|
|-b| Status codes to block; blocking 301 stops redirects|

##### Subdomain scan
```
gobuster dns -d [SITE].com -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t 30
```


## feroxbuster
```
feroxbuster --url http://[IP]:[PORT] -e --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```