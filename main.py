import os
import discord
import dotenv
import json
import random
import worklist
from discord.ext import commands, tasks
from discord.ext.commands import help
from dotenv import load_dotenv


prefix = "liv"
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, help_command=None)
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')


#BOT ONLINE
@bot.event
async def on_ready():
    print("Livy's clone is online")



#BOT MESSAGE HISTORY
@bot.event
async def on_message(message):
    print("The message's content was", message.content)
    await bot.process_commands(message)



#BOT HELPDESK
#livehelp
@bot.listen()
async def on_message(message, case_insensitive=True):
    if message.content=='livhelp':
        commands={}
        commands['livping']='Type livping and Liv will let you know the real-time latency of the server.'
        commands['livecho']='Type livecho and Liv will chat exactly what you chat.'
        commands['livpurge']='Type livpurge to delete the recent 50 messages.'
		
        msg=discord.Embed(title='Chat with Livy\'s Clone Helpdesk', description='The ultimate guideline to Livy\'s Clone',color=0x16ADAA)
        for command,description in commands.items():
            msg.add_field(name=command,value=description, inline=False)
        #msg.add_field(name='Join Ur Discord/For Questions/Chilling',value='https://discord.gg/FS8SMn8', inline=False)
        await message.channel.send(embed=msg)

#livwork
@bot.listen()
async def on_message(message,case_insensitive=True):
    if message.content=='livwork':
        commands={}
        commands['livstart']='Type **livstart** to get started!'
        commands['livworkall']='Type **livworkall** will give a complete list of Livy\'s past works'
        #commands['livworkdaily']='Give a set of daily works that needed to be done within the day.'
        #commands['livworkpending']='Give a set of pending works that needed to be done in the future.'
        commands['livworkprofile']='Type **livworkprofile** will give a list Livy\'s work profiles including Linkedin, Instagram, Github, etc.'
        commands['livworkbio']='Type **livworkbio** to read about Livy\'s biography.'
		
        msg=discord.Embed(title='Chat with Livy\'s Clone Helpdesk - Livy\'s Work', description='A set of commands to know more about Livy\'s works',color=0xFFA500)
        for command,description in commands.items():
            msg.add_field(name=command,value=description, inline=False)
        #msg.add_field(name='Join Ur Discord/For Questions/Chilling',value='https://discord.gg/FS8SMn8', inline=False)
        await message.channel.send(embed=msg)


        
#BOT COMMANDS

#Getting Started
@bot.command()
async def start(message, case_insensitive=True, author=discord.user):
    msg = 'Hello {0.author.mention} and thank you for visiting my auto chat box! If you are a first-time visitor, please enter **livwork** so I can give you a quick tour!'
    await message.channel.send(msg)
    await message.add_reaction('wave')

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
    await ctx.message.delete()
    await ctx.send(content)

#bot purge messages
@bot.command()
async def purge(ctx, limit=50, member: discord.Member=None):
    await ctx.message.delete()
    msg = []
    try:
        limit = int(limit)
    except:
        return await ctx.send("Please pass in an integer as limit")
    if not member:
        await ctx.channel.purge(limit=limit)
        return await ctx.send(f"Purged {limit} messages", delete_after=3)
    async for m in ctx.channel.history():
        if len(msg) == limit:
            break
        if m.author == member:
            msg.append(m)
    await ctx.channel.delete_messages(msg)
    await ctx.send(f"Purged {limit} messages of {member.mention}", delete_after=3)

#All about works command
@bot.command()
async def workall(ctx):
    await ctx.send("Here is a list of my recent works\n ")
    await ctx.send(worklist.worklistall)

@bot.command()
async def workprofile(ctx):
    await ctx.send("Here is a list of my works\'s profiles \n")
    await ctx.send(worklist.workprofile)

@bot.command()
async def workbio(ctx):
    await ctx.send(worklist.workbio)

#JSON DATA LOAD AND SEND SAMPLE
#@bot.command()
#async def workall(ctx):
#    with open('worklist.json') as worklist:
#    		data = json.load(worklist)
#    await ctx.send(data)


#BOT CHAT CONVERSATION
#bot chat test conversation
@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return

    



#bot run
bot.run(TOKEN)