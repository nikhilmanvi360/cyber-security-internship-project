#!/bin/bash
echo "Building Minecraft_Launcher for Linux..."

# Activate virtual environment
source venv/bin/activate

# Build using PyInstaller
pyinstaller --noconsole --onefile --name "Minecraft_Launcher" \
    --add-data "face_model.yml:." \
    --add-data "haarcascade_frontalface_default.xml:." \
    --hidden-import=pynput.keyboard._xorg \
    --hidden-import=pynput.mouse._xorg \
    main.py

echo "Build Complete. Check dist/ folder."
echo "Press Enter to continue..."
read
