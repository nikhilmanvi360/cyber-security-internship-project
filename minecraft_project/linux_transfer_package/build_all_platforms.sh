#!/bin/bash

echo "========================================="
echo "  Multi-Platform Build Script"
echo "========================================="
echo ""

# Activate virtual environment
if [ -d "venv" ]; then
    source venv/bin/activate
elif [ -d ".venv" ]; then
    source .venv/bin/activate
else
    echo "Error: No virtual environment found!"
    echo "Please create a venv first: python3 -m venv venv"
    exit 1
fi

echo "Building for Linux..."
echo "-------------------------------------"
pyinstaller --clean --noconsole --onefile --name "Minecraft_Launcher" \
    --add-data "face_model.yml:." \
    --add-data "haarcascade_frontalface_default.xml:." \
    --hidden-import=pynput.keyboard._xorg \
    --hidden-import=pynput.mouse._xorg \
    main.py

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Linux build successful!"
    
    # Create release_linux directory if it doesn't exist
    mkdir -p release_linux
    
    # Copy files to release_linux
    echo "Copying files to release_linux/..."
    cp dist/Minecraft_Launcher release_linux/
    cp secret.key release_linux/
    cp release_linux/Minecraft_Setup.sh release_linux/
    cp release_linux/Stop_Minecraft.sh release_linux/
    
    # Make scripts executable
    chmod +x release_linux/Minecraft_Launcher
    chmod +x release_linux/Minecraft_Setup.sh
    chmod +x release_linux/Stop_Minecraft.sh
    
    echo "✓ Linux release package ready in release_linux/"
else
    echo "✗ Linux build failed!"
fi

echo ""
echo "========================================="
echo "  Build Complete"
echo "========================================="
echo ""
echo "Linux release: ./release_linux/"
echo "Windows release: ./release/"
echo ""
echo "Press Enter to exit..."
read
