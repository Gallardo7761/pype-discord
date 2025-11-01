import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
import hmtai
from settings import GUILD_IDS

class InteraccionNSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    nsfw = SlashCommandGroup("nsfw", "Comandos NSFW", guild_ids=GUILD_IDS)

    @nsfw.command(name='creampie', guild_ids=GUILD_IDS,  description="Lechita.")
    async def creampie(self, ctx, *, miembro: discord.Member = None):
        if ctx.channel.is_nsfw():
            if miembro:
                embed = discord.Embed(description=f"{ctx.author.mention} se vino en {miembro.mention} 😳", color=discord.Color.from_rgb(177,18,46))
            else:
                embed = discord.Embed(description=f"{ctx.author.mention} se vino 😳", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","creampie"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral=True)

    @nsfw.command(name='hentai', guild_ids=GUILD_IDS,  description="Go to horny jail.")
    async def hentai(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(description="Disfruta 😳", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","classic"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral=True)

    @nsfw.command(name='anal', guild_ids=GUILD_IDS,  description="Es la hora de dar por culo.")
    async def anal(self, ctx, *, miembro: discord.Member):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(description=f"{ctx.author.mention}: * le da por culo *\n {miembro.mention}: Man dao por culo Dios mío! Hola.", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","anal"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral = True)

    @nsfw.command(name='ass', guild_ids=GUILD_IDS,  description="Culito, culito!")
    async def ass(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(description=f"{ctx.author.mention} toma culo!", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","ass"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral = True)

    @nsfw.command(name='bdsm', guild_ids=GUILD_IDS,  description="Atar?")
    async def bdsm(self, ctx,*,miembro: discord.Member = None):
        if ctx.channel.is_nsfw():
            if miembro:
                embed = discord.Embed(description=f"{ctx.author.mention} le practicó el BDSM a {miembro.mention} 😳", color=discord.Color.from_rgb(177,18,46))
            else:
                embed = discord.Embed(description=f"A {ctx.author.mention} le gusta el BDSM!", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","bdsm"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral=True)

    @nsfw.command(name='doujin', guild_ids=GUILD_IDS,  description="Página random de un doujinshi.")
    async def doujin(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(description=f"Aquí tienes tu página random de un doujin, {ctx.author.mention}.", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","manga"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral=True)

    @nsfw.command(name='fap', guild_ids=GUILD_IDS,  description="Fap fap fap fap.")
    async def fap(self, ctx, *, miembro: discord.Member = None):
        if ctx.channel.is_nsfw():
            if miembro:
                embed = discord.Embed(description=f"{ctx.author.mention} hizo sentir rico a {miembro.mention} 😳", color=discord.Color.from_rgb(177,18,46))
            else:
                embed = discord.Embed(description=f"{ctx.author.mention} se tocó 😳", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","handjob"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral=True)

    @nsfw.command(name='ero', guild_ids=GUILD_IDS,  description="Fucking pervert.")
    async def ero(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(description=f"Aquí tienes tu contenido ero, {ctx.author.mention}.", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","ero"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral=True)

    @nsfw.command(name='yuri', guild_ids=GUILD_IDS,  description="Imagen yuri 🏳️‍🌈.")
    async def yuri(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(description=f"Aquí tienes tu contenido yuri, {ctx.author.mention}.", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","yuri"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral=True)

    @nsfw.command(name='blowjob', guild_ids=GUILD_IDS,  description="* clk clk clk *")
    async def blowjob(self, ctx, *, miembro: discord.Member = None):
        if ctx.channel.is_nsfw():
            if miembro:
                embed = discord.Embed(description=f"{ctx.author.mention} * clk clk clk * {miembro.mention} 😳", color=discord.Color.from_rgb(177,18,46))
            else:
                embed = discord.Embed(description=f"{ctx.author.mention} realizó la AutoM", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","blowjob"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral=True)

    @nsfw.command(name='boobs', guild_ids=GUILD_IDS,  description="tetas tetitas tetazas tetotas tetarracas.")
    async def boobs(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(description=f"Aquí tienes tus tetas tetarracas, {ctx.author.mention}.", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","boobs"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral=True)

    @nsfw.command(name='pussy', guild_ids=GUILD_IDS,  description="Es temporada de recogida de higos.")
    async def pussy(self, ctx):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(description=f"{ctx.author.mention} recogió un higo.", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","pussy"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral=True)

    @nsfw.command(name='boobjob', guild_ids=GUILD_IDS,  description="Tetas tetarracas + * clk clk clk *")
    async def boobjob(self, ctx,*,miembro: discord.Member):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(description=f"{ctx.author.mention} le hizo una boobjob a {miembro.mention}", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","boobjob"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral=True)

    @nsfw.command(name='gangbang', guild_ids=GUILD_IDS,  description="Muchas tuneladoras para un sólo túnel.")
    async def gangbang(self, ctx, *, abusador_1: discord.Member, abusador_2: discord.Member, abusador_3: discord.Member, victima: discord.Member):
        if ctx.channel.is_nsfw():
            embed = discord.Embed(description=f"{ctx.author.mention} & {abusador_1.mention},{abusador_2.mention},{abusador_3.mention} taladraron a {victima.mention} 😳", color=discord.Color.from_rgb(177,18,46))
            embed.set_image(url=hmtai.get("hmtai","gangbang"))
            await ctx.respond(embed=embed)
        else:
            await ctx.respond("*Debes usar el comando en un canal NSFW...*", ephemeral=True)
    
def setup(bot):
    bot.add_cog(InteraccionNSFW(bot))