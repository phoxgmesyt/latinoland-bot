# Guía Rápida: Despliegue en Railway (Recomendado)

## ¿Por qué Railway?
- ✅ Gratis (hasta ciertos recursos)
- ✅ Deploy automático desde GitHub
- ✅ Variables de entorno seguras
- ✅ Reinicia automáticamente si el bot cae
- ✅ No necesita Docker instalado localmente

---

## Paso 1: Crear Repositorio en GitHub

1. Crea una cuenta en https://github.com (si no tienes)
2. Crea un nuevo repositorio público: `latinoland-bot`
3. Clona el repo localmente:
   ```powershell
   cd C:\Users\Yefrid Valverde\Desktop
   git clone https://github.com/tu_usuario/latinoland-bot.git
   cd latinoland-bot
   ```

4. Copia los archivos de `discord-bot/` al root del repo:
   ```powershell
   # Desde tu carpeta raíz del repo
   Copy-Item C:\Users\Yefrid Valverde\Desktop\weblatinoland\discord-bot\bot.py .
   Copy-Item C:\Users\Yefrid Valverde\Desktop\weblatinoland\discord-bot\requirements.txt .
   Copy-Item C:\Users\Yefrid Valverde\Desktop\weblatinoland\discord-bot\Dockerfile .
   Copy-Item C:\Users\Yefrid Valverde\Desktop\weblatinoland\discord-bot\.env.example .
   # Más archivos si quieres (config.py, GUIA_RAPIDA.md, etc.)
   ```

5. Crea un `.gitignore` para no subir tokens:
   ```
   .env
   *.log
   venv/
   __pycache__/
   *.pyc
   .DS_Store
   ```

6. Haz commit y push:
   ```powershell
   git add .
   git commit -m "Initial commit: Discord bot LATINOLAND"
   git push -u origin main
   ```

---

## Paso 2: Conectar a Railway

1. Ve a https://railway.app
2. Crea una cuenta (puedes conectar con GitHub)
3. **Create a new project** → **Deploy from GitHub repo**
4. Autoriza GitHub y selecciona tu repo `latinoland-bot`
5. Railway detectará el `Dockerfile` o `requirements.txt` automáticamente
6. Presiona **Deploy**

---

## Paso 3: Configurar Variables de Entorno en Railway

1. En Railway, ve a la pestaña **Variables**
2. Haz clic en **New Variable**
3. Añade:
   - **Nombre:** `DISCORD_TOKEN`
   - **Valor:** tu token del bot (pega sin comillas)
4. Presiona Enter y luego **Deploy** nuevamente

---

## Paso 4: Ver Logs

En Railway, haz clic en **Deployments** para ver el estado y logs del bot en tiempo real.

Deberías ver algo como:
```
✅ Bot conectado como LATINOLAND ARK Bot#1234
🎮 LATINOLAND ARK Bot listo
📝 8 comandos sincronizados con Discord
```

---

## Troubleshooting

### El bot no inicia
1. Verifica que `DISCORD_TOKEN` está configurada en Railway
2. Ve a Logs y busca el error
3. Asegúrate de que el token es válido (copiar de Discord Developer Portal nuevamente)

### El bot dice "DISCORD_TOKEN no encontrada"
- En Railway: Variables → añade `DISCORD_TOKEN` nuevamente
- Presiona **Redeploy**

### ¿Cómo actualizar el bot?
- Edita `bot.py` localmente
- Haz commit y push a GitHub
- Railway redeploy automático (o presiona el botón Redeploy manual)

---

## Alternativa: Desplegar localmente (sin Docker, sin Railway)

Si prefieres ejecutar el bot en tu máquina 24/7 (sin apagar):

1. Crea el archivo `.env` en `discord-bot/`:
   ```
   DISCORD_TOKEN=tu_token_aqui
   ```

2. Ejecuta el script `run-local.ps1` (también está en `discord-bot/`):
   ```powershell
   cd C:\Users\Yefrid Valverde\Desktop\weblatinoland\discord-bot
   .\run-local.ps1
   ```

3. El script:
   - Crea un virtualenv automáticamente
   - Instala dependencias
   - Ejecuta el bot
   - La próxima vez solo ejecuta el script (ya está el venv)

⚠️ **Nota:** Si cierras PowerShell, el bot se detiene. Para mantenerlo en background 24/7, usa Railway.

---

## Resumen Rápido

| Opción | Ventaja | Desventaja |
|--------|---------|-----------|
| **Railway** | Fácil, 24/7, automático, GitHub | Requiere GitHub |
| **Local + run-local.ps1** | Funciona ahora | Requiere PC siempre encendida |
| **Docker (si instalas)** | Total control, profesional | Curva de aprendizaje |

---

¿Necesitas ayuda con algún paso? Pregunta en Discord o abre un issue en GitHub.
