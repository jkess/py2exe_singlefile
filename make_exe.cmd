@ECHO OFF
REM requires python 2.7 and py2exe module
set CWD=%~dp0
cd /d "%cwd%"
python.exe setup.py py2exe
pause
