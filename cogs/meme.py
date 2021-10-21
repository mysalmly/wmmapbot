import discord
from discord.ext import commands
import aiohttp
import random
import os
client = commands.Bot(command_prefix='.')



class meme(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client

    @commands.command()
    async def meme(self, ctx):
      async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/IslamicHistoryMeme/.json") as r:
          memes = await r.json()
          embed = discord.Embed(
              color = discord.Color.purple()
            )
          embed.set_image(url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
          embed.set_footer(text=f"Powered by r/Islamichistorymeme | Meme requested by {ctx.author}")
          await ctx.send(embed=embed)


def setup(client:commands.Bot):
    client.add_cog(meme(client))