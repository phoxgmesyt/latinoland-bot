import discord
from discord.ext import commands
from discord import app_commands
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
# DATOS DEL SERVIDOR ARK (desde google_sites_version.html)
# =====================================================

SHOP_ITEMS = [
    {"id": "01", "nombre": "Runestone", "tipo": "item", "descripcion": "Piedra runica", "nivel": "-", "precio": 200, "comando": "/buy Runestone", "cantidad": 1},
    {"id": "02", "nombre": "tools", "tipo": "item", "descripcion": "Pico y hacha metal", "nivel": "-", "precio": 500, "comando": "/buy tools", "cantidad": 1},
    {"id": "03", "nombre": "Aqualyrium", "tipo": "item", "descripcion": "Aqualyrium", "nivel": "-", "precio": 9999, "comando": "/buy Aqualyrium", "cantidad": 25},
    {"id": "04", "nombre": "Barnacle", "tipo": "item", "descripcion": "Barnacle", "nivel": "-", "precio": 9999, "comando": "/buy Barnacle", "cantidad": 50},
    {"id": "05", "nombre": "Wood", "tipo": "item", "descripcion": "Crystallized Wood", "nivel": "-", "precio": 9999, "comando": "/buy Wood", "cantidad": 50},
    {"id": "06", "nombre": "Fish", "tipo": "item", "descripcion": "Fish Scale", "nivel": "-", "precio": 9999, "comando": "/buy Fish", "cantidad": 50},
    {"id": "07", "nombre": "HardenedSteelIngot", "tipo": "item", "descripcion": "Hardened Steel Ingot", "nivel": "-", "precio": 9999, "comando": "/buy HardenedSteelIngot", "cantidad": 50},
    {"id": "08", "nombre": "Seaweed", "tipo": "item", "descripcion": "Seaweed", "nivel": "-", "precio": 5000, "comando": "/buy Seaweed", "cantidad": 50},
    {"id": "09", "nombre": "Manganese", "tipo": "item", "descripcion": "Manganese", "nivel": "-", "precio": 5000, "comando": "/buy Manganese", "cantidad": 50}
]

SELL_ITEMS = [
    {"id": "10", "nombre": "rex", "tipo": "item", "descripcion": "Trofeo cabeza de rex", "precio": 50, "comando": "/sell rex"},
    {"id": "12", "nombre": "dragon", "tipo": "item", "descripcion": "Trofeo dragon en gamma", "precio": 4000, "comando": "/sell dragon"},
    {"id": "15", "nombre": "argy", "tipo": "item", "descripcion": "Argentavis Talon", "precio": 50, "comando": "/sell argy"},
    {"id": "100", "nombre": "arana", "tipo": "item", "descripcion": "Trofeo araña en gamma", "precio": 3000, "comando": "/sell arana"},
    {"id": "101", "nombre": "mono", "tipo": "item", "descripcion": "Trofeo mono en gamma", "precio": 3000, "comando": "/sell mono"},
    {"id": "102", "nombre": "allo", "tipo": "item", "descripcion": "Cerebro de Allosaurus", "precio": 50, "comando": "/sell allo"},
    {"id": "103", "nombre": "basil", "tipo": "item", "descripcion": "Grasa Basilosaurus", "precio": 150, "comando": "/sell basil"},
    {"id": "104", "nombre": "giga", "tipo": "item", "descripcion": "Corazon Giganotosaurus", "precio": 300, "comando": "/sell giga"},
    {"id": "105", "nombre": "megal", "tipo": "item", "descripcion": "Diente Megalodon", "precio": 50, "comando": "/sell megal"}
]

DINOS = [
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
]

DINOS_ABYSSAL = [
    {"id": "128", "nombre": "Abyssal Ankylosaurus", "tipo": "dino", "descripcion": "Abyssal", "nivel": 300, "precio": 180000, "comando": "/buy abyssal_ankylosaurus"},
    {"id": "129", "nombre": "Abyssal Moschops", "tipo": "dino", "descripcion": "Abyssal", "nivel": 300, "precio": 140000, "comando": "/buy abyssal_moschops"},
    {"id": "130", "nombre": "Abyssal Procoptodon", "tipo": "dino", "descripcion": "Abyssal", "nivel": 300, "precio": 120000, "comando": "/buy abyssal_procoptodon"},
    {"id": "131", "nombre": "Abyssal Stegosaurio", "tipo": "dino", "descripcion": "Abyssal", "nivel": 300, "precio": 160000, "comando": "/buy abyssal_stegosaurio"},
    {"id": "132", "nombre": "Abyssal Therizinosaur", "tipo": "dino", "descripcion": "Abyssal", "nivel": 300, "precio": 200000, "comando": "/buy abyssal_therizinosaur"},
    {"id": "133", "nombre": "Abyssal Thylacoleo", "tipo": "dino", "descripcion": "Abyssal", "nivel": 300, "precio": 190000, "comando": "/buy abyssal_thylacoleo"}
]

