import discord
from discord.ext import commands
import config

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="shloopy"))

# Load cogs
async def setup_hook():
    await bot.load_extension("cogs.general")

bot.setup_hook = setup_hook

if __name__ == "__main__":
    bot.run(config.TOKEN)
