@echo off
cd /d "%~dp0"
set "MPLCONFIGDIR=%~dp0.venv\matplotlib-cache"
"%~dp0.venv\Scripts\python.exe" "%~dp0my-learning\practice.py"
pause
