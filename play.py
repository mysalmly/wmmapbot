import discord
from discord.ext import commands
import random

class play(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        latency = self.client.latency
        tlatency = latency * 1000
        await ctx.send(f'Pong! it takes me {round(tlatency)} milliseconds to respond')

    @commands.command()
    async def rps(self, ctx, message):
        answer = message.lower()
        choices = ["rock", "paper", "scissors"]
        computers_answer = random.choice(choices)
        if answer not in choices:
            await ctx.send("Not a valid option please use either: rock, paper or scissors")
        else:
            if computers_answer == answer:
                await ctx.send("Tie! we both picked " + answer) #tie for both answers
            if computers_answer == "rock":
                if answer == "paper":
                    await ctx.send("You win! my choice was.." + computers_answer + " and you chose "  + answer + " !")# rock-paper-you win
            if computers_answer == "paper":
                if answer == "rock":
                    await ctx.send("I win! my choice was.." + computers_answer + " and you chose " + answer + " !") # paper rock i win
            if computers_answer == "scissors":
                if answer == "rock":
                    await ctx.send("You win! my choice was.." + computers_answer + " and you chose " + answer + " !") #scissors rock you win
            if computers_answer == "rock":
                if answer == "scissors":
                    await ctx.send("I win! my choice was.." + computers_answer + " and you chose " + answer + " !")    # rock scissors i win  
            if computers_answer == "paper":
                if answer == "scissors":
                    await ctx.send("You win! my choice was.." + computers_answer + " and you chose " + answer + " !") # paper scissors you win
            if computers_answer == "scissors":
                if answer == "paper":
                    await ctx.send("I win! my choice was.." + computers_answer + "and you chose " + answer + " !") # paper scissors i win

def setup(client:commands.Bot):
    client.add_cog(play(client))