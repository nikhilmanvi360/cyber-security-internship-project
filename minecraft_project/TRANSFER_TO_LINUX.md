# Transfer Guide: Moving Project to Linux

## Quick Transfer Methods

### Method 1: USB Drive (Easiest)
1. Copy the entire `minecraft_project` folder to a USB drive
2. Plug USB into Linux machine
3. Copy folder from USB to Linux home directory

### Method 2: Cloud Storage (Google Drive, Dropbox, etc.)
1. Compress the project folder:
   - Right-click `minecraft_project` folder
   - Send to → Compressed (zipped) folder
2. Upload `minecraft_project.zip` to cloud storage
3. Download on Linux machine
4. Extract: `unzip minecraft_project.zip`

### Method 3: SCP (if you have SSH access to Linux machine)
```cmd
scp -r "C:\Users\91984\Downloads\minecraft_project\minecraft_project" username@linux-ip:~/
```

### Method 4: Git Repository
```cmd
cd C:\Users\91984\Downloads\minecraft_project\minecraft_project
git init
git add .
git commit -m "Initial commit with Linux support"
git remote add origin <your-repo-url>
git push -u origin main
```
Then on Linux:
```bash
git clone <your-repo-url>
```

### Method 5: Network Share (if on same network)
1. Share the folder on Windows
2. Access from Linux using Samba/CIFS

## Files Included for Linux

### Build Scripts ✅
- `build_portable_linux.sh` - Linux build script
- `build_all_platforms.sh` - Complete build + package script
- `Minecraft_Launcher_Linux.spec` - PyInstaller spec for Linux

### Release Files ✅
- `release_linux/Minecraft_Setup.sh` - Installer
- `release_linux/Stop_Minecraft.sh` - Uninstaller
- `release_linux/README_LINUX.md` - User documentation

### Source Code ✅
All Python files and dependencies are included

## Setup on Linux Machine

Once transferred, run these commands:

```bash
# Navigate to project
cd ~/minecraft_project

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install system dependencies (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install python3-tk python3-dev python3-xlib

# Make scripts executable
chmod +x build_portable_linux.sh
chmod +x build_all_platforms.sh
chmod +x release_linux/*.sh

# Build the project
./build_all_platforms.sh
```

## After Building

Your Linux release will be in: `release_linux/`

Contains:
- `Minecraft_Launcher` (Linux executable)
- `Minecraft_Setup.sh` (installer)
- `Stop_Minecraft.sh` (uninstaller)
- `secret.key` (encryption key)
- `README_LINUX.md` (instructions)

## Distribution to End Users

Zip the `release_linux/` folder and distribute it. Users run:
```bash
chmod +x Minecraft_Setup.sh
./Minecraft_Setup.sh
```

## Troubleshooting

### "Permission denied" errors
```bash
chmod +x *.sh
chmod +x release_linux/*.sh
```

### Missing Python dependencies
```bash
pip install pyinstaller pynput opencv-python cryptography pillow numpy
```

### X11 errors
Make sure you're using X11/Xorg (not Wayland):
```bash
echo $XDG_SESSION_TYPE
# Should output: x11
```

## Notes

- ✅ Windows files in `release/` folder are **untouched**
- ✅ Linux files in `release_linux/` folder are **separate**
- ✅ Both platforms fully supported
- ⚠️ Build Linux executables **only on Linux** (PyInstaller limitation)
- ⚠️ Build Windows executables **only on Windows**
