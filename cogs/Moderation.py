import discord
from discord.ext import commands
client = commands.Bot(command_prefix='.')


class Mod(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f"{member} was banned!")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member} was kicked!")

def setup(client:commands.Bot):
    client.add_cog(Mod(client))