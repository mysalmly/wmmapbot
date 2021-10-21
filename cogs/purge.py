import discord
from discord.ext import commands

class purge(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.bot = client

    @commands.command(aliases = ['clear'])
    async def purge(self, ctx, amount=11):
        if (not ctx.author.guild_permissions.manage_messages):
            await ctx.send("You do not have the permission `manage messages`")
            return
        amount = amount +1
        if amount > 501:
            await ctx.send("You cannot delete more than that")
        else:
            await ctx.channel.purge(limit=amount)
            await ctx.send('Cleared messages')


