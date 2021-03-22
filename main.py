import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

prefix = "liv"
bot = commands.Bot(command_prefix=prefix)
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

#Bot online message
@bot.event
async def on_ready():
    print("Livy's clone is online")

#Bot message history
@bot.event
async def on_message(message):
    print("The message's content was", message.content)
    await bot.process_commands(message)

#Bot ping
@bot.command()
async def ping(ctx):
    '''
    Let you know the real-time latency
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

#Bot echo commands
@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)

#bot run
bot.run(TOKEN)