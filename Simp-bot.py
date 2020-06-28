import os
import discord
import random
import asyncio
from discord.utils import get
from Token import DISCORD_TOKEN
from discord.ext.commands import Bot
from datetime import datetime
from random import choice
BOT_PREFIX = ","


TOKEN = DISCORD_TOKEN
print(TOKEN)
alarm_time = '11:59'
client = Bot(command_prefix=BOT_PREFIX)


#Tell's user when the bot is connected
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
reactions = ("s_", "i_", "m_", "p_")


#8 ball command. When ",8ball" is called it responds to them with a random response.
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


<<<<<<< HEAD
async def time_check():
    await client.wait_until_ready()
    while not client.is_closed:
        now = datetime.strftime(datetime.now(), '%H:%M')
        channel = client.get_channel(channel_id)
        messages = ('Test')
        guild = discord.utils.find(lambda g: g.name == 'Trap Nation', client.guilds)
        if now == alarm_time:
           user = choice(channel.guild.members)
           await channel.send(f'{test}')
        else:
           time = 1
        await asyncio.sleep(time)


=======
#ping pong, all there really is.
>>>>>>> 7e5b1950ecf4127643868248eef3805e7025655c
@client.command(name='ping',
                pass_context=True)
async def ping(ctx):
    await ctx.send("pong")

#This even occurs every message and reacts to the message with simp emotes.
@client.event
async def on_message(message):
    sender = message.author
    for roles in sender.roles:
        print(f'{roles}')
        currentrole = str(roles)
	#gets the Trap nation guild which allows us to use the simp emotes.
        guild = discord.utils.find(lambda g: g.name == 'Trap Nation', client.guilds)
        if currentrole == 'Simps':
            for emote in reactions:
                emoji = discord.utils.get(guild.emojis, name=emote)
                if emoji:
                   await message.add_reaction(emoji)
    await client.process_commands(message)


client.run(TOKEN)
