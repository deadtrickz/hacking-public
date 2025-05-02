# Cobalt Strike: Beacon Commands Reference

## Beacon Overview

Beacons are Cobalt Strike’s payloads used for command and control. Once deployed, operators interact with Beacons via the console to control compromised hosts.

## Managing Beacons

### View Active Beacons
- Use the **GUI** or `beacons` tab to see all active sessions.

### Interact with a Beacon
- Double-click a Beacon in the GUI or use:
  - `interact [Beacon ID]` – Start an interactive session with a Beacon.

### Rename a Beacon
- `rename [new name]` – Rename the active Beacon session for easy tracking.

## Beacon Tasks (Command Examples)

### Check In / Communication
- `sleep [time] [jitter]` – Set how often the Beacon calls back.
  - Example: `sleep 60 20` (60s with 20% jitter)

### Migrate to Another Process
- `inject [pid]` – Inject the Beacon into another process.
- `migrate [pid]` – Migrate the Beacon to another process and exit current one.

### Kill the Beacon
- `exit` – Terminate the Beacon session on the target.

## Beacon Types

- **HTTP/HTTPS Beacon** – Communicates over web protocols.
- **TCP Beacon** – Peer-to-peer communication over TCP.
- **DNS Beacon** – Uses DNS requests for C2 (low and slow).

## Staging Options

- **Staged Payload** – Downloads Beacon in parts.
- **Stageless Payload** – Contains full Beacon in one stage (more stealthy).

## Notes
- Use different Beacon types depending on network restrictions and OPSEC needs.
- Always configure the Beacon's sleep and jitter values to reduce detectability.
