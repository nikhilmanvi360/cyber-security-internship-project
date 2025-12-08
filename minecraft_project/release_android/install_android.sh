#!/bin/bash

echo "========================================="
echo "  Android APK Installer"
echo "========================================="
echo ""

APK_FILE="Minecraft_Launcher.apk"

if [ ! -f "$APK_FILE" ]; then
    echo "Error: $APK_FILE not found!"
    echo "Please build the APK first using build_android.sh"
    exit 1
fi

# Check if adb is installed
if ! command -v adb &> /dev/null; then
    echo "Error: ADB (Android Debug Bridge) not found!"
    echo ""
    echo "Install ADB:"
    echo "  Ubuntu/Debian: sudo apt-get install adb"
    echo "  Fedora: sudo dnf install android-tools"
    echo "  Arch: sudo pacman -S android-tools"
    echo ""
    echo "Or download Android Platform Tools from:"
    echo "  https://developer.android.com/studio/releases/platform-tools"
    exit 1
fi

echo "Checking for connected devices..."
adb devices

echo ""
echo "Make sure:"
echo "1. USB Debugging is enabled on your Android device"
echo "2. Device is connected via USB"
echo "3. You've authorized this computer on your device"
echo ""
read -p "Press Enter to continue with installation..."

echo ""
echo "Installing APK..."
adb install -r "$APK_FILE"

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================="
    echo "  Installation Successful!"
    echo "========================================="
    echo ""
    echo "The app has been installed on your device."
    echo "You can now launch 'Minecraft Launcher' from your app drawer."
    echo ""
    echo "Note: You may need to grant permissions when first launching."
else
    echo ""
    echo "========================================="
    echo "  Installation Failed!"
    echo "========================================="
    echo ""
    echo "Common issues:"
    echo "- Device not connected or USB debugging disabled"
    echo "- Device not authorized (check device screen)"
    echo "- Insufficient storage on device"
    echo ""
    echo "Alternative: Transfer the APK to your phone and install manually"
fi

echo ""
echo "Press Enter to exit..."
read
