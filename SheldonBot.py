# SheldonBot.py
import os
import sys

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='sheldon', help='Ask Sheldon to do something')
async def sheldon_main(ctx, cmd):
    match cmd.lower():
        case 'speak':
            await ctx.send('Mrow!')
        case 'sleep':
            await ctx.send('Zzz...')
            sys.exit()
        case _:
            await ctx.send('Sheldon looks at you in confusion')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if 'i love sheldon' in message.content.lower():
        await message.channel.send('Mrow! :heart:')


bot.run(TOKEN)
