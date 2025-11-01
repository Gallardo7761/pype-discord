import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
import hmtai
import random
import json
from settings import GUILD_IDS, EMBED_COLOR
from utils.files import read_json

class Interaccion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    inter = SlashCommandGroup("inter", "Comandos de Interacción", guild_ids=GUILD_IDS)

    @inter.command(name='wave', guild_ids=GUILD_IDS, description="Saluda a alguien.")
    async def wave(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} saludó a {miembro.mention}.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "wave"))
        await ctx.respond(embed=embed)

    @inter.command(name='dance', guild_ids=GUILD_IDS, description="Saca los pasos prohibidos.")
    async def dance(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} se puso a bailar.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "dance"))
        await ctx.respond(embed=embed)

    @inter.command(name='nice', guild_ids=GUILD_IDS, description="Di que te gusta.")
    async def nice(self, ctx):
        embed = discord.Embed(
            description=f"A {ctx.author.mention} le gustó eso.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "like"))
        await ctx.respond(embed=embed)

    @inter.command(name='nosebleed', guild_ids=GUILD_IDS, description="OwO")
    async def nosebleed(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} empezó a sangrar por la nariz.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "nosebleed"))
        await ctx.respond(embed=embed)

    @inter.command(name='punch', guild_ids=GUILD_IDS, description="ONE PUUUUUUUNCH.")
    async def punch(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le dio un puñetazo a {miembro.mention}.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "punch"))
        await ctx.respond(embed=embed)

    @inter.command(name='feed', guild_ids=GUILD_IDS, description="Ñam ñam.")
    async def feed(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le dio de comer a {miembro.mention}.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "feed"))
        await ctx.respond(embed=embed)

    @inter.command(name='tickle', guild_ids=GUILD_IDS, description="Tortura de la risa.")
    async def tickle(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le hizo cosquillas a {miembro.mention}.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "tickle"))
        await ctx.respond(embed=embed)

    @inter.command(name='bite', guild_ids=GUILD_IDS, description="Muerde a alguien.")
    async def bite(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le dio un mordisco a {miembro.mention}.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "bite"))
        await ctx.respond(embed=embed)

    @inter.command(name='hug', guild_ids=GUILD_IDS, description="Abraza a alguien.")
    async def hug(self, ctx, *, miembro: discord.Member):
        hugdata = read_json("../resources/files/hugs.json")
        key = str(miembro.id)
        if key not in hugdata.keys():
            hugdata[key] = 1
        elif key in hugdata.keys():
            hugdata[key]+=1
        with open("/home/container/data/hugs.json", 'w', encoding='utf8') as outfile:
                str_ = json.dumps(hugdata, indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=False)
                outfile.write(str_)
        
        nabrazos = hugdata[str(miembro.id)]

        embed = discord.Embed(
            description=f"{ctx.author.mention} le dio un abrazo a {miembro.mention}", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "hug"))
        embed.set_footer(text=f"{miembro.name} ha sido abrazado {nabrazos} veces.")
        await ctx.respond(embed=embed)

    @inter.command(name='kill', guild_ids=GUILD_IDS, description="Arrebátale la vida a alguien.")
    async def kill(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} asesinó a {miembro.mention}", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "kill"))
        await ctx.respond(embed=embed)

    @inter.command(name='kiss', guild_ids=GUILD_IDS, description="Cómele la boca a alguien.")
    async def kiss(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le dio un beso a {miembro.mention} >.<", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "kiss"))
        await ctx.respond(embed=embed)

    @inter.command(name='pat', guild_ids=GUILD_IDS, description="Acaricia a alguien.")
    async def pat(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} acarició a {miembro.mention} UwU", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "pat"))
        await ctx.respond(embed=embed)

    @inter.command(name='slap', guild_ids=GUILD_IDS, description="Abofetea a alguien.")
    async def slap(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le dio una bofetada a {miembro.mention} >:)", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "slap"))
        await ctx.respond(embed=embed)

    @inter.command(name='sleep', guild_ids=GUILD_IDS, description="A mimir.")
    async def sleep(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} se fue a mimir", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "sleep"))
        await ctx.respond(embed=embed)

    @inter.command(name='cry', guild_ids=GUILD_IDS, description="Expresa tu tristeza...")
    async def cry(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} se puso triste :(", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "cry"))
        await ctx.respond(embed=embed)

    @inter.command(name='cuddle', guild_ids=GUILD_IDS, description="Acurrúcate con alguien.")
    async def cuddle(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} se acurrucó con {miembro.mention}", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "cuddle"))
        await ctx.respond(embed=embed)

    @inter.command(name='lick', guild_ids=GUILD_IDS, description="Lámele a alguien. 7u7")
    async def lick(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} lamió sensualmente a {miembro.mention}", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "lick"))
        await ctx.respond(embed=embed)

    @inter.command(name='threaten', guild_ids=GUILD_IDS, description="Amenaza a alguien.")
    async def threaten(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} amenazó con cortarle la picha a {miembro.mention}", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=hmtai.get("hmtai", "threaten"))
        await ctx.respond(embed=embed)
    
    @inter.command(name='femboy', guild_ids=GUILD_IDS, description="Femboiza a alguien.")
    async def femboy(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} ha convertido en femboy a {miembro.mention}", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/femboy.png", filename="imagen.png")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file,embed=embed)

    # ----------------| ESPECÍFICAS |-------------------------------------------------------------------------------------------------------------------

    @inter.command(name='run', guild_ids=GUILD_IDS, description="Huye!!!")
    async def run(self, ctx): # type: ignore
        embed = discord.Embed(
            description=f"{ctx.author.mention} se puso a correr", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/run.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

    @inter.command(name='fbi', guild_ids=GUILD_IDS, description="Llama al FBI.")
    async def run(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} ha llamado al FBI. Corre {miembro.mention}!", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/fbi.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

    @inter.command(name='spank', guild_ids=GUILD_IDS, description="Reparte nalgadas como panes.")
    async def spank(self, ctx, *, alguien: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} nalgueó a {alguien.mention} >///<", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/spank.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

    @inter.command(name='ship', guild_ids=GUILD_IDS, description="Shipea a dos personas (porcentaje de compatibilidad).")
    async def ship(self, ctx, *, persona1: discord.Member, persona2: discord.Member):
        embed = discord.Embed(
            description=f"{persona1.mention} x {persona2.mention}\n ❤️ La compatibilidad es del: **{random.randint(0, 100)}%**", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/ship.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

    @inter.command(name='moan', guild_ids=GUILD_IDS, description="Gime como una perra.")
    async def moan(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} gimió como una perra.", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/moan.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

def setup(bot):
    bot.add_cog(Interaccion(bot))