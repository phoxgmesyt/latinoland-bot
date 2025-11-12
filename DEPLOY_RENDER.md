# Despliegue en Render (Worker) — LATINOLAND Bot

Esta guía te lleva paso a paso para desplegar tu bot en Render como un *worker* (apto para bots de Discord) y dejarlo online 24/7.

## Archivos que añadí
- `render.yaml` — definición del servicio worker para deploy automático con Render.

## Resumen rápido
- Conecta tu repo de GitHub a Render
- Crea un servicio de tipo **Worker** (Render detecta `render.yaml` si está presente)
- Añade la variable de entorno `DISCORD_TOKEN` en el dashboard
- Deploy automático y logs en la UI de Render

---

## Paso a paso

1) Verifica que tu repo en GitHub contiene estos archivos en la raíz:
   - `bot.py`
   - `requirements.txt`
   - `Procfile` (opcional)
   - `render.yaml` (nuevo: define el worker)

2) Si aún no has subido los cambios (por ejemplo el `render.yaml`), haz commit y push:

```powershell
cd C:\Users\Yefrid Valverde\Desktop\latinoland-bot
git add render.yaml DEPLOY_RENDER.md
git commit -m "Add Render config + deploy guide"
git push origin main
```

3) Conecta el repo en Render:
   - Ve a https://render.com
   - Inicia sesión con GitHub
   - Click en **New** → **From Repo**
   - Busca y selecciona `phoxgmesyt/latinoland-bot`

4) Render detectará `render.yaml` y propondrá crear el servicio `latinoland-bot-worker` como Worker.
   - Si no detecta `render.yaml`, crea manualmente un nuevo **Worker**:
     - **Name**: latinoland-bot-worker
     - **Environment**: Python
     - **Build command**: pip install -r requirements.txt
     - **Start command**: python bot.py
     - **Instance type/plan**: free (o según plan)

5) Añade la variable de entorno en Render:
   - En el servicio, ve a **Environment** → **Environment Variables**
   - Añade `DISCORD_TOKEN` = `tu_token_aquí` (pega sin comillas)
   - (Opcional) añade `GUILD_ID` si quieres sincronizar comandos a un guild durante pruebas

6) Despliega y revisa logs:
   - Render hará build automáticamente (o haz click en Deploy)
   - Abre **Logs** y busca mensajes de conexión del bot: "Bot conectado como ..." o los logs que imprime `bot.py`

7) Prueba en Discord
   - En tu servidor escribe `/` y prueba los comandos.

---

## Notas y recomendaciones
- Usa `GUILD_ID` (env var) y sincroniza comandos por guild para pruebas (aparecen inmediatamente); deja global cuando todo esté ok.
- No subas `.env` al repo. Usa el dashboard de Render para secretos.
- Si tu bot necesita paquetes nativos, revisa los errores de build en los logs; tal vez requieras un `Dockerfile` (Render soporta Docker también).

---

Si quieres, puedo:
- Crear el commit con estos dos archivos (`render.yaml`, `DEPLOY_RENDER.md`) directamente en tu repo local (ya los añadí a la carpeta del workspace) y preparar el `git commit` (pero no puedo hacer el `git push` por ti — yo puedo aplicar el patch local; tú ejecutas `git push`).
- Ajustar `bot.py` para leer `GUILD_ID` y preferir la sincronización por guild en `on_ready` si pasas `GUILD_ID`.

¿Quieres que añada el snippet de sincronización por `GUILD_ID` en `bot.py` ahora (para pruebas rápidas en tu servidor)?