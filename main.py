import discord, json, asyncio, os, platform, sys
import random
from discord.ext import tasks, commands
from discord.ext.commands import Bot
from dotenv import load_dotenv

# Loads the token .env file that resides on the same level as the script.
load_dotenv()



description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

#bot = commands.Bot(command_prefix='p', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await bot.send_message(message.channel, msg)

#Get token and run the bot
token = os.getenv("DISCORD_BOT_TOKEN")
bot.run(token)





