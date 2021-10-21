#info commands i.e userinfo, serverinfo
import discord
from discord.ext import commands


class info(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client

    @commands.command()
    async def server(self, ctx):
        name = ctx.guild.name
        description = ctx.guild.description
        owner = ctx.guild.id
        region = ctx.guild.region
        membercount = ctx.guild.member_count

        icon = ctx.guild.icon_url

        em = discord.Embed(
            name = name + "Server information",
            description=description,
            color = discord.Color.blue()
            
            )
        em.set_thumbnail(url=icon)
        em.add_field(name="Owner", value = owner, inline=True)
        em.add_field(name="Server ID", value = id, inline=True)
        em.add_field(name="Current amount of members", value = membercount, inline=True)

        await ctx.send(embed=em)

def setup(client:commands.Bot):
    client.add_cog(info(client))