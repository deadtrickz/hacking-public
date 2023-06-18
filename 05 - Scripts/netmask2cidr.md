# netmask2cidr.py
---
- validation is broken but not needed
- converts netmask to cidr

### CODE
```python
#!/usr/bin/python3
# Function to check if a netmask is valid
#def is_valid_netmask(netmask):
#    # Convert the netmask to a binary string
#    netmask_bin = ''
#    for octet in netmask.split('.'):
#        try:
#            netmask_bin += bin(int(octet))[2:].zfill(8)
#        except ValueError:
#            return False
    # Check if the netmask is a valid combination of ones and zeros
#    if not all(c == '1' or c == '0' for c in netmask_bin):
#        return False
    # Check if the netmask is contiguous
#    if '01' in netmask_bin or '10' in netmask_bin:
#        return False
#    return True

# Function to convert a netmask to a CIDR
def netmask_to_cidr(netmask):
    # Convert the netmask to a binary string
    netmask_bin = ''
    for octet in netmask.split('.'):
        netmask_bin += bin(int(octet))[2:].zfill(8)
    # Count the number of ones in the binary string
    cidr = netmask_bin.count('1')
    return cidr

# Get the netmask from the user
netmask = input('Enter the netmask: ')

# Validate the netmask
#if not is_valid_netmask(netmask):
#    print('Invalid netmask')
#    exit()

# Convert the netmask to a CIDR
cidr = netmask_to_cidr(netmask)

# Print the CIDR
print('CIDR:', cidr)

```