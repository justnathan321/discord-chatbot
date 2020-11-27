import random
import discord
import time
import asyncio

from discord.ext import commands

client = discord.Client()

TOKEN = ""

msg_greetings = ["Hey", "Whats up?", "I'm always here!", "Heya! Let's talk.", "I would like to!", "Let's have a chat",
                 "Hey, let's talk!",
                 "https://giphy.com/gifs/raydonovan-season-6-episode-10-ray-donovan-57UyhoLuq6n81uiHkt",
                 "https://giphy.com/gifs/raydonovan-season-7-ray-donovan-708-l3b1jcyA73gz3vveI8",
                 "https://giphy.com/gifs/YourHappyWorkplace-your-happy-workplace-wendy-conrad-lets-talk-vfoz5YXYqyGcdoJCf1",
                 "https://giphy.com/gifs/DrSquatchSoapCo-lets-talk-wecantalk-we-can-ehCBaednkq0KBpppwt"]

msg_start_1 = "can someone talk"


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return

    if message.content.startswith(msg_start_1):
        await message.channel.send(msg_greetings[random.randint(0, len(msg_greetings) - 1)])


@client.event
async def on_ready():
    print("RUNNING")


client.run(TOKEN)
