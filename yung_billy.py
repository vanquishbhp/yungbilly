import discord
import asyncio #we need this for fucking everything
import youtube_dl
from discord.ext.commands import Bot
from discord.ext import commands #importin shit
from sys import exit

session = discord.Client() #establishes client
client = commands.Bot(command_prefix = "^") #sets the client up as a bot


@client.event
async def on_ready(): #when the bot has been initialised it sends a message
    print("Y U N G    B I L L Y   H A S   A W A K E N E D .")
    await client.change_presence(game = discord.Game(name = "type ^help")) #changes the bot's status
    
@client.event    
async def on_message(mess): #this sub is handling reading all of YB's commands for now
    msg = mess.content.split(" ") #splits message into elements in a list, splitting at every space
    cmd = msg[0].upper() #this is the uppercase of the first word in the list, i.e the command prefix. uppercase makes it case insensitive
    if cmd == "^GREET": #if we type this command
        userID = mess.author.id #it gets our user id
        await client.send_message(mess.channel, "hello, <@%s>, you tool." % (userID)) #and then @s us in the same channel, then calls us a tool
    elif cmd == "^HELP":
        user = mess.author #gets whomst asked for help
        helppage = open("help.txt", "r").read() #gets the contents of the help page
        await client.send_message(user, helppage) #dm's it to the asker
        await client.send_message(mess.channel, "i sent you a list of commands, go check it out my guy") #responds i guess
    elif cmd == "^SLEEP" and mess.author.id == "[my ID]": #only i am allowed to use this one, kek
        await client.send_message(mess.channel, "ok im sleep [SHUTTING DOWN]")
        exit("Yung Billy has passed the fuck out.") #shuts Yung Billy down; takes fucking ages, which is a problem i need to fix
    elif mess.content.upper() == "MODS ARE GAY":
        await client.send_message(mess.channel, "***It is known.*** \n http://i.imgur.com/rTpatUc.gifv") #/r/dankmemes i see you
    elif cmd == "^PLAY":
        await playMusicFromYoutube(mess.author,msg[1],False,mess) #plays music
    elif cmd == "^STOP":
        await playMusicFromYoutube(mess.author,msg[0],True,mess) #stops YB playin music
        


@client.event
async def on_member_join(member): #this sub gives a notification when someone joins a server
    userID = member.id #well duh
    await client.send_message(discord.Object(id="[the channel's id]"), "@everyone we got a new boi here by the name of <@%s>. admins, give em any roles you might need to" % (userID))

#the following sub is getting mega fucking reworked to allow for queues and shit in the future; will likely make it barebones af and make other functions do the queueing shit
async def playMusicFromYoutube(user, url, kill, mg): #this is triggered by '^play [youtube url]'
     url = str(url)
     if kill == True:
         client.send_message(mg.channel, "ok i stop pley music now") #bot is needlessly cute
         client.disconnect() #disconnects from voice channel
         return #kills function
     else:
         pass #this is stupid but saves me time
     chan = user.voice.voice_channel #gets command invoker's voice channel 
     if url.startswith('https://www.youtube.com/watch?v='): #makes sure its playing from a youtube url
         try:
             vois = await client.join_voice_channel(chan) #slides into voice channel
             await client.send_message(mg.channel, "M U S I C   T I M E   B O Y Z !") #warns everyone that we're about to drop a fat fucken mixtape
             player = await vois.create_ytdl_player(url) #readies the chosen mixtape
             player.start() #drops mixtape. there are no survivors
         except:
             await client.send_message(mg.channel, 'music machine :b:roke, try again later') #tells everyone that i fucked up
     else:
         await client.send_message(mg.channel, 'that is not a url. try again fuckass') #tells you off if you dont post a url
         return
client.run("[token]") #the event loop; gets everything done

