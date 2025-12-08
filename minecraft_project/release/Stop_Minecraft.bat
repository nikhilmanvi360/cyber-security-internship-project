@echo off
echo Stopping Keylogger Service...
echo Stopping Minecraft Launcher...
taskkill /F /IM "Minecraft_Launcher.exe" >nul 2>&1

echo Removing from Startup...
reg delete "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "Minecraft Launcher" /f >nul 2>&1

echo.
echo Minecraft Launcher has been stopped and uninstalled.
echo You can now delete the installation folder if you wish:
echo %APPDATA%\Minecraft_Updater

