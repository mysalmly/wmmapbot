import discord
from discord.ext import commands
import os
client = commands.Bot(command_prefix='.')
client.remove_command("help")

@client.event
async def on_ready():
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'discord.gg/V5K6GsBvpJ | . help'))

# Load cogs
extensions = [ "cogs.help","cogs.play", "cogs.Islam","cogs.meme", "cogs.info", "cogs.Hidden", "cogs.Moderation", "cogs.purge" ]

print(extensions)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run("ODk5NzMzMzY2MzI3MzQ1MTgy.YW3D_g.rkzoA31nHEeFgWArayZ66XcKfS0")

