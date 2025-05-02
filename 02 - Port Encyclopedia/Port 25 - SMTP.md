# SMTP

## Enumeration

```bash
nc -nv [IP] 25
```
```bash
telnet [IP] 25
```

| Command   | Purpose                                                |
|-----------|--------------------------------------------------------|
| HELO      | Initiates SMTP session (used in spoof tests)           |
| EHLO      | Extended HELO; starts ESMTP session                    |
| MAIL      | Specifies sender's email address                       |
| RCPT      | Specifies recipient's email address                    |
| DATA      | Starts the message content transfer                    |
| RSET      | Aborts current email transaction                       |
| QUIT      | Ends the SMTP session                                  |
| HELP      | Displays available commands                            |
| AUTH      | Authenticates to the server                            |
| STARTTLS  | Initiates TLS encryption                               |
| VRFY      | Verifies existence of user/email                       |
| EXPN      | Expands a mailing list to show member addresses        |

| Spoofing/Relay Techniques                                          |
|--------------------------------------------------------------------|
| HELO [anything]                                                    |
| MAIL FROM: [spoofed_address]                                       |
| RCPT TO: [valid_email]                                             |
| MAIL FROM: nobody@domain RCPT TO: nobody@domain                   |
| MAIL FROM: user@unknown_domain                                     |
| MAIL FROM: user@localhost                                          |
| MAIL FROM:                                                         |
| MAIL FROM: <> RCPT TO: nobody@recipient_domain                     |
| MAIL FROM: user@IP RCPT TO: nobody@recipient_domain                |
| MAIL FROM: user@domain RCPT TO: "user@recipient-domain"            |
| RCPT TO: <nobody@recipient_domain@[IP]>                            |
| MAIL FROM: <user@[IP]> RCPT TO: @domain:nobody@recipient-domain    |
| MAIL FROM: <user@[IP]> RCPT TO:                                    |
### Automation
- takes a  list of supplied usernames and attempts to "VRFY" them.

##### Usage
```python
python3 smtp_enum.py mail.domain.com usernames.txt
```

##### smtp_user_enum.py
```python
#!/usr/bin/python3
import socket
import sys

if len(sys.argv) != 3:
    print("Usage: smtp_user_enum.py <host> <userlist.txt>")
    sys.exit(1)

host = sys.argv[1]
userlist = sys.argv[2]
port = 25

try:
    with open(userlist, "r") as file:
        for line in file:
            user = line.strip()
            if not user:
                continue
            try:
                s = socket.socket()
                s.settimeout(5)
                s.connect((host, port))

                # Receive the banner
                banner = s.recv(1024).decode(errors="ignore")

                # Send VRFY command
                s.send(f"VRFY {user}\r\n".encode())
                response = s.recv(1024).decode(errors="ignore")

                print(f"[{user}] -> {response.strip()}")

                s.close()
            except Exception as e:
                print(f"[{user}] -> Connection error: {e}")
except FileNotFoundError:
    print(f"User list file not found: {userlist}")
    sys.exit(1)

```

#### Nmap
```bash
nmap --script=smtp-commands [IP]
```

##### Common Username Enumeration
```bash
nmap --script=smtp-commands,smtp-enum-users,smtp-vuln-cve2010-4344,smtp-vuln-cve2011-1720,smtp-vuln-cve2011-1764 -p 25 [IP]
```

##### Metasploit
```bash
use auxiliary/scanner/smtp/smtp_enum
```