import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
import random
import json
from settings import GUILD_IDS, EMBED_COLOR
from utils.files import read_json
from animegifs import animegifs

gifs = animegifs.Animegifs()

class Interaccion(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    ########################################
    #              CUTE                 #
    ########################################
    # Ej: wave, dance, nosebleed, cry, blush, happy, disgust, exploding, facedesk,
    # facepalm, icecream, nod, note...
        
    @commands.slash_command(name='tickle', guild_ids=GUILD_IDS, description="Tortura de la risa.")
    async def tickle(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le hizo cosquillas a {miembro.mention}.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('tickle'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='hug', guild_ids=GUILD_IDS, description="Abraza a alguien.")
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
        embed.set_image(url=gifs.get_gif('hug'))
        embed.set_footer(text=f"{miembro.name} ha sido abrazado {nabrazos} veces.")
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='kiss', guild_ids=GUILD_IDS, description="Cómele la boca a alguien.")
    async def kiss(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le dio un beso a {miembro.mention} >.<", color=discord.Color(EMBED_COLOR))
        r = random.randint(0,1)
        embed.set_image(url=gifs.get_gif('kiss') if r == 0 else gifs.get_gif('french_kiss'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='pat', guild_ids=GUILD_IDS, description="Acaricia a alguien.")
    async def pat(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} acarició a {miembro.mention} UwU", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('pat'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='cuddle', guild_ids=GUILD_IDS, description="Acurrúcate con alguien.")
    async def cuddle(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} se acurrucó con {miembro.mention}", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('cuddle'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='blush', guild_ids=GUILD_IDS, description="Enrojece todo tímido.")
    async def blush(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} se sonrojó >///<",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('blush'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='flick', guild_ids=GUILD_IDS, description="Dale un toquecito a alguien.")
    async def flick(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le dio un toque en la frente a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('flick'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='flirt', guild_ids=GUILD_IDS, description="Coquetea un poquito.")
    async def flirt(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} coqueteó con {miembro.mention} 😳👉👈",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('flirt'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='handhold', guild_ids=GUILD_IDS, description="Agarra la manita.")
    async def handhold(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le agarró la mano a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('handhold'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='love', guild_ids=GUILD_IDS, description="Expresa amor puro.")
    async def love(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} siente amor por {miembro.mention} ❤️",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('love'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='marry', guild_ids=GUILD_IDS, description="Proponle matrimonio a alguien.")
    async def marry(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} quiere casarse con {miembro.mention} 💍",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('marry'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='nuzzle', guild_ids=GUILD_IDS, description="Frota la carita contra alguien.")
    async def nuzzle(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} se restregó cariñosamente contra {miembro.mention} UwU",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('nuzzle'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='peck', guild_ids=GUILD_IDS, description="Besito rápido.")
    async def peck(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le dio un besito a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('peck'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='poke', guild_ids=GUILD_IDS, description="Poke poke.")
    async def poke(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} pinchó a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('poke'))
        await ctx.respond(embed=embed)
            
    @commands.slash_command(name='pout', guild_ids=GUILD_IDS, description="Hace puchero.")
    async def pout(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} está haciendo pucheritos >:(",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('pout'))
        await ctx.respond(embed=embed)        
    
    ########################################
    #            AGRESIVAS                 #
    ########################################
    # Ej: punch, slap, kill, threaten, attack, harass, insult, bonk, bloodsuck...
    
    @commands.slash_command(name='kill', guild_ids=GUILD_IDS, description="Arrebátale la vida a alguien.")
    async def kill(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} asesinó a {miembro.mention}", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('kill'))
        await ctx.respond(embed=embed)
    
    @commands.slash_command(name='punch', guild_ids=GUILD_IDS, description="ONE PUUUUUUUNCH.")
    async def punch(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le dio un puñetazo a {miembro.mention}.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('punch'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='slap', guild_ids=GUILD_IDS, description="Abofetea a alguien.")
    async def slap(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le dio una bofetada a {miembro.mention} >:)", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('slap'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='threaten', guild_ids=GUILD_IDS, description="Amenaza a alguien.")
    async def threaten(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} amenazó con cortarle la picha a {miembro.mention}", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('threat'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='attack', guild_ids=GUILD_IDS, description="Ataca a alguien.")
    async def attack(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} atacó salvajemente a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('attack'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='bloodsuck', guild_ids=GUILD_IDS, description="Chúpale la sangre a alguien.")
    async def bloodsuck(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le chupó la sangre a {miembro.mention}. 🧛",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('bloodsuck'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='exploding', guild_ids=GUILD_IDS, description="Kaboom.")
    async def exploding(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} explotó. Literal.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('exploding'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='harass', guild_ids=GUILD_IDS, description="Molesta a alguien (suavecito).")
    async def harass(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} molestó a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('harass'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='insult', guild_ids=GUILD_IDS, description="Insulta a alguien (suave).")
    async def insult(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} insultó finamente a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('insult'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='punish', guild_ids=GUILD_IDS, description="Castiga a alguien.")
    async def punish(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} castigó a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('punish'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='scold', guild_ids=GUILD_IDS, description="Regaña a alguien.")
    async def scold(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} regañó a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('scold'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='shoot', guild_ids=GUILD_IDS, description="PUM PUM.")
    async def shoot(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} disparó a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('shoot'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='threat', guild_ids=GUILD_IDS, description="Amenaza (otra versión).")
    async def threat(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} amenazó a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('threat'))
        await ctx.respond(embed=embed)
    
    ########################################
    #                VARIAS                #
    ########################################
    # Ej: hug, kiss, pat, cuddle, lick, love, marry, flirt, brofist, highfive,
    # tickle, bite, handhold...
    
    @commands.slash_command(name='wave', guild_ids=GUILD_IDS, description="Saluda a alguien.")
    async def wave(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} saludó a {miembro.mention}.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('wave'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='dance', guild_ids=GUILD_IDS, description="Saca los pasos prohibidos.")
    async def dance(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} se puso a bailar.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('dance'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='nosebleed', guild_ids=GUILD_IDS, description="OwO")
    async def nosebleed(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} empezó a sangrar por la nariz.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('nosebleed'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='bite', guild_ids=GUILD_IDS, description="Muerde a alguien.")
    async def bite(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le dio un mordisco a {miembro.mention}.", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('bite'))
        await ctx.respond(embed=embed)
    
    @commands.slash_command(name='cry', guild_ids=GUILD_IDS, description="Expresa tu tristeza...")
    async def cry(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} se puso triste :(", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('cry'))
        await ctx.respond(embed=embed)
    
    @commands.slash_command(name='lick', guild_ids=GUILD_IDS, description="Lámele a alguien. 7u7")
    async def lick(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} lamió sensualmente a {miembro.mention}", color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('lick'))
        await ctx.respond(embed=embed)
    
    @commands.slash_command(name='bonk', guild_ids=GUILD_IDS, description="BONK! A la cárcel del horny.")
    async def bonk(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le hizo BONK a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('bonk'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='brofist', guild_ids=GUILD_IDS, description="Bro fist 🔥")
    async def brofist(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} chocó puños con {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('brofist'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='disgust', guild_ids=GUILD_IDS, description="Qué asco.")
    async def disgust(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} está asqueado 🤢",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('disgust'))
        await ctx.respond(embed=embed)
    
    @commands.slash_command(name='facedesk', guild_ids=GUILD_IDS, description="Se estampó contra la mesa.")
    async def facedesk(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} hizo un facedesk brutal.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('facedesk'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='facepalm', guild_ids=GUILD_IDS, description="Facepalm extremo.")
    async def facepalm(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} hizo un facepalm legendario.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('facepalm'))
        await ctx.respond(embed=embed)
    
    @commands.slash_command(name='happy', guild_ids=GUILD_IDS, description="Expresa tu felicidad.")
    async def happy(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} está feliz :D",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('happy'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='highfive', guild_ids=GUILD_IDS, description="Choca esos cinco.")
    async def highfive(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} chocó esos cinco con {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('highfive'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='icecream', guild_ids=GUILD_IDS, description="Cómete un helao.")
    async def icecream(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} se está comiendo un helao 🍦",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('icecream'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='nod', guild_ids=GUILD_IDS, description="Asiente con la cabeza.")
    async def nod(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} asintió.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('nod'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='note', guild_ids=GUILD_IDS, description="Toma apuntes.")
    async def note(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} está tomando notas.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('note'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='popcorn', guild_ids=GUILD_IDS, description="A ver el drama con palomitas.")
    async def popcorn(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} está viendo el drama con palomitas 🍿",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('popcorn'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='sad', guild_ids=GUILD_IDS, description="Tristón.")
    async def sad(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} está triste...",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('sad'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='scared', guild_ids=GUILD_IDS, description="Se asusta.")
    async def scared(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} está asustado 😱",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('scared'))
        await ctx.respond(embed=embed)
        
    @commands.slash_command(name='shrug', guild_ids=GUILD_IDS, description="Encogerse de hombros.")
    async def shrug(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} se encogió de hombros.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('shrug'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='sip', guild_ids=GUILD_IDS, description="Bebe algo.")
    async def sip(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} tomó un sorbo. ☕",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('sip'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='smack', guild_ids=GUILD_IDS, description="Golpecito rápido.")
    async def smack(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} le dio un smacc a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('smack'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='smirk', guild_ids=GUILD_IDS, description="Sonrisa de listillo.")
    async def smirk(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} sonrió con cara de sabelotodo.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('smirk'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='sorry', guild_ids=GUILD_IDS, description="Pide perdón.")
    async def sorry(self, ctx, *, miembro: discord.Member = None):
        if miembro:
            desc = f"{ctx.author.mention} pidió perdón a {miembro.mention} 🙏"
        else:
            desc = f"{ctx.author.mention} pidió perdón."

        embed = discord.Embed(description=desc, color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('sorry'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='stare', guild_ids=GUILD_IDS, description="Mira fijamente.")
    async def stare(self, ctx, *, miembro: discord.Member = None):
        if miembro:
            desc = f"{ctx.author.mention} miró fijamente a {miembro.mention} 👀"
        else:
            desc = f"{ctx.author.mention} está mirando fijamente..."

        embed = discord.Embed(description=desc, color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('stare'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='tease', guild_ids=GUILD_IDS, description="Molestia juguetona.")
    async def tease(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} molestó pícaramente a {miembro.mention}.",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('tease'))
        await ctx.respond(embed=embed)
 
    @commands.slash_command(name='tired', guild_ids=GUILD_IDS, description="Estoy cansao.")
    async def tired(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} está cansadísimo…",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('tired'))
        await ctx.respond(embed=embed)

    @commands.slash_command(name='yawn', guild_ids=GUILD_IDS, description="Bosteza.")
    async def yawn(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} bostezó 🥱",
            color=discord.Color(EMBED_COLOR))
        embed.set_image(url=gifs.get_gif('yawn'))
        await ctx.respond(embed=embed)
 
    # ----------------| CUSTOM |-------------------------------------------------------------------------------------------------------------------

    @commands.slash_command(name='femboy', guild_ids=GUILD_IDS, description="Femboiza a alguien.")
    async def femboy(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} ha convertido en femboy a {miembro.mention}", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/femboy.png", filename="imagen.png")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file,embed=embed)

    @commands.slash_command(name='run', guild_ids=GUILD_IDS, description="Huye!!!")
    async def run(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} se puso a correr", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/run.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

    @commands.slash_command(name='fbi', guild_ids=GUILD_IDS, description="Llama al FBI.")
    async def run(self, ctx, *, miembro: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} ha llamado al FBI. Corre {miembro.mention}!", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/fbi.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

    @commands.slash_command(name='spank', guild_ids=GUILD_IDS, description="Reparte nalgadas como panes.")
    async def spank(self, ctx, *, alguien: discord.Member):
        embed = discord.Embed(
            description=f"{ctx.author.mention} nalgueó a {alguien.mention} >///<", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/spank.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

    @commands.slash_command(name='ship', guild_ids=GUILD_IDS, description="Shipea a dos personas (porcentaje de compatibilidad).")
    async def ship(self, ctx, *, persona1: discord.Member, persona2: discord.Member):
        embed = discord.Embed(
            description=f"{persona1.mention} x {persona2.mention}\n ❤️ La compatibilidad es del: **{random.randint(0, 100)}%**", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/ship.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

    @commands.slash_command(name='moan', guild_ids=GUILD_IDS, description="Gime como una perra.")
    async def moan(self, ctx):
        embed = discord.Embed(
            description=f"{ctx.author.mention} gimió como una perra.", color=discord.Color(EMBED_COLOR))
        file = discord.File("../resources/images/interaction/moan.gif", filename="imagen.gif")
        embed.set_image(url="attachment://imagen.gif")
        await ctx.respond(file=file, embed=embed)

def setup(bot):
    bot.add_cog(Interaccion(bot))