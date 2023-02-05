# Import the discord and discord.ext.commands modules
import discord
from discord.ext import commands

# Create a discord intents object with all intents enabled
intents = discord.Intents.all()

# Create a bot object with a command prefix of "!" and the intents object defined earlier
bot = commands.Bot(command_prefix="!", intents=intents)

# Define an event listener for when the bot is ready
@bot.listen()
async def on_ready():
    # Print a message indicating the bot is ready to use
    print('Its going to fart!')

# Define a command that sends a message to a user specified by ID or mention
@bot.command()
async def msg(userid: str, member: discord.Member = None, *, message: str):
    # If no member was specified, try to get a user by their ID
    if member is None:
        member = bot.get_user(int(userid))
    
    # If a member was found, send them the message in an infinite loop
    if member is not None:
        while True:
            await member.send(message)
    
    # If no member was found, send a message indicating that the user could not be found
    else:
        await ctx.send("Couldn't find the user.")
       
bot.run('token')       
