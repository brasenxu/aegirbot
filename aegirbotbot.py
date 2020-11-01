import os
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
@client.command(
    brief="Will tell you the client latency with a nice PONG!",
    help="Aegirbot really wants you to stop pinging him with you pings and pongs."
)
async def ping(ctx):
    await ctx.send(f'Fuck off! {round(client.latency * 1000)}ms')


#Pic of Aegir command
@client.command(
    help="Gives you beautiful pictures of the hotties on this server.",
    brief="Sends back a pretty picture."
)
async def pic(ctx, arg=None):
    samPic = []

    hojinPic = ['https://imgur.com/QY3Mxr1']

    minwooPic = ['https://imgur.com/45UwZND',
                 'https://imgur.com/a2COmdL',
                 'https://imgur.com/dpYpgdL',
                 'https://imgur.com/UvjA5nZ',
                 'https://imgur.com/IOZHJL2',
                 'https://imgur.com/13Ktw24',
                 'https://imgur.com/4FVQ9CI',
                 'https://imgur.com/LPeqdM2',
                 'https://imgur.com/x4o7U3F',
                 'https://imgur.com/c3YnKLY',
                 'https://imgur.com/omqSthS',
                 'https://imgur.com/iGfpxNI',
                 'https://imgur.com/fjABLoD',
                 'https://imgur.com/a265CZM',
                 'https://imgur.com/f29x0XH',
                 'https://imgur.com/aMbMgN5',
                 'https://imgur.com/zRz7FpE',
                 'https://imgur.com/dvJnJGl',
                 'https://imgur.com/AgyF8n3',
                 'https://imgur.com/eWd7pOH',
                 'https://imgur.com/hhVNvgr',
                 'https://imgur.com/jCO475U']

    jeffersonPic = []

    aegirPic = ['https://imgur.com/F2UhyI4',
                'https://imgur.com/51YfC6m',
                'https://imgur.com/Y3cWAFA',
                'https://imgur.com/b9ab84N',
                'https://imgur.com/m9yolDG',
                'https://imgur.com/s0nv6IX',
                'https://imgur.com/yD18plG',
                'https://imgur.com/tXn7zcy',
                'https://imgur.com/wVuJ48N',
                'https://imgur.com/weompm7',
                'https://imgur.com/syvTjFn',
                'https://imgur.com/mJT8N67',
                'https://imgur.com/JDwI3nm',
                'https://imgur.com/IuTbaFo',
                'https://imgur.com/XI3UYQv',
                'https://imgur.com/td9PrSW',
                'https://imgur.com/iCw7FEf',
                'https://imgur.com/zplmtyR',
                'https://imgur.com/V1qhyu3',
                'https://imgur.com/F47qXHj',
                'https://imgur.com/5GwZILV',
                'https://imgur.com/V0toia5',
                'https://imgur.com/zGsFyeL',
                'https://imgur.com/fMeaI8k',
                'https://imgur.com/UMCyooO',
                'https://imgur.com/Lmka6IP',
                'https://imgur.com/jxboPQq',
                'https://imgur.com/RDCEtV1',
                'https://imgur.com/QEljUxX']

    if not arg or arg == "aegir":
        await ctx.send(f'{random.choice(aegirPic)}'.format(ctx))
    else:
        if arg == "minwoo":
            await ctx.send(f'{random.choice(minwooPic)}'.format(ctx))
        elif (arg == "hojin") or (arg == "david"):
            await ctx.send(f'{random.choice(hojinPic)}'.format(ctx))

#Aegir StopStopStop Comment
@client.command(
    help="It's time to stop.",
    brief="ITS OVER ITS ACTUALLY OVER"
)
async def aegir(ctx):
    await ctx.send(f'Stop stop stop. Its actually over.')


#Hao Command
@client.command(
    help="Hao Cui Hao Cui",
    brief="It's Hao"
)
async def hao(ctx):
    await ctx.send(f'I will take \"Ur mom to the old town road\"')


#Aegir Shut up Comment
@client.command(
    help="Shut the fuck up.",
    brief="For when Aegir wants you to shut up."
)
async def shutup(ctx):
    await ctx.send(f'Shut up. Please shut up.')
    await ctx.send(f'https://imgur.com/JgfEmNu')


#say command
@client.command(
    help="Say something, Aegirbot will say too.",
    brief="Put words in Aegirbot's mouth"
)
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send(msg)


#weirdchamp
@client.command(
    help="Hao has to be banned from the #nsfw channel tbh",
    brief="This is for when Hao gets overly weird."
)
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
client.run('NzUyMTkxNTk2MjE2MzIwMTAw.X1UDAw.5uyb9r4uaq_JyEhYmyQnHPbgSyM')
#client.run(os.getenv('BOT_TOKEN'))
