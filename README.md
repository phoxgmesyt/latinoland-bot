# 🤖 Bot Discord LATINOLAND ARK

Bot oficial para el servidor LATINOLAND ARK en Discord. Muestra items, dinos, VIPs, packs y más información del servidor.

## 📋 Características

✅ **Comandos Slash** (`/comprar`, `/vender`, `/dinos`, etc.)
✅ **Items de Compra/Venta** - Listados completos con precios
✅ **Dinosaurios** - Normales y Abyssal
✅ **Crianza (P/Stats)** - Dinos especiales para crianza
✅ **VIPs y Packs** - Paquetes disponibles
✅ **Info del Servidor** - IP, conexión, Discord
✅ **Embeds bonitos** - Diseño profesional con colores

## 🚀 Instalación

### Paso 1: Crear Bot en Discord Developer Portal

1. Ve a: https://discord.com/developers/applications
2. Haz clic en **New Application**
3. Dale un nombre: `LATINOLAND ARK Bot`
4. Ve a la pestaña **Bot** → **Add Bot**
5. En **TOKEN**, haz clic en **Copy** para copiar tu token
6. Guarda el token en un lugar seguro

### Paso 2: Configurar Permisos y Obtener URL de Autorización

**En Discord Developer Portal:**

1. Ve a **OAuth2** (menú lateral izquierdo)
2. Haz clic en **URL Generator** (si existe) o ve a **Scopes**

3. **Selecciona Scopes:**
   ```
   ☑ bot
   ☑ applications.commands
   ```

4. **Selecciona Permissions:**
   ```
   ☑ Send Messages
   ☑ Embed Links
   ☑ Read Message History
   ☑ Manage Messages
   ```

5. **Copia la URL generada** (aparecerá en la parte baja)
6. **Abre la URL en tu navegador**
7. Selecciona tu servidor del dropdown
8. Autoriza al bot

**Nota:** Si la interfaz de Discord ha cambiado, busca las opciones equivalentes en OAuth2/Bot Management. La funcionalidad es la misma pero el diseño puede variar.

### Paso 3: Instalar Dependencias

Abre PowerShell en la carpeta `discord-bot` y ejecuta:

```powershell
pip install -r requirements.txt
```

### Paso 4: Crear archivo .env

1. Copia `.env.example` a `.env`:
   ```powershell
   Copy-Item .env.example .env
   ```

2. Abre `.env` y reemplaza `tu_token_aqui` con tu token de bot:
   ```
   DISCORD_TOKEN=tu_token_de_bot_aqui
   ```

### Paso 5: Ejecutar el Bot

```powershell
python bot.py
```

Deberías ver:
```
✅ Bot conectado como LATINOLAND ARK Bot#1234
🎮 LATINOLAND ARK Bot listo
📝 8 comandos sincronizados con Discord
```

## 📝 Comandos Disponibles

| Comando | Descripción |
|---------|-------------|
| `/comprar` | Muestra items para comprar (9 items, paginados) |
| `/vender` | Muestra items para vender (9 items, paginados) |
| `/dinos` | Muestra todos los dinos (regulares + abyssal) |
| `/crianza` | Muestra dinos P/Stats para crianza |
| `/abyssal` | Muestra solo dinos Abyssal |
| `/vips` | Muestra paquetes VIP |
| `/packs` | Muestra packs especiales |
| `/servidor` | Información del servidor ARK |
| `/ayuda` | Lista completa de comandos |

## 🎮 Uso

En tu servidor Discord, escribe cualquier comando con `/`:

```
/comprar          → Ver items de shop
/dinos            → Ver todos los dinos
/vips             → Ver paquetes VIP
/servidor         → Info de conexión
```

Los comandos aparecerán automáticamente cuando escribas `/` en el chat.

## 🔧 Configuración Avanzada

### Cambiar Color de Embeds

En `bot.py`, busca:
```python
EMBED_COLOR = discord.Color.from_rgb(0, 245, 255)  # Cyan
```

Cámbialo a cualquier RGB:
- **Rojo**: `(255, 0, 0)`
- **Verde**: `(0, 255, 0)`
- **Azul**: `(0, 0, 255)`
- **Amarillo**: `(255, 255, 0)`

### Agregar Más Items

En `bot.py`, edita las listas:
- `SHOP_ITEMS` - Items de compra
- `SELL_ITEMS` - Items de venta
- `DINOS` - Dinosaurios normales
- `DINOS_ABYSSAL` - Dinos Abyssal

Estructura de un item:
```python
{
    "id": "10",
    "nombre": "rex",
    "tipo": "item",
    "descripcion": "Trofeo cabeza de rex",
    "precio": 50,
    "comando": "/sell rex"
}
```

## 🌐 Hosting Externo (24/7)

Para que el bot esté siempre en línea:

### Opción 1: Replit (Fácil, Gratis)
1. Ve a https://replit.com
2. Crea una cuenta
3. Haz clic en **Create Repl**
4. Selecciona **Python**
5. Copia los archivos (`bot.py`, `requirements.txt`, `.env`)
6. Haz clic en **Run**

### Opción 2: Railway (Recomendado)
1. Ve a https://railway.app
2. Conecta tu GitHub o sube archivos
3. Configura la variable `DISCORD_TOKEN`
4. Deploy automático

### Opción 3: VPS (DigitalOcean, Linode, etc.)
1. Renta un VPS ($5-10/mes)
2. Conéctate por SSH
3. Sube los archivos
4. Instala Python y ejecuta en background con `screen` o `tmux`

## 📦 Estructura del Proyecto

```
discord-bot/
├── bot.py              # Código principal del bot
├── requirements.txt    # Dependencias Python
├── .env               # Token (crear manualmente)
├── .env.example       # Ejemplo de .env
└── README.md          # Este archivo
```

## 🆘 Troubleshooting

### Error: "No se encontró DISCORD_TOKEN"
- Verifica que el archivo `.env` existe en la misma carpeta que `bot.py`
- Verifica que tiene la línea `DISCORD_TOKEN=tu_token`

### El bot no responde
- Verifica que el bot tiene permisos en el canal
- Asegúrate de que sincronizó los comandos (mira el log)
- Intenta recargar el servidor (desconecta y conecta)

### Error de permisos
- Ve a Discord Developer Portal → Bot → Permissions
- Asegúrate de que tiene `Send Messages` y `Embed Links`

## 📞 Soporte

- 🎮 Discord Server: [LATINOLAND](https://discord.gg/WAnqWz9RQ5)
- 🐛 Reporta bugs en Discord

## 📄 Licencia

Este bot es para uso interno del servidor LATINOLAND ARK.

---

**¡Gracias por usar el Bot LATINOLAND ARK! 🎉**
