import discord
from discord.ext import commands
import asyncio
import threading

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(activity=discord.Game(name='Hi Bot'))

def send_messages():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    @bot.event
    async def on_connect():
        await bot.wait_until_ready()  # Wait until the bot is ready before sending messages
        guild = bot.get_guild(1115082241064828978)  # Replace with your guild ID
        channels = [channel for channel in guild.text_channels]

        while True:
            for channel in channels:
                await channel.send('@everyone')

    try:
        bot.start('MTA4NjEwNDI2ODc0MzkwMTI0NQ.Gn3Qtf.wHpmeRUUwIuZdqoolajKOP65SEa5oan2_Nbxi0')
    finally:
        loop.run_until_complete(bot.close())  # Close the connection and log out the bot
        loop.close()

t = threading.Thread(target=send_messages)
t.start()

while True:
    pass

