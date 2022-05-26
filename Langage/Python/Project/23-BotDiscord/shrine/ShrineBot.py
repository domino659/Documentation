from discord.ext import commands
from unidecode import unidecode

class ShrineBot(commands.Bot):
    def __init__(self, bot):
        super().__init__(bot)

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur.")


    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            general_channel: discord.TextChannel = client.get_channel(978952267887697962)
            await general_channel.send(content=f"Coucou {member.display_name} !")


    # @commands.command(name='del')
    # async def delete(self, ctx, number_of_messages: int):
    #     messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    #     for each_message in messages:
    #         await each_message.delete()


    async def on_message(self, message):
        string = unidecode(message.content).lower()
        print(string)
        if "fleur" in string:
            await message.channel.send("Grossier Merle")

            print(message.content)
 