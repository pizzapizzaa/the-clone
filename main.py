import discord, json, asyncio, os, platform, sys
from discord.ext import tasks, commands
from dotenv import load_dotenv

# Loads the .env file that resides on the same level as the script.
load_dotenv()

client = discord.Client()



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
       
        else:
           inp = message.content
           result = model.predict([bag_of_words(inp, words)])[0]
           result_index = np.argmax(result)
           tag = labels[result_index]
           
           if result[result_index] > 0.7:
               for tg in data["intents"]:
                   if tg['tag'] == tag:
                       responses = tg['responses']
                
               bot_response=random.choice(responses)
               await message.channel.send(bot_response.format(message))
           else:
               await message.channel.send("I didnt get that. Can you explain or try again.".format(message))

token = os.getenv("DISCORD_BOT_TOKEN")
client.run(token)

