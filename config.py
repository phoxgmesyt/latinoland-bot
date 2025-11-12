# config.py - Configuración centralizada del bot

# =====================================================
# INFORMACIÓN DEL SERVIDOR
# =====================================================

SERVER_NAME = "LATINOLAND ARK"
SERVER_IP = "216.245.177.39"
SERVER_PORT = "27051"
DISCORD_INVITE = "https://discord.gg/WAnqWz9RQ5"

# Colores para embeds (RGB)
# Colores predefinidos:
COLORS = {
    "cyan": (0, 245, 255),      # Color principal LATINOLAND
    "magenta": (255, 0, 255),
    "rojo": (255, 0, 0),
    "verde": (0, 255, 0),
    "azul": (0, 0, 255),
    "amarillo": (255, 255, 0),
    "naranja": (255, 165, 0),
}

# Color por defecto para embeds
DEFAULT_COLOR = COLORS["cyan"]

# =====================================================
# CONFIGURACIÓN DE EMBEDS
# =====================================================

# Mostrar footer con el nombre del servidor en cada embed
SHOW_FOOTER = True

# Footer personalizado
FOOTER_TEXT = "LATINOLAND ARK - Servidor PVE"

# Icono del footer (URL)
FOOTER_ICON = None  # O: "https://example.com/logo.png"

# =====================================================
# PAGINACIÓN
# =====================================================

# Items por página
ITEMS_PER_PAGE = 10

# Mostrar ID de item
SHOW_ITEM_ID = True

# =====================================================
# FORMATEO DE PRECIOS
# =====================================================

# Símbolo de moneda
CURRENCY_SYMBOL = "pts"  # "pts", "coins", "$", etc.

# Formato: "{price} {symbol}"
PRICE_FORMAT = "{price} {symbol}"

# =====================================================
# MENSAJES PERSONALIZADOS
# =====================================================

MESSAGES = {
    "no_items": "❌ No hay items disponibles",
    "no_dinos": "❌ No hay dinos disponibles",
    "no_vips": "❌ No hay paquetes VIP disponibles",
    "no_packs": "❌ No hay packs disponibles",
    "welcome": "👋 Bienvenido al Bot LATINOLAND ARK",
    "error": "❌ Ocurrió un error",
}

# =====================================================
# LOGGING
# =====================================================

# Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL = "INFO"

# Guardar logs en archivo
LOG_TO_FILE = True
LOG_FILE = "bot.log"
