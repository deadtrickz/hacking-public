# Kerberos Concepts

## Overview

Kerberos is a **network authentication protocol** that uses **tickets** and **symmetric key cryptography** to allow nodes to prove their identity securely.


## Key Components

| Component           | Description |
|---------------------|-------------|
| **KDC (Key Distribution Center)** | Central authority that issues tickets. Includes the AS and TGS services. |
| **AS (Authentication Service)** | Validates user credentials and issues TGTs (Ticket Granting Tickets). |
| **TGS (Ticket Granting Service)** | Issues service-specific tickets (TGS) based on a valid TGT. |
| **TGT (Ticket Granting Ticket)** | A reusable ticket that allows users to request access to specific services without re-entering credentials. |
| **SPN (Service Principal Name)** | Unique name associated with a service account used to identify the service on the network. |
| **Principal** | Any entity (user or service) participating in the Kerberos realm. |


## Authentication Flow

1. **User -> AS**  
   Sends a request with their username (no password yet).

2. **AS -> User**  
   Returns an encrypted TGT (using user’s password-derived key).

3. **User -> TGS**  
   Sends the TGT to request access to a specific service (SPN).

4. **TGS -> User**  
   Sends back a service ticket encrypted with the service account’s key.

5. **User -> Service**  
   Sends the service ticket to authenticate to the service.


## Common Attacks

| Attack Type | Description |
|-------------|-------------|
| **Kerberoasting** | Requesting service tickets (TGS) for SPNs, then cracking them offline to obtain service account passwords. |
| **AS-REP Roasting** | Targeting accounts that do not require pre-authentication, retrieving encrypted data, and cracking it offline. |
| **Pass-the-Ticket** | Reusing a valid Kerberos ticket (e.g., TGT) to authenticate to services without the password. |
| **Golden Ticket** | Forging a TGT using the KRBTGT account hash (requires domain compromise). |
| **Silver Ticket** | Forging a service ticket for a specific service using the service account's hash. |


## Key Ports

| Port | Protocol | Description |
|------|----------|-------------|
| 88   | TCP/UDP  | Kerberos Authentication |
| 464  | TCP/UDP  | Kerberos Change/Set Password |


## Useful Tools

- **Impacket** (`GetUserSPNs.py`, `ticketer.py`)
- **Rubeus** (TGT/TGS extraction, ticket requests)
- **PowerView** (SPN enumeration)
- **Mimikatz** (Ticket manipulation, golden ticket generation)

## Kerberoasting

| **Kerberos (Legitimate Use)**                                                                                                  | **Kerberoasting (Exploitation)**                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| 1️⃣ User logs in and requests a Ticket-Granting Ticket (TGT) from the Key Distribution Center (KDC).                           | 1️⃣ Attacker (a domain user) requests service tickets for a target account (e.g., high-privileged service).             |
| 2️⃣ KDC verifies credentials and issues a **TGT** encrypted with a secret key known only to the KDC.                           | 2️⃣ KDC provides a service ticket, which is **encrypted using the account’s NTLM hash (password hash)**.                |
| 3️⃣ User presents TGT to KDC, requesting access to a specific network service.                                                 | 3️⃣ Attacker extracts the service ticket from system memory (doesn’t need admin access).                                |
| 4️⃣ KDC issues a **service ticket**, encrypted with the target service’s secret key, allowing access.                          | 4️⃣ Attacker takes the ticket offline and **brute-forces the NTLM hash** to obtain the plaintext password.              |
| 5️⃣ The target service decrypts the ticket, verifies authenticity, and grants access **without exposing the user’s password**. | 5️⃣ If successful, attacker gains access to the **service account**, which may have **high privileges** in the network. |
| ✅ Secure authentication without exposing credentials.                                                                          | ❌ Exploits weak service account passwords for **privilege escalation**.                                                 |

