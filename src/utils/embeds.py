import discord
from discord.ext import commands
from settings import EMBED_COLOR, TIMEZONE
from datetime import datetime
import pytz

def crear_embed(ctx: commands.Context,
                title: str,
                description: str,    
                fields: str = None,
                footer_text: str = None,
                timestamp: bool = False,
                author_name: str = None,
                image_url: str = None,
                thumbnail_url: str = None,
                color: int = None):
    def bool_parser(string):
            if string.lower() == "true":
                return True
            elif string.lower() == "false":
                return False
            else:
                raise commands.BadArgument("El valor debe ser True o False")
    embed = discord.Embed(title=title, description=description, color=EMBED_COLOR)
    if fields:
        fields_list = fields.split(";;")
        for field in fields_list:
            name, value, inline = field.split(",,")
            embed.add_field(name=name, value=value, inline=bool_parser(inline))
    if footer_text:        
        embed.set_footer(text=footer_text)
    if image_url:
        embed.set_image(url=image_url)
    if thumbnail_url:
        embed.set_thumbnail(url=thumbnail_url)
    if author_name:
        embed.set_author(name=author_name, icon_url=ctx.author.avatar.url)
    if timestamp:
        embed.timestamp = datetime.now(pytz.timezone(TIMEZONE))
    if color:
        embed.color = color
    return embed