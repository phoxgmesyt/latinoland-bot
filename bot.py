import discord
from discord.ext import commands
from discord import app_commands, ui
import json
from typing import Optional
import os
from dotenv import load_dotenv
import logging
from datetime import datetime, timezone

# --- logging setup ---
logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(os.path.dirname(__file__), 'bot.log'),
    filemode='a',
    format='[%(asctime)s] [%(levelname)s] %(name)s: %(message)s'
)
logger = logging.getLogger('latinoland-bot')

# record start time
START_TIME = datetime.now(timezone.utc)

# Cargar variables de entorno
load_dotenv()

# Opcional: sincronizar comandos por GUILD_ID para pruebas (aparecen instantáneamente)
GUILD_ID = os.getenv("GUILD_ID")

# Crear bot con intents
intents = discord.Intents.default()
# No activar 'message_content' (privileged intent) porque este bot usa comandos slash.
# Si necesitas procesar mensajes de texto (mensajes normales), habilita Message Content
# en Discord Developer Portal o cambia a "intents.message_content = True" y habilítalo allí.
intents.message_content = False
bot = commands.Bot(command_prefix="l!", intents=intents)

# Color para embeds
EMBED_COLOR = discord.Color.from_rgb(0, 245, 255)  # Cyan (color del tema LATINOLAND)

# =====================================================
# CARGADOR DE DATOS DINÁMICOS (desde data.json)
# =====================================================

