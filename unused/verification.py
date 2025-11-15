from discord.ext import commands
from discord.commands import SlashCommandGroup
from settings import (
    GUILD_IDS, VERIFICATION_CHANNEL_ID, VERIFIED_ROLE_ID, UNVERIFIED_ROLE_ID, SUPPORT_ROLE_ID
)
import asyncio

class Verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    verification = SlashCommandGroup("verification", "Verify through the bot", guild_ids=GUILD_IDS)

    @verification.command(name="verify", guild_ids=GUILD_IDS, description="Verify yourself in the server using a command.")
    async def verificar(self, ctx):
        if ctx.channel.id == VERIFICATION_CHANNEL_ID:
            verified = ctx.guild.get_role(VERIFIED_ROLE_ID)
            unverified = ctx.guild.get_role(UNVERIFIED_ROLE_ID)
            support_role = ctx.guild.get_role(SUPPORT_ROLE_ID)

            if verified not in ctx.author.roles:
                await ctx.author.add_roles(unverified)
                await ctx.send(f"{ctx.author.mention}, please specify your origin (CurseForge/SpigotMC) or enter the secret code to get verified.")

                try:
                    # Esperar la respuesta del usuario en el mismo canal
                    response = await self.bot.wait_for(
                        "message",
                        check=lambda message: message.author == ctx.author and message.channel == ctx.channel,
                        timeout=120  # Puedes ajustar el tiempo límite según tus necesidades
                    )

                    # Verificar la respuesta del usuario
                    if "CurseForge" in response.content or "SpigotMC" in response.content:
                        await ctx.author.add_roles(support_role)
                        await ctx.author.remove_roles(unverified)
                        await ctx.send(f"{ctx.author.mention} has been verified from CurseForge or SpigotMC!")
                        await ctx.channel.purge(limit=100)
                    elif "cHV0b3RvbnRvWEQ=" in response.content:
                        await ctx.author.add_roles(verified)
                        await ctx.author.remove_roles(unverified)
                        await ctx.send(f"{ctx.author.mention} has been verified using the secret code!")
                        await ctx.channel.purge(limit=100)
                    else:
                        await ctx.respond("Invalid response. Please specify CurseForge/SpigotMC or the secret code.", ephemeral=True)

                except asyncio.TimeoutError:
                    await ctx.respond("Verification process timed out. Please run the command again.", ephemeral=True)

            else:
                await ctx.respond("You are already verified.", ephemeral=True)
        else:
            await ctx.respond(f"You can only verify in <#{VERIFICATION_CHANNEL_ID}>.", ephemeral=True)

def setup(bot):
    bot.add_cog(Verification(bot))