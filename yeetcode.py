import discord
import os
import asyncio
import aiohttp
from discord import Embed
from discord.ext import commands
from discord.ext.commands import Bot

from keep_alive import keep_alive

bot = commands.Bot(command_prefix="$")


bot = discord.Client()



@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    



@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    


    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('Go outside')
    
    if msg.startswith('$go'):
        await message.channel.send('cringe noises')




keep_alive()
bot.run(os.getenv('TOKEN'))