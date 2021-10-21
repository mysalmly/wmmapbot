import discord
from discord.ext import commands


class Hidden(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client

    @commands.command()
    async def uh(self, ctx):
        em = discord.Embed
        em.add_field(name = "uh", value = "you found a hidden command there are 9 more of these find them all for **Secret**")
        await ctx.send(embed = em)

    @commands.command()
    async def supersecretcommandnooneknowsabout(self, ctx):
        embed = discord.Embed(name="CONGRATS 🎉", value=f"You have found the super secret command now .kick {ctx.author} ")

    @commands.command()
    async def report(self, ctx):
        await ctx.send("A link to an important news report ^^! : https://www.youtube.com/watch?v=xfr64zoBTAQ&t=5s")


def setup(client:commands.Bot):
    client.add_cog(Hidden(client))