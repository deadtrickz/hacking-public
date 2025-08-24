# Active Reconnaissance

## Discovery Scanning


#### Nmap Legend

| Option       | Description                                                                                |
| :----------- | :----------------------------------------------------------------------------------------- |
| -sT          | TCP scan - default and only identifies TCP ports that are open                             |
| -sW          | Windows scan.                                                                              |
| -sU          | UDP scan - identifies only UDP ports that are open                                         |
| -sV          | Versioning scanning - banner grabs all TCP services during scanning                        |
| -sC          | Script scanning with default scripts in /usr/share/nmap/scripts                            |
| -sS          | SYN scan - stealth scan with a handshake of SYN-SYN/ACK-RST. No TCP connection established |
| -sN          | Null Scan - no flags set AKA inverse TCP; Doesn't work on windows                          |
| -sX          | XMAS Scan - all flags set; Doesn't work on Windows                                         |
| -sn          | Ping sweep an IP range (older versions use -sP)                                            |
| -sn          | No port scan, just does host discovery                                                     |
| -n           | Disable DNS resolution                                                                     |
| -O           | Operating System Version Scan                                                              |
| --traceroute | Performs Traceroute                                                                        |
| -sO          | Protocol Scan                                                                              |
| -A           | Performs -O, -sV, -sC and --traceroute                                                     |
| -vv          | Very verbose                                                                               |
| -oN          | Normal output                                                                              |
| -oX          | XML output                                                                                 |
| -oA          | Outputs to all formats                                                                     |
| -T0          | Paranoid                                                                                   |
| -T1          | Sneaky                                                                                     |
| -T2          | Polite                                                                                     |
| -T3          | Normal - default (Setting -T3 does nothing)                                                |
| -T4          | Agressive                                                                                  |
| -T5          | Insane                                                                                     |

##### Running scripts
```sh
nmap –-script=[script-name] [IP]
```
```sh
nmap --script-help [script name/category]
```


