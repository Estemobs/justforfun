import discord
import asyncio

from discord.ext import commands

bot = commands.Bot(command_prefix='r')


@bot.listen()
async def on_ready():
    print('Sa va péter !')




async def msg(ctx,userid:str,*,msg):
       user = ctx.message.guild.get_member(userid) or user = bot.get_member(userid)
       await ctx.send(user,msg)


       
       
bot.run('token')       
