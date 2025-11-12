# Ejecutar bot LATINOLAND localmente
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$venvPath = Join-Path $scriptPath "venv"
$botPath = Join-Path $scriptPath "bot.py"
$envPath = Join-Path $scriptPath ".env"

if (-Not (Test-Path $envPath)) {
    Write-Host "ERROR: archivo .env no encontrado" -ForegroundColor Red
    Write-Host "Crea .env con: DISCORD_TOKEN=tu_token"
    exit 1
}

Write-Host "Activando virtualenv..."
if (-Not (Test-Path $venvPath)) {
    python -m venv venv
    Write-Host "venv creado"
}

& "$venvPath\Scripts\Activate.ps1"
pip install -q -r requirements.txt
Write-Host "Bot iniciado. Presiona Ctrl+C para detener."
python $botPath
