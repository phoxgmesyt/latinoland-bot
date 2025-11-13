# 🔄 Sincronización Dinámica de Datos - Documentación

## 📌 Descripción General

El bot ahora carga todos sus datos (items, dinos, VIPs, packs) desde un archivo `data.json` centralizado. Esto significa que **puedes actualizar precios y contenido sin editar el código del bot**.

---

## 🎯 Cómo Funciona

### 1. **Flujo de Carga de Datos**

```
Inicio del Bot
    ↓
cargar_datos() se ejecuta
    ↓
¿Existe data.json? 
    ↓ Sí
Carga datos desde data.json
    ↓ No
Usa datos por defecto (hardcoded)
    ↓
SHOP_ITEMS, DINOS, VIPS, etc. quedan cargados en memoria
    ↓
Bot listo para responder comandos
```

### 2. **Actualizar Datos en Tiempo Real**

#### **Opción A: Editar `data.json` directamente**
1. Abre `data.json` en tu editor
2. Modifica precios, nombres, descripciones
3. Ejecuta `/reload` en Discord
4. ✅ Los cambios se aplican instantáneamente

#### **Opción B: Usar `/reload` desde Discord**
1. Un administrador ejecuta `/reload`
2. El bot lee `data.json` nuevamente
3. Todos los datos se actualizan en memoria
4. ✅ Los cambios están disponibles en los siguientes comandos

---

## 📋 Estructura de `data.json`

El archivo `data.json` contiene todo lo necesario para el bot:

```json
{
  "version": "1.1.0",
  "lastUpdated": "2025-11-12T00:00:00Z",
  "shop_items": [...],
  "sell_items": [...],
  "dinos": [...],
  "dinos_abyssal": [...],
  "vips": [...],
  "packs": [...],
  "servidor": {...}
}
```

### **Campos de un Item**
```json
{
  "id": "01",
  "nombre": "Runestone",
  "tipo": "item",
  "descripcion": "Piedra runica",
  "precio": 200,
  "comando": "/buy Runestone",
  "cantidad": 1
}
```

### **Campos de un Dino**
```json
{
  "id": "50",
  "nombre": "Carbonemys",
  "tipo": "dino",
  "descripcion": "(P/stats)",
  "nivel": 1,
  "precio": 1500,
  "comando": "/buy bcarb"
}
```

### **Campos de un VIP**
```json
{
  "nombre": "VIP1",
  "tipo": "vip",
  "descripcion": "🔹250 puntos cada 10 minutos...",
  "precio": "$10",
  "duracion": "15 días"
}
```

---

## 🔧 Comandos Relacionados

### **`/reload` - Recargar Datos**
```
/reload
```

**Requisitos:**
- ✅ Solo administradores del servidor pueden ejecutarlo
- ✅ Recarga `data.json` sin reiniciar el bot

**Respuesta:**
```
✅ Datos Recargados

Se han recargado correctamente los datos desde data.json

📋 Items para comprar: 9
💰 Items para vender: 9
🦕 Dinos normales: 10
⚫ Dinos Abyssal: 6
👑 Paquetes VIP: 3
📦 Ofertas especiales: 3
```

**Errores Posibles:**
- `❌ Permiso Denegado` — No eres administrador
- `❌ Error al Recargar` — data.json tiene formato inválido (revisa la sintaxis JSON)

---

## 💡 Casos de Uso Comunes

### **Cambiar un Precio**

1. Abre `data.json`
2. Busca el item (ej: "Runestone")
3. Cambia `"precio": 200` a `"precio": 300`
4. Guarda el archivo
5. Ejecuta `/reload` en Discord
6. ✅ Hecho! El nuevo precio aparece en `/comprar`

**Antes:**
```json
{"id": "01", "nombre": "Runestone", "precio": 200}
```

**Después:**
```json
{"id": "01", "nombre": "Runestone", "precio": 300}
```

### **Agregar un Nuevo Item**

1. Abre `data.json`
2. Ve a la sección `shop_items`
3. Copia un item existente y modifica:

```json
{
  "id": "10",
  "nombre": "NuevoItem",
  "tipo": "item",
  "descripcion": "Descripción del nuevo item",
  "nivel": "-",
  "precio": 5000,
  "comando": "/buy NuevoItem",
  "cantidad": 1
}
```

4. Guarda y ejecuta `/reload`
5. ✅ El nuevo item aparece en `/comprar`

### **Cambiar Descripción de un VIP**

1. Abre `data.json`, sección `vips`
2. Modifica la descripción (puedes usar saltos de línea con `\n`)
3. Guarda y ejecuta `/reload`
4. ✅ La descripción se actualiza en `/vips`

---

## 🛡️ Validación de `data.json`

### **Validar Sintaxis JSON**

