@echo off
echo ========================================
echo Creating Linux Transfer Package
echo ========================================
echo.

:: Create a temporary directory for the package
set "PACKAGE_DIR=linux_transfer_package"
if exist "%PACKAGE_DIR%" rmdir /s /q "%PACKAGE_DIR%"
mkdir "%PACKAGE_DIR%"

echo Copying files...

:: Copy all Python source files
copy /Y *.py "%PACKAGE_DIR%\" >nul 2>&1

:: Copy Linux build scripts
copy /Y build_portable_linux.sh "%PACKAGE_DIR%\" >nul 2>&1
copy /Y build_all_platforms.sh "%PACKAGE_DIR%\" >nul 2>&1
copy /Y Minecraft_Launcher_Linux.spec "%PACKAGE_DIR%\" >nul 2>&1

:: Copy data files
copy /Y face_model.yml "%PACKAGE_DIR%\" >nul 2>&1
copy /Y haarcascade_frontalface_default.xml "%PACKAGE_DIR%\" >nul 2>&1
copy /Y secret.key "%PACKAGE_DIR%\" >nul 2>&1
copy /Y requirements.txt "%PACKAGE_DIR%\" >nul 2>&1

:: Copy documentation
copy /Y README.md "%PACKAGE_DIR%\" >nul 2>&1
copy /Y BUILD_INSTRUCTIONS.md "%PACKAGE_DIR%\" >nul 2>&1
copy /Y TRANSFER_TO_LINUX.md "%PACKAGE_DIR%\" >nul 2>&1

:: Copy release_linux folder
xcopy /E /I /Y release_linux "%PACKAGE_DIR%\release_linux\" >nul 2>&1

echo.
echo ========================================
echo Package Created Successfully!
echo ========================================
echo.
echo Location: %CD%\%PACKAGE_DIR%
echo.
echo Next Steps:
echo 1. Transfer the '%PACKAGE_DIR%' folder to your Linux machine
echo 2. See TRANSFER_TO_LINUX.md for detailed instructions
echo.
echo Suggested transfer methods:
echo - USB drive
echo - Cloud storage (Google Drive, Dropbox)
echo - SCP/SFTP
echo - Git repository
echo.
pause
