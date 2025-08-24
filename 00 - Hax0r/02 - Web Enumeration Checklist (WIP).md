# Web Enumeration Checklist

- [ ] Web Directory Enumeration
```
gobuster dir -u http://[URL] -w [wordlist location]
```
```
gobuster dir -u [IP] -w /usr/share/dirbuster/[LIST]
```
```
gobuster dir -u $URL -w /usr/share/wordlists/dirb/common.txt -t 5 -b 301
```
```
feroxbuster --url http://192.168.205.101:80 --wordlist /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

- [ ] HTTP Enumeration
```sh
nikto -h http://[IP]
```
```sh
nmap -p80 --script=http-enum [IP]
```

- [ ] Subdomain Enumeration
```
gobuster dns -d [IP/Domain] -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t 30
```

- [ ] sqlmap with request file
```sh
sqlmap -r search-test.txt -p param
```
### If PUT method is enabled
```sh
davtest -move -sendbd auto -url http://[IP]
cadaver [IP]
cad> PUT met.asp met.asp
```
