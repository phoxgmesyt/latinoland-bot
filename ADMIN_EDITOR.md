# 🔧 Admin Editor - Interfaz Web para Editar Precios

## 📌 Descripción

`admin-editor.html` es una interfaz web moderna y fácil de usar para editar todos los datos del bot (precios, items, dinos, VIPs, packs) **sin necesidad de editar código JSON manualmente**.

---

## 🚀 Cómo Usar

### 1. **Abrir la Interfaz**

Simplemente abre `admin-editor.html` en tu navegador:
```
Double-click: admin-editor.html
O en el navegador: file:///C:/ruta/admin-editor.html
```

### 2. **Interfaz Principal**

```
┌─────────────────────────────────────┐
│ 🔧 LATINOLAND ARK - Admin Editor   │
│ Edita precios y datos sin código   │
└─────────────────────────────────────┘

[📂 Cargar] [💾 Guardar] [📥 Descargar] [🔄 Limpiar]

┌─────────────────────────────────────┐
│ 📊 ESTADÍSTICAS                     │
│ 9 Items | 9 Vender | 10 Dinos | ... │
└─────────────────────────────────────┘

🛒 Comprar | 💰 Vender | 🦕 Dinos | ⚫ Abyssal | 👑 VIPs | 📦 Packs
```

---

## 🎯 Funciones Principales

### **Editar Precios**

1. Haz clic en la pestaña deseada (ej: 🛒 Comprar)
2. Busca el item en la tabla
3. Modifica el **Precio** directamente en la celda
4. Los cambios se guardan automáticamente en memoria

**Ejemplo:**
```
[Runestone] [200] ← Haz clic y cambia a [300]
```

### **Editar Nombre o Descripción**

1. Haz clic en la celda de **Nombre** o **Descripción**
2. Escribe el nuevo valor
3. El cambio se aplica al instante

### **Agregar Nuevo Item**

1. Ve a la pestaña del item (ej: 🛒 Comprar)
2. Completa los campos en la sección "➕ Agregar Nuevo Item"
3. Haz clic en **Agregar Item**
4. El nuevo item aparece en la tabla

**Campos Obligatorios:**
- ✅ ID (identificador único)
- ✅ Nombre
- ✅ Precio

**Campos Opcionales:**
- 📝 Descripción

### **Eliminar un Item**

1. Encuentra el item en la tabla
2. Haz clic en el botón 🗑️ (Eliminar) en la fila
3. El item se elimina inmediatamente

---

## 💾 Guardar y Exportar

### **Opción 1: Guardar en el Navegador (Temporal)**

```
Botón: [💾 Guardar Localmente]
```

- Guarda los datos en el almacenamiento local del navegador
- ✅ Los datos persisten si cierras y reabre la página
- ⚠️ Se pierden si limpias el caché del navegador
- Solo en **este navegador/dispositivo**

**Uso:** Para guardar cambios mientras trabajas

### **Opción 2: Descargar JSON (Permanente)**

```
Botón: [📥 Descargar JSON]
```

- Descarga un archivo `data-YYYY-MM-DD.json`
- ✅ Guardado permanente en tu computadora
- ✅ Listo para subir al servidor

**Flujo Recomendado:**
1. Haz cambios en la interfaz
2. Haz clic en **Descargar JSON**
3. Reemplaza el `data.json` actual del bot con el descargado
4. Ejecuta `/reload` en Discord para aplicar cambios

---

## 📂 Cargar Datos Existentes

### **Opción A: Cargar desde Archivo**

```
Botón: [📂 Cargar data.json]
```

1. Haz clic en **Cargar data.json**
2. Selecciona tu archivo `data.json`
3. Los datos se cargan en la interfaz
4. Ahora puedes editarlos

**Casos de Uso:**
- Editar los datos actuales del bot
- Hacer backup y modificar
- Actualizar precios después de una sincronización

### **Opción B: Restaurar desde Almacenamiento Local**

Si guardaste datos localmente, se cargan automáticamente al abrir la página.

---

## 📊 Pestañas Disponibles

| Pestaña | Descripción | Acciones |
|---------|------------|----------|
| **🛒 Comprar** | Items para comprar | Editar precio, agregar, eliminar |
| **💰 Vender** | Items para vender | Editar precio, agregar, eliminar |
| **🦕 Dinos** | Dinosaurios normales | Editar nivel/precio, agregar, eliminar |
| **⚫ Abyssal** | Dinos especiales | Editar precio, agregar, eliminar |
| **👑 VIPs** | Paquetes de membresía | Editar beneficios, precio, agregar |
| **📦 Packs** | Ofertas especiales | Editar descripción, agregar |

---

## ✨ Características

### **Interfaz Responsiva**
- ✅ Funciona en Desktop, Tablet y Mobile
- ✅ Diseño oscuro (tema LATINOLAND)
- ✅ Botones y campos fáciles de usar

### **Edición En Tiempo Real**
- ✅ Los cambios se reflejan instantáneamente
- ✅ No requiere guardar manualmente cada cambio
- ✅ Los datos se guardan en memoria

### **Validación**
- ✅ Verifica campos obligatorios
- ✅ Previene errores de formato
- ✅ Mensajes de confirmación

### **Operaciones Seguras**
- ✅ Botón para descargar datos (backup)
- ✅ Confirmación antes de limpiar todo
- ✅ Recuperable desde almacenamiento local

