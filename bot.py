import discord
from discord.ext import commands
import asyncio
import os
import json

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)

CONFIG_FILE = "config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE) as f:
        return json.load(f)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            await bot.load_extension(f"cogs.{file[:-3]}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(os.getenv("TOKEN"))

asyncio.run(main())