@echo off
echo ========================================
echo Creating Android Transfer Package
echo ========================================
echo.

:: Create a temporary directory for the package
set "PACKAGE_DIR=android_transfer_package"
if exist "%PACKAGE_DIR%" rmdir /s /q "%PACKAGE_DIR%"
mkdir "%PACKAGE_DIR%"

echo Copying files...

:: Copy all Python source files
copy /Y *.py "%PACKAGE_DIR%\" >nul 2>&1

:: Copy Android build files
copy /Y buildozer.spec "%PACKAGE_DIR%\" >nul 2>&1

:: Copy data files
copy /Y face_model.yml "%PACKAGE_DIR%\" >nul 2>&1
copy /Y haarcascade_frontalface_default.xml "%PACKAGE_DIR%\" >nul 2>&1
copy /Y secret.key "%PACKAGE_DIR%\" >nul 2>&1
copy /Y requirements.txt "%PACKAGE_DIR%\" >nul 2>&1

:: Copy documentation
copy /Y README.md "%PACKAGE_DIR%\" >nul 2>&1

:: Copy release_android folder
xcopy /E /I /Y release_android "%PACKAGE_DIR%\release_android\" >nul 2>&1

echo.
echo ========================================
echo Android Package Created Successfully!
echo ========================================
echo.
echo Location: %CD%\%PACKAGE_DIR%
echo.
echo IMPORTANT: Android APKs must be built on LINUX!
echo.
echo Next Steps:
echo 1. Transfer '%PACKAGE_DIR%' folder to a Linux machine
echo 2. Install Buildozer: pip install buildozer
echo 3. Run: ./release_android/build_android.sh
echo 4. Wait 15-30 minutes for first build
echo 5. APK will be in: release_android/Minecraft_Launcher.apk
echo.
echo See release_android/README_ANDROID.md for full instructions
echo.
pause
