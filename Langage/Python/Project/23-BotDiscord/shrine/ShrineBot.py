import discord
from discord.ext import commands
from unidecode import unidecode

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)

class ShrineBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='/', intents=intents)


    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur.")


    async def respond(self, ctx):
        await ctx.send(f'Hey {ctx.author.name}')


    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            general_channel: discord.TextChannel = client.get_channel(978952267887697962)
            await general_channel.send(content=f"Coucou {member.display_name} !")

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def say(self, ctx, message):

        def get_message(self, ctx, message):
            message = ctx.message.content.split("!say", " ")
            
            return message

        await ctx.send(message) 


    # @commands.command(name='del')
    # async def delete(self, ctx, number_of_messages: int):
    #     messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    #     for each_message in messages:
    #         await each_message.delete()


    # async def on_message(self, message):
    #     string = unidecode(message.content).lower()
    #     print(string)
    #     if "fleur" in string:
    #         await message.channel.send("Grossier Merle")

    #         print(message.content)
