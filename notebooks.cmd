@echo off
cd /d "%~dp0"
set "MPLCONFIGDIR=%~dp0.venv\matplotlib-cache"
set "JUPYTER_CONFIG_DIR=%~dp0.venv\jupyter-config"
set "JUPYTER_DATA_DIR=%~dp0.venv\share\jupyter"
set "JUPYTER_RUNTIME_DIR=%~dp0.venv\jupyter-runtime"
set "IPYTHONDIR=%~dp0.venv\ipython"
"%~dp0.venv\Scripts\python.exe" -m jupyterlab --ServerApp.ip=127.0.0.1
pause
