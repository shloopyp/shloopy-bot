import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Check bot latency"""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

    @commands.command()
    async def hello(self, ctx):
        """Say hello"""
        await ctx.send("Hello! I'm shloopy's clone!")

async def setup(bot):
    await bot.add_cog(General(bot))
