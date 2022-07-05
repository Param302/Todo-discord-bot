# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import os
import discord
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('&'):
        """
        Commands:-
        & addme - For adding a user
        & addtask - For adding single task
        & show - For showing today's task
        & showcompleted - For looking which tasks are completed
        & change - For changing a specific task
        """

        data = (message.content).split(" ")
        await message.channel.send(f'Command = {data[1]}')


try:
    client.run(os.getenv("TOKEN"))
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
        print("Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests")
    else:
        raise e