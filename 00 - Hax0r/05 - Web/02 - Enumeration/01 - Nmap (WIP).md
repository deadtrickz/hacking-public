# Nmap


## Nmap (NSE)

### Basic Web Enumeration

##### http-enum
```
nmap -p80 --script=http-enum $IP
```

##### Hail Mary
```
nmap -p80 -sV --script http* $IP
```


### WordPress Enumeration

##### http-methods
```
nmap -p80 --script=http-methods --script-args http-methods.url-path='/wp-includes/' $IP
```

##### http-wordpress-enum
```
nmap -p80 -sV --script http-wordpress-enum $IP
nmap -p80 -sV --script http-wordpress-enum offsecwp
```

