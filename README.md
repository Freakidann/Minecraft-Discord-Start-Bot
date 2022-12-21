# Minecraft-Discord-Start-Bot
#Minecraft-Discord-Start-Bot
# :warning: *Attention a Ne pas spam ou ajouter un Temps d'utilisation (Create By DelaHost) !* :warning:

<br>

## Dela Start bot :robot: :chart_with_upwards_trend:

[![Discord Bot status](https://top.gg/api/widget/status/816747912888975362.svg)](https://top.gg/bot/816747912888975362)
[![Discord Bots](https://top.gg/api/widget/servers/816747912888975362.svg) ](https://top.gg/bot/816747912888975362)

<br>

Rejoignez le serveur DelaHost si vous avez des Questions :

Discord : https://discord.gg/QN2MakSe3F

![img1](https://cdn.discordapp.com/attachments/1048325449740193813/1055053142456270868/image.png)


## *Commands*
"Start'

<br>

<br>

**Normal commands:**

**'Bientot'**

<br>

## :information_source: *Notes and additional info*
* Permet de lancer des fichiers à partir du bot
* Le bot peut être lancer H24
* Mettre le Py du Bot dans le meme dossier du Fichier à ouvrir !
* Des questions? Rejoin le [Support server](https://discord.gg/QN2MakSe3F) et questions !

<br>

## *Maintainers*
This project is currently maintained by:
* [@Cappig](https://github.com/Freakidann)

<br>
<hr>


``Script Python :

import discord
import subprocess
from discord.ext import commands
import io
import aiohttp

intents = discord.Intents.all()
client = discord.Client(command_prefix='/', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
@commands.has_role("everyone")
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('/start'):
        embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        file = discord.File("DelaServStart.png", filename="image.png")
        embed.set_image(url="https://cdn.discordapp.com/attachments/788749055605997609/1055057926131302420/20221221_104308.gif")
        await message.channel.send(file=file)
        await message.channel.send('Start...')
        await message.channel.send('Ouverture dans moin de 5 minutes')
        await message.channel.send('Start bungeeCord...')
        await message.channel.send('Ouverture Serveur Principal')
        subprocess.run(["YOURFILE.bat"])
        
        ##Change subprocess by YourFile.exe,YourFile.bat,YourFile.jar...
        
client.run('YOURTOKENBOT')

## ChangeToken
