# PAT (Port Address Translation) - Concepts

## What Is PAT?

- PAT, also called NAT Overload, allows multiple devices on a private network to share a single public IP address.
- It uses **different source port numbers** for each session to distinguish connections.
- It's a type of **NAT** most commonly used in home and small business networks.

## How It Works

1. A device (e.g., 192.168.1.10) wants to access the internet.
2. The router replaces the device’s private IP with its own public IP and changes the source port (e.g., from 1234 to 50001).
3. The router records the mapping of internal IP/port to external IP/port in a translation table.
4. When the response returns, the router uses the port number to forward traffic to the correct internal device.

## Example

Private IPs:
```bash
192.168.1.10:1234
192.168.1.11:1235
```

Translated to:
```bash
203.0.113.5:50001
203.0.113.5:50002
```

## Benefits

- Conserves public IP addresses.
- Adds a layer of basic security by hiding internal IPs.
- Supports many internal devices with only one public IP.

## Use Cases

- Home networks
- Office LANs
- Any network with limited public IPs

## Cisco Configuration Example

Enable PAT:
```bash
ip nat inside source list 1 interface GigabitEthernet0/1 overload
```

View current translations:
```bash
show ip nat translations
```

## Things to Know

- PAT only allows **outbound connections** by default.
- You may need **port forwarding** for inbound traffic (like games or VoIP).
- There's a **port number limit** (~65,000) — rarely hit, but possible in large environments.

## Related Terms

- NAT – Network Address Translation (general term)
- Static NAT – Maps one internal IP to one public IP
- Dynamic NAT – Maps from a pool of public IPs
- PAT – Maps many private IPs to one public IP using ports
