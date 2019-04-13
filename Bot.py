import discord
from discord.ext import commands
import asyncio
import time

bot=commands.Bot(command_prefix='!')
dabs='440281410197258280'
start=time.time()

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------')
    await bot.change_presence(game=discord.Game(name='!help for command!',type=0))
    
@bot.command(pass_context=True)
async def ping():
    await bot.say(':ping_pong:')
    await bot.say('You pinged me haha')
    
@bot.command(pass_context=True)
async def mute(ctx,target:discord.Member):
    if ctx.message.author.id==(dabs):
      role=discord.utils.get(ctx.message.server.roles,name='Muted')

      await bot.add_roles(target,role)
    else:
        await bot.say('No permission!')

@bot.command(pass_context=True)
async def warn(ctx,target:discord.Member):
    if ctx.message.author.id==(dabs):
      await bot.send_message(target,'Warning!!')
    else:
        await bot.say('No permission!')
        
@bot.command(pass_context=True)
async def kick(ctx,target:discord.Member):
    if ctx.message.author.id==(dabs):
      await bot.kick(target)
    else:
        await bot.say('No permission!')

@bot.command(pass_context=True)
async def ban(ctx,target:discord.Member):
    if ctx.message.author.id==(dabs):
      await bot.ban(target)
    else:
        await bot.say('No permission!')
    
@bot.command(pass_context=True)
async def uptime(ctx):
    now=time.time()
    sec=int(now-start)
    mins=int(sec//60)
    await bot.say(f'Uptime is {sec} seconds!')
    
@bot.command(pass_context=True)
async def clear(ctx,num:int):
    if ctx.message.author.id==(dabs):
        await bot.purge_from(ctx.message.channel,limit=num)
        await bot.say(f'Cleared {num} messages.')
    else:
          await bot.say('No permission!')
          
@bot.command(pass_context=True)
async def presence(ctx,text:str,type:int):
    if ctx.message.author.id==(dabs):
        await bot.change_presence(game=discord.Game(name=text,type=type))
    else:
          await bot.say('No permission!')

bot.run('your token here')
