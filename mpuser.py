import discord
import asyncio

from discord.ext import commands

bot = commands.Bot(command_prefix='r')


@bot.listen()
async def on_ready():
    print('raid bot prêt')




async def msg(ctx,userid:str,*,msg):
       user = ctx.message.server.get_member(userid) or user = client.get_member(userid)
       await client.send_message(user,msg)
       
       
       
       
bot.run('token')       
