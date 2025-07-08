# ssh tunneling
- SSH tunneling allows securely forwarding traffic from one machine to another using the SSH protocol. There are three main types of SSH tunnels:
	- Local Port Forwarding  
	- Remote Port Forwarding  
	- Dynamic Port Forwarding  

##### Example Network:
- ATK: Attack Platform
- PC1: accessible from ATK via SSH   
- PC2: accessible from PC1 
- PC3: accessible from PC2  
- PC4: only accessible from PC3  

## Local Port Forwarding (-L)
- the -L section `4445:192.168.1.20:445` is actually `127.0.0.1:4445:192.168.1.20:445`
	- the 127.0.0.1 is implied but can be changed to a specific interface IP on your local machine.

### Using Jumps (-J)
##### Command

```
ssh -L [127.0.0.1:]4445:[PC4_IP]:445 -J [PC1_USER]@[PC1_IP]:22,[PC2_USER]@[PC2_IP]:2222 [PC3_USER]@[PC3_IP] -p 22
```

### Stacking Tunnels (PC1 as a foothold)

##### ATK to PC1 -> PC2
```
ssh -N -L 2222:[PC2_IP]:22 [PC1_USER]@[PC1_IP] -p 8888
```
##### ATK -> (PC1->PC2) -> PC3
```
ssh -N -L 3333:[PC3_IP]:22 [PC2_USER]@127.0.0.1 -p 2222
```
##### ATK to PC3 SSH
```
ssh [PC3_USER]@127.0.0.1 -p 3333 
```


---
---


## Remote Port Forwarding (`-R`)
- The `-R` section `4444:192.168.1.1:4444` is actually `127.0.0.1:4444:192.168.1.1:4444` 
	- the 127.0.0.1 is the remote localhost and the IP is where the data is sent to
	- 0.0.0.0 must be used if options like "GatewayPorts=yes" are used (multiple NICs)

### Using Jumps (`-J`)
#### Command
```
ssh -v -N -o GatewayPorts=yes -J [PC1_USER]@[PC1_IP]:22,[PC2_USER]@[PC2_IP]:2222,[PC3_USER]@[PC3_IP]:22 [PC4_USER]@[PC4_IP] -p 22 -R 0.0.0.0:4444:[ATK_IP]:4444
```

### Stacking Tunnels (PC1 as a foothold)
##### Initial Tunnel to PC1:2222 -> PC2:22
```
ssh -N -L 2222:[PC2_IP]:22 [PC1_USER]@[PC1_IP] -p 8888
```
##### Tunnel from PC2:3333 -> PC3:22
```
ssh -N -L 3333:[PC3_IP]:22 [PC2_USER]@127.0.0.1 -p 2222
```
##### Tunnel from PC3:4445 -> PC4:445
```
ssh -N -L 4444:[PC4_IP]:445 [PC3_USER]@127.0.0.1 -p 3333
```

##### Reverse Tunnel
```
ssh -N -R 4444:127.0.0.1:4444 [PC3_USER]@127.0.0.1 -p 3333
```

##### Metasploit Info
```
RHOSTS 127.0.0.1
RPORT 4444
LHOST [PC3_IP]
LPORT 4444
```


---
---


## Dynamic Port Forwarding
- Used to create a local SOCKS proxy that dynamically routes traffic through multiple SSH hosts.
	- Creates a SOCKS proxy on PC1  
	- Routes outbound traffic dynamically through SSH chain  
	- Useful for web browsing or accessing any remote-hosted service through PC4's network 
##### Proxychains
- nmap -A/icmp/arp will NOT work with proxychains
- proxychains nmap commands must be ran as root user with nmap -sT -n
- `proxychains telnet/nc IP PORT` is the most reliable way to connect to a port with proxychains
### Using Jump (-J)
##### Command
```
ssh -D [PC1_Local_Port] -J [USER]@[IP_of_PC2],[USER]@[IP_of_PC3],[USER]@[IP_of_PC4] [USER]@[IP_of_PC4]
```

### Stacking Tunnels (PC1 as a foothold)

##### ATK -> PC1 -> PC2
```
ssh -N -L 2222:[PC2_IP]:22 [PC1_USER]@[PC1_IP] -p 8888
```
##### PC2 -> PC3
```
ssh -N -L 3333:[PC3_IP]:22 [PC2_USER]@127.0.0.1 -p 2222
```
##### PC3 -> PC4
```
ssh -N -L 4444:[PC4_IP]:445 [PC3_USER]@127.0.0.1 -p 3333
```

##### Dynamic Forward
```
ssh -N -D 1080 [PC3_USER]@127.0.0.1 -p 3333
```


### Stacking Tunnels (Reverse) (PC1 as a foothold)

##### ATK to PC1 -> PC2
```
ssh -N -L 2222:[PC2_IP]:22 [PC1_USER]@[PC1_IP] -p 8888
```
##### PC2: -> PC3
```
ssh -N -L 3333:[PC3_IP]:22 [PC2_USER]@127.0.0.1 -p 2222
```
##### PC3 -> PC4
```
ssh -N -L 4444:[PC4_IP]:445 [PC3_USER]@127.0.0.1 -p 3333
```

##### Reverse Tunnel
```
ssh -N -D 1080 [PC3_USER]@127.0.0.1 -p 3333
```
## Which to Use

- Local Port Forwarding  
	- Use when you want to access a remote service from your local machine  
	- Example: Forward a port from PC4 to PC1  

- Remote Port Forwarding  
	- Use when a remote machine needs access to a service on your local machine  
	- Example: Let PC4 reach a dev server running on PC1  

- Dynamic Port Forwarding  
	- Use when you want a SOCKS proxy to browse through remote machines  
	- Example: Route traffic from PC1 through PC4’s network  


---
---


## Diagram: SSH Tunneling Path from PC1 to PC4

```
[PC1]       [PC2]       [PC3]       [PC4]
  |           |           |           |
  | SSH --->  | SSH --->  | SSH --->  |
  |           |           |           |
  |           |           |           |
  | -L port1> PC3 -L port2> PC4       |   (Local Port Forwarding)
  |                                   |
  | <R port1- PC2 <R port2- PC3 <R port3- PC4   (Remote Port Forwarding)
  |                                   |
  | --D port--> proxy --J--> PC2--->PC3--->PC4  (Dynamic Port Forwarding)
```

Legend:
- `-L`: local port forwarding from one host to a deeper internal one
- `-R`: remote port forwarding to expose a local service outward
- `-D`: dynamic port forwarding (SOCKS proxy)
- `--J-->`: jump host used to route SSH through intermediate systems

Notes:
- All connections flow left to right.
- Traffic always originates on PC1.
- PC4 is only accessible from PC3.
- Use combinations of tunnels for deeper access.
