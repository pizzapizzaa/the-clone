import discord, asyncio, os, platform, sys
from discord.ext import tasks, commands
import os

client = discord.Client()
#token = os.getenv('DISCORD_TOKEN')



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

token = os.getenv("DISCORD_BOT_TOKEN")
client.run(token)

