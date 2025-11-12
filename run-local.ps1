# Script para ejecutar el bot LATINOLAND localmente en Windows
# Uso: .\run-local.ps1

$botName = "LATINOLAND Bot"
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$botPath = Join-Path $scriptPath "bot.py"
$envPath = Join-Path $scriptPath ".env"

# Verificar que .env existe
if (-Not (Test-Path $envPath)) {
    Write-Host "[ERROR] No se encontró .env en $scriptPath" -ForegroundColor Red
    Write-Host "Crea un archivo .env con DISCORD_TOKEN=tu_token" -ForegroundColor Yellow
    exit 1
}

# Verificar que python está disponible
$pythonTest = python --version 2>$null
if (-Not $?) {
    Write-Host "[ERROR] Python no está instalado o no está en el PATH" -ForegroundColor Red
    exit 1
}

Write-Host "[INFO] Iniciando $botName..." -ForegroundColor Green
Write-Host "[INFO] Ubicación: $scriptPath" -ForegroundColor Cyan
Write-Host "[INFO] Python: $pythonTest" -ForegroundColor Cyan
Write-Host ""

# Crear venv si no existe
$venvPath = Join-Path $scriptPath "venv"
if (-Not (Test-Path $venvPath)) {
    Write-Host "[INFO] Creando virtualenv..." -ForegroundColor Cyan
    python -m venv venv
    & "$venvPath\Scripts\Activate.ps1"
    pip install --upgrade pip -q
    pip install -r requirements.txt
} else {
    Write-Host "[OK] Virtualenv ya existe, activando..." -ForegroundColor Cyan
    & "$venvPath\Scripts\Activate.ps1"
}

Write-Host "[INFO] Ejecutando bot.py..." -ForegroundColor Green
Write-Host "Presiona Ctrl+C para detener" -ForegroundColor Yellow
Write-Host ""

# Ejecutar bot
python $botPath

Write-Host ""
Write-Host "[INFO] Bot detenido." -ForegroundColor Yellow
