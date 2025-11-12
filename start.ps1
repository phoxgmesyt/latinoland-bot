#!/usr/bin/env pwsh

# =====================================================
# Script para iniciar el Bot Discord LATINOLAND ARK (PowerShell)
# =====================================================

Write-Host ""
Write-Host "====================================" -ForegroundColor Cyan
Write-Host "LATINOLAND ARK - Discord Bot" -ForegroundColor Cyan
Write-Host "====================================" -ForegroundColor Cyan
Write-Host ""

# Verificar si Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ Python encontrado: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ ERROR: Python no está instalado" -ForegroundColor Red
    Write-Host "Descarga desde: https://www.python.org/downloads/" -ForegroundColor Yellow
    pause
    exit 1
}

# Verificar si el archivo .env existe
if (-not (Test-Path ".env")) {
    Write-Host ""
    Write-Host "❌ ERROR: Archivo .env no encontrado" -ForegroundColor Red
    Write-Host ""
    Write-Host "Sigue estos pasos:" -ForegroundColor Yellow
    Write-Host "1. Copia .env.example a .env:" -ForegroundColor Yellow
    Write-Host "   Copy-Item .env.example .env" -ForegroundColor White
    Write-Host ""
    Write-Host "2. Abre .env y reemplaza 'tu_token_aqui' con tu token" -ForegroundColor Yellow
    Write-Host "3. Obtén tu token en: https://discord.com/developers/applications" -ForegroundColor Yellow
    Write-Host ""
    pause
    exit 1
}

# Verificar/crear ambiente virtual
if (-not (Test-Path "venv")) {
    Write-Host ""
    Write-Host "📦 Creando ambiente virtual..." -ForegroundColor Cyan
    python -m venv venv
    
    Write-Host "📥 Activando ambiente y instalando dependencias..." -ForegroundColor Cyan
    & "venv\Scripts\Activate.ps1"
    pip install -r requirements.txt
    
    Write-Host "✅ Dependencias instaladas" -ForegroundColor Green
} else {
    Write-Host "✅ Ambiente virtual encontrado" -ForegroundColor Green
    & "venv\Scripts\Activate.ps1"
}

# Iniciar el bot
Write-Host ""
Write-Host "🚀 Iniciando bot..." -ForegroundColor Cyan
Write-Host ""

python bot.py

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "❌ El bot se cerró inesperadamente (código: $LASTEXITCODE)" -ForegroundColor Red
    pause
}
