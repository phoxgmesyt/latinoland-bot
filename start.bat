@echo off
REM =====================================================
REM Script para iniciar el Bot Discord LATINOLAND ARK
REM =====================================================

echo.
echo ====================================
echo LATINOLAND ARK - Discord Bot
echo ====================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python no está instalado o no está en PATH
    echo Descarga Python desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Verificar si el archivo .env existe
if not exist ".env" (
    echo.
    echo ERROR: Archivo .env no encontrado
    echo Por favor, sigue estos pasos:
    echo.
    echo 1. Copia el archivo .env.example a .env
    echo    ^(puedes renombrarlo manualmente o ejecutar:^)
    echo    copy .env.example .env
    echo.
    echo 2. Abre .env y reemplaza 'tu_token_aqui' con tu token de bot
    echo.
    echo 3. Obtén tu token en: https://discord.com/developers/applications
    echo.
    pause
    exit /b 1
)

REM Verificar si virtual environment existe
if not exist "venv" (
    echo.
    echo Creando ambiente virtual...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Instalando dependencias...
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

REM Iniciar el bot
echo.
echo ✅ Iniciando bot...
echo.
python bot.py

if %errorlevel% neq 0 (
    echo.
    echo ERROR: El bot se cerró inesperadamente
    pause
)
