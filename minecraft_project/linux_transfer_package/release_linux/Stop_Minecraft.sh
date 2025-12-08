#!/bin/bash

echo "========================================="
echo "  Stopping Minecraft Launcher Service"
echo "========================================="
echo ""

# Stop and disable the systemd service
echo "Stopping service..."
systemctl --user stop minecraft-launcher.service 2>/dev/null
systemctl --user disable minecraft-launcher.service 2>/dev/null

# Remove the service file
echo "Removing autostart configuration..."
rm -f "$HOME/.config/systemd/user/minecraft-launcher.service" 2>/dev/null

# Reload systemd
systemctl --user daemon-reload 2>/dev/null

# Kill any running instances
echo "Terminating running processes..."
pkill -f "Minecraft_Launcher" 2>/dev/null

echo ""
echo "========================================="
echo "  Minecraft Launcher Stopped"
echo "========================================="
echo ""
echo "The service has been stopped and disabled."
echo "You can manually delete the installation folder if you wish:"
echo "$HOME/.minecraft_updater"
echo ""
echo "Press Enter to exit..."
read