def cargar_datos():
    """Carga todos los datos desde data.json. Si falla, usa datos por defecto."""
    data_path = os.path.join(os.path.dirname(__file__), 'data.json')
    
    # Datos por defecto (fallback si no existe data.json)
    defaults = {
        "SHOP_ITEMS": [
            {"id": "01", "nombre": "Runestone", "tipo": "item", "descripcion": "Piedra runica", "nivel": "-", "precio": 200, "comando": "/buy Runestone", "cantidad": 1},
            {"id": "02", "nombre": "tools", "tipo": "item", "descripcion": "Pico y hacha metal", "nivel": "-", "precio": 500, "comando": "/buy tools", "cantidad": 1},
            {"id": "03", "nombre": "Aqualyrium", "tipo": "item", "descripcion": "Aqualyrium", "nivel": "-", "precio": 9999, "comando": "/buy Aqualyrium", "cantidad": 25},
            {"id": "04", "nombre": "Barnacle", "tipo": "item", "descripcion": "Barnacle", "nivel": "-", "precio": 9999, "comando": "/buy Barnacle", "cantidad": 50},
            {"id": "05", "nombre": "Wood", "tipo": "item", "descripcion": "Crystallized Wood", "nivel": "-", "precio": 9999, "comando": "/buy Wood", "cantidad": 50},
            {"id": "06", "nombre": "Fish", "tipo": "item", "descripcion": "Fish Scale", "nivel": "-", "precio": 9999, "comando": "/buy Fish", "cantidad": 50},
            {"id": "07", "nombre": "HardenedSteelIngot", "tipo": "item", "descripcion": "Hardened Steel Ingot", "nivel": "-", "precio": 9999, "comando": "/buy HardenedSteelIngot", "cantidad": 50},
            {"id": "08", "nombre": "Seaweed", "tipo": "item", "descripcion": "Seaweed", "nivel": "-", "precio": 5000, "comando": "/buy Seaweed", "cantidad": 50},
            {"id": "09", "nombre": "Manganese", "tipo": "item", "descripcion": "Manganese", "nivel": "-", "precio": 5000, "comando": "/buy Manganese", "cantidad": 50}
        ],
        "SELL_ITEMS": [
            {"id": "10", "nombre": "rex", "tipo": "item", "descripcion": "Trofeo cabeza de rex", "precio": 50, "comando": "/sell rex"},
            {"id": "12", "nombre": "dragon", "tipo": "item", "descripcion": "Trofeo dragon en gamma", "precio": 4000, "comando": "/sell dragon"},
            {"id": "15", "nombre": "argy", "tipo": "item", "descripcion": "Argentavis Talon", "precio": 50, "comando": "/sell argy"},
            {"id": "100", "nombre": "arana", "tipo": "item", "descripcion": "Trofeo araña en gamma", "precio": 3000, "comando": "/sell arana"},
            {"id": "101", "nombre": "mono", "tipo": "item", "descripcion": "Trofeo mono en gamma", "precio": 3000, "comando": "/sell mono"},
            {"id": "102", "nombre": "allo", "tipo": "item", "descripcion": "Cerebro de Allosaurus", "precio": 50, "comando": "/sell allo"},
            {"id": "103", "nombre": "basil", "tipo": "item", "descripcion": "Grasa Basilosaurus", "precio": 150, "comando": "/sell basil"},
            {"id": "104", "nombre": "giga", "tipo": "item", "descripcion": "Corazon Giganotosaurus", "precio": 300, "comando": "/sell giga"},
            {"id": "105", "nombre": "megal", "tipo": "item", "descripcion": "Diente Megalodon", "precio": 50, "comando": "/sell megal"}
        ],
        "DINOS": [
            {"id": "50", "nombre": "Carbonemys", "tipo": "dino", "descripcion": "(P/stats)", "nivel": 1, "precio": 1500, "comando": "/buy bcarb"},
            {"id": "51", "nombre": "Daeodon", "tipo": "dino", "descripcion": "Crianza", "nivel": 300, "precio": 36000, "comando": "/buy daeodon"},
            {"id": "55", "nombre": "Giganotosaurus", "tipo": "dino", "descripcion": "Crianza", "nivel": 300, "precio": 80000, "comando": "/buy giga"},
            {"id": "57", "nombre": "Grifo", "tipo": "dino", "descripcion": "Crianza", "nivel": 300, "precio": 36000, "comando": "/buy griffin"},
            {"id": "60", "nombre": "Mosasaurus", "tipo": "dino", "descripcion": "Crianza", "nivel": 300, "precio": 56000, "comando": "/buy mosa"},
            {"id": "63", "nombre": "Rex", "tipo": "dino", "descripcion": "Crianza", "nivel": 300, "precio": 54000, "comando": "/buy rex"},
            {"id": "65", "nombre": "Stegosaurus", "tipo": "dino", "descripcion": "Crianza", "nivel": 300, "precio": 38000, "comando": "/buy stego"},
            {"id": "67", "nombre": "Therizinosaurus", "tipo": "dino", "descripcion": "Crianza", "nivel": 300, "precio": 42000, "comando": "/buy theri"},
            {"id": "79", "nombre": "Basilisco", "tipo": "dino", "descripcion": "Crianza", "nivel": 300, "precio": 45000, "comando": "/buy basilisk"},
            {"id": "106", "nombre": "Reaper", "tipo": "dino", "descripcion": "Crianza", "nivel": 300, "precio": 75000, "comando": "/buy reaper"},
        ],
        "DINOS_ABYSSAL": [
            {"id": "128", "nombre": "Abyssal Ankylosaurus", "tipo": "dino", "descripcion": "Abyssal", "nivel": 300, "precio": 180000, "comando": "/buy abyssal_ankylosaurus"},
            {"id": "129", "nombre": "Abyssal Moschops", "tipo": "dino", "descripcion": "Abyssal", "nivel": 300, "precio": 140000, "comando": "/buy abyssal_moschops"},
            {"id": "130", "nombre": "Abyssal Procoptodon", "tipo": "dino", "descripcion": "Abyssal", "nivel": 300, "precio": 120000, "comando": "/buy abyssal_procoptodon"},
            {"id": "131", "nombre": "Abyssal Stegosaurio", "tipo": "dino", "descripcion": "Abyssal", "nivel": 300, "precio": 160000, "comando": "/buy abyssal_stegosaurio"},
            {"id": "132", "nombre": "Abyssal Therizinosaur", "tipo": "dino", "descripcion": "Abyssal", "nivel": 300, "precio": 200000, "comando": "/buy abyssal_therizinosaur"},
            {"id": "133", "nombre": "Abyssal Thylacoleo", "tipo": "dino", "descripcion": "Abyssal", "nivel": 300, "precio": 190000, "comando": "/buy abyssal_thylacoleo"}
        ],
        "VIPS": [
            {"nombre": "VIP1", "tipo": "vip", "descripcion": "🔹250 puntos cada 10 minutos\n🔹Comandos-ark exclusivos\n🔹Rol exclusivo en Discord y Ark\n🔹Bonus extra x1 en sorteos", "precio": "$10", "duracion": "15 días"},
            {"nombre": "VIP2", "tipo": "vip", "descripcion": "🔸350 puntos cada 10 minutos\n🔸Comandos-ark exclusivos\n🔸Rol exclusivo en Discord y Ark\n🔸Bonus extra x2 en sorteos", "precio": "$20", "duracion": "15 días"},
            {"nombre": "VIP3", "tipo": "vip", "descripcion": "🔺450 puntos cada 10 minutos\n🔺Comandos-ark exclusivos\n🔺Rol exclusivo en Discord y Ark\n🔺Bonus extra x3 en sorteos", "precio": "$30", "duracion": "15 días"}
        ],
        "PACKS": [
            {"nombre": "PACK1", "tipo": "pack", "descripcion": "🔹175.000 puntos + VIP1", "precio": "$15"},
            {"nombre": "PACK2", "tipo": "pack", "descripcion": "🔸300.000 puntos + VIP2", "precio": "$25"},
            {"nombre": "PACK3", "tipo": "pack", "descripcion": "🔺425.000 puntos + VIP3", "precio": "$35"}
        ]
    }
    
    try:
        if os.path.exists(data_path):
            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logger.info(f"✅ Datos cargados desde {data_path}")
            return {
                "SHOP_ITEMS": data.get("shop_items", defaults["SHOP_ITEMS"]),
                "SELL_ITEMS": data.get("sell_items", defaults["SELL_ITEMS"]),
                "DINOS": data.get("dinos", defaults["DINOS"]),
                "DINOS_ABYSSAL": data.get("dinos_abyssal", defaults["DINOS_ABYSSAL"]),
                "VIPS": data.get("vips", defaults["VIPS"]),
                "PACKS": data.get("packs", defaults["PACKS"])
            }
        else:
            logger.warning(f"⚠️ data.json no encontrado en {data_path}. Usando datos por defecto.")
            return {
                "SHOP_ITEMS": defaults["SHOP_ITEMS"],
                "SELL_ITEMS": defaults["SELL_ITEMS"],
                "DINOS": defaults["DINOS"],
                "DINOS_ABYSSAL": defaults["DINOS_ABYSSAL"],
                "VIPS": defaults["VIPS"],
                "PACKS": defaults["PACKS"]
            }
    except Exception as e:
        logger.error(f"❌ Error al cargar data.json: {e}")
        return {
            "SHOP_ITEMS": defaults["SHOP_ITEMS"],
            "SELL_ITEMS": defaults["SELL_ITEMS"],
            "DINOS": defaults["DINOS"],
            "DINOS_ABYSSAL": defaults["DINOS_ABYSSAL"],
            "VIPS": defaults["VIPS"],
            "PACKS": defaults["PACKS"]
        }

