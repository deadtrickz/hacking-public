#!/bin/python3
import argparse
import requests
import random

# Set up the argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help="the URL or IP address to send the request to")
parser.add_argument("-o", "--ips", required=True, help="a text file containing a list of possible IP addresses to use as the source for the request")
args = parser.parse_args()

# The URL to send the request to
url = args.url

# Read the possible IP addresses from the text file
with open(args.ips, "r") as f:
    possible_ips = f.readlines()

# Choose a random IP address from the list
source_ip = random.choice(possible_ips)

# Set the "X-Forwarded-For" header to the chosen IP address
headers = {"X-Forwarded-For": source_ip}

# Send the request
response = requests.get(url, headers=headers)

# Print the response
print(response.text)

# python script.py -u http://IP_ADDRESS/path -o ips.txt
