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
        case _:
            await ctx.send('Sheldon looks at you in confusion')


bot.run(TOKEN)
