# Cobalt Strike: Listener Commands Reference

## Listener Management

### Show Listeners
- `listeners` – Display all active listeners and their configurations.

### Create a Listener
- `listener_create [name] [type]` – Create a new listener.
  - Example: `listener_create http beacon_http`

### Edit a Listener
- `listener_edit [name] [option] [value]` – Modify a listener setting.
  - Example: `listener_edit http HostName attacker.com`

### Delete a Listener
- `listener_kill [name]` – Delete a listener by name.

### Start/Stop Listener
- Listeners generally start automatically when created.
- Use `listener_kill` to stop them.

## Listener Types (Examples)
- `beacon_http` – HTTP Beacon
- `beacon_https` – HTTPS Beacon
- `beacon_tcp` – TCP Beacon
- `beacon_dns` – DNS Beacon

## Listener Options (Common)
- `HostName` – Hostname or domain name for the listener.
- `Port` – Listening port.
- `Payload` – Type of payload (e.g., windows/beacon_http/reverse_http).
- `BindTo` – Interface/IP to bind the listener.

## Notes
- Listener names must be unique.
- Listeners are required for launching Beacons and lateral movement.
- Use the Cobalt Strike GUI (`Cobalt Strike > Listeners`) for a visual setup if preferred.
