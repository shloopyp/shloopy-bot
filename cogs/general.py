import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *, message: str):
        """Make the bot say something"""
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def embed(self, ctx, title: str, *, description: str):
        """Send a custom embed. Usage: !embed Title Here | Description here"""
        embed = discord.Embed(title=title, description=description, color=discord.Color.blue())
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int = 5):
        """Delete messages. Usage: !purge 10"""
        deleted = await ctx.channel.purge(limit=amount + 1)
        msg = await ctx.send(f"Deleted {len(deleted) - 1} messages.")
        await msg.delete(delay=3)

    @commands.command()
    async def ping(self, ctx):
        """Check bot latency"""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")

async def setup(bot):
    await bot.add_cog(General(bot))
