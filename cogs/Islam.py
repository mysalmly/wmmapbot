# for islamic commands
import discord
from discord.ext import commands
import random


class Islam(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client = client

    @commands.command(aliases = ["if", "islamicfact"])
    async def Islamicfact(self, ctx):
        islamicfax = ["The Arabic root word for Islam means submission, obedience, peace, and purity. In a religious context, it means `voluntary submission to God` ", "It’s the second largest religion in the world (1.8billion)", "Muslims should pray 5 times a day also known as Salah. Every Muslim should pray five times a day at specific times as of the following: \n`Salat al-fajr: dawn, before sunrise` \nSalat al-zuhr: `midday, after the sun passes its highest`, \nSalat al-‘asr: `the late part of the afternoon` ,\nSalat al-maghrib: `just after sunset` \nSalat al-‘isha: `between sunset and midnight`", "The Quran is the holy book", "Just like the Torah in Judaism and the Bible in Christianity, the Quran is the holy book within the Islamic faith. ", "There are five pillars: Shahada – The declaration of faith. The Salah, or Salat – The five daily prayers Zakat – The practice of charitable giving Sawm – The fasting Haji – The Pilgrimage to Mecca", "The original Arabic text of the Quran has not been altered", "The Islamic calendar started in 622 AD"]
        await ctx.send(random.choice(islamicfax))


    @commands.command(aliases = ["rh", "randomhadith"])
    async def ranhadith(self, ctx):
        hadiths = ["The Prophet of Allah, sallallahu alayhee wa alehee wasalam said: “Religion is sincerity.” We said: “To whom, O the Prophet of Allah?” He said: “To Allah, His Book, His Messenger, to the leaders of the Muslims and their common folk.” ", "“Islam necessitates having good moral qualities.” ", "Whoever is not merciful (to the creation) will not be shown mercy by Allah.", "“Whoever opens a way to a charitable deed is like the one that has done this good deed (himself).“", "“Fear Allah wherever you are. Do good immediately after a sinful act to erase it, and always be well-mannered in your relationship with people.”", "“None of you will have true faith till he wishes for his (Muslim) brother what he likes for himself.” " ]
        await ctx.send(random.choice(hadiths))


    @commands.command(aliases = ["qf"])
    async def quranfact(self, ctx):
        quranfax = ["The Holy Quran has 114 surahs & The Holy Quran has 30 parts", "The revelation started in the Holy month of Ramadan", "Quran was revealed over 23 years: 13 in Mecca and 10 in Madina", "Whoever reads one letter of the Quran gets 10 Rewards", "Baqarah is the longest sura but Kawthar is the shortest sura", "Quran was revealed to Prophet Muhammad (PBUH) through the angel Jibril", "Prophet (PBUH) was 40 years old when the first verse of Quran was revealed to Him", "The literal meaning of Quran is “that which is being read”", "25 Prophets are mentioned in the Holy Quran"]
        await ctx.send(random.choice(quranfax))
def setup(client:commands.Bot):
    client.add_cog(Islam(client))