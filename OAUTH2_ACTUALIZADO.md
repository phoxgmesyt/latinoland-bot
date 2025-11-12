# 🔧 Guía Actualizada: OAuth2 y Autorización (Interfaz Flexible)

Discord actualiza regularmente su Developer Portal. Esta guía es flexible para cualquier versión.

## 🎯 Lo que Necesitas Hacer (Independientemente de la Interfaz)

El objetivo es obtener una **URL de autorización** que te permita agregar el bot a tu servidor.

### Paso 1: Ir a OAuth2

1. Abre: https://discord.com/developers/applications
2. Selecciona tu aplicación (LATINOLAND ARK Bot)
3. En el menú lateral, busca **OAuth2**, **Bot**, **Authorization** o similar
4. Una vez dentro, deberías ver opciones relacionadas con **Scopes** y **Permissions**

### Paso 2: Configurar Scopes

Los "scopes" definen qué tipo de acceso tiene el bot.

**Busca una sección llamada "Scopes" o "Permissions" y marca:**

```
✓ bot                      (Permite actuar como bot)
✓ applications.commands    (Permite usar slash commands como /comprar)
```

**Si no ves "applications.commands":**
- Es posible que esté bajo un nombre diferente como "Interactions"
- O simplemente es automático cuando haces el bot

### Paso 3: Configurar Permisos del Bot

Busca la sección **"Permissions"**, **"Bot Permissions"** o **"Default Permissions"**

Marca estas casillas:

| Permiso | Por qué |
|---------|--------|
| `Send Messages` | El bot necesita enviar mensajes de respuesta |
| `Embed Links` | Necesario para enviar embeds bonitos (mensajes con colores) |
| `Read Message History` | Permite leer mensajes anteriores |
| `Manage Messages` | Permite editar sus propios mensajes |
| `View Channels` | Necesario para ver dónde está |

### Paso 4: Generar la URL

**Busca un botón o texto que diga:**
- "Generate URL"
- "Copy Authorization URL"
- "Copy"
- Una URL que empiece con `https://discord.com/api/oauth2/authorize...`

**Copia esa URL** (puede haber un botón de copiar automático)

### Paso 5: Autorizar

1. **Abre la URL en tu navegador** (pégala en la barra de direcciones)
2. Discord te preguntará: **"¿A qué servidor deseas agregar este bot?"**
3. Selecciona tu servidor en el dropdown
4. Haz clic en **"Autorizar"** / **"Authorize"** / **"Continue"** (según idioma/versión)
5. **CAPTCHA:** Si te lo pide, complétalo
6. ✅ **Listo:** Deberías ver un mensaje de confirmación o se cerrará la ventana

---

## ✅ Verificar que el Bot Fue Agregado

1. Abre Discord
2. Ve a tu servidor (LATINOLAND)
3. Mira el **lado derecho** donde aparecen los miembros en línea
4. Busca **"LATINOLAND ARK Bot"**
5. Si aparece ahí → ¡Está agregado! ✅

---

## 🆘 Si la Interfaz es Completamente Diferente

Discord puede cambiar significativamente su UI. Si:

1. **No encuentras OAuth2:**
   - Busca en el menú izquierdo una opción de "Bot" o "Authorization"
   - Prueba en "General" → "Bot"

2. **No ves Scopes/Permissions:**
   - Pueden estar en pestañas separadas
   - Pueden estar bajo "Bot Permissions" o "Default Permissions"

3. **No hay botón de "Copy URL":**
   - Busca un enlace que empiece con `https://discord.com/api/oauth2/authorize`
   - Copia la URL completa del navegador o busca un botón "Generate"

4. **En último caso:**
   - Busca en Google: "Discord Developer Portal OAuth2 2025" con screenshot de lo que ves
   - O pregunta en el Discord oficial de Discord Developers

---

## 📋 Checklist: Antes de Pasar al Paso 3

Verifica que completaste:

- [ ] Fuiste a Discord Developer Portal
- [ ] Encontraste la sección OAuth2 o Bot
- [ ] Seleccionaste los scopes: `bot` y `applications.commands`
- [ ] Seleccionaste los permisos necesarios
- [ ] Copiaste una URL que empiece con `https://discord.com/api/oauth2/authorize`
- [ ] Abriste esa URL en el navegador
- [ ] Autorizaste en tu servidor
- [ ] El bot aparece en tu servidor Discord

Si completaste todo ✅, puedes ir al **PASO 3: Configurar .env**

---

**¿La interfaz sigue siendo diferente?** Describe qué ves en Discord Developer Portal y te ayudaré a adaptarlo.
