# Author: Nathan Tetroashvili
# Version: Work in progress
# Discord bot that will start a conversation with you

import random
import discord
import asyncio
from discord.ext import commands

client = discord.Client()

# Discord Bot Token
TOKEN = ""
# Array with strings with greetings that will pop up after the start conversation msg
msg_greetings = ["Hey", "Whats up?", "I'm always here!", "Heya! Let's talk.", "I would like to!", "Let's have a chat",
                 "Hey, let's talk!",
                 "https://giphy.com/gifs/raydonovan-season-6-episode-10-ray-donovan-57UyhoLuq6n81uiHkt",
                 "https://giphy.com/gifs/raydonovan-season-7-ray-donovan-708-l3b1jcyA73gz3vveI8",
                 "https://giphy.com/gifs/YourHappyWorkplace-your-happy-workplace-wendy-conrad-lets-talk"
                 "-vfoz5YXYqyGcdoJCf1",
                 "https://giphy.com/gifs/DrSquatchSoapCo-lets-talk-wecantalk-we-can-ehCBaednkq0KBpppwt"]
# Msg of client to start the conversation
msg_start_1 = "can someone talk"
# Bool conversation started, false if not
conv_started = False


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