VIPS = [
    {"nombre": "VIP1", "tipo": "vip", "descripcion": "🔹250 puntos cada 10 minutos\n🔹Comandos-ark exclusivos\n🔹Rol exclusivo en Discord y Ark\n🔹Bonus extra x1 en sorteos", "precio": "$10", "duracion": "15 días"},
    {"nombre": "VIP2", "tipo": "vip", "descripcion": "🔸350 puntos cada 10 minutos\n🔸Comandos-ark exclusivos\n🔸Rol exclusivo en Discord y Ark\n🔸Bonus extra x2 en sorteos", "precio": "$20", "duracion": "15 días"},
    {"nombre": "VIP3", "tipo": "vip", "descripcion": "🔺450 puntos cada 10 minutos\n🔺Comandos-ark exclusivos\n🔺Rol exclusivo en Discord y Ark\n🔺Bonus extra x3 en sorteos", "precio": "$30", "duracion": "15 días"}
]

PACKS = [
    {"nombre": "PACK1", "tipo": "pack", "descripcion": "🔹175.000 puntos + VIP1", "precio": "$15"},
    {"nombre": "PACK2", "tipo": "pack", "descripcion": "🔸300.000 puntos + VIP2", "precio": "$25"},
    {"nombre": "PACK3", "tipo": "pack", "descripcion": "🔺425.000 puntos + VIP3", "precio": "$35"}
]

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
            embed = discord.Embed(
                title=f"{titulo} (Página {page_num})",
                color=EMBED_COLOR
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
# EVENTOS DEL BOT
# =====================================================

@bot.event
async def on_ready():
    """Se ejecuta cuando el bot se conecta exitosamente."""
    print(f"✅ Bot conectado como {bot.user}")
    print(f"🎮 LATINOLAND ARK Bot listo")
    logger.info(f"Bot conectado como {bot.user}")
    logger.info("LATINOLAND ARK Bot listo")
    try:
        synced = await bot.tree.sync()
        print(f"📝 {len(synced)} comandos sincronizados con Discord")
        logger.info(f"{len(synced)} comandos sincronizados con Discord")
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
        await interaction.response.send_message(embeds=embeds[:1])
        for embed in embeds[1:]:
            await interaction.followup.send(embed=embed)
    else:
        await interaction.response.send_message("❌ No hay items disponibles", ephemeral=True)
        logger.info("/comprar returned no items")

@bot.tree.command(name="vender", description="Muestra los items disponibles para vender")
async def vender(interaction: discord.Interaction):
    """Comando para mostrar items de venta."""
    logger.info(f"/vender invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)})")
    embeds = crear_embed_items(SELL_ITEMS, "💰 VENDER - Items", usar_paginas=True)
    
    if embeds:
        await interaction.response.send_message(embeds=embeds[:1])
        for embed in embeds[1:]:
            await interaction.followup.send(embed=embed)
    else:
        await interaction.response.send_message("❌ No hay items para vender", ephemeral=True)
        logger.info("/vender returned no items")

@bot.tree.command(name="dinos", description="Muestra los dinosaurios disponibles para comprar")
async def dinos_cmd(interaction: discord.Interaction):
    """Comando para mostrar dinos normales."""
    logger.info(f"/dinos invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)})")
    todos_dinos = DINOS + DINOS_ABYSSAL
    embeds = crear_embed_items(todos_dinos, "🦕 DINOS - Dinosaurios Disponibles", usar_paginas=True)
    
    if embeds:
        await interaction.response.send_message(embeds=embeds[:1])
        for embed in embeds[1:]:
            await interaction.followup.send(embed=embed)
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
        await interaction.response.send_message(embeds=embeds[:1])
        for embed in embeds[1:]:
            await interaction.followup.send(embed=embed)
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
        value="Muestra todos los dinosaurios disponibles",
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
    
    embed.set_footer(text="Usa / para ver todos los comandos disponibles")
    await interaction.response.send_message(embed=embed)
    logger.info(f"/ayuda invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)})")


@bot.tree.command(name="status", description="Muestra el estado y uptime del bot")
async def status_cmd(interaction: discord.Interaction):
    """Comando para mostrar uptime y estado del bot."""
    now = datetime.utcnow()
    uptime = now - START_TIME
    hours, remainder = divmod(int(uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    text = f"Uptime: {hours}h {minutes}m {seconds}s\nStarted (UTC): {START_TIME.isoformat()}"
    embed = discord.Embed(title="🟢 STATUS - Bot", description=text, color=EMBED_COLOR)
    embed.set_footer(text="LATINOLAND ARK Bot")
    await interaction.response.send_message(embed=embed)
    logger.info(f"/status invoked by {interaction.user} (guild={getattr(interaction.guild, 'name', None)}) - uptime {hours}:{minutes}:{seconds}")

# =====================================================
# INICIAR BOT
# =====================================================

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_TOKEN")
    
    if not TOKEN:
        print("❌ ERROR: No se encontró DISCORD_TOKEN en el archivo .env")
        print("Por favor, crea un archivo .env con tu token de bot")
        exit(1)
    
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"❌ Error al iniciar el bot: {e}")
