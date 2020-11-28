# Author: Nathan Tetroashvili
# Version: Work in progress
# Discord bot that will start a conversation with you
# How to start conversation: type (check msg_start) in chat
# How to end conversation: type (check msg_stop) in chat

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import datetime
import requests
import random
import discord
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatbotResponder
import asyncio
from discord.ext import commands

# Defining discord client
client = discord.Client()

# Discord Bot Token
TOKEN = "NzgxOTQ2MDY4Njg2NDcxMTk4.X8FCBg.KHeXilMFssaRDBIeM_AXlfienVk"
# Array with greetings that will pop up after the start conversation msg
msg_greetings = ["Hey", "Whats up?", "I'm always here!", "Heya! Let's talk.", "I would like to!", "Let's have a chat",
                 "Hey, let's talk!",
                 "https://giphy.com/gifs/raydonovan-season-6-episode-10-ray-donovan-57UyhoLuq6n81uiHkt",
                 "https://giphy.com/gifs/raydonovan-season-7-ray-donovan-708-l3b1jcyA73gz3vveI8",
                 "https://giphy.com/gifs/YourHappyWorkplace-your-happy-workplace-wendy-conrad-lets-talk"
                 "-vfoz5YXYqyGcdoJCf1",
                 "https://giphy.com/gifs/DrSquatchSoapCo-lets-talk-wecantalk-we-can-ehCBaednkq0KBpppwt"]

# Array with goodbye texts
msg_bye = ["Well... We had a great talk! Goodbye.", "Hope to talk to you again soon. Bye X", "Such a bummer! Had a "
                                                                                             "great time with you. "
                                                                                             "Lets talk again very "
                                                                                             "soon!"]
# Msg of client to start the conversation
msg_start = "hey voca"
# Msg of client to stop the conversation
msg_stop = "bye voca"
# Bool conversation started, false if not
conv_started = False


# Create chatbot
#  If you wish to disable the bot’s ability to learn after the training, you can include the “read_only=True” command.
#  “logic_adapters” denotes the list of adapters used to train the chatbot.
#  “chatterbot.logic.MathematicalEvaluation” helps the bot to solve math problems,
#  “chatterbot.logic.BestMatch” helps it to choose the best match from the list of responses already provided.
# my_bot = ChatBot(name="ChatBot",
#                 logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])
# Responses to train chatbot
# TO-DO

# Train the bot by writing an instance of “ListTrainer” and supplying it with a list of strings
# list_trainer = ListTrainer(my_bot)
# for item in (small_talk, joke_talk):
#    list_trainer.train(item)

# corpus_trainer = ChatterBotCorpusTrainer(my_bot)
# corpus_trainer.train('chatterbot.corpus.english')


# Discord event
@client.event
# When message is sent by client
# When message is sent by client
async def on_message(message):
    global conv_started
    if message.author == client.user:
        return
    # Make message content lowercase
    message.content = message.content.lower()
    if message.content.startswith(msg_start):
        if conv_started:
            await message.channel.send(
                "We are in a conversation already? :-( \nDid you just try to drop me?\nType **" + msg_stop + "** to "
                                                                                                             "stop "
                                                                                                             "this "
                                                                                                             "conversation.")
        else:
            await message.channel.send(msg_greetings[random.randint(0, len(msg_greetings) - 1)])
            emoji = '\N{THUMBS UP SIGN}'
            await message.add_reaction(emoji)
            conv_started = True
            print(
                "CONVERSATION STARTED: '" + message.content + "' by " + message.author.name + " at " + datetime.now().strftime(
                    "%H:%M:%S"))
            await message.channel.send(
                "From now on we are in a conversation! Type **'" + msg_stop + "'** to stop this "
                                                                              "conversation.\n" + "Alright, **" + message.author.name + "**, tell me, "
                                                                                                                                        "what do you want to "
                                                                                                                                        "talk about?")
    elif message.content.startswith(msg_stop):
        if conv_started:
            await message.channel.send(
                msg_bye[random.randint(0, len(msg_bye) - 1)])
            conv_started = False
    elif conv_started:
        # get a respone from the chatbot
        await chatbotResponder.get_response(message)


# Discord event
@client.event
# When bot is ready/running, print "RUNNING"
async def on_ready():
    print("RUNNING")
    await client.change_presence(activity=discord.Game(name='Ready to talk with you'))


# Run bot
# Param = TOKEN (Bot token)
client.run(TOKEN)
