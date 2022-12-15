import os
import discord
import time
import requests
from keep_alive import keep_alive
import logging

TOKEN = os.environ['TOKEN']
PUSH_URL = os.environ['PUSH_URL']


class MyClient(discord.Client):
    async def on_ready(self):
        now_time = time.strftime('[%Y-%m-%d %H:%M:%S]',
                                 time.localtime(time.time()))
        print(now_time + 'Logged on as',self.user)

    async def on_message(self, message):
        now_time = time.strftime('[%Y-%m-%d %H:%M:%S]',
                                 time.localtime(time.time()))
        print(now_time + message.content)

        #push msg
        if "Wei" in message.content or "Mokamoka" in message.content or \
         "Madnick" in message.content:
            try:
                url = PUSH_URL + message.content
                res = requests.get(url)
                print(now_time + res.text)
            except:
                print(now_time + "!!! push qq msg fail!!!" + res.text)
        #print("*" * 75)

        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
keep_alive()

try:
    client.run(TOKEN)
except:
    os.system("kill 1")