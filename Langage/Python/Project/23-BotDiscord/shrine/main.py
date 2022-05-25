import os

from utils import env
from ShrineBot import ShrineBot

import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Say (self,ctx,*,arg):

        def get_message(self, ctx, message):
            message = ctx.message.content.split("!say", " ")
            
            return message

        await ctx.send(message)

if __name__ == '__main__':
    shrine_bot = ShrineBot()
    shrine_bot.run(os.getenv("TOKEN"))
