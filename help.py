#for help commands
import discord
from discord.ext import commands
client = commands.Bot(command_prefix='.')
client.remove_command("help")

class Help(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client

    @commands.command(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title = "Help", description = "A list of available commands" ,color = ctx.author.color )

        em.add_field(name = "Play", value = "`meme , ping , rps , helpFun `", inline = True)
        em.add_field(name = "Extra", value = "`userinfo, server`", inline = True)
        em.add_field(name = "islamic", value = "`Islamicfact  , ranhadith , quranfact `", inline = True)
        await ctx.send(embed = em)

    @commands.command()
    async def helpFun(self, ctx):
        em = discord.Embed(title = "Help", description = "A list of fun commands" ,color = ctx.author.color )

        em.add_field(name = "Commands", value = "`meme , ping , rps , Islamicfact`")
        
        await ctx.send(embed = em)




def setup(client:commands.Bot):
    client.add_cog(Help(client))

