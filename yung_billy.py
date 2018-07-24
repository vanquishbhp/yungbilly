import discord
import asyncio #we need this for fucking everything
from discord.ext.commands import Bot
from discord.ext import commands #importin shit
from sys import exit

session = discord.Client() #establishes client 
client = commands.Bot(command_prefix = "^") #establishes bot

@client.event
async def on_ready(): #when the bot has been initialised it sends a message
    print("Y U N G    B I L L Y   H A S   A W A K E N E D .")
    
@client.event    
async def on_message(msg): #this sub is handling reading all of YB's commands for now
    if msg.content.upper().startswith("^GREET"): #if we type this command (the upper() makes it case insensitive)
        userID = msg.author.id #it gets our user id
        await client.send_message(msg.channel, "hello, <@%s>, you tool." % (userID)) #and then @s us in the same channel, then calls us a tool
    elif msg.content.upper().startswith("^HELP"):
        user = msg.author #gets who asked for help
        helppage = open("help.txt", "r").read() #gets the contents of the help page
        await client.send_message(user, helppage) #dm's it to the asker
        await client.send_message(msg.channel, "i sent you a list of commands, go check it out my guy") #responds, i guess
    elif msg.content.upper().startswith("^SLEEP") and msg.author.id == "[insert discord id here]": #only i (or the operator) am allowed to use this one, kek
        await client.send_message(msg.channel, "ok im sleep [SHUTTING DOWN]")
        exit("Yung Billy has passed the fuck out.") #shuts Yung Billy down; takes fucking ages, which is a problem i need to fix

@client.event
async def on_member_join(member): #this sub gives a notification when someone joins a server
    userID = member.id #well duh
    await client.send_message(discord.Object(id="[channel id goes here]"), "@everyone we got a new boi here by the name of <@%s>. admins, give em any roles you might need to" % (userID)) 



client.run("[Token goes here]") #the event loop; it's pretty much 'main'
