import discord

async def ReactAddHandler(client, reaction, user):#704076592837820459
    if reaction.message_id == 717400236758138890 and reaction.emoji.name == "surrender": #message id of the welcome message and id for :aye:
        server = client.get_guild(reaction.guild_id)
        member = server.get_member(user.id)
        role = discord.utils.get(server.roles, name = "Shipmates")
        await member.add_roles(role)

async def ReactRemoveHandler(client, reaction, user):
    if reaction.message_id == 717400236758138890 and reaction.emoji.name == "surrender": #message id of the welcome message
        server = client.get_guild(reaction.guild_id)
        member = server.get_member(user.id)
        role = discord.utils.get(server.roles, name = "Shipmates")
        await member.remove_roles(role)