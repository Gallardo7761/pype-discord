import discord
import wavelink
from discord.ext import commands
from discord.commands import SlashCommandGroup
import wavelink
from settings import (
    EMBED_COLOR, GUILD_IDS, WAVELINK_URI, WAVELINK_PASSWORD, GUILD_NAME
)
from utils.logger.pype_logger import PypeLogger

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    musica = SlashCommandGroup("musica", "Comandos de música", guild_ids=GUILD_IDS)

    async def setup_hook(self) -> None:
        # Wavelink 2.0 has made connecting Nodes easier... Simply create each Node
        # and pass it to NodePool.connect with the client/bot.
        node: wavelink.Node = wavelink.Node(uri=WAVELINK_URI, password=WAVELINK_PASSWORD, secure=False)
        await wavelink.NodePool.connect(client=self.bot, nodes=[node])
        PypeLogger.success(f"Se ha conectado a -> {node}")   
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.setup_hook()
    
    @commands.Cog.listener()
    async def on_wavelink_track_start(self, track: wavelink.TrackEventPayload):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=track.track.title))

    @commands.Cog.listener()
    async def on_wavelink_track_end(self, track: wavelink.TrackEventPayload):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=GUILD_NAME))

    @musica.command(name="play", guild_ids=GUILD_IDS, description="Reproduce una canción")
    async def play(self, ctx: commands.Context, *, cancion: str, sitio: str = "youtube") -> None:
        if not ctx.voice_client:
            vc: wavelink.Player = await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            vc: wavelink.Player = ctx.voice_client
        if sitio == "spotify":
            #decoded = spotify.decode_url(cancion)
            #if not decoded or decoded['type'] is not spotify.SpotifySearchType.track:
            #    await ctx.send('Sólo se permiten urls de Spotify.')
            #    return
            #track = await spotify.SpotifyTrack.search(cancion)
            ctx.respond("Próximamente")
        elif sitio == "youtube":
            track = await wavelink.YouTubeTrack.search(cancion, return_first=True)
        if not vc.is_playing():
            await vc.play(track)
            try:
                await self.bot.user.edit(avatar=open("../resources/images/djpype.png", "rb").read())
            except:
                pass
            embed = discord.Embed(title="▶️ Reproduciendo", description=track.title + " de " + track.author + " en " + sitio, color=EMBED_COLOR)
        elif vc.is_playing():
            cola: wavelink.BaseQueue = vc.auto_queue
            vc.autoplay = True
            await cola.put_wait(track)
            embed = discord.Embed(title="🎶 Añadido a la cola", description=track.title + " de " + track.author + " en " + sitio, color=EMBED_COLOR)
            if cola.is_empty:
                embed = discord.Embed(title="▶️ Reproduciendo", description="La cola está vacía.", color=EMBED_COLOR)
        await ctx.respond(embed=embed)

    @musica.command(name="pause", guild_ids=GUILD_IDS, description="Pausa la canción")
    async def pausa(self, ctx: commands.Context) -> None:
        vc: wavelink.Player = ctx.voice_client
        if vc.is_playing():
            if vc.is_paused():
                embed = discord.Embed(title="⏸️ Pausado", description="La canción ya está pausada.", color=EMBED_COLOR)
            await vc.pause()
            embed = discord.Embed(title="⏸️ Pausado", description="La canción ha sido pausada.", color=EMBED_COLOR)
        await ctx.respond(embed=embed)
    
    @musica.command(name="resume", guild_ids=GUILD_IDS, description="Reanuda la canción")
    async def reanudar(self, ctx: commands.Context) -> None:
        vc: wavelink.Player = ctx.voice_client
        await vc.resume()
        embed = discord.Embed(title="▶️ Reproduciendo", description="La canción ha sido reanudada.", color=EMBED_COLOR)
        await ctx.respond(embed=embed)

    @musica.command(name="stop", guild_ids=GUILD_IDS, description="Detiene la canción")
    async def parar(self, ctx: commands.Context) -> None:
        vc: wavelink.Player = ctx.voice_client
        await vc.stop()
        embed = discord.Embed(title="⏹️ Detenido", description="La canción ha sido detenida.", color=EMBED_COLOR)
        await ctx.respond(embed=embed)

    @musica.command(name="join", guild_ids=GUILD_IDS, description="Conecta al bot al canal de voz")
    async def conectar(self, ctx: commands.Context) -> None:
        if not ctx.voice_client:
            await ctx.author.voice.channel.connect(cls=wavelink.Player)
        else:
            ctx.voice_client
        embed = discord.Embed(title="🔊 Conectado", description="Me he conectado al canal de voz.", color=EMBED_COLOR)
        await ctx.respond(embed=embed)

    @musica.command(name="leave", guild_ids=GUILD_IDS, description="Desconecta al bot del canal de voz")
    async def desconectar(self, ctx: commands.Context) -> None:
        vc: wavelink.Player = ctx.voice_client
        await vc.disconnect()
        await self.bot.user.edit(avatar=open("../resources/images/pype.png", "rb").read())
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Concord"))
        embed = discord.Embed(title="🔊 Desconectado", description="Me he desconectado del canal de voz.", color=EMBED_COLOR)
        await ctx.respond(embed=embed)

    @musica.command()
    async def ahora(self, ctx: commands.Context) -> None:
        vc: wavelink.Player = ctx.voice_client
        track: wavelink.Track = vc.current
        embed = discord.Embed(title="🎶 Canción actual", description=track.title + " de " + track.author, color=EMBED_COLOR)
        await ctx.respond(embed=embed)

    @musica.command(name="volume", guild_ids=GUILD_IDS, description="Cambia el volumen del bot")
    async def volumen(self, ctx: commands.Context, volumen: int) -> None:
        vc: wavelink.Player = ctx.voice_client
        if volumen < 100:
            await vc.set_volume(volumen)
            embed = discord.Embed(title="🔊 Volumen", description="El volumen ha sido cambiado a " + str(volumen), color=EMBED_COLOR)
        else:
            embed = discord.Embed(title="🔊 Volumen", description="El volumen no puede ser mayor a 100.", color=EMBED_COLOR)
        await ctx.respond(embed=embed)

    @musica.command(name="loop", guild_ids=GUILD_IDS, description="Repite la canción o la cola")
    async def bucle(self, ctx: commands.Context, *, bucle = "current") -> None:
        vc: wavelink.Player = ctx.voice_client
        if bucle == "current":
            vc.queue.loop = True
            embed = discord.Embed(title="🔁 Repetir", description="La canción se repetirá indefinidamente.", color=EMBED_COLOR)
        elif bucle == "all":
            vc.queue.loop_all = True
            embed = discord.Embed(title="🔁 Repetir", description="La cola se repetirá indefinidamente.", color=EMBED_COLOR)
        elif bucle == "off":
            vc.queue.loop = False
            vc.queue.loop_all = False
            embed = discord.Embed(title="🔁 Repetir", description="La repetición ha sido desactivada.", color=EMBED_COLOR)
        await ctx.respond(embed=embed)

    @musica.command(name="seek", guild_ids=GUILD_IDS, description="Avanza la canción x segundos")
    async def avanzar(self, ctx: commands.Context, segundos: int) -> None:
        vc: wavelink.Player = ctx.voice_client
        await vc.seek(segundos*1000)
        embed = discord.Embed(title="⏩ Avanzar", description="Se han adelantado " + str(segundos) + "s.", color=EMBED_COLOR)
        await ctx.respond(embed=embed)

    @musica.command(name="queue", guild_ids=GUILD_IDS, description="Muestra la cola de canciones")
    async def cola(self, ctx: commands.Context) -> None:
        vc: wavelink.Player = ctx.voice_client
        cola = vc.auto_queue
        embed = discord.Embed(title="🎶 Cola", description="", color=EMBED_COLOR)
        i = 1
        for track in cola._queue:
            embed.add_field(name=f"Canción nº{i}", value=f"{track.title} de {track.author}", inline = False)
            i+=1
        await ctx.respond(embed=embed)

    @musica.command(name="skip", guild_ids=GUILD_IDS, description="Salta a la siguiente canción")
    async def saltar(self, ctx: commands.Context) -> None:
        vc: wavelink.Player = ctx.voice_client
        await vc.play(vc.auto_queue.get()) 
        embed = discord.Embed(title="⏭️ Saltar", description=f"Se ha saltado a la siguiente canción", color=EMBED_COLOR)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Music(bot))