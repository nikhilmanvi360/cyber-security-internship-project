#!/bin/bash

echo "========================================="
echo "  Android APK Uninstaller"
echo "========================================="
echo ""

PACKAGE_NAME="com.minecraft.minecraftlauncher"

# Check if adb is installed
if ! command -v adb &> /dev/null; then
    echo "Error: ADB (Android Debug Bridge) not found!"
    echo "Install ADB or uninstall manually from device settings."
    exit 1
fi

echo "Checking for connected devices..."
adb devices

echo ""
read -p "Press Enter to uninstall the app..."

echo ""
echo "Uninstalling $PACKAGE_NAME..."
adb uninstall "$PACKAGE_NAME"

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================="
    echo "  Uninstallation Successful!"
    echo "========================================="
    echo ""
    echo "The app has been removed from your device."
else
    echo ""
    echo "========================================="
    echo "  Uninstallation Failed!"
    echo "========================================="
    echo ""
    echo "The app may not be installed, or device is not connected."
    echo ""
    echo "To uninstall manually:"
    echo "1. Go to Settings > Apps"
    echo "2. Find 'Minecraft Launcher'"
    echo "3. Tap 'Uninstall'"
fi

echo ""
echo "Press Enter to exit..."
read
