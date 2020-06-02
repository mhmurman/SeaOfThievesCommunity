import discord
from include import react
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_react_add(reaction, user):
    react.ReactHandler(reaction, user)

f = open("discord_bot_token.txt")
token = f.read()
client.run(token)
