#!/bin/python3
import argparse
import requests
import random

# Set up the argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help="the URL or IP address to send the request to")
args = parser.parse_args()

# The URL to send the request to
url = args.url

# A list of possible IP addresses to use as the source for the request
possible_ips = ["1.2.3.4", "5.6.7.8", "9.10.11.12"]

# Choose a random IP address from the list
source_ip = random.choice(possible_ips)

# Set the "X-Forwarded-For" header to the chosen IP address
headers = {"X-Forwarded-For": source_ip}

# Send the request
response = requests.get(url, headers=headers)

# Print the response
print(response.text)


# python script.py -u http://IP_ADDRESS/path
