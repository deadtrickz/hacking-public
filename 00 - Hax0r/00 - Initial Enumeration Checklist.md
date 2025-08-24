# Initial Enumeration Checklist

- [ ] Nmap Network Mapping
```sh
nmap -sP -sn -n [IP]
```

- [ ] Nmap Default TCP Port Scan; Internal Network (sT); External Network (sS)
```sh
nmap -sT -A -vv -T2 -oA [output_file] [IP]
```
```sh
sudo nmap -sS -A -vv -T2 -p- -oA [output_file] [IP]
```

- [ ] Nmap FULL TCP Port Scan; Internal Network (sT); External Network (sS)
```sh
nmap -sT -A -vv -T4 -p- -oA [output_file] [IP]
```
```sh
sudo nmap -sS -A -vv -T4 -p- -oA [output_file] [IP]
```

- [ ] Nmap UDP Port Scan
```sh
sudo nmap -sU -A -vv -T4 -oA [output_file] [IP]
```

- [ ]  **Utilize Port Encyclopedia**
