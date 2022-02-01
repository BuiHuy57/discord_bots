# discord_bot.py

import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
@bot.event
async def on_member_join(member):
    default_role = discord.utils.get(member.guild.roles, name="Plebeian")
    member.add_role(default_role)
    
@bot.command(name='create-text-channel', help='creates new channel')
@commands.has_role('Emperor')
async def create_text_channel(ctx, channel_name='new channel'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)
        
@bot.command(name='assign-role', help='Assign role to a member')
async def assign_role(ctx, * role:discord.Role):
    user = ctx.message.author
    print(user)
    print(role)
    await user.add_roles(role)
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have permissions for this command')
        
bot.run(TOKEN)