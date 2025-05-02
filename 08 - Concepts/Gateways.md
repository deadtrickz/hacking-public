# Gateways

[User Device]
192.168.1.100
     |
     v
[Default Gateway]
192.168.1.1
(NAT occurs here)
     |
     v
[Gateway of Last Resort]
(used if no specific route exists)
     |
     v
[ISP Router]
Public IP assigned by ISP
     |
     v
[Internet]
(External websites, servers, services)



## Overview

- A gateway is a device that connects different networks and controls traffic entering and leaving a local network.
- It can function as a router, firewall, NAT device, or proxy server.

## Key Components

- Default Gateway: The router a device sends traffic to when the destination is outside its local network.
- Gateway of Last Resort: A fallback route used when no specific route exists in the routing table.
- Routing Table: A list of routes that determines how network packets are forwarded.
- NAT (Network Address Translation): A method used to translate private IP addresses into public ones.
- Proxy Gateway: Acts as an intermediary between clients and servers, often used for filtering or anonymity.

## How Gateway Routing Works (Step-by-Step)

1. A device on the local network wants to send data to an IP outside its own subnet.
2. The device checks its routing table and sees that the destination is not local.
3. It forwards the packet to its default gateway.
4. The default gateway (usually a router) receives the packet.
5. The router checks its routing table for a matching route.
6. If a specific route is found, it forwards the packet to the next hop or destination.
7. If no route is found, the router uses the Gateway of Last Resort.
8. If the router is also a NAT device, it performs address translation (private IP → public IP).
9. The packet is sent to the internet or the target external network.
10. When the destination responds, the process is reversed:
    - The packet is received at the public IP
    - NAT converts the address back to the internal private IP
    - The router forwards the response to the original device

## Gateway Functions

- Routing: Moves packets between different networks or subnets.
- Security: Can include firewall features to filter traffic.
- NAT: Converts internal IPs to public IPs for internet use.
- Traffic Management: Controls bandwidth, enforces QoS, prioritizes traffic.

## Types of Gateways

- Router Gateway: Connects different networks and routes traffic between them.
- Proxy Gateway: Forwards client requests, often adding anonymity or filtering.
- Firewall Gateway: Filters traffic based on rules and security policies.
- VPN Gateway: Creates encrypted tunnels between remote clients and internal networks.

## Gateway of Last Resort

- Used when no specific route to a destination exists in the routing table.
- Functions as the default route for unknown destinations.
- Helps maintain connectivity when the routing table lacks a precise match.

## Common Gateway-related Commands

- Show routing table on Cisco:
  ```bash
  show ip route
  ```

- Add static route on Cisco:
  ```bash
  ip route [destination] [subnet mask] [gateway]
  ```

- Add default gateway on Linux:
  ```bash
  route add default gw [IP]
  ```

- View routing table on Linux:
  ```bash
  route -n
  ```

- View routing table on Windows:
  ```bash
  netstat -r
  ```

## Useful Tools

- Traceroute: Shows the path data takes from source to destination.
- Netstat: Displays network connections and routing tables.
- Route: Used to view and modify routing tables on various systems.
