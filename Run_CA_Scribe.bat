@echo off
setlocal enabledelayedexpansion

TITLE CA Scribe - Auto Launcher
cd /d "%~dp0\code"

echo =========================================
echo        CA Scribe - Auto Launcher      
echo =========================================
echo.

:: 1. Port Cleanup (Kill process on port 8000)
echo [Cleaning] Checking for old processes on port 8000...
for /f "tokens=5" %%a in ('netstat -aon ^| find ":8000" ^| find "LISTENING"') do (
    echo    Killing PID %%a...
    taskkill /F /PID %%a >nul 2>&1
)

:: 2. Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python 3 is not installed.
    echo.
    echo Attempting auto-install via Winget...
    winget install -e --id Python.Python.3.11 --source winget
    
    if !errorlevel! equ 0 (
        echo.
        echo [Success] Python has been installed successfully!
        echo.
        echo ========================================================
        echo  PLEASE RESTART THIS SCRIPT
        echo ========================================================
        echo  Windows needs to reload the environment variables.
        echo  Please close this window and double-click the script again.
        echo ========================================================
        pause
        exit /b
    )

    echo.
    echo [Failed] Automatic install failed.
    echo Opening Python download page...
    start https://www.python.org/downloads/
    echo.
    echo ========================================================
    echo  MANUAL INSTALL REQUIRED
    echo ========================================================
    echo  1. The Python website has opened.
    echo  2. Download and run the installer.
    echo  3. IMPORTANT: Check "Add Python to PATH" during install.
    echo  4. Run this script again after installing.
    echo ========================================================
    pause
    exit /b
)

:: 3. Setup Virtual Env
if not exist ".venv" (
    echo [Setup] Creating virtual environment...
    python -m venv .venv
)

:: 4. Activate & Install
echo [Setup] Checking dependencies...
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip >nul 2>&1
pip install -q pip-system-certs
pip install -q -r requirements.txt

:: 5. Launch
:: 5. Launch
echo [Launch] Starting Server via Launcher...

python launcher.py

echo.
echo Server stopped.
pause
