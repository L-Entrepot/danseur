import discord
import os
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} est prêt.')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Ping moi !"))

@client.event
async def on_message(message):
    if client.user in message.mentions and not message.mention_everyone:
        video_folder = "videos/"

        video_files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.mov', '.webm'))]

        if video_files:
            random_video = random.choice(video_files)
            video_path = os.path.join(video_folder, random_video)
            await message.channel.send(file=discord.File(video_path))
        else:
            await message.channel.send("Aucune vidéo trouvée dans le dossier !")

client.run('TOKEN')
