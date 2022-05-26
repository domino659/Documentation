import os
import discord
from discord.ext import commands

from utils import env
from ShrineBot import ShrineBot

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)

if __name__ == '__main__':
    shrine_bot = ShrineBot(bot)
    shrine_bot.run(os.getenv("TOKEN"))
