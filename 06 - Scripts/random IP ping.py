#!/bin/python3
import random
import subprocess

# Read the list of IPs from the file
with open('ips.txt', 'r') as f:
    ips = f.read().splitlines()

# Ping each IP and simulate the ping coming from a random IP
for ip in ips:
    random_ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    result = subprocess.run(['ping', '-c', '1', '-f', '-I', random_ip, ip], stdout=subprocess.PIPE)
    print(result.stdout.decode())



#python script.py
#reads from ips.txt



