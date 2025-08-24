# PowerShell Empire: Client Usage Reference

## Starting the Empire Client

```bash
./empire
```

## Core Commands

### Help
- `help` - Show available commands and usage info.

### Exit
- `exit` - Exit the Empire client.

## Listeners

- `listeners` - View active listeners.
- `uselistener [type]` - Select a listener module.
- `set [option] [value]` - Set options for the listener.
- `execute` - Start the listener.
- `kill [name]` - Stop a listener.

## Stagers

- `usestager [type]` - Select a stager module.
- `set Listener [name]` - Link the stager to a listener.
- `set [option] [value]` - Configure stager settings.
- `execute` - Generate the payload.

## Agents

- `agents` - List all active agents.
- `interact [agent_name]` - Interact with a specific agent.

### In-Agent Commands
Once inside an agent session:
- `shell [command]` - Run a shell command.
- `usemodule [path]` - Load a module for post-exploitation.
- `upload [local]` - Upload a file to the target.
- `download [remote]` - Download a file from the target.
- `exit` - Exit the agent interaction.

## Modules

- `usemodule [category/module_name]` - Load a post-exploitation module.
- `info` - Show module details.
- `set [option] [value]` - Set required options.
- `execute` - Run the module.

## Notes

- Use `back` to exit a module or stager context.
- Use `reload` to refresh the module list if changes are made.
- Tab completion is supported for commands and options.
