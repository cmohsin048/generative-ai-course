@echo off
cd /d "%~dp0"
where code >nul 2>nul
if errorlevel 1 (
  start "" notepad.exe "%~dp0START-HERE.md"
) else (
  call code . START-HERE.md
)