Si cometes un error de sintaxis, el bot fallará al cargar. **Síntomas:**
- El comando `/reload` devuelve error
- Los datos no se actualizan

**Cómo arreglarlo:**

1. **Usa un validador JSON online:** https://jsonlint.com/
2. Copia el contenido de `data.json` en el sitio
3. Si hay error, te mostrará la línea exacta
4. Corrige y guarda nuevamente

**Errores Comunes:**
- ❌ Comilla simple `'` en lugar de doble `"`
- ❌ Coma faltante entre campos
- ❌ Corchete o llave sin cerrar
- ❌ Valor sin comillas si es texto

**Correcto:**
```json
{"nombre": "Item", "precio": 100}
```

**Incorrecto:**
```json
{nombre: "Item", precio: 100}  // Faltan comillas
{"nombre": 'Item', "precio": 100}  // Comillas simples
```

---

## 🚀 Flujo de Actualización (Producción)

### **Escenario: Cambiar Precios en Vivo**

1. **Adminstra edita `data.json`** (en la carpeta del bot)
   ```
   C:\Users\...\latinoland-bot\data.json
   ```

2. **Ejecuta `/reload` en Discord**
   - El bot recarga datos inmediatamente
   - No hay reinicio necesario

3. **Los cambios se reflejan en todos los comandos**
   - `/comprar` — muestra nuevos precios
   - `/dinos` — muestra precios actualizados
   - etc.

4. **Opcional: Sincronizar cambios a GitHub**
   ```bash
   git add data.json
   git commit -m "Update prices"
   git push origin main
   ```
   - Esto actualiza el repo de respaldo
   - Replit se sincroniza automáticamente

---

## 📊 Sincronización con el Sitio Web (Futuro)

**Plan para fase siguiente:**

1. Agregar botón **"Exportar a JSON"** en `google_sites_version.html`
2. El sitio genera `data.json` con los datos actuales
3. Descargar y reemplazar el `data.json` del bot
4. Ejecutar `/reload`

**Ejemplo de exportación (JavaScript en HTML):**
```javascript
function exportData() {
  const data = {
    shop_items: SHOP_ITEMS,
    sell_items: SELL_ITEMS,
    dinos: DINOS,
    dinos_abyssal: DINOS_ABYSSAL,
    vips: VIPS,
    packs: PACKS
  };
  
  const json = JSON.stringify(data, null, 2);
  const blob = new Blob([json], {type: "application/json"});
  const url = URL.createObjectURL(blob);
  
  const a = document.createElement("a");
  a.href = url;
  a.download = "data.json";
  a.click();
}
```

---

## ⚙️ Configuración Avanzada

### **Cambiar Ubicación de `data.json`**

Por defecto, el bot busca `data.json` en la misma carpeta que `bot.py`:
```python
data_path = os.path.join(os.path.dirname(__file__), 'data.json')
```

Para usar una ruta diferente, modifica `cargar_datos()`:
```python
# Ejemplo: usar desde carpeta 'data/'
data_path = os.path.join(os.path.dirname(__file__), 'data', 'data.json')
```

### **Fallback Automático**

Si `data.json` no existe o está dañado, el bot usa datos por defecto (hardcoded en el código). **Esto asegura que el bot siempre funcione**, incluso si hay un problema con el archivo.

```python
logger.warning(f"⚠️ data.json no encontrado. Usando datos por defecto.")
```

---

## 🐛 Troubleshooting

| Problema | Solución |
|----------|----------|
| `/reload` retorna error | Valida la sintaxis JSON en jsonlint.com |
| Los datos no se actualizan | Asegúrate de estar en admin, ejecuta `/reload` nuevamente |
| data.json no se encuentra | Coloca el archivo en la misma carpeta que `bot.py` |
| Bot no inicia | Revisa `bot.log` para ver el error exacto |
| Cambios en data.json pero no se reflejan | Necesitas ejecutar `/reload` después de editar |

---

## 📚 Archivos Relacionados

- `bot.py` — Bot principal con función `cargar_datos()`
- `data.json` — Archivo de datos sincronizado
- `bot.log` — Log con detalles de carga de datos
- `UX_IMPROVEMENTS.md` — Documentación de mejoras UX

---

## ✅ Checklist de Implementación

- [x] Crear función `cargar_datos()` en bot.py
- [x] Crear archivo `data.json` con estructura completa
- [x] Agregar comando `/reload` (admin-only)
- [x] Agregar manejo de errores y fallback
- [x] Actualizar logs para registrar cargas
- [x] Documentar el sistema
- [ ] Agregar exportación desde sitio web (fase siguiente)
- [ ] Implementar sincronización automática con Replit (fase siguiente)

---

**Versión:** 1.1.0 - Dynamic Data Sync  
**Fecha:** Noviembre 12, 2025  
**Estado:** ✅ Listo para Producción
