# HTTP

## Server Hosting

##### Python
```bash
python3 -m http.server 80
```

##### Busybox
```bash
busybox httpd -f -p 80 -h /[PATH]/
```

##### Netcat Web Server
```bash
{ echo -ne "HTTP/1.1 200 OK\r\nContent-Length: $(wc -c < file)\r\n\r\n"; cat file; } | nc -l -p 80
```

##### Node.js
```js
// Save this as server.js
const http = require('http');
const fs = require('fs');
const server = http.createServer((req, res) => {
  const stream = fs.createReadStream('[FILE]');
  res.writeHead(200, { 'Content-Type': 'application/[FILE_TYPE]' });
  stream.pipe(res);
});
server.listen(80);
```

##### Netcat
```
nc -l -p 80 < [FILE]
```

---
---


## Downloading
##### Curl
```bash
curl http://[IP]/[FILE] > [FILE]
```

##### wget
```bash
wget http://[IP]/[FILE]
```

##### Node.js
```js
node server.js
```

##### certutil
```bash
certutil -urlcache -split -f http://[IP]/[FILE] [FILE]
```

##### PowerShell
```powershell
Invoke-WebRequest -Uri http://[IP]/[FILE] -OutFile [FILE]
```

##### Telnet
```bash
telnet [IP] 80
```
```bash
GET /[FILE] HTTP/1.1
Host: [IP]
```

##### Netcat
```bash
nc [IP] 80 > [FILE]
```

