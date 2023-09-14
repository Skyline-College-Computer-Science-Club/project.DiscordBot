#
# Bare bones bot with an example command, ping, which takes two numbers and responds its sum back as a message
# Not bad, eh? It's what our club's original bot used.
#

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx, input1: int, input2: int):
    await ctx.send('pong: ' + str(input1 + input2))

bot.run('MTExNDQDU1M[[[[[[[[redacted]]]]]]]]dp1NfzDzB3E4')