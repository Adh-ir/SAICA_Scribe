#!/bin/bash
cd "$(dirname "$0")"
source .venv/bin/activate 2>/dev/null || true
pip install streamlit >/dev/null 2>&1
python3 code/streamlit_launcher.py
