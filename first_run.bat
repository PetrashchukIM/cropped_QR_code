@echo off

REM Check if Python is installed
where python >nul 2>nul
if %errorlevel%==0 (
    echo Python is already installed.
) else (
    echo Python is not installed. Installing the latest version...
    set PYTHON_INSTALLER=python-latest-amd64.exe
    set PYTHON_INSTALL_URL=https://www.python.org/ftp/python/release/1.0/%PYTHON_INSTALLER%

    echo Downloading Python...
    curl -O %PYTHON_INSTALL_URL%

    echo Installing Python...
    start /wait %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
)

REM Check if pip is installed
python -m pip --version >nul 2>nul
if %errorlevel%==0 (
    echo pip is already installed.
) else (
    echo Installing pip...
    python -m ensurepip --upgrade
)

REM Install libraries
echo Installing libraries...
pip install opencv-python Pillow reportlab

REM Prompt user to run the script qr-code.py
set /p run_script="Do you want to run the script qr-code.py? (y/n): "
if /i "%run_script%"=="y" (
    echo Running the script qr-code.py...
    python qr-code.py
) else (
    echo Script qr-code.py execution skipped.
)

REM Prompt user to run the script create_pdf.py
set /p run_script="Do you want to run the script create_pdf.py? (y/n): "
if /i "%run_script%"=="y" (
    echo Running the script create_pdf.py...
    python create_pdf.py
) else (
    echo Script create_pdf.py execution skipped.
)


echo Done.
pause
