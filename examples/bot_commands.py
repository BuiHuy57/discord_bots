# discord_bot.py
import os
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
@bot.command(name='99', help='Responds with a random quote from the Cult of Wide Jay server')
async def nine_nine(ctx):
    quotes = ['So uhhh...', 'BRYAN', 'Sh!t']
    response = random.choice(quotes)
    await ctx.send(response)
    
@bot.command(name='roll_dice', help='Rolls a fair n-sided die')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
            ]
    await ctx.send(', '.join(dice))
    
@bot.command(name='create-channel')
@commands.has_role('Founder')
async def create_channel(ctx, channel_name='placeholder'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
        
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command')

bot.run(TOKEN)