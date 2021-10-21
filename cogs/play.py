import discord
from discord.ext import commands
import random
Salams = ["Assalamualaikum", "asc", "Asc", "Salam"]
client = commands.Bot

class play(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client

    
    @commands.Cog.listener()
    async def on_message(self, message):
        for i in range (len(Salams)):
            if Salams[i]in message.content:
                for j in range(1):
                    await message.channel.send("وَعَلَيْكُمُ ٱلسَّلَامُ وَرَحْمَةُ ٱللَّٰهِ وَبَرَكَاتُهُ")

    
    
    
    
    @commands.command(aliases = ['p', "pingerino"])
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


    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        responses = [
        'Hell no.',
        'Probably not.',
        'Idk bro.',
        'Probably.',
        'Hell yeah my dude.',
        'It is certain.',
        'It is decidedly so.',
        'Without a Doubt.',
        'Yes - Definitely.',
        'You may rely on it.',
        'As i see it, Yes.',
        'Most Likely.',
        'Outlook Good.',
        'Yes!',
        'No!',
        'Signs a point to Yes!',
        'Reply Hazy, Try again.',
        'IDK',
        'Better not tell you know.',
        'Cannot predict now.',
        'Concentrate and ask again.',
        "Don't Count on it.",
        'My reply is No.',
        'My sources say No.',
        'Outlook not so good.',
        'Very Doubtful']
        await ctx.send(f':8ball: Question: {question}\n:8ball: answer:{random.choice(responses)}')

def setup(client:commands.Bot):
    client.add_cog(play(client))