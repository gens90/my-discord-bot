import discord
from discord.ext import commands
import os

# -----------------------------
# PUT YOUR DISCORD BOT TOKEN HERE
# Option 1 (Recommended): Use environment variable
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Option 2 (Not recommended for public repos):
# TOKEN = "PASTE_YOUR_TOKEN_HERE"
# -----------------------------

intents = discord.Intents.default()
intents.message_content = True  # Required for reading messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I am your bot 🤖")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong 🏓")

bot.run(TOKEN)
