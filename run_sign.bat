@echo off
REM === Set working directory to script folder ===
cd /d "%~dp0"

REM === Check if virtual environment exists ===
if not exist "env\" (
    echo Creating virtual environment...
    python -m venv env
)

REM === Install required packages silently ===
echo Installing required libraries...
env\Scripts\python.exe -m pip install --quiet --upgrade pip
env\Scripts\python.exe -m pip install --quiet pymupdf reportlab

REM === Run the signing script ===
echo Running PDF signing tool...
env\Scripts\python.exe sign_v1.2.py

echo.
echo ✅ Done! Check your 'output' folder.
pause
