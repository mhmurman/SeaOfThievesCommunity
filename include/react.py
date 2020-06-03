import discord

async def ReactAddShipmates(client, reaction, user):#704076592837820459
    if reaction.message_id == 704076592837820459 and reaction.emoji.name == "aye": #message id of the welcome message
        server = client.get_guild(reaction.guild_id)
        member = server.get_member(user.id)
        role = discord.utils.get(server.roles, name = "Shipmates")
        await member.add_roles(role)

async def ReactRemoveShipmates(client, reaction, user):
    if reaction.message_id == 704076592837820459 and reaction.emoji.name == "aye": #message id of the welcome message
        server = client.get_guild(reaction.guild_id)
        member = server.get_member(user.id)
        role = discord.utils.get(server.roles, name = "Shipmates")
        await member.remove_roles(role)