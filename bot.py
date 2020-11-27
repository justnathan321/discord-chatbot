import random
import discord
import time
import asyncio

from discord.ext import commands

client = discord.Client()

TOKEN = "NzgxOTQ2MDY4Njg2NDcxMTk4.X8FCBg.H-0m4UN0JwYfw0xIzwwsnlh67B0"

greetings = ["Hey", "Whats up?", "I'm always here!", "Heya!", "I would like to!", "Let's have a chat"]


@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return

    if message.content.startswith("can someone talk with me"):
        await message.channel.send(greetings[random.randint(0, 5)])


@client.event
async def on_ready():
    print("RUNNING")


client.run(TOKEN)
