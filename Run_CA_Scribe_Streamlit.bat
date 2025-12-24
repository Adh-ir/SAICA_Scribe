@echo off
cd /d "%~dp0"
call .venv\Scripts\activate.bat 2>nul
pip install streamlit >nul 2>&1
streamlit run code\streamlit_app.py
pause
