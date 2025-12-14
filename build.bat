@echo off
REM Build script for Relics & Ruins .exe
echo.
echo ========================================
echo Building Relics and Ruins .exe
echo ========================================
echo.

REM Build using PyInstaller
pyinstaller --onefile --windowed --name "Relics and Ruins" main.py

echo.
echo ========================================
echo Build complete!
echo ========================================
echo.
echo The .exe is located in: dist\Relics and Ruins.exe
echo.
pause
