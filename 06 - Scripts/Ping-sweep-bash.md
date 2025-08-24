# Ping-sweep-bash
- Also checks open ports

##### Code
```bash
#!/bin/bash
ports=(20 21 22 23 25 43 53 69 79 80 88 110 111 443 445)
#ports=(80 110 135 111 445)
timeout_duration=1  #timeout duration

ipClass=$1
startingOctet=$2
lastOctet=$3

while [ $startingOctet -le $lastOctet ]
do
    ipAddress=$ipClass.$startingOctet

    # Check if target is UP
    ping -c 1 -W 1 $ipAddress > /dev/null
    if [ $? -eq 0 ]
    then 
        # Print online targets
        echo "$ipAddress is UP"
        for portNumber in ${ports[*]}
        do
            # Check the port
            timeout $timeout_duration bash -c "echo '' > /dev/tcp/$ipAddress/$portNumber" 2> /dev/null
            if [ $? -eq 0 ]
            then
                echo "Port $portNumber is OPEN"
            fi
        done
    fi
    # Increment Octet
    startingOctet=$((startingOctet + 1))
done
```