#!/bin/python3
import argparse
import requests
import random
import threading

# Set up the argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help="the URL or IP address to send the request to")
parser.add_argument("-ips", "--ips", required=True, help="a text file containing a list of possible IP addresses to use as the source for the request")
parser.add_argument("-n", "--num_requests", required=True, help="the number of requests to send", type=int)
parser.add_argument("-h", "--help", action="help", help="show this help message and exit")
args = parser.parse_args()

# The URL to send the request to
url = args.url

# Read the possible IP addresses from the text file
with open(args.ips, "r") as f:
    possible_ips = f.readlines()

# A function to send a request from a random IP address
def send_request():
    # Choose a random IP address from the list
    source_ip = random.choice(possible_ips)

    # Set the "X-Forwarded-For" header to the chosen IP address
    headers = {"X-Forwarded-For": source_ip}

    try:
        # Send the request
        response = requests.get(url, headers=headers)
    except Exception as e:
        print("An error occurred:", e)

# Create a thread for each request
threads = []
for i in range(args.num_requests):
    t = threading.Thread(target=send_request)
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("All requests completed")


# python script.py -u http://IP_ADDRESS/path -ips ips.txt -n 10