import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
from settings import EMBED_COLOR, GUILD_IDS, ADMIN_ROLE_ID, ANNOUNCES_CHANNEL_ID, TIMEZONE
from utils.embeds import crear_embed
from utils.logger.pype_logger import PypeLogger
from utils.files import read_json, write_json
from utils.reactions import añadir_reacciones
from datetime import datetime
import pytz
import json

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    admin = SlashCommandGroup(
        name="admin",
        description="Comandos de administración",
        guild_ids=GUILD_IDS
    )

    @admin.command(name="anuncio", guild_ids=GUILD_IDS, description="Anuncia algo.")
    async def anuncio(self, ctx, *, mensaje) -> None:
        embed = discord.Embed(color=discord.Color(EMBED_COLOR))
        embed.add_field(name="📢** | Anuncio**", value=mensaje)
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            channel = ctx.guild.get_channel(ANNOUNCES_CHANNEL_ID)
            await channel.send(embed=embed)
            await ctx.respond(f"Se ha anunciado el mensaje, {ctx.author.mention} ", ephemeral=True)
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)

    # crea un embed con fields, footer, image, thumbnail, author, title, description, color, timestamp a elegir
    @admin.command(name="embed", guild_ids=GUILD_IDS, description="Crea un embed.")
    async def create_embed(self, ctx: commands.Context, *,
                       title: str,
                       description: str,    
                       fields: str = None,
                       footer_text: str = None,
                       timestamp: bool = False,
                       author_name: str = None,
                       image_url: str = None,
                       thumbnail_url: str = None,
                       color: int = None) -> None:
        embed = crear_embed(ctx,title,description,fields,footer_text,timestamp,author_name,image_url,thumbnail_url,color)        
        await ctx.send(embed=embed)
        await ctx.respond(f"Se ha creado el embed, {ctx.author.mention} ", ephemeral=True)
        

    @admin.command(name='ban', guild_ids=GUILD_IDS, description="Alza el martillo del ban.")
    async def ban(self, ctx, *, miembro: discord.Member) -> None:
        embed = discord.Embed(color=discord.Color(EMBED_COLOR))
        embed.add_field(
            name="🚫** | BAN**", value=f"{miembro.mention} ha sido golpead@ por el martillo del Ban.")
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            await ctx.respond(embed=embed)
            await miembro.ban()
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)

    @admin.command(name='unban', guild_ids=GUILD_IDS, description="Baja el martillo del ban.")
    async def unban(self, ctx, *, miembro: discord.Member) -> None:
        embed = discord.Embed(color=discord.Color(EMBED_COLOR))
        embed.add_field(name="🚫** | UNBAN**",
                        value=f"{miembro.name} se ha recuperado del martillazo.")
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            await ctx.respond(embed=embed)
            await miembro.unban()
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)

    @admin.command(name='kick', guild_ids=GUILD_IDS, description="Expulsa a un miembro.")
    async def kick(self, ctx, *, miembro: discord.Member, razon: str = "mal comportamiento") -> None:
        embed = discord.Embed(color=discord.Color(EMBED_COLOR))
        embed.add_field(
            name="🦵🏽** | KICK**", value=f"{miembro.mention} ha sido expulsado por: {razon}.")
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            await ctx.respond(embed=embed)
            await miembro.kick(reason=razon)
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)

    @admin.command(name="mute", guild_ids=GUILD_IDS, description="Silencia a un miembro.")
    async def mute(self, ctx, *, miembro: discord.Member) -> None:
        embed = discord.Embed(color=discord.Color(EMBED_COLOR))
        embed.add_field(
            name="🔇** | MUTE**", value=f"{miembro.mention} ha sido silenciad@.")
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            await ctx.respond(embed=embed)
            await miembro.edit(mute=True)
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)
    
    @admin.command(name="unmute", guild_ids=GUILD_IDS, description="Desilencia a un miembro.")
    async def unmute(self, ctx, *, miembro: discord.Member) -> None:
        embed = discord.Embed(color=discord.Color(EMBED_COLOR))
        embed.add_field(
            name="🔊** | UNMUTE**", value=f"{miembro.mention} ha sido desilenciad@.")
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            await ctx.respond(embed=embed)
            await miembro.edit(mute=False)
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)

    @admin.command(name="clearch", guild_ids=GUILD_IDS, description="Borra mensajes.")
    async def clear(self, ctx, cantidad: int) -> None:
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            await ctx.respond(f"Se han limpiado {cantidad} mensajes, {ctx.author.mention}", ephemeral=True)
            await ctx.channel.purge(limit=cantidad)
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)
    
    @admin.command(name="lock", guild_ids=GUILD_IDS, description="Bloquea un canal.")
    async def lock(self, ctx) -> None:
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            await ctx.respond(f"Se ha bloqueado el canal, {ctx.author.mention}", ephemeral=True)
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)
    
    @admin.command(name="unlock", guild_ids=GUILD_IDS, description="Desbloquea un canal.")
    async def unlock(self, ctx) -> None:
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            await ctx.respond(f"Se ha desbloqueado el canal, {ctx.author.mention}", ephemeral=True)
            await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)

    @admin.command(name="nick", guild_ids=GUILD_IDS, description="Cambia el apodo de un miembro.")
    async def nick(self, ctx, miembro: discord.Member, *, apodo: str) -> None:
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            await ctx.respond(f"Se ha cambiado el apodo de {miembro.mention} a {apodo}, {ctx.author.mention}", ephemeral=True)
            await miembro.edit(nick=apodo)
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)

    @admin.command(name="role", guild_ids=GUILD_IDS, description="Añade o quita un rol a un miembro.")
    async def role(self, ctx, miembro: discord.Member, *, rol: discord.Role) -> None:
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            if rol in miembro.roles:
                await ctx.respond(f"Se ha quitado el rol {rol.mention} a {miembro.mention}, {ctx.author.mention}", ephemeral=True)
                await miembro.remove_roles(rol)
            else:
                await ctx.respond(f"Se ha añadido el rol {rol.mention} a {miembro.mention}, {ctx.author.mention}", ephemeral=True)
                await miembro.add_roles(rol)
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)

    @admin.command(name='votacion', guild_ids=GUILD_IDS, description="Crea una votación.")
    async def votacion(self, ctx, *, pregunta, reacciones, tiempo = None) -> None:
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            emojis = "1\uFE0F\u20E3;2\uFE0F\u20E3;3\uFE0F\u20E3;4\uFE0F\u20E3;5\uFE0F\u20E3;6\uFE0F\u20E3;7\uFE0F\u20E3;8\uFE0F\u20E3;9\uFE0F\u20E3"
            emojis_list = emojis.split(";")
            if tiempo:
                embed = discord.Embed(title=pregunta, description=f"Acaba en {tiempo}", color=discord.Color(EMBED_COLOR))
            else:
                embed = discord.Embed(title=pregunta, description="", color=discord.Color(EMBED_COLOR))
            reacciones = reacciones.split(",")
            a=0
            for r in reacciones:
                embed.add_field(name=f"{emojis_list[a]} : {r}", value="", inline=False)
                a+=1
            embed.set_author(name=f"Votación 📊", icon_url=ctx.author.avatar.url)
            embed.set_footer(text=f"Concord")
            embed.timestamp = datetime.now(pytz.timezone(TIMEZONE))
            msg = await ctx.send(embed=embed)
            await añadir_reacciones(msg, emojis, len(reacciones)) 
            await ctx.respond(f"Se ha creado la votación, {ctx.author.mention}", ephemeral=True)
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)

    @admin.command(name='warn', guild_ids=GUILD_IDS, description="Añade una advertencia a un miembro.")
    async def warn(self, ctx, miembro: discord.Member, *, razon) -> None:
        warned_users = read_json("../resources/files/warns.json")
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            embed = discord.Embed(color=discord.Color(EMBED_COLOR))
            embed.add_field(
                name="⚠️** | WARN**", value=f"{miembro.mention} ha sido advertid@ por {razon}.")
            
            await ctx.respond(embed=embed)
            await miembro.send(f"Has sido advertid@ en {ctx.guild.name} por {razon}.")
            
            key = str(miembro.id)
            if key not in warned_users.keys():
                warned_users[key] = 1
            elif key in warned_users.keys():
                warned_users[key]+=1

            warnsfile = "../resources/files/warns.json"
            
            write_json(warnsfile, warned_users)

        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)

    @admin.command(name='warns', guild_ids=GUILD_IDS, description="Muestra las advertencias de un miembro.")
    async def warns(self, ctx, miembro: discord.Member) -> None:
        warned_users = read_json("../resources/files/warns.json")
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            embed = discord.Embed(color=discord.Color(EMBED_COLOR))
            embed.add_field(
                name="⚠️** | WARN**", value=f"{miembro.mention} tiene {warned_users[str(miembro.id)]} advertencias.")
            await ctx.respond(embed=embed, ephemeral=True)
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)

    @admin.command(name='clearwarns', guild_ids=GUILD_IDS, description="Elimina las advertencias de un miembro.")
    async def clearwarns(self, ctx, miembro: discord.Member) -> None:
        warned_users = read_json("../resources/files/warns.json")
        if ctx.author.guild.get_role(ADMIN_ROLE_ID) in ctx.author.roles:
            embed = discord.Embed(color=discord.Color(EMBED_COLOR))
            embed.add_field(
                name="⚠️** | WARN**", value=f"{miembro.mention} ha sido desadvertid@.")
            
            await ctx.respond(embed=embed, ephemeral=True)

            warned_users[str(miembro.id)] = 0
            warnsfile = "../resources/files/warns.json"

            write_json(warnsfile, warned_users)
        else:
            await ctx.respond(f"No tienes permisos para eso, {ctx.author.mention} ", ephemeral=True)

def setup(bot) -> None:
    bot.add_cog(Admin(bot))
