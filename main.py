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
        commands={}
        commands['livOwner']='Shows who is the Owners of the server'
        commands['livinvite']='Type &Invite Gives you a link to inv the bot to this server!'
        commands['livecho']='Type livecho and Liv will chat exactly what you chat'
		
        msg=discord.Embed(title='Chat with Livy\'s Clone Helpdesk', description="bux minh",color=0x0000ff)
        for command,description in commands.items():
            msg.add_field(name=command,value=description, inline=False)
        #msg.add_field(name='Join Ur Discord/For Questions/Chilling',value='https://discord.gg/FS8SMn8', inline=False)
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
    await ctx.message.delete()
    await ctx.send(content)



#bot chat test conversation
@bot.listen()
async def on_message(message):
   if message.author == bot.user:
      return
   
   if message.content.startswith('Lisa'):
       await message.channel.send('Bả đi ngủ rồi')
       await message.add_reaction("\U0001f642")


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


#bot run
bot.run(TOKEN)