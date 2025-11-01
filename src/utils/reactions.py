import discord

async def añadir_reacciones(message: discord.Message, reactions: str, n: int) -> None:
    reactions_list = reactions.split(";")
    for i in range(n):
        await message.add_reaction(reactions_list[i])
        i+=1