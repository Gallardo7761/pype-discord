import discord
from discord.ext import commands
from settings import (
    EMBED_COLOR, BOT_NAME, ADMIN_CHANNEL_ID, BOT_LOGO, COUNTER_CHANNEL_ID, 
    WELCOME_CHANNEL_ID, UNVERIFIED_ROLE_ID, VERIFIED_ROLE_ID
)
from utils.logger.pype_logger import PypeLogger
import asyncio
from utils.bot import bot_status_randomizer
from utils.files import read, write

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_ready(self):
        PypeLogger.success(f"Logged in as {self.bot.user.name}#{self.bot.user.discriminator}")
        channel = self.bot.get_channel(ADMIN_CHANNEL_ID)
        embed = discord.Embed(title = f"{BOT_NAME} Console", 
            description = "```✅ | Logged in as Pype#6125\n🐍 | Estoy listo pa\n🐍 | >>>```", 
            color=discord.Color(EMBED_COLOR))
        await channel.send(embed=embed)
        await self.bot.user.edit(avatar=open("../"+BOT_LOGO, "rb").read())
        while True:
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, 
                name=bot_status_randomizer("../resources/files/shows.txt")))
            await asyncio.sleep(60)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, 
                name=bot_status_randomizer("../resources/files/juegos.txt")))
            await asyncio.sleep(60)
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, 
                name=bot_status_randomizer("../resources/files/grupos.txt")))
            await asyncio.sleep(60)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author != self.bot.user:
            if message.channel.id == COUNTER_CHANNEL_ID:
                if message.author != self._last_member:
                    try:
                        # Evaluar el contenido del mensaje como una expresión matemática
                        numero = int(eval(message.content))
                        file = "../resources/files/counter.csv"
                        n = int(read(file))
                        
                        if numero == n + 1:
                            await message.add_reaction("✅")
                            self._last_member = message.author
                            n += 1
                            write(file, str(n))
                        else:
                            await message.add_reaction("❌")
                            await message.channel.send(f"{message.author.mention} falló, reseteando el contador.")
                            write(file, "0")
                    except (ValueError, SyntaxError):
                        await message.delete()
                else:
                    await message.delete()


    @commands.Cog.listener()
    async def on_member_join(self, member):
        bienvenidas = self.bot.get_channel(WELCOME_CHANNEL_ID)
        """defaultrole = member.guild.get_role(UNVERIFIED_ROLE_ID)
        verifiedrole = member.guild.get_role(VERIFIED_ROLE_ID)
        if member.guild.get_role(VERIFIED_ROLE_ID) in member.roles: 
            await member.remove_roles(verifiedrole)
        await member.add_roles(defaultrole)"""
        await bienvenidas.send(f"¡Bienvenido {member.mention}! Espero que te lo pases bien en el servidor. Recuerda leer las <#1092518793143652352> para evitar ser sancionado. ¡Diviértete! :D")

    @commands.Cog.listener()
    async def on_member_leave(self, after):
        adminchannel = self.bot.get_channel(ADMIN_CHANNEL_ID)
        await adminchannel.send(f"**{after.name}** ha abandonado el servidor")   

    @commands.Cog.listener()
    async def on_application_command(self, ctx):
        PypeLogger.command(f"{ctx.author} ha ejecutado el comando {ctx.command} en {ctx.guild.name}.")

def setup(bot):
    bot.add_cog(Events(bot))