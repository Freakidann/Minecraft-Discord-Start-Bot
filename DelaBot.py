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
