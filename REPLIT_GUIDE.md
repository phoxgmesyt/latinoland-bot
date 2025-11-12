# Despliegue en Replit — LATINOLAND Bot

Esta guía te muestra cómo usar Replit para ejecutar tu bot 24/7 (o mientras tu plan lo permita).

## 1) Preparar el repo (ya hecho)
Asegúrate de que tu repo contiene:
- `bot.py`
- `requirements.txt`
- `.replit` (este archivo define el comando de inicio)
- `Procfile` (opcional)

## 2) Crear un Repl desde GitHub
1. Ve a https://replit.com y crea una cuenta o inicia sesión.
2. Haz clic en **Create** → **Import from GitHub**.
3. Autoriza la conexión a GitHub si es necesario y selecciona el repo `phoxgmesyt/latinoland-bot`.
4. Replit importará el repo. Espera a que termine.

## 3) Verifica la instalación de dependencias
- Replit instala automáticamente paquetes listados en `requirements.txt`. Si no lo hace, abre la pestaña **Packages** y busca los paquetes o ejecuta en Shell:

```bash
pip install -r requirements.txt
```

## 4) Configurar Secrets (Environment variables)
1. En el Repl, abre la pestaña **Secrets** (icono de llave en la barra lateral).
2. Añade:
   - Key: `DISCORD_TOKEN` → Value: tu token del bot
   - Opcional Key: `GUILD_ID` → Value: id numérico del servidor de pruebas (para sync instantáneo)
3. Guarda.

## 5) Ejecutar el bot
- Presiona **Run** en Replit. El panel de Output mostrará los logs del proceso.
- Deberías ver mensajes como:
  - `✅ Bot conectado como LATINOLAND#0759`
  - `LATINOLAND ARK Bot listo`
  - `📝 X comandos sincronizados...`

## 6) Mantener el bot online 24/7
- Replit en plan gratuito puede suspender procesos inactivos. Para uptime 24/7 necesitas un plan **Hacker** (pago) o usar un ping keeper externo (no oficial).
- Replit ofrece la opción de activar **Always On** en la configuración del Repl (requiere plan de pago).

## 7) Logs y troubleshooting
- Usa la pestaña **Console/Output** para ver logs.
- Errores comunes:
  - `DISCORD_TOKEN not found` → revisa Secrets
  - Dependencias faltantes → instala en Shell `pip install -r requirements.txt`
  - Permisos de intents → habilita `message_content` en el Developer Portal solo si es necesario

## 8) Actualizar el bot
- Edita `bot.py` localmente → git commit + push → Replit redeployará automáticamente si importaste desde GitHub, o haz manual **Pull** desde la pestaña Git.

---

Si quieres, te guío desde aquí paso a paso mientras conectas el Repl y pegas los secrets. También puedo añadir un pequeño `run-replit.ps1` para probar localmente si lo deseas.
