import discord
from discord.ext import commands, pages
from discord.commands import SlashCommandGroup
from settings import (
    EMBED_COLOR, GUILD_IDS, INDICE, VARIOS, 
    INTERACCION, INTERACCION_2, NSFW, MATEMATICAS, MUSICA, VERIFICACION, HELP
)

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    help = SlashCommandGroup("help", "Comandos de Ayuda", guild_ids=GUILD_IDS) 

    @help.command(name="all", guild_ids=GUILD_IDS, description="Abre el menú de ayuda de comandos.")
    async def all(self, ctx: discord.ApplicationContext):
        indice_embed = discord.Embed(
            title="**📖 | MENÚ DE COMANDOS**", color=discord.Color(EMBED_COLOR))
        indice_embed.add_field(name="**📝 | Categorías**", value=INDICE)
        
        varios_embed = discord.Embed(
            title="**📖 | MENÚ DE COMANDOS**", color=discord.Color(EMBED_COLOR))
        varios_embed.add_field(name="**🪶 | Varios**", value=VARIOS)
        
        interaccion_embed = discord.Embed(
            title="**📖 | MENÚ DE COMANDOS**", color=discord.Color(EMBED_COLOR))
        interaccion_embed.add_field(
            name="**👥 | Interacción**", value=INTERACCION, inline=False)
        interaccion_embed.add_field(
            name="**👥 | Interacción**", value=INTERACCION_2, inline=False)
        
        nsfw_embed = discord.Embed(
            title="**📖 | MENÚ DE COMANDOS**", color=discord.Color(EMBED_COLOR))
        nsfw_embed.add_field(name="**🔞 | NSFW**", value=NSFW)
        
        matematicas_embed = discord.Embed(
            title="**📖 | MENÚ DE COMANDOS**", color=discord.Color(EMBED_COLOR))
        matematicas_embed.add_field(
            name="**🧮 | Matemáticas**", value=MATEMATICAS)
        
        musica_embed = discord.Embed(
            title="**📖 | MENÚ DE COMANDOS**", color=discord.Color(EMBED_COLOR))
        musica_embed.add_field(name="**🎶 | Música**", value=MUSICA)
        
        verificacion_embed = discord.Embed(
            title="**📖 | MENÚ DE COMANDOS**", color=discord.Color(EMBED_COLOR))
        verificacion_embed.add_field(
            name="**✅ | Verificación**", value=VERIFICACION)
        
        help_embed = discord.Embed(
            title="**📖 | MENÚ DE COMANDOS**", color=discord.Color(EMBED_COLOR))
        help_embed.add_field(name="**🆘 | Ayuda**", value=HELP)
        
        paginator = pages.Paginator(
            pages=[
                indice_embed,
                varios_embed,
                interaccion_embed,
                nsfw_embed,
                matematicas_embed,
                musica_embed,
                verificacion_embed,
                help_embed
            ],
            loop_pages=True
        )
        await paginator.respond(ctx.interaction, ephemeral=False)


def setup(bot):
    bot.add_cog(Help(bot))