# Cargar datos al iniciar
_datos = cargar_datos()
SHOP_ITEMS = _datos["SHOP_ITEMS"]
SELL_ITEMS = _datos["SELL_ITEMS"]
DINOS = _datos["DINOS"]
DINOS_ABYSSAL = _datos["DINOS_ABYSSAL"]
VIPS = _datos["VIPS"]
PACKS = _datos["PACKS"]

# =====================================================
# FUNCIONES AUXILIARES
# =====================================================

def crear_embed_items(items: list, titulo: str, usar_paginas: bool = False) -> list:
    """Crea embeds con items. Si son muchos, los divide en paginas."""
    embeds = []
    
    if not usar_paginas or len(items) <= 10:
        # Un solo embed
        embed = discord.Embed(title=titulo, color=EMBED_COLOR)
        for item in items[:10]:
            if isinstance(item, dict):
                nombre = item.get("nombre", "Desconocido")
                descripcion = item.get("descripcion", "")
                precio = item.get("precio", "N/A")
                comando = item.get("comando", "")
                
                valor = f"**Precio:** {precio} pts\n**Comando:** `{comando}`\n{descripcion}"
                embed.add_field(name=nombre, value=valor, inline=False)
        
        embeds.append(embed)
    else:
        # Múltiples páginas (10 items por página)
        for i in range(0, len(items), 10):
            pagina = items[i:i+10]
            page_num = (i // 10) + 1
            total_pages = (len(items) + 9) // 10
            embed = discord.Embed(
                title=f"{titulo}",
                color=EMBED_COLOR,
                description=f"**Página {page_num} de {total_pages}**"
            )
            
            for item in pagina:
                if isinstance(item, dict):
                    nombre = item.get("nombre", "Desconocido")
                    descripcion = item.get("descripcion", "")
                    precio = item.get("precio", "N/A")
                    comando = item.get("comando", "")
                    
                    valor = f"**Precio:** {precio} pts\n**Comando:** `{comando}`\n{descripcion}"
                    embed.add_field(name=nombre, value=valor, inline=False)
            
            embeds.append(embed)
    
    return embeds

# =====================================================
# VISTAS INTERACTIVAS (Buttons, Select Menus)
# =====================================================

class PaginationView(ui.View):
    """Vista con botones para navegar entre páginas."""
    def __init__(self, embeds: list, timeout=300):
        super().__init__(timeout=timeout)
        self.embeds = embeds
        self.current_page = 0
        self.update_buttons()
    
    def update_buttons(self):
        """Actualiza el estado de los botones según la página actual."""
        self.previous_button.disabled = (self.current_page == 0)
        self.next_button.disabled = (self.current_page == len(self.embeds) - 1)
        
        if len(self.embeds) <= 1:
            self.previous_button.disabled = True
            self.next_button.disabled = True
    
    @ui.button(label="⬅️ Anterior", style=discord.ButtonStyle.blurple)
    async def previous_button(self, interaction: discord.Interaction, button: ui.Button):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_buttons()
            await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)
        else:
            await interaction.response.defer()
    
    @ui.button(label="Siguiente ➡️", style=discord.ButtonStyle.blurple)
    async def next_button(self, interaction: discord.Interaction, button: ui.Button):
        if self.current_page < len(self.embeds) - 1:
            self.current_page += 1
            self.update_buttons()
            await interaction.response.edit_message(embed=self.embeds[self.current_page], view=self)
        else:
            await interaction.response.defer()


