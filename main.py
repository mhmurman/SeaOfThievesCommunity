import discord
from include import react
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_raw_reaction_add(reaction):
    user = client.get_user(reaction.user_id)
    await react.ReactAddShipmates(client, reaction, user)
@client.event
async def on_raw_reaction_remove(reaction):
    user = client.get_user(reaction.user_id)
    await react.ReactRemoveShipmates(client, reaction, user)


f = open("discord_bot_token.txt")
token = f.read()
f.close()
client.run(token)