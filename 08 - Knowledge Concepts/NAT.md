# NAT (Network Address Translation) Concepts

## Overview

- NAT allows multiple devices on a local/private network to share a single public IP address when accessing the internet.
- It's commonly used to conserve public IP addresses and hide internal network structures for security.

## Key Components

- **Private IP Address**: IPs used inside local networks, such as 192.168.x.x, 10.x.x.x, or 172.16.x.x - 172.31.x.x.
- **Public IP Address**: Globally routable IPs used on the internet.
- **NAT Device**: Typically a router or firewall that handles IP translation.
- **Internal Network**: Devices within the private LAN.
- **External Network**: Everything outside the LAN (e.g., the internet).

## Types of NAT

- **Static NAT**: Maps one private IP to one public IP. Common for servers needing external access.
- **Dynamic NAT**: Maps private IPs to any available public IP from a pool.
- **PAT (Port Address Translation)**: Maps many private IPs to one public IP using port numbers. Also known as NAT Overload.

## How NAT Works

1. Devices inside the LAN send packets with private IPs to the NAT device.
2. NAT modifies the packet, replacing the source IP with the public IP.
3. If PAT is used, the source port is also changed to ensure uniqueness.
4. NAT keeps track of this mapping in a table.
5. Return traffic from the internet is translated back to the correct private IP and port.

## Benefits

- **IP Conservation**: Reduces the need for many public IP addresses.
- **Basic Security**: Internal IPs are hidden from the internet.
- **Simplified Management**: Easier IP management in large networks.

## Use Cases

- **Home Routers**: Allow multiple devices to access the internet through one IP.
- **Web Servers**: Use static NAT to expose internal services to the internet.
- **VoIP or Video Conferencing**: Often used with NAT traversal techniques.

## Common Commands (Cisco)

- Show active NAT mappings:
  ```bash
  show ip nat translations
  ```

- Static NAT mapping:
  ```bash
  ip nat inside source static [local IP] [global IP]
  ```

- Dynamic NAT with access list and pool:
  ```bash
  ip nat inside source list [access-list] pool [pool-name]
  ```

- NAT Overload (PAT):
  ```bash
  ip nat inside source list 1 interface GigabitEthernet0/1 overload
  ```

## Security Considerations

- **NAT Traversal**: Some apps (VoIP, games) require special handling like STUN/TURN.
- **Not a Firewall**: NAT hides internal IPs but doesn't control traffic—combine it with proper firewall rules.
- **Port Forwarding**: Needed to allow external access to internal devices (e.g., game servers).
