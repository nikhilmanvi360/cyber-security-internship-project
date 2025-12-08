@echo off
echo Building Minecraft_Launcher.exe...
call venv\Scripts\activate
pyinstaller --noconsole --onefile --name "Minecraft_Launcher" --add-data "face_model.yml;." --add-data "haarcascade_frontalface_default.xml;." --hidden-import=pynput.keyboard._win32 --hidden-import=pynput.mouse._win32 main.py
echo Build Complete. Check dist/ folder.
pause
