# Passive Scanning
## Banner Grabbing

#### netcat
```bash
nc -vv [IP] [port]
```

## Host Discovery

#### netdiscover
```sh
sudo netdiscover -p
```
- -p means passive; only receives traffic and does not send

## WHOIS Enumeration
```bash
whois domain.com | less
```
- registrant name
- name servers

##### Reverse Lookup (IP Lookup)
```bash
whois [IP] | less
```
