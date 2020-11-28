import requests
import random

how_are_you_answer = ["I'm good, thanks! You?", "I'm feeling... robotic. How about you?", "I am aaallll right! And you?"]

positive_answer = ["Great!", "Excellent!", "Super!", "Fantastic!"]


async def get_response(message):
    if "how are you" in message.content or "how do you feel" in message.content or "what's up" in message.content:
        await message.channel.send(how_are_you_answer[random.randint(0, len(how_are_you_answer)-1)])
    elif "very good" in message.content or "fine" in message.content or "good" in message.content:
        await message.channel.send(positive_answer[random.randint(0, len(positive_answer)-1)])
    elif "joke" in message.content:
        chuckJoke = requests.get('http://api.icndb.com/jokes/random?')
        if chuckJoke.status_code == 200:
            chuckJoke = chuckJoke.json()['value']['joke']
            await message.channel.send(chuckJoke)

