#!/bin/bash

echo "========================================="
echo "  Building Android APK"
echo "========================================="
echo ""

# Check if buildozer is installed
if ! command -v buildozer &> /dev/null; then
    echo "Error: Buildozer not found!"
    echo "Install with: pip install buildozer"
    echo ""
    echo "Also install Android dependencies:"
    echo "  sudo apt-get install -y git zip unzip openjdk-17-jdk wget"
    echo "  sudo apt-get install -y python3-pip autoconf libtool pkg-config"
    echo "  sudo apt-get install -y zlib1g-dev libncurses5-dev libncursesw5-dev"
    echo "  sudo apt-get install -y libtinfo5 cmake libffi-dev libssl-dev"
    exit 1
fi

# Initialize buildozer if buildozer.spec doesn't exist
if [ ! -f "buildozer.spec" ]; then
    echo "Initializing buildozer..."
    buildozer init
fi

# Clean previous builds
echo "Cleaning previous builds..."
buildozer android clean

# Build the APK
echo "Building APK (this may take 15-30 minutes on first build)..."
buildozer -v android debug

if [ $? -eq 0 ]; then
    echo ""
    echo "========================================="
    echo "  Build Successful!"
    echo "========================================="
    echo ""
    echo "APK Location: bin/*.apk"
    echo ""
    
    # Copy APK to release_android folder
    mkdir -p release_android
    cp bin/*.apk release_android/Minecraft_Launcher.apk 2>/dev/null
    
    if [ -f "release_android/Minecraft_Launcher.apk" ]; then
        echo "Release APK: release_android/Minecraft_Launcher.apk"
        echo ""
        echo "To install on device:"
        echo "  adb install release_android/Minecraft_Launcher.apk"
        echo ""
        echo "Or transfer the APK to your phone and install manually."
    fi
else
    echo ""
    echo "========================================="
    echo "  Build Failed!"
    echo "========================================="
    echo "Check the error messages above."
fi

echo ""
echo "Press Enter to exit..."
read