class DinoFilterSelect(ui.Select):
    """Select menu para filtrar dinos por tipo."""
    def __init__(self):
        options = [
            discord.SelectOption(label="Todos los Dinos", value="todos", emoji="🦕"),
            discord.SelectOption(label="Normales (Crianza)", value="normal", emoji="🥚"),
            discord.SelectOption(label="Abyssal", value="abyssal", emoji="⚫"),
        ]
        super().__init__(
            placeholder="Selecciona el tipo de dino...",
            min_values=1,
            max_values=1,
            options=options
        )
    
    async def callback(self, interaction: discord.Interaction):
        """Manejador del select."""
        filter_type = self.values[0]
        
        if filter_type == "todos":
            items = DINOS + DINOS_ABYSSAL
            titulo = "🦕 DINOS - Todos Disponibles"
        elif filter_type == "normal":
            items = [d for d in DINOS if d.get("descripcion") != "Abyssal"]
            titulo = "🥚 DINOS - Normales (Crianza)"
        elif filter_type == "abyssal":
            items = DINOS_ABYSSAL
            titulo = "⚫ DINOS ABYSSAL"
        
        embeds = crear_embed_items(items, titulo, usar_paginas=True)
        view = PaginationView(embeds)
        
        await interaction.response.edit_message(embeds=[embeds[0]], view=view)


class DinoFilterView(ui.View):
    """Vista que contiene el select para filtrar dinos."""
    def __init__(self):
        super().__init__(timeout=300)
        self.add_item(DinoFilterSelect())


@bot.event
async def on_ready():
    """Se ejecuta cuando el bot se conecta exitosamente."""
    print(f"✅ Bot conectado como {bot.user}")
    print(f"🎮 LATINOLAND ARK Bot listo")
    logger.info(f"Bot conectado como {bot.user}")
    logger.info("LATINOLAND ARK Bot listo")
    try:
        if GUILD_ID:
            # Sincroniza solo en el guild de pruebas (aparece instantáneo)
            guild_obj = discord.Object(id=int(GUILD_ID))
            synced = await bot.tree.sync(guild=guild_obj)
            print(f"📝 {len(synced)} comandos sincronizados en guild {GUILD_ID}")
            logger.info(f"{len(synced)} comandos sincronizados en guild {GUILD_ID}")
        else:
            synced = await bot.tree.sync()
            print(f"📝 {len(synced)} comandos sincronizados con Discord (global)")
            logger.info(f"{len(synced)} comandos sincronizados con Discord (global)")
    except Exception as e:
        print(f"❌ Error al sincronizar comandos: {e}")
        logger.exception(f"Error al sincronizar comandos: {e}")

