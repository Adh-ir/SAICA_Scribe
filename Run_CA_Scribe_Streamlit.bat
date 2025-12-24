@echo off
cd /d "%~dp0"
call .venv\Scripts\activate.bat 2>nul
pip install streamlit >nul 2>&1
python code\streamlit_launcher.py
pause
