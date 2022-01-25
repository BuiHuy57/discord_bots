# discord_bot.py
import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    quotes = ['So uhhh...', 'BRYAN', 'PIPEY POO']
    
    if message.content == "99!":
        response = random.choice(quotes)
        await message.channel.send(response)
    elif message.content == "raise-exception":
        raise discord.DiscordException
    
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise
    
client.run(TOKEN)