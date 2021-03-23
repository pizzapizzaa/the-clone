import os
import discord
from discord.ext import commands, tasks
from discord.ext.commands import help
from dotenv import load_dotenv


prefix = "liv"
bot = commands.Bot(command_prefix=prefix, help_command=None)
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


#bot help
@bot.listen()
async def on_message(message):
   if message.content.lower().startswith('livhelp'):
        commands=[]
        commands['livping']='Show the real-time latency of the server.'
        commands['livecho']='Liv will chat what you want her to chat.'

        msg=discord.Embed(title='Chat with Livy\'s clone', description="Test",color=0x97ebdb)
        for command,description in commands.items():
            msg.add_field(name=command,value=description, inline=False)
            msg.add_field(name='Join Our Discord/For Questions/Chilling',value='https://discord.gg/JWSBzyNyg3', inline=False)
        await message.channel.send(embed=msg)


#Bot ping
@bot.command()
async def ping(ctx):
    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)

#Bot echo commands
@bot.command()
async def echo(ctx, *, content:str):
    '''
    echo command help goes here
    '''
    await ctx.send(content)



#bot chat test conversation
@bot.listen()
async def on_message(message):
   if message.author == bot.user:
      return
   
   if message.content.startswith('Lisa'):
       await message.channel.send('Bả đi ngủ rồi')
       await message.add_reaction("\U0001f642")

#bot run
bot.run(TOKEN)