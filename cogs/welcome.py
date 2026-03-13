import discord
from discord.ext import commands
import json
from utils.image import create_card

CONFIG_FILE = "config.json"

def load_config():
    with open(CONFIG_FILE) as f:
        return json.load(f)

class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

        config = load_config()
        channel_id = config.get("welcome_channel")

        channel = self.bot.get_channel(channel_id)

        if not channel:
            return

        card = await create_card(member, config)

        file = discord.File(card, "welcome.png")

        await channel.send(content=f"Welcome {member.mention}", file=file)

async def setup(bot):
    await bot.add_cog(Welcome(bot))