# =====================================================
# COMANDOS SLASH
# =====================================================

@bot.tree.command(name="comprar", description="Muestra los items disponibles para comprar")
async def comprar(interaction: discord.Interaction):
    """Comando para mostrar items de compra."""
    logger.info(f"/comprar invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)})")
    embeds = crear_embed_items(SHOP_ITEMS, "🛒 SHOP - Comprar Items", usar_paginas=True)
    
    if embeds:
        view = PaginationView(embeds)
        await interaction.response.send_message(embed=embeds[0], view=view)
    else:
        await interaction.response.send_message("❌ No hay items disponibles", ephemeral=True)
        logger.info("/comprar returned no items")

@bot.tree.command(name="vender", description="Muestra los items disponibles para vender")
async def vender(interaction: discord.Interaction):
    """Comando para mostrar items de venta."""
    logger.info(f"/vender invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)})")
    embeds = crear_embed_items(SELL_ITEMS, "💰 VENDER - Items", usar_paginas=True)
    
    if embeds:
        view = PaginationView(embeds)
        await interaction.response.send_message(embed=embeds[0], view=view)
    else:
        await interaction.response.send_message("❌ No hay items para vender", ephemeral=True)
        logger.info("/vender returned no items")

@bot.tree.command(name="dinos", description="Muestra los dinosaurios disponibles para comprar (con filtros)")
async def dinos_cmd(interaction: discord.Interaction):
    """Comando para mostrar dinos con filtro."""
    logger.info(f"/dinos invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)})")
    todos_dinos = DINOS + DINOS_ABYSSAL
    embeds = crear_embed_items(todos_dinos, "🦕 DINOS - Todos Disponibles", usar_paginas=True)
    
    if embeds:
        view = DinoFilterView()
        pagination = PaginationView(embeds)
        
        # Combinar ambas vistas
        for item in pagination.children:
            view.add_item(item)
        
        await interaction.response.send_message(embed=embeds[0], view=view)
    else:
        await interaction.response.send_message("❌ No hay dinos disponibles", ephemeral=True)
        logger.info("/dinos returned no dinos")

@bot.tree.command(name="crianza", description="Muestra los dinos de crianza (P/stats)")
async def crianza_cmd(interaction: discord.Interaction):
    """Comando para mostrar dinos de crianza."""
    dinos_crianza = [d for d in DINOS if "(P/stats)" in d.get("descripcion", "")]
    logger.info(f"/crianza invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)})")
    embeds = crear_embed_items(dinos_crianza, "🥚 CRIANZA - Dinos P/Stats", usar_paginas=False)
    
    if embeds:
        await interaction.response.send_message(embeds=embeds)
    else:
        await interaction.response.send_message("❌ No hay dinos de crianza", ephemeral=True)
        logger.info("/crianza returned no dinos")

@bot.tree.command(name="abyssal", description="Muestra los dinos Abyssal")
async def abyssal_cmd(interaction: discord.Interaction):
    """Comando para mostrar dinos abyssal."""
    logger.info(f"/abyssal invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)})")
    embeds = crear_embed_items(DINOS_ABYSSAL, "⚫ DINOS ABYSSAL", usar_paginas=True)
    
    if embeds:
        view = PaginationView(embeds)
        await interaction.response.send_message(embed=embeds[0], view=view)
    else:
        await interaction.response.send_message("❌ No hay dinos abyssal", ephemeral=True)
        logger.info("/abyssal returned no dinos")

@bot.tree.command(name="vips", description="Muestra los paquetes VIP disponibles")
async def vips_cmd(interaction: discord.Interaction):
    """Comando para mostrar paquetes VIP."""
    embed = discord.Embed(title="👑 VIP - Paquetes Disponibles", color=EMBED_COLOR)
    
    logger.info(f"/vips invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)})")
    for vip in VIPS:
        nombre = vip.get("nombre", "VIP")
        descripcion = vip.get("descripcion", "")
        precio = vip.get("precio", "N/A")
        duracion = vip.get("duracion", "")
        
        valor = f"**Precio:** {precio}\n**Duración:** {duracion}\n\n{descripcion}"
        embed.add_field(name=nombre, value=valor, inline=False)
    
    embed.set_footer(text="💳 Compra en Discord o contacta a los admins")
    await interaction.response.send_message(embed=embed)
    logger.info("/vips sent embed")

