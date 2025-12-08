# Build Instructions

This project supports building for both **Windows** and **Linux** platforms.

## Prerequisites

### Windows
- Python 3.7+
- Virtual environment with dependencies installed
- PyInstaller

### Linux
- Python 3.7+
- Virtual environment with dependencies installed
- PyInstaller
- X11/Xorg display server

## Building for Windows

### Option 1: Using Batch Script
```cmd
build_portable.bat
```

### Option 2: Using PyInstaller Directly
```cmd
call venv\Scripts\activate
pyinstaller Minecraft_Launcher.spec
```

**Output:** `dist/Minecraft_Launcher.exe`

**Release Files Location:** `release/` directory
- `Minecraft_Launcher.exe`
- `Minecraft_Setup.bat`
- `Stop_Minecraft.bat`
- `secret.key`

## Building for Linux

### Option 1: Using Shell Script
```bash
chmod +x build_portable_linux.sh
./build_portable_linux.sh
```

### Option 2: Using PyInstaller Directly
```bash
source venv/bin/activate
pyinstaller Minecraft_Launcher_Linux.spec
```

### Option 3: Build and Package (Recommended)
```bash
chmod +x build_all_platforms.sh
./build_all_platforms.sh
```

**Output:** `dist/Minecraft_Launcher` (Linux binary)

**Release Files Location:** `release_linux/` directory
- `Minecraft_Launcher`
- `Minecraft_Setup.sh`
- `Stop_Minecraft.sh`
- `secret.key`
- `README_LINUX.md`

## Platform-Specific Notes

### Windows
- Uses Win32 API for keyboard/mouse hooks
- Installs to: `%APPDATA%\Minecraft_Updater`
- Autostart via Registry: `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`

### Linux
- Uses X11/Xorg for keyboard/mouse hooks
- Installs to: `~/.minecraft_updater`
- Autostart via systemd user service: `~/.config/systemd/user/minecraft-launcher.service`

## Cross-Platform Building

**Note:** You cannot cross-compile between platforms with PyInstaller.

- Build Windows executables **on Windows**
- Build Linux binaries **on Linux**

## Troubleshooting

### Windows Build Issues
- Ensure virtual environment is activated
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Verify PyInstaller is installed: `pip install pyinstaller`

### Linux Build Issues
- Ensure X11 development libraries are installed:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install python3-xlib
  
  # Fedora
  sudo dnf install python3-xlib
  
  # Arch
  sudo pacman -S python-xlib
  ```
- Make sure scripts have execute permissions: `chmod +x *.sh`
- Verify pynput supports your display server (X11/Xorg required)

## File Structure

```
minecraft_project/
├── build_portable.bat              # Windows build script
├── build_portable_linux.sh         # Linux build script
├── build_all_platforms.sh          # Unified Linux build & package
├── Minecraft_Launcher.spec         # Windows PyInstaller spec
├── Minecraft_Launcher_Linux.spec   # Linux PyInstaller spec
├── release/                        # Windows release files
│   ├── Minecraft_Launcher.exe
│   ├── Minecraft_Setup.bat
│   ├── Stop_Minecraft.bat
│   └── secret.key
└── release_linux/                  # Linux release files
    ├── Minecraft_Launcher
    ├── Minecraft_Setup.sh
    ├── Stop_Minecraft.sh
    ├── secret.key
    └── README_LINUX.md
```

## Distribution

### Windows
Distribute the entire `release/` folder. Users run `Minecraft_Setup.bat`.

### Linux
Distribute the entire `release_linux/` folder. Users run:
```bash
chmod +x Minecraft_Setup.sh
./Minecraft_Setup.sh
```
