# Web Enumeration

## Nikto (HTTP enumeration)
```bash
nikto -h http://[IP]
```

## sqlmap

##### search-test.txt
```bash
GET /search.php?param=value HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Cookie: sessionid=abc123
```

##### sqlmap with request file
```bash
sqlmap -r search-test.txt -p param
```

##### sqlmap database search
```bash
sqlmap -r search-test.txt -p param --dbs --batch
```


---
---


### Cadaver with PUT method
```bash
davtest -move -sendbd auto -url http://[IP]
cadaver [IP]
PUT met.asp met.asp
```


---
---


### Gobuster
```bash
gobuster dir -u http://[IP] -w [WORDLIST]
```
```bash
gobuster dir -u [IP] -w /usr/share/dirbuster/[WORDLIST]
```