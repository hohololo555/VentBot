import discord
import time
import asyncio

TOKEN = (#put bot token here)
CHANNEL = (#put channel id to delete from here)

client = discord.Client()
#put bot code in between this and token

@client.event
async def on_ready():
    print("on and ready")

@client.event
async def on_message(message):
    channel = message.channel
    if channel == client.get_channel(CHANNEL):
        print("started")
        await asyncio.sleep(300) #change sleep time to change how long till message is deleted, default is 5 minutes
        await message.delete()

client.run(TOKEN)
