import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
from settings import EMBED_COLOR, BOT_NAME, VERSION, OWNER_ID, DISCORD_LOGO, BOT_LOGO, GUILD_IDS
from datetime import datetime
from random import randint, choice

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    misc = SlashCommandGroup(
        name="misc",
        description="Comandos varios",
        guild_ids=GUILD_IDS
    )

    @misc.command(name="ping", guild_ids=GUILD_IDS, description="Muestra la latencia del bot.")
    async def ping(self, ctx) -> None:
        await ctx.respond(f'Pong! Latency is {round(float(self.bot.latency * 1000), 2)}')

    @misc.command(name="info", guild_ids=GUILD_IDS, description="Muestra información sobre el servidor.")
    async def info(self, ctx) -> None:
        embed1 = discord.Embed(title=f"{ctx.guild.name}", description="Información del servidor",
                               timestamp=datetime.now(), color=discord.Color(EMBED_COLOR))
        embed1.add_field(name="Miembros: ", value=f"{ctx.guild.member_count}")
        embed1.add_field(name="Creador: ",  value=f"{ctx.guild.owner}")
        embed1.add_field(name="Nº comandos", value=f"{len(self.bot.commands)}")
        mclogo = discord.File("../"+DISCORD_LOGO, filename="image.png")
        embed1.set_footer(icon_url="attachment://image.png",
                          text=f"pedido por {ctx.author.name}")
        embed1.set_thumbnail(url="attachment://image.png")

        embed2 = discord.Embed(
            title=f"Nuestro bot {BOT_NAME}", color=discord.Color(EMBED_COLOR))
        embed2.add_field(name="Lenguaje", value=f"Python", inline=False)
        embed2.add_field(name="Tipo", value=f"Multipropósito", inline=False)
        embed2.add_field(name="Versión", value=str(VERSION), inline=False)
        pypeav = discord.File("../"+BOT_LOGO, filename="image.png")
        embed2.set_image(url="attachment://image.png")

        await ctx.respond(file=mclogo, embed=embed1)
        await ctx.respond(file=pypeav, embed=embed2)

    @misc.command(name='say', guild_ids=GUILD_IDS, description="Manda un mensaje a través del bot.")
    async def say(self, ctx, *, algo) -> None:
        await ctx.respond("Mensaje enviado :)", ephemeral=True)
        await ctx.send(algo)

    @misc.command(name='platano', guild_ids=GUILD_IDS, description="Conoce la medida de tu plátano.")
    async def platano(self, ctx) -> None:
        banana = randint(-5, 21)
        embed = discord.Embed(
            title=f"El plátano de **{ctx.author}** mide {banana} cm 😳", color=discord.Color(EMBED_COLOR))
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/755529601333067940/853072892702490624/banana.png")
        await ctx.respond(embed=embed)

    @misc.command(name='dado', guild_ids=GUILD_IDS, description="Tira un dado de 6 caras.")
    async def dado(self, ctx) -> None:
        res = randint(1, 6)
        embed = discord.Embed(title="🎲 Se ha lanzado un dado",
                              color=discord.Color(EMBED_COLOR))
        embed.add_field(name="Resultado: ", value=str(res))
        await ctx.respond(embed=embed)

    @misc.command(name='moneda', guild_ids=GUILD_IDS, description="Tira una moneda al aire.")
    async def moneda(self, ctx) -> None:
        coinResults = ("Cara 😀", "Cruz ❌")
        res = choice(coinResults)
        embed = discord.Embed(title="🪙 Se ha lanzado la moneda",
                              color=discord.Color(EMBED_COLOR))
        embed.add_field(name="Resultado: ", value=res)
        await ctx.respond(embed=embed)

    @misc.command(name='avatar', guild_ids=GUILD_IDS, description="Renderiza el avatar de alguien.")
    async def avatar(self, ctx, *, miembro: discord.Member) -> None:
        embed = discord.Embed(color=discord.Color(EMBED_COLOR))
        embed.add_field(name='Avatar de:', value=miembro.mention)
        if miembro.avatar:
            pfp = miembro.avatar.with_size(1024)
            embed.set_image(url=pfp)
        else:
            embed.add_field(name='No hay avatar', value='Este usuario no tiene un avatar personalizado.')
        await ctx.respond(embed=embed)

    @misc.command(name='paredes', guild_ids=GUILD_IDS, description="Están por las paredes.")
    async def paredes(self, ctx, *, miembro: discord.Member) -> None:
        embed = discord.Embed(
            description=f"{miembro.mention} está por las paredes!", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/paredes.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

    @misc.command(name='oooh', guild_ids=GUILD_IDS, description="Ooohh.")
    async def oooh(self, ctx) -> None:
        embed = discord.Embed(color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/oooh.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

    @misc.command(name='carey', guild_ids=GUILD_IDS, description="Feliz navidad.")
    async def carey(self, ctx) -> None:
        file = discord.File("../resources/images/interaction/dale al play.webm")
        await ctx.respond(file=file)

    @misc.command(name='beber', guild_ids=GUILD_IDS, description="Bebe alcohol.")
    async def beber(self, ctx) -> None:
        # lista de bebidas alcohólicas
        bebidas = ["cerveza", "vino", "whisky", "ron", "vodka", "tequila", "ginebra", "sidra", "champán", "cava", "sake", "absenta", "brandy", "licor", "vermut", "mezcal", "pacharán", "anís", "aguardiente", "coñac", "cóctel", "cubata", "cóctel", "cubalibre"]
        bebida = choice(bebidas)
        embed = discord.Embed(
            description=f"{ctx.author.mention} ha bebido {bebida}", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/beber.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

    @misc.command(name="bombardeen", guild_ids=GUILD_IDS, description="Bombardea a alguien/algo.")
    async def bombardeen(self, ctx, *, objetivo) -> None:
        embed = discord.Embed(
            description=f"Bombardeen {objetivo}", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/bombardeen.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))