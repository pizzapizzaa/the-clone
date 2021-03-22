import discord, json, asyncio, os, platform, sys
from discord.ext import tasks, commands
from dotenv import load_dotenv

# Loads the .env file that resides on the same level as the script.
load_dotenv()

client = discord.Client()

responses = {
    "WHAT'S YOUR NAME?": "My name is ChatBot!",
    "COOKIE": ":cookie:"
}



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message) :
    content = message.content.upper()
    if content in responses:
        await client.send_message(message.channel, responses[content])  
    

#@client.event
#async def on_message(message):
 #   if message.author == client.user:
  #      return

   # if message.content.startswith('$hello'):
    #    await message.channel.send('Hello!')


token = os.getenv("DISCORD_BOT_TOKEN")
client.run(token)

