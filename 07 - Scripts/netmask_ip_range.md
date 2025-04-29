# netmask_ip_range.py
- takes an IP and netmask then prints the IP range

### usage

##### Get the range

```
python netmask_ip_range.py 192.168.1.1 255.255.255.0
```

##### output results to iplist.txt 
```
python netmask_ip_range.py -o 192.168.1.0 255.255.255.0
```

##### CODE
```python
#!/usr/bin/python3
# Import the necessary modules
import argparse
import ipaddress

# Function to check if an IP address is valid
def is_valid_ip(ip):
    try:
        ipaddress.ip_network(ip)
        return True
    except:
        return False

# Function to convert a netmask to a CIDR
def netmask_to_cidr(netmask):
    # Convert the netmask to a binary string
    netmask_bin = ''
    for octet in netmask.split('.'):
        netmask_bin += bin(int(octet))[2:].zfill(8)
    # Count the number of ones in the binary string
    cidr = netmask_bin.count('1')
    return cidr

# Set up the argument parser
parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help='write the range of IP addresses to a file')
parser.add_argument('ip', type=str, help='the IP address')
parser.add_argument('netmask', type=str, help='the netmask')
args = parser.parse_args()

# Validate the IP address and netmask
if not is_valid_ip(args.ip):
    print('Invalid IP address')
    exit()
if not is_valid_ip(args.netmask):
    print('Invalid netmask')
    exit()

# Convert the netmask to a CIDR
cidr = netmask_to_cidr(args.netmask)

# Create the IP address and CIDR string
ip_cidr = args.ip + '/' + str(cidr)

# Get the network and broadcast addresses
network = ipaddress.ip_network(ip_cidr, strict=False)
first_ip = network.network_address
last_ip = network.broadcast_address

# Print the range of IP addresses
print('IP address range:', first_ip, '-', last_ip)

# If the -o option is specified, write the range of IP addresses to a file
if args.output:
    with open('iplist.txt', 'w') as f:
        for ip in network:
            f.write(str(ip) + '\n')

```