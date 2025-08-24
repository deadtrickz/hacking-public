# ip2txt.py
- Prints an IP range to ips.txt
##### Code
```python
#!/usr/bin/python3
import socket
import struct

# Function to check if an IP address is valid
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except:
        return False

# Get the start and end IP addresses from the user
start_ip = input('Enter the start IP address: ')
end_ip = input('Enter the end IP address: ')

# Validate the start and end IP addresses
if not is_valid_ip(start_ip):
    print('Invalid start IP address')
    exit()
if not is_valid_ip(end_ip):
    print('Invalid end IP address')
    exit()

# Convert the start and end IP addresses to integers
start_int = struct.unpack('!L', socket.inet_aton(start_ip))[0]
end_int = struct.unpack('!L', socket.inet_aton(end_ip))[0]

# Open the file in write mode
with open('ips.txt', 'w') as f:
    # Iterate over the range of IP addresses
    for i in range(start_int, end_int+1):
        # Convert the integer to an IP address
        ip = socket.inet_ntoa(struct.pack('!L', i))
        # Write the IP address to the file
        f.write(ip + '\n')
```

