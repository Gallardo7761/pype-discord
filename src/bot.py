import discord
from settings import BOT_TOKEN
from os import listdir
from utils.logger.pype_logger import PypeLogger

bot = discord.Bot(intents=discord.Intents.all())

def load_cogs():
    for file in listdir("./cogs"):
        if(file.endswith(".py")):
            try:
                bot.load_extension(f"cogs.{file[:-3]}")
                PypeLogger.info(f"{file[:-3]} has been loaded")
            except Exception as e:
                PypeLogger.error(f"Error loading {file[:-3]}",e)

def main():
    load_cogs()
    bot.run(BOT_TOKEN)

if __name__ == "__main__":
    main()
