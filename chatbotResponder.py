from datetime import datetime

import requests
import random
import discord
import pandas as pd

how_are_you_answer = ["I'm good, thanks! You?", "I'm feeling... robotic. How about you?",
                      "I am aaallll right! And you?"]

positive_answer = ["Great!", "Excellent!", "Super!", "Fantastic!"]

small_talk = ['how are you?',
              'how do you feel?',
              'that is great',
              'too bad... sorry to hear that',
              'glad to hear that!',
              'sorry to hear that...',
              'excellent, glad to hear that',
              'i am fine, thank you',
              'i feel awesome',
              'i feel... robotic?',
              'i am a robot, i feel robotic!',
              'ask me a funny joke, please.',
              'please ask me a funny joke',
              'i want to tell you a joke, please ask me for one']

api_key_weather = "3a74041e01a5ae1fe0889735c8cce3d3"
base_url_weather = "http://api.openweathermap.org/data/2.5/weather?"


async def get_response(message):
    if "how are you" in message.content or "how do you feel" in message.content or "what's up" in message.content:
        await message.channel.send(how_are_you_answer[random.randint(0, len(how_are_you_answer) - 1)])
    elif "very good" in message.content or "fine" in message.content or "good" in message.content:
        await message.channel.send(positive_answer[random.randint(0, len(positive_answer) - 1)])
    elif "joke" in message.content:
        chuckJoke = requests.get('http://api.icndb.com/jokes/random?')
        if chuckJoke.status_code == 200:
            chuckJoke = chuckJoke.json()['value']['joke']
            await message.channel.send(chuckJoke)
    elif "weather" in message.content:
        await weather(city="Antwerp", ctx=message)
        await message.channel.send("That's the climate in Antwerp, " + message.author.name + " :-)")
        await message.channel.send("Sometimes people wonder why I only know the climate in Antwerp... BECAUSE THATS WHERE I LIVE OKAY. I am not Google.")


async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url_weather + "appid=" + api_key_weather + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.channel
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}",
                                  color=ctx.guild.me.top_role.color,
                                  timestamp=datetime.now(), )
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            await channel.send(embed=embed)
    else:
        await channel.send("City not found.")
