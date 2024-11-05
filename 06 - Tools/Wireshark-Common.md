# Wireshark Commands
- Useful Commands


## ETH

##### Isolate Traffic coming from [IP] at the the Ethernet layer
```
##### Find mac with arp.opcode == 2
eth.src == [MAC]
```

##### Isolate all ipv6 traffic at ethernet layer
```
eth.type == 0x86dd
```

##### Isolate all IPv4 traffic going to a [MAC]
```
eth.type == 0x0800 && eth.dst == [MAC]
```

##### Isolate all ARP traffic at the the ethernet layer
```
eth.type == 0x0806
```

##### Isolate all broadcast traffic at the ethernet layer
```
eth.addr == ff:ff:ff:ff:ff:ff

```
```
eth.dst == ff:ff:ff:ff:ff:ff
```


## IP
--

##### Isolate all IP packets going to [IP]
```
ip.dst == [IP]
```

##### Isolate all IP packets coming from [IP]
```
ip.src == [IP]
```

##### Isolate traffic TO and FROM [IP], do not show traffic from [IP]
```
ip.addr == [IP] && !ip.addr == [IP]
```

##### Find Original packet using ID
```
ip.id == 0x[ID]
```


## ARP
--

##### Find [IP] and [MAC] corralation using arp
```
arp.opcode == 2
```

##### Find all packets going to a host at the the ethernet layer
```
arp.src.hw_mac == [MAC]
```

##### Determine how many packets did an IP send, using ARP data only
```
arp.src.proto_ipv4 == [IP]
```

##### Isolate traffic where TARGET MAC address is 00:00:00:00:00:00
```
arp.dst.hw_mac == 00:00:00:00:00:00
```

##### Determine ARP replies from [IP]
```
arp.opcode == 2 && arp.dst.proto_ipv4 == [IP]
```


## ICMP
--

##### show icmp packets
```
icmp
```

##### Show only packets where TTL has exceeded
```
icmp.type in {11}
```

##### Isolate ICMP packets where Destination was Unreachable
```
icmp.type in {3}
``` 

##### Isolate Packets that have been redirected
```
icmp.type {5}
```

##### Isolate only echo Requests
```
icmp.type {8}
```

##### Isolate only echo Replies not from [IP]
```
icmp.type {0} && !ip.addr == [IP]
```

