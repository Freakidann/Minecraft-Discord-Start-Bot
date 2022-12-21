import discord
import subprocess
 
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('start'):
        subprocess.run(["DelaServeurStart.bat"])
        await message.channel.send('Serveur Start Wait...')
 
client.run('YOURBOTTOKEN')