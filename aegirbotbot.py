import discord
import random
from discord.ext import commands


client = commands.Bot(command_prefix = '.') #Aegirbot command prefix


#Tells you when Aegirbot is ready to rock and roll
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Aegir Life'))
    print('Aegirbot is ready.')


#Ping command to find latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Fuck off! {round(client.latency * 1000)}ms')


#Pic of Aegir command
@client.command()
async def pic(ctx):
    pictures = ['https://imgur.com/F2UhyI4',
                'https://imgur.com/51YfC6m',
                'https://imgur.com/M79Ic6z',
                'https://imgur.com/b9ab84N',
                'https://imgur.com/m9yolDG']

    await ctx.send(f'{random.choice(pictures)}'.format(ctx))


#Aegir StopStopStop Comment
@client.command()
async def aegir(ctx):
    await ctx.send(f'Stop stop stop. Its actually over.')


#Aegir Shut up Comment
@client.command()
async def shutup(ctx):
    await ctx.send(f'Shut up. Please shut up.')
    await ctx.send(f'https://imgur.com/JgfEmNu')


#say command
@client.command()
async def say(self, ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)


#weirdchamp
@client.command()
async def weirdchamp(ctx):
    await ctx.send(f'https://imgur.com/qK1PD1T')


#When you say aegir the bot does :at:
@client.event
async def on_message(message):
    await client.process_commands(message)
    truemessage = message.content.lower() #converts message to all lowercase

    if 'aegir' in truemessage:
        await message.add_reaction(':at:699437200672292935')


'''
@client.event
async def on_message(message):
    aegir1 = 'aegir'  # Word that you want to check in a string
    aegir2 = 'Aegir'
    aegir3 = 'AEGIR'

    if aegir1 in message.content:
        await message.add_reaction(':at:699437200672292935')
    elif aegir2 in message.content:
        await message.add_reaction(':at:699437200672292935')
    elif aegir3 in message.content:
        await message.add_reaction(':at:699437200672292935')
'''

client.run('NzUyMTkxNTk2MjE2MzIwMTAw.X1UDAw.5isGbIFuEo0bsFeOB0mGv4Uxo_s')
