# ping-sweep_short
- Also checks open ports

##### Code
```bash
#!/bin/bash
# Global Variable
ports=(20 21 22 23 25 43 53 69 79 80 88 110 111 443 445) 

# Script Start
classIP=$1; startingOctet=$2; lastOctet=$3
while [ $startingOctet -le $lastOctet ]; do
    ipAddress=$classIP.$startingOctet
    ping -c 1 -W 1 $ipAddress > /dev/null && echo "$ipAddress is UP" && for portNumber in ${ports[*]}; do
        timeout 1 bash -c "echo '' > /dev/tcp/$ipAddress/$portNumber" 2>/dev/null && echo "Port $portNumber is OPEN"
    done
    startingOctet=$((startingOctet + 1))
done
```