@bot.tree.command(name="packs", description="Muestra los packs de compra disponibles")
async def packs_cmd(interaction: discord.Interaction):
    """Comando para mostrar packs."""
    embed = discord.Embed(title="📦 PACKS - Ofertas Especiales", color=EMBED_COLOR)
    
    logger.info(f"/packs invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)})")
    for pack in PACKS:
        nombre = pack.get("nombre", "PACK")
        descripcion = pack.get("descripcion", "")
        precio = pack.get("precio", "N/A")
        
        valor = f"**Precio:** {precio}\n{descripcion}"
        embed.add_field(name=nombre, value=valor, inline=False)
    
    embed.set_footer(text="💳 Compra en Discord o contacta a los admins")
    await interaction.response.send_message(embed=embed)
    logger.info("/packs sent embed")

@bot.tree.command(name="servidor", description="Información del servidor ARK LATINOLAND")
async def servidor_cmd(interaction: discord.Interaction):
    """Comando para mostrar información del servidor."""
    embed = discord.Embed(
        title="🌋 LATINOLAND ARK - SERVIDOR PVE",
        description="Bienvenido al servidor LATINOLAND. Un lugar para forjar alianzas, conquistar territorios y vivir aventuras sin fin.",
        color=EMBED_COLOR
    )
    
    embed.add_field(
        name="📍 Conexión Steam",
        value="```\nsteam://connect/216.245.177.39:27051\n```",
        inline=False
    )
    
    embed.add_field(
        name="📍 IP Epic Games",
        value="```\n216.245.177.39:27051\n```",
        inline=False
    )
    
    embed.add_field(
        name="💬 Comunidad",
        value="[Únete a nuestro Discord](https://discord.gg/WAnqWz9RQ5)",
        inline=False
    )
    
    embed.add_field(
        name="🌐 Web",
        value="Visita el sitio web para más info",
        inline=False
    )
    
    embed.set_footer(text="¡Nos vemos en el servidor! 🎮")
    await interaction.response.send_message(embed=embed)
    logger.info(f"/servidor invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)})")

@bot.tree.command(name="ayuda", description="Muestra la lista de comandos disponibles")
async def ayuda_cmd(interaction: discord.Interaction):
    """Comando de ayuda."""
    embed = discord.Embed(
        title="❓ AYUDA - Comandos Disponibles",
        description="Lista de todos los comandos del bot LATINOLAND ARK",
        color=EMBED_COLOR
    )
    
    embed.add_field(
        name="/comprar",
        value="Muestra todos los items disponibles para comprar",
        inline=False
    )
    embed.add_field(
        name="/vender",
        value="Muestra todos los items disponibles para vender",
        inline=False
    )
    embed.add_field(
        name="/dinos",
        value="Muestra todos los dinosaurios disponibles con filtros",
        inline=False
    )
    embed.add_field(
        name="/crianza",
        value="Muestra dinos de crianza (P/stats)",
        inline=False
    )
    embed.add_field(
        name="/abyssal",
        value="Muestra dinos Abyssal especiales",
        inline=False
    )
    embed.add_field(
        name="/vips",
        value="Muestra los paquetes VIP disponibles",
        inline=False
    )
    embed.add_field(
        name="/packs",
        value="Muestra los packs especiales",
        inline=False
    )
    embed.add_field(
        name="/servidor",
        value="Muestra información de conexión del servidor",
        inline=False
    )
    embed.add_field(
        name="/status",
        value="Muestra el estado y uptime del bot",
        inline=False
    )
    embed.add_field(
        name="/reload",
        value="[ADMIN] Recarga los datos desde `data.json`",
        inline=False
    )
    
    embed.set_footer(text="Usa / para ver todos los comandos disponibles")
    await interaction.response.send_message(embed=embed)
    logger.info(f"/ayuda invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)})")


