# Despliegue 24/7 — Bot LATINOLAND ARK

Este documento contiene instrucciones para ejecutar el bot 24/7 sin necesidad de instalar Docker.

> Requisitos previos
> - Token del bot (`DISCORD_TOKEN`)
> - Python 3.9+ instalado (solo si despliegas localmente)
> - Cuenta GitHub (para Railway — recomendado)

---

## ✅ Opción 1: Railway (Recomendado — Fácil, 24/7, Gratis)

**Ventajas:**
- ✅ Automático: GitHub → Railway → Online
- ✅ 24/7 sin apagar tu PC
- ✅ Reinicia si cae
- ✅ No requiere Docker instalado
- ✅ Variables de entorno seguras

**Pasos:** Ve a `RAILWAY_GUIDE.md` en esta carpeta para instrucciones completas.

---

## ✅ Opción 2: Ejecutar Localmente (Sin Esperar a Railway)

**Ventajas:**
- ✅ Funciona ya
- ✅ Sin dependencias externas (solo Python)
- ✅ Ver logs en tiempo real

**Desventajas:**
- ❌ Requiere tu PC encendida 24/7

**Pasos:**

1. Crea un archivo `.env` en `discord-bot/`:
   ```
   DISCORD_TOKEN=tu_token_aqui
   ```

2. Ejecuta el script `run-local.ps1`:
   ```powershell
   cd C:\Users\Yefrid Valverde\Desktop\weblatinoland\discord-bot
   .\run-local.ps1
   ```

3. El script automáticamente:
   - Crea un `venv` (virtualenv)
   - Instala dependencias
   - Arranca el bot

4. Verás:
   ```
   ✅ Bot conectado como LATINOLAND ARK Bot#1234
   🎮 LATINOLAND ARK Bot listo
   ```

5. Presiona `Ctrl+C` para detener.

---

## 📦 Opción 3: Docker (Si lo Necesitas Instalado)

Si ya tienes Docker instalado o quieres aprender, ve a `DEPLOYMENT.md` anterior (antigua versión) o consulta:
- https://docs.docker.com/get-started/
- Luego: `docker build -t latinoland-bot . && docker run --env-file .env latinoland-bot`

---

## 🔐 Seguridad y Buenas Prácticas

1. **Nunca subas tu token a GitHub.** Usa variables de entorno (Railway, .env local, etc.)
2. **Usa .gitignore** — no incluyas `.env` ni archivos sensibles
3. **Mantén intents seguros** — `message_content` está desactivado por defecto

---

## 📞 Resumen Rápido

| Opción | Costo | Setup | 24/7 | Actualizar |
|--------|-------|-------|------|-----------|
| Railway | Gratis* | 5 min | ✅ | Git push |
| Local | Gratis | 2 min | ❌ | Reiniciar script |
| Docker | Gratis | 10 min | ✅ | Rebuild image |

*Railway: primeros $5/mes gratis; luego cobran por recursos (generalmente sigue siendo gratis para bots pequeños)

---

## 🚀 Próximos Pasos

1. **Railway (recomendado):** Ve a `RAILWAY_GUIDE.md`
2. **Local ahora:** Ejecuta `run-local.ps1` 
3. **Ayuda:** Pregunta en Discord o abre un issue en GitHub

