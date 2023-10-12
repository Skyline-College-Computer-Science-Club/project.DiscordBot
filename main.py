#
# Bare bones bot with an example command, ping, which takes two numbers and responds its sum back as a message
# Not bad, eh? It's what our club's original bot used.
#

import discord
from discord.ext import commands
import logging
from termcolor import colored

#import the smccd_directory_client as smccd web smart client
import smccd_directory as DirectoryClient
import smccd_websmart as WebSmartClient

logging.basicConfig(level=logging.INFO)

#use dir to list the methods available to console
logging.info(colored("Functions available in Directory Client: ====> \n", 'green') + colored(str(dir(DirectoryClient)), 'red'))
logging.info(colored("Functions available in WebSmart Client: ====> \n", 'green') + colored(str(dir(WebSmartClient)), 'red'))


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx, input1: int, input2: int):
    embed = discord.Embed(title="Pong!", description=str(input1 + input2), color=0x00ff00)
    await ctx.send(embed=embed)

bot.run('MTExNDQDU1M[[[[[[[[redacted]]]]]]]]dp1NfzDzB3E4')