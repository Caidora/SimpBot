import os
import discord
import random
import asyncio
from discord.utils import get
from Token import DISCORD_TOKEN
from discord.ext.commands import Bot
from datetime import datetime

BOT_PREFIX = ","


TOKEN = DISCORD_TOKEN
print(TOKEN)
alarm_time = '11:59'
client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
reactions = ("s_", "i_", "m_", "p_")


@client.command(name='8ball',
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(ctx):
    possible_responses = [
        'Outlook good',
        'Yes',
        'Perhaps',
        'Maybe',
        'No',
        'It could be argued',
        'mayhaps',

    ]
    await ctx.send(random.choice(possible_responses) + ", " + ctx.message.author.mention)


@client.command(name='ping',
                pass_context=True)
async def ping(ctx):
    await ctx.send("pong")


@client.event
async def on_message(message):
    sender = message.author
    for roles in sender.roles:
        print(f'{roles}')
        currentrole = str(roles)
        guild = discord.utils.find(lambda g: g.name == 'Trap Nation', client.guilds)
        if currentrole == 'Simps':
            for emote in reactions:
                emoji = discord.utils.get(guild.emojis, name=emote)
                if emoji:
                   await message.add_reaction(emoji)
    await client.process_commands(message)


client.run(TOKEN)
