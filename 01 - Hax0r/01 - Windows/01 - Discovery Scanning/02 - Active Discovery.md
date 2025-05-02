# Active Discovery

## Discovery Scanning

### Masscan
##### Full Port Scan
```bash
sudo masscan -p1-65535,U:1-65535 [IP/CIDR] --rate=1000 -e [NIC]
```

##### Top 100
```bash
sudo masscan [IP/CIDR] ‐‐top-ports 100 -e [NIC]
```

### Nmap

#### Slightly Quiet

##### Basic TCP Scan
```sh
sudo nmap -sC -sV -vv -oA [output_file] [IP]
```

##### Basic UDP Scan
```sh
sudo nmap -sU -sV -vv -oA [output_file] [IP]
```


#### Loud

##### Ping Sweep
```sh
nmap -sP -sn -n [IP] 
```

##### Full Port Scan
```sh
nmap -p- -T4 [IP]
```

##### Version and safe scripts scan on ports
```sh
nmap -p [port] -sC -sV [IP]
```

##### Full TCP scan with versioning and safe scripts
```sh
nmap -sT -sV -sC  -O -vv -p- [IP]
```

##### Full UDP scan with versioning and safe scripts
```sh
nmap -sU -sV -sC  -O -vv -p- [IP]
```

##### Full Windows Scan
```sh
nmap -W -sV -sC -O  -vv -p- [IP]
```

##### Running scripts
```sh
nmap –-script=[script-name] [IP]
```


---
---


#### Nmap Legend

| Option | Description                                                                                |
| :----- | :----------------------------------------------------------------------------------------- |
| -sT    | TCP scan - default and only identifies TCP ports that are open                             |
| -sW    | Windows scan.                                                                              |
| -sU    | UDP scan - identifies only UDP ports that are open                                         |
| -sV    | Versioning scanning - banner grabs all TCP services during scanning                        |
| -sC    | Script scanning with default scripts in /usr/share/nmap/scripts                            |
| -sS    | SYN scan - stealth scan with a handshake of SYN-SYN/ACK-RST. No TCP connection established |
| -sN    | Null Scan - no flags set AKA inverse TCP; Doesn't work on windows                          |
| -sX    | XMAS Scan - all flags set; Doesn't work on Windows                                         |
| -sP    | Ping sweep an IP range                                                                     |
| -sn    | No port scan, just does host discovery                                                     |
| -n     | Disable DNS resolution                                                                     |
| -sO    | Protocol Scan                                                                              |
| -vv    | Very verbose                                                                               |
| -oN    | Normal output                                                                              |
| -oX    | XML output                                                                                 |
| -oA    | Outputs to all formats                                                                     |
| -T0    | Paranoid                                                                                   |
| -T1    | Sneaky                                                                                     |
| -T2    | Polite                                                                                     |
| -T3    | Normal - default (Setting -T3 does nothing)                                                |
| -T4    | Agressive                                                                                  |
| -T5    | Insane                                                                                     |
```sh
nmap --script=[script name/category]
```