### **Sincronización**
- ✅ Carga/descarga JSON fácilmente
- ✅ Compatible con `data.json` del bot
- ✅ Formato estructurado y validable

---

## 🔄 Flujo Completo de Trabajo

### **Escenario: Cambiar Precio de un Item**

```
1. Abre admin-editor.html en el navegador
   └─ Los datos se cargan localmente (si los guardaste)

2. Ve a la pestaña 🛒 Comprar
   └─ Ves la tabla con todos los items

3. Busca el item "Runestone"
   └─ Haz clic en su celda de Precio

4. Cambia 200 → 300
   └─ El cambio se aplica automáticamente

5. Haz clic en [💾 Guardar Localmente]
   └─ Se guarda en el navegador (copia de trabajo)

6. Cuando termines todos los cambios, haz clic en [📥 Descargar JSON]
   └─ Se descarga data-2025-11-12.json

7. Reemplaza el data.json actual con el descargado
   └─ En: C:\...\discord-bot\data.json

8. En Discord, admin ejecuta: /reload
   └─ El bot carga los nuevos precios
```

---

## 🎨 Secciones de la Interfaz

### **Panel Superior**

```
[📂 Cargar] [💾 Guardar] [📥 Descargar] [🔄 Limpiar]
```

- **Cargar**: Importa un JSON
- **Guardar**: Guarda en navegador
- **Descargar**: Descarga como archivo
- **Limpiar**: Borra todo (con confirmación)

### **Estadísticas**

```
9 Items | 9 Vender | 10 Dinos | 6 Abyssal | 3 VIPs | 3 Packs
```

Muestra el conteo actualizado en tiempo real

### **Pestañas**

```
🛒 Comprar | 💰 Vender | 🦕 Dinos | ⚫ Abyssal | 👑 VIPs | 📦 Packs
```

Navega entre categorías

### **Formulario Agregar (+)**

Campos para añadir nuevos items/dinos/etc.

### **Tabla Editable**

Filas con inputs para editar directamente

---

## 💡 Consejos Útiles

### **Trabajar Sin Conexión**
```
✅ Puedes usar la interfaz sin internet
✅ Los datos se guardan localmente
✅ Descarga cuando termines
```

### **Hacer Backup**
```
1. Descarga el JSON actual
2. Renómbralo: data-backup-20251112.json
3. Guárdalo en una carpeta segura
4. Si cometes un error, carga este backup
```

### **Cambios en Lote**
```
1. Abre admin-editor.html
2. Carga data.json actual
3. Edita múltiples items a la vez
4. Descarga el JSON
5. Reemplaza el original
6. /reload
```

### **Encontrar Items Rápidamente**
```
Usa Ctrl+F en el navegador para buscar dentro de la tabla
Ej: Ctrl+F → "Runestone"
```

---

## 🔒 Seguridad

### **Datos Locales**
- ✅ Los datos se guardan SOLO en tu navegador
- ✅ No se envían a internet
- ✅ No se conecta a servidores externos

### **Descarga de Archivo**
- ✅ El JSON es validable en cualquier editor
- ✅ Puedes revisar antes de usar
- ✅ Compatible con el bot

---

## 🐛 Troubleshooting

| Problema | Solución |
|----------|----------|
| No puedo abrir el archivo | Asegúrate de que admin-editor.html está en la carpeta del bot |
| Los datos no se guardan | Haz clic en [💾 Guardar Localmente] |
| El JSON descargado no funciona | Valida en https://jsonlint.com |
| Quiero recuperar cambios antiguos | Carga un data-backup-XXX.json que hayas descargado |
| Los números tienen decimales | Asegúrate de usar [📥 Descargar JSON] en lugar de copiar/pegar |

---

## 📚 Integración con el Bot

### **Paso 1: Editar Datos**
```
admin-editor.html → Editas precios
                  → Descargas data.json
```

### **Paso 2: Actualizar Bot**
```
Reemplaza el data.json anterior
  ↓
Ejecuta /reload en Discord
  ↓
Bot carga nuevos datos
```

### **Paso 3: Verificar**
```
Usuario ejecuta /comprar
  ↓
Precios actualizados aparecen
  ↓
✅ Confirmación exitosa
```

---

## 🚀 Casos de Uso

### **Gerente de Precios**
```
✅ Cambiar precios sin código
✅ Agregar items nuevos
✅ Editar descripciones
```

### **Administrador del Servidor**
```
✅ Actualizar ofertas VIP
✅ Crear nuevas promociones
✅ Modificar beneficios
```

### **Backup y Recuperación**
```
✅ Descargar datos actuales
✅ Restaurar desde backup
✅ Migrar a otro servidor
```

---

## 📞 Soporte

Si encuentras errores o tienes sugerencias:

1. **JSON inválido**: Valida en https://jsonlint.com
2. **No carga datos**: Revisa que el archivo sea valid JSON
3. **Datos no se guardan**: Verifica localStorage en dev tools (F12)

---

**Versión:** 1.0.0 - Web Admin Editor  
**Fecha:** Noviembre 12, 2025  
**Estado:** ✅ Listo para Producción

---

## 🎁 Bonus: Atajos de Teclado

| Atajo | Acción |
|-------|--------|
| `Ctrl+S` | Guardar (si implementas) |
| `Ctrl+F` | Buscar en tabla |
| `Ctrl+Shift+I` | Abrir Inspector (debug) |
| `Ctrl+Z` | Deshacer en navegador |

