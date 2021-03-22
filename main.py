import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


# Handle the on member join event
@bot.event
async def on_member_join(member):
    # Create a direct message
    await member.create_dm()
    # Send the message
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

bot.run(TOKEN)