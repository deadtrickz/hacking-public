# Cobalt Strike: Basic Commands Reference

## Beacon Console Commands

### Session Management
- `help` – Show available commands.
- `clear` – Clear the Beacon console screen.
- `exit` – Close the Beacon session.

### Host Interaction
- `shell [command]` – Run a system command via cmd.exe.
- `powershell [command]` – Execute a PowerShell command.
- `execute-assembly [path]` – Run a .NET assembly in memory.
- `run [script.cna]` – Execute a Cobalt Strike Aggressor script.

### File Operations
- `upload [file]` – Upload a file to the target.
- `download [file]` – Download a file from the target.
- `ls` – List files in the current directory.
- `cd [path]` – Change directory on the target.

### Privilege Escalation
- `getuid` – Show current user context.
- `make_token [DOMAIN\user] [password]` – Create a token for another user.
- `rev2self` – Revert to the original Beacon token.
- `steal_token [pid]` – Impersonate a token from another process.

### Persistence
- `persist [options]` – Set up persistence on the target system.

### Lateral Movement
- `jump psexec [target] [listener]` – Lateral movement using PsExec.
- `link [ip]` – Link to another Beacon.
- `spawnas [DOMAIN\user] [password] [listener]` – Spawn a Beacon as another user.

### Post-Exploitation
- `keylogger` – Start a keylogger.
- `screencap` – Take a screenshot.
- `ps` – List running processes.
- `kill [pid]` – Terminate a process.

## Notes
- Use `help [command]` for detailed usage.
- Commands may behave differently based on privileges and context.
