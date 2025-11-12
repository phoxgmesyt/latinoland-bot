# 🤖 GUÍA RÁPIDA: Bot Discord LATINOLAND ARK

## ⚡ Inicio Rápido (5 minutos)

### PASO 1️⃣: Obtener Token del Bot

1. Ve a: **https://discord.com/developers/applications**
2. Haz clic en **"New Application"**
3. Escribe el nombre: `LATINOLAND ARK Bot`
4. Acepta los términos y crea la app
5. Ve a la pestaña **"Bot"** (lado izquierdo)
6. Haz clic en **"Add Bot"**
7. En la sección **TOKEN**, haz clic en **"Copy"**
8. **Guarda este token** en un lugar seguro (lo necesitaremos en el PASO 3)

### PASO 2️⃣: Autorizar el Bot en tu Servidor (Interfaz Actualizada)

#### Opción A: Usar URL Generator (Método Recomendado)

1. En Discord Developer Portal, ve a **"OAuth2"** (en el menú lateral izquierdo)
2. Haz clic en **"URL Generator"**

3. En la sección **SCOPES**, marca:
   ```
   ☑ bot
   ☑ applications.commands
   ```

4. En la sección **PERMISSIONS**, marca:
   ```
   ☑ Send Messages (Enviar mensajes)
   ☑ Embed Links (Insertar links/embeds)
   ☑ Read Message History (Leer historial)
   ☑ Manage Messages (Administrar mensajes)
   ```

5. **Copia la URL generada** que aparece en la parte baja
6. **Abre la URL en tu navegador**
7. Selecciona tu servidor en el dropdown
8. Haz clic en **"Authorize"** o **"Continuar"**
9. Completa el CAPTCHA si aparece

✅ El bot ahora debería estar en tu servidor

#### Opción B: Si la Interfaz es Diferente (Nueva UI)

Si Discord cambió la interfaz:

1. Ve a **OAuth2** → **General** (o **Bot Authorization**)
2. Busca la sección de **Scopes** (puede estar en otra pestaña)
3. Selecciona:
   - `bot`
   - `applications.commands`
4. En **Default Permissions** o **Bot Permissions**, selecciona los mismos permisos
5. Copia la URL del Authorization link
6. Autoriza en tu servidor

**Nota:** Discord actualiza su interfaz regularmente. Si los nombres exactos cambian, busca por funcionalidad (OAuth2, Scopes, Permissions)

### PASO 3️⃣: Configurar el Archivo .env

1. Abre la carpeta `discord-bot` en Windows Explorer
2. Busca el archivo `.env.example`
3. Haz clic derecho → **"Copiar"**
4. Haz clic derecho en el espacio vacío → **"Pegar"**
5. Renombra el archivo copiado a `.env`
6. Abre `.env` con Notepad (clic derecho → Abrir con → Notepad)
7. Reemplaza esto:
   ```
   DISCORD_TOKEN=tu_token_aqui
   ```
   Con tu token del PASO 1. Ejemplo:
   ```
   DISCORD_TOKEN=MTk4NjIyNDgzNzEyODQ4MzI0.CrYiOg.Z7DFjkajdlfjasdklf_example
   ```
8. **Guarda el archivo** (Ctrl+S)

⚠️ **IMPORTANTE**: Nunca compartas tu token con nadie. Si lo haces, regenera uno nuevo en Discord Developer Portal.

### PASO 4️⃣: Instalar Dependencias Python

Opción A - Usando el Script (Recomendado):
- Haz doble clic en `start.ps1` (Windows)
  O
- En PowerShell, ve a la carpeta y ejecuta:
  ```powershell
  .\start.ps1
  ```

Opción B - Manual:
```powershell
# 1. Abrir PowerShell en la carpeta discord-bot
# 2. Ejecutar:
pip install -r requirements.txt
```

### PASO 5️⃣: Ejecutar el Bot

Opción A - Con Script:
```powershell
.\start.ps1
```

Opción B - Directo:
```powershell
python bot.py
```

✅ Verás en la consola:
```
✅ Bot conectado como LATINOLAND ARK Bot#1234
🎮 LATINOLAND ARK Bot listo
📝 9 comandos sincronizados con Discord
```

### PASO 6️⃣: Usar el Bot en Discord

En tu servidor Discord, escribe:
```
/comprar
/dinos
/vips
```

¡El bot debe responder! 🎉

---

## 📝 Todos los Comandos

| Comando | Qué hace |
|---------|---------|
| `/comprar` | Muestra items para comprar (shop) |
| `/vender` | Muestra items para vender |
| `/dinos` | Muestra todos los dinosaurios |
| `/crianza` | Muestra dinos P/Stats |
| `/abyssal` | Muestra dinos Abyssal |
| `/vips` | Muestra paquetes VIP |
| `/packs` | Muestra packs especiales |
| `/servidor` | Info de conexión del servidor ARK |
| `/ayuda` | Lista todos los comandos |

---

## 🆘 Solución de Problemas

### ❌ Error: "No se encontró DISCORD_TOKEN"
- Verifica que el archivo `.env` existe
- Asegúrate de que tiene `DISCORD_TOKEN=` con tu token

### ❌ El bot no responde en Discord
- Verifica que el bot aparece en el servidor (lado derecho, en la lista de usuarios)
- Intenta recargar Discord (F5 o cierra y abre)
- Verifica que tienes permisos para usar slash commands

### ❌ Error de Python "No module named discord"
- Instala las dependencias:
  ```powershell
  pip install -r requirements.txt
  ```

### ❌ Error "Token inválido o expirado"
- Regenera el token en Discord Developer Portal
- Actualiza `.env` con el nuevo token

### ❌ El bot se desconecta constantemente
- Verifica tu conexión a internet
- Verifica que el token es correcto
- Mira en `bot.log` si hay errores

---

## 🌟 Próximos Pasos

### Agregar Más Items
Edita `bot.py` y busca:
```python
SHOP_ITEMS = [
    # Agrega aquí más items...
]
```

### Cambiar Color del Bot
En `bot.py`, busca:
```python
EMBED_COLOR = discord.Color.from_rgb(0, 245, 255)  # Cyan
```

Cambios populares:
- Rojo: `(255, 0, 0)`
- Verde: `(0, 255, 0)`
- Azul: `(0, 0, 255)`

### Dejar el Bot 24/7
Ve a **README.md** y busca "Hosting Externo"

---

## 📞 ¿Necesitas Ayuda?

- Usa `/ayuda` en Discord
- Pregunta en el canal de soporte del servidor
- Discord: https://discord.gg/WAnqWz9RQ5

---

**¡Listo para usar! 🚀**
