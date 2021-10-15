# SheldonBot.py
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.command(name='sheldon', help='Ask Sheldon to do something')
async def sheldon_main(ctx):
    await ctx.send('Mrow!')


bot.run(TOKEN)
