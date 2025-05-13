# ssh tunneling
- SSH tunneling allows securely forwarding traffic from one machine to another using the SSH protocol. There are three main types of SSH tunnels:
	- Local Port Forwarding  
	- Remote Port Forwarding  
	- Dynamic Port Forwarding  

##### Example Network:
- PC1: your local machine  
- PC2: accessible by PC1 via SSH  
- PC3: accessible from PC2  
- PC4: only accessible from PC3  

## Local Port Forwarding
- Used to access a service from PC1 that is only reachable from a machine further down the chain (e.g., PC4).
	- Traffic flows from PC1 to a local port  
	- Then forwarded to a destination only accessible through remote machines  
	- Useful when a service is behind multiple layers and you want to access it locally  

### Example: PC1 wants to access a service running on PC4

##### Command on PC1
```
ssh -L [PC1_Local_Port]:PC3:[PC2_Destination_Port] [USER]@[IP_of_PC2]
```

##### Command inside PC2 session
```
ssh -L [PC2_Local_Port]:PC4:[PC3_Destination_Port] [USER]@[IP_of_PC3]
```

- PC1 connects to localhost:[PC1_Local_Port]  
- Tunnel flows PC1 → PC2 → PC3 → PC4  


## Remote Port Forwarding
- Used to expose a local service from PC1 so that a machine further down the chain (e.g., PC4) can reach it.
	- Opens a port on a remote machine  
	- Forwards that port to a service on PC1  
	- Useful when the destination cannot initiate a connection back to PC1 directly  

### Example: PC4 needs to access a web server on PC1

##### Command on PC1
```
ssh -R [PC2_Port]:localhost:[PC1_Local_Port] [USER]@[IP_of_PC2]
```

##### Command on PC2
```
ssh -R [PC3_Port]:localhost:[PC2_Port] [USER]@[IP_of_PC3]
```

##### Command on PC3
```
ssh -R [PC4_Port]:localhost:[PC3_Port] [USER]@[IP_of_PC4]
```

- PC4 connects to localhost:[PC4_Port]  
- Tunnel flows PC4 → PC3 → PC2 → PC1  


## Dynamic Port Forwarding
- Used to create a local SOCKS proxy that dynamically routes traffic through multiple SSH hosts.
	- Creates a SOCKS proxy on PC1  
	- Routes outbound traffic dynamically through SSH chain  
	- Useful for web browsing or accessing any remote-hosted service through PC4's network  

### Example: PC1 uses a SOCKS proxy to route traffic through PC2 → PC3 → PC4

##### Command on PC1
```
ssh -D [PC1_Local_Port] -J [USER]@[IP_of_PC2],[USER]@[IP_of_PC3],[USER]@[IP_of_PC4] [USER]@[IP_of_PC4]
```

- SOCKS proxy is available at localhost:[PC1_Local_Port]  
- Configure browser or apps to use it as a proxy  


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
