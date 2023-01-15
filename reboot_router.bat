@echo off

rem Create virtual environment
python -m venv venv

rem Activate virtual environment
venv\Scripts\activate.bat

rem Install requirements
pip install -r requirements.txt

rem Run the script
python restart.py

rem Deactivate virtual environment
venv\Scripts\deactivate.bat