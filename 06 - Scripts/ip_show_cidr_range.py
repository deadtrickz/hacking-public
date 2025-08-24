#!/bin/python3
import ipaddress

# Function to check if an IP address is valid
def is_valid_ip(ip):
    try:
        ipaddress.ip_network(ip)
        return True
    except:
        return False

# Get the IP address and CIDR from the user
ip_cidr = input('Enter the IP address and CIDR (e.g. 192.168.1.0/24): ')

# Validate the IP address and CIDR
if not is_valid_ip(ip_cidr):
    print('Invalid IP address and CIDR')
    exit()

# Get the network and broadcast addresses
network = ipaddress.ip_network(ip_cidr, strict=False)
first_ip = network.network_address
last_ip = network.broadcast_address

# Print the range of IP addresses
print('IP address range:', first_ip, '-', last_ip)
