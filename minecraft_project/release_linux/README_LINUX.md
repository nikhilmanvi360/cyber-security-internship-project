# Minecraft Launcher - Linux Release

## Contents

- `Minecraft_Launcher` - The main executable (Linux binary)
- `Minecraft_Setup.sh` - Installation script
- `Stop_Minecraft.sh` - Uninstall/stop script
- `secret.key` - Encryption key file

## Installation

1. Make the setup script executable:
   ```bash
   chmod +x Minecraft_Setup.sh
   ```

2. Run the setup script:
   ```bash
   ./Minecraft_Setup.sh
   ```

The installer will:
- Copy files to `~/.minecraft_updater/`
- Create a systemd user service
- Enable autostart on login
- Start the service immediately

## Uninstallation

1. Make the stop script executable:
   ```bash
   chmod +x Stop_Minecraft.sh
   ```

2. Run the stop script:
   ```bash
   ./Stop_Minecraft.sh
   ```

This will:
- Stop the running service
- Disable autostart
- Remove the systemd service file

To completely remove all files, also delete:
```bash
rm -rf ~/.minecraft_updater
```

## Manual Service Control

Check service status:
```bash
systemctl --user status minecraft-launcher.service
```

Stop service:
```bash
systemctl --user stop minecraft-launcher.service
```

Start service:
```bash
systemctl --user start minecraft-launcher.service
```

View logs:
```bash
journalctl --user -u minecraft-launcher.service
```

## Requirements

- Linux with systemd (most modern distributions)
- X11 or Xorg display server
- Python libraries are bundled in the executable

## Notes

- The launcher runs as a user service (no root required)
- Logs are stored in the installation directory
- The service automatically restarts if it crashes
- Compatible with most Linux distributions (Ubuntu, Debian, Fedora, Arch, etc.)
