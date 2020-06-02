import discord

def ReactHandler(reaction, user):
    print(user.displayname + " added a reaction on " + reaction.message)