# Fuzzing

## wfuzz
##### File scan
```bash
wfuzz -c -z file,/usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt --hc 301,404,403 "http://[SITE].com"
```

##### Directory scan
```bash
wfuzz -c -z file,/usr/share/seclists/Discovery/Web-Content/raft-medium-directories.txt --hc 404,403,301 "http://[SITE]:[PORT]/FUZZ/"
```

##### Parameter Discovery
```bash
wfuzz -c -z file,/usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt --hc 404,301 "http://[SITE]:[PORT]/index.php?FUZZ=data/FUZZ"
```

##### Parameter Values
```bash
wfuzz -c -z file,/usr/share/seclists/Usernames/cirt-default-usernames.txt --hc 404 http://[SITE]:[PORT]/index.php?fpv=FUZZ
```
```bash
wfuzz -c -z file,/usr/share/seclists/Usernames/cirt-default-usernames.txt --hc 404,301 http://[SITE]:[PORT]/index.php?fpv=FUZZ
```
```bash
wfuzz -c -z file,/usr/share/seclists/Usernames/cirt-default-usernames.txt --hc 404,301 http://[SITE]:[PORT]/index.php/?xss=FUZZ
```
```bash
wfuzz -c -z file,/usr/share/seclists/Fuzzing/XSS-Fuzzing --hc 404,301 --hh 40106,0,14 http://[SITE]:[PORT]/?xss=FUZZ
```

##### Credential Fuzz
```bash
wfuzz -z list,admin-password-words-morewords --basic FUZZ:FUZZ http://[IP]:[PORT]/[LOGON].php
```

##### POST Data (Brute Force Password)
```bash
wfuzz -c -z file,/usr/share/seclists/Passwords/xato-net-10-million-passwords-100000.txt --hc 404 -d "log=admin&pwd=FUZZ" http://[IP]:[PORT]/[LOGON].php
```

##### Authenticated Fuzz (using cookie)
```bash
wfuzz -c -z file,/usr/share/seclists/Discovery/Web-Content/raft-medium-files.txt -b '[COOKIE]' --hc 301,404,403 http://[SITE]/wp-admin/FUZZ
```


