# PowerShell Empire: Server Usage Reference

## Overview

The Empire **server** is the backend that handles communication with agents, listeners, and clients. It is typically started before the client.

## Starting the Server

```bash
./empire --server
```

This launches the Empire RESTful API server and backend services.

## Server Configuration

Server settings are usually defined in the `empire/config.yml` or via CLI arguments.

### Common Config Options

- `bind_address` – IP address to bind the API (default: `127.0.0.1`).
- `port` – Port for the API server (default: `1337`).
- `username` / `password` – API authentication credentials.
- `debug` – Enable verbose debug output (`true` or `false`).

## Server Logs

- Logs are typically written to `empire/server.log`.
- Use logs to debug agent communication, listener issues, or client API requests.

## Server API

Once the server is running, it can be accessed via:
```bash
https://[IP]:1337/api
```

Empire’s client connects to this API internally. You can also use custom scripts or tools to interact with it if authenticated.

## Useful Tips

- Always start the server before launching the Empire client.
- Make sure the server port is not blocked by a firewall.
- If running on a remote host, update `bind_address` in the config to `0.0.0.0` or the host’s IP.

## Restarting the Server

To apply config changes, you must fully stop and restart the server:
```bash
pkill -f empire
./empire --server
```

## Notes

- For full functionality, both the server and client must run in sync.
- API authentication is required unless disabled (not recommended).
- The server can be run as a background process or service in operational environments.

---
---

# PowerShell Empire: Starkiller Usage Reference

## Overview

Starkiller is the GUI frontend for PowerShell Empire, allowing for a more user-friendly, visual interface for interacting with agents, listeners, and modules. It connects to the PowerShell Empire server and provides a graphical interface to manage operations.

## Starting Starkiller

### Launch Starkiller
```bash
./starkiller
```

Once launched, Starkiller will automatically connect to the PowerShell Empire server (ensure the server is running first).

## Starkiller Features

### Authentication
- Upon launch, you will be prompted to log in.
- Default credentials can be set in the `empire/config.yml` file.

### Main Interface

- **Listeners**: View and manage active listeners.
- **Agents**: Display and interact with active agents.
- **Modules**: Load and execute post-exploitation modules.
- **Tasks**: Monitor and manage active tasks (e.g., running modules or commands).

### Creating Listeners
1. Navigate to the **Listeners** tab.
2. Click **Add Listener**.
3. Choose the listener type (e.g., HTTP, HTTPS, TCP).
4. Configure the listener options (e.g., Hostname, Port).
5. Click **Start Listener**.

### Creating Agents (Stagers)
1. Go to the **Stagers** tab.
2. Select a stager (e.g., `windows/launcher_bat`, `windows/hta`).
3. Set the listener that the agent will connect to.
4. Click **Generate** to output the payload.
5. Distribute the payload to the target.

### Interacting with Agents
1. Go to the **Agents** tab.
2. Select an agent from the list.
3. Click **Interact** to enter an interactive session.
4. Run shell commands, upload/download files, or use post-exploitation modules.

### Running Modules
1. Navigate to the **Modules** tab.
2. Select a module to run (e.g., `privesc`, `recon`).
3. Configure module options.
4. Click **Execute** to run the module on the agent.

### Task Management
- View running tasks in the **Tasks** tab.
- You can monitor progress, stop tasks, or view results.

### Persistence and Escalation
1. In the **Modules** tab, select a **persistence** or **privesc** module.
2. Set options (e.g., username, password, listener).
3. Execute the module to establish persistence or escalate privileges.

## Notes

- Starkiller connects to a running Empire server, so ensure it is started before launching Starkiller.
- The GUI provides a more accessible way to manage listeners, agents, and modules without manually typing commands.
- Some modules and tasks may require elevated privileges or specific configurations on the target.