@bot.tree.command(name="status", description="Muestra el estado y uptime del bot")
async def status_cmd(interaction: discord.Interaction):
    """Comando para mostrar uptime y estado del bot."""
    now = datetime.now(timezone.utc)
    uptime = now - START_TIME
    hours, remainder = divmod(int(uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    text = f"Uptime: {hours}h {minutes}m {seconds}s\nStarted (UTC): {START_TIME.isoformat()}"
    embed = discord.Embed(title="🟢 STATUS - Bot", description=text, color=EMBED_COLOR)
    embed.set_footer(text="LATINOLAND ARK Bot")
    await interaction.response.send_message(embed=embed)
    logger.info(f"/status invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)}) - uptime {hours}:{minutes}:{seconds}")

@bot.tree.command(name="reload", description="[ADMIN] Recarga los datos desde data.json")
async def reload_cmd(interaction: discord.Interaction):
    """Comando para recargar los datos desde data.json. Solo para administradores."""
    # Verificar si el usuario es administrador
    if not interaction.user.guild_permissions.administrator:
        embed = discord.Embed(
            title="❌ Permiso Denegado",
            description="Solo los administradores pueden usar este comando.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        logger.warning(f"/reload invoked by non-admin {interaction.user} - access denied")
        return
    
    try:
        await interaction.response.defer()
        
        # Recargar datos
        global SHOP_ITEMS, SELL_ITEMS, DINOS, DINOS_ABYSSAL, VIPS, PACKS
        _datos = cargar_datos()
        SHOP_ITEMS = _datos["SHOP_ITEMS"]
        SELL_ITEMS = _datos["SELL_ITEMS"]
        DINOS = _datos["DINOS"]
        DINOS_ABYSSAL = _datos["DINOS_ABYSSAL"]
        VIPS = _datos["VIPS"]
        PACKS = _datos["PACKS"]
        
        embed = discord.Embed(
            title="✅ Datos Recargados",
            description=f"Se han recargado correctamente los datos desde `data.json`\n\n"
                        f"📋 Items para comprar: {len(SHOP_ITEMS)}\n"
                        f"💰 Items para vender: {len(SELL_ITEMS)}\n"
                        f"🦕 Dinos normales: {len(DINOS)}\n"
                        f"⚫ Dinos Abyssal: {len(DINOS_ABYSSAL)}\n"
                        f"👑 Paquetes VIP: {len(VIPS)}\n"
                        f"📦 Ofertas especiales: {len(PACKS)}",
            color=discord.Color.green()
        )
        embed.set_footer(text="Los cambios están disponibles inmediatamente")
        
        await interaction.followup.send(embed=embed)
        logger.info(f"/reload executed by {interaction.user} - data reloaded successfully")
        
    except Exception as e:
        logger.error(f"Error en /reload: {e}")
        embed = discord.Embed(
            title="❌ Error al Recargar",
            description=f"Ocurrió un error al recargar los datos:\n```{str(e)}```",
            color=discord.Color.red()
        )
        await interaction.followup.send(embed=embed)


# =====================================================
# INICIAR BOT
# =====================================================

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")

    # Sanitize token (remove accidental surrounding quotes, whitespace or "Bot " prefix)
    if TOKEN:
        TOKEN = TOKEN.strip()
        if TOKEN.startswith('"') and TOKEN.endswith('"'):
            TOKEN = TOKEN[1:-1]
        if TOKEN.startswith("Bot "):
            # Some users paste the header-style token 'Bot <token>' by mistake
            TOKEN = TOKEN.split(" ", 1)[1]

    if not TOKEN:
        print("❌ ERROR: No se encontró DISCORD_TOKEN en las variables de entorno")
        print("Por favor, añade tu token en .env local o en las Secrets/Environment del hosting (DISCORD_TOKEN)")
        exit(1)

    # Basic validation to give a clearer error message before discord.py raises
    if len(TOKEN) < 40:
        masked = TOKEN[:6] + "..." + TOKEN[-6:] if len(TOKEN) > 12 else TOKEN
        print(f"❌ ERROR: El token parece inválido o está incompleto: {masked}")
        print("-> Asegúrate de pegar el Bot Token (no el Client Secret), y sin comillas ni prefijo 'Bot '")
        print("-> Si no funciona, genera uno nuevo en Discord Developer Portal -> Bot -> Reset Token")
        exit(1)
    
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"❌ Error al iniciar el bot: {e}")
