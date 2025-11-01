import time
import discord
import matplotlib.pyplot as plt
import numpy as np
from discord.ext import commands
from discord.commands import SlashCommandGroup
from matplotlib.patches import Circle
from settings import EMBED_COLOR, GUILD_IDS
from utils.bot import esPar, esPrimo

class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    mates = SlashCommandGroup("mates", "Comandos de Matemáticas", guild_ids=GUILD_IDS)

    @mates.command(name='contar', guild_ids=GUILD_IDS, description="Cuenta desde a hasta b.")
    async def contar(self, ctx, a: int, b: int):
        await ctx.respond(f"*Contando desde {a} hasta {b}...*", ephemeral=True)
        i = a
        time.sleep(1)
        await ctx.send(a)
        time.sleep(1)
        for i in range(a, b):
            await ctx.send(str(i+1))
            time.sleep(1)

    @mates.command(name="calc", guild_ids=GUILD_IDS, description="Resuelve una expresión matemática.")
    async def calc(self, ctx, *, expresion):
        embed = discord.Embed(color=discord.Color(EMBED_COLOR))
        embed.add_field(name="**Resultado**",
                        value=f"{expresion} = " + str(eval(expresion)))
        await ctx.respond(embed=embed)

    @mates.command(name="par", guild_ids=GUILD_IDS, description="Dice si un número es par o no.")
    async def par(self, ctx, numero: int):
        numres = esPar(numero)
        embed = discord.Embed(color=discord.Color(EMBED_COLOR))
        embed.add_field(name="**Resultado**", value=numres)
        await ctx.respond(embed=embed)

    @mates.command(name="primo", guild_ids=GUILD_IDS, description="Dice si un número es primo o no.")
    async def primo(self, ctx, numero: int):
        numres = esPrimo(numero)
        embed = discord.Embed(color=discord.Color(EMBED_COLOR))
        embed.add_field(name="**Resultado**", value=numres)
        await ctx.respond(embed=embed)

    @mates.command(name='grafseno', guild_ids=GUILD_IDS, description="Grafica una función seno (a, k).")
    async def grafseno(self, ctx, a: int, k: int):
        x = np.linspace(0, 2*np.pi, 400)
        y = a * np.sin(k*x)
        plt.axhline(0, color="black")
        plt.plot(x, y, color="#b2122f")
        plt.savefig("../resources/images/graphics/graf.png")
        await ctx.respond(file=discord.File("../resources/images/graphics/graf.png"))
        plt.clf()

    @mates.command(name='grafcoseno', guild_ids=GUILD_IDS, description="Grafica una función coseno (a, k).")
    async def grafcoseno(self, ctx, a: int, k: int):
        x = np.linspace(0, 2*np.pi, 400)
        y = a * np.cos(k*x)
        plt.axhline(0, color="black")
        plt.plot(x, y, color="#b2122f")
        plt.savefig("../resources/images/graphics/graf.png")
        await ctx.respond(file=discord.File("../resources/images/graphics/graf.png"))
        plt.clf()

    @mates.command(name='grafrecta', guild_ids=GUILD_IDS, description="Grafica una función lineal (m, n).")
    async def grafrecta(self, ctx, m: int, n: int):
        def f(x):
            return m*x+n
        x = range(-10000, 10000)
        y = [f(i) for i in x]
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.xlim(-10, 10)
        plt.ylim(-20, 20)
        plt.plot(x, y, color="#b2122f")
        plt.savefig("../resources/images/graphics/graf.png")
        await ctx.respond(file=discord.File("../resources/images/graphics/graf.png"))
        plt.clf()

    @mates.command(name='grafparabola', guild_ids=GUILD_IDS, description="Grafica una parábola (a, b, c).")
    async def grafparabola(self, ctx, a: int, b: int, c: int):
        def f(x):
            return a*(x*x)+b*x+c
        x = np.linspace(-10, 10, 1000)
        y = [f(i) for i in x]
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.xlim(-10, 10)
        plt.ylim(-20, 20)
        plt.plot(x, y, color="#b2122f")
        plt.savefig("../resources/images/graphics/graf.png")
        await ctx.respond(file=discord.File("../resources/images/graphics/graf.png"))
        plt.clf()

    @mates.command(name='grafcircunferencia', guild_ids=GUILD_IDS, description="Grafica una circunferencia (r).")
    async def grafcircunferencia(self, ctx, r: int):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        circle1 = Circle((0, 0), r, color='r')
        ax.add_artist(circle1)
        plt.xlim(-10, 10)
        plt.ylim(-10, 10)
        plt.savefig("../resources/images/graphics/graf.png")
        await ctx.respond(file=discord.File("../resources/images/graphics/graf.png"))
        plt.clf()
    
    @mates.command(name='graflog', guild_ids=GUILD_IDS, description="Grafica una función logarítmica (a, b).")
    async def graflog(self, ctx, a: int, b: int):
        def f(x):
            return a*np.log(x)+b
        x = np.linspace(-10, 10, 1000)
        y = [f(i) for i in x]
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.xlim(-10, 10)
        plt.ylim(-20, 20)
        plt.plot(x, y, color="#b2122f")
        plt.savefig("../resources/images/graphics/graf.png")
        await ctx.respond(file=discord.File("../resources/images/graphics/graf.png"))
        plt.clf()

    @mates.command(name='grafexp', guild_ids=GUILD_IDS, description="Grafica una función exponencial (a, b).")
    async def grafexp(self, ctx, a: int, b: int):
        def f(x):
            return a*np.exp(b*x)
        x = np.linspace(-10, 10, 1000)
        y = [f(i) for i in x]
        plt.axhline(0, color="black")
        plt.axvline(0, color="black")
        plt.xlim(-10, 10)
        plt.ylim(-20, 20)
        plt.plot(x, y, color="#b2122f")
        plt.savefig("../resources/images/graphics/graf.png")
        await ctx.respond(file=discord.File("../resources/images/graphics/graf.png"))
        plt.clf()

def setup(bot):
    bot.add_cog(Math(bot))