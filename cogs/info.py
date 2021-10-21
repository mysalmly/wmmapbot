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


    @commands.command()
    async def userinfo(self, ctx):
        user = ctx.author

        embed=discord.Embed(title="USER INFO", description=f"Here is the info we retrieved about {user}", colour=user.colour)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="NAME", value=user.name, inline=True)
        embed.add_field(name="NICKNAME", value=user.nick, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="STATUS", value=user.status, inline=True)
        embed.add_field(name="TOP ROLE", value=user.top_role.name, inline=True)
        await ctx.send(embed=embed)


def setup(client:commands.Bot):
    client.add_cog(info(client))