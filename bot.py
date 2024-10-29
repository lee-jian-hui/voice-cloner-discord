import discord
from discord.ext import commands
from configs import *
import logging
import uuid
import os
# from TTS.api import TTS

# tts_model_path = "./trained_model/best_model.pth"
# tts = TTS(tts_model_path)

intents = discord.Intents.default()
intents.message_content = True

# Create a logger
logger = logging.getLogger(__name__)


# Set command prefix
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

@bot.command(name='repeat')
async def repeat(ctx, *, message):
    await ctx.send(message)

@bot.command(name='coleslaw')
async def coleslaw(ctx):
    await ctx.send("hi i am coleslaw, i looksmaxx everyday and is a mechanically gifted valorant competitve player!")

@bot.command(name='foozi')
async def foozi(ctx):
    await ctx.send("hi i am foozi, i live in joceys dungeon and feast on rat droppings!")



# @bot.event
# async def on_ready():
#     print(f"Logged in as {bot.user}")

# @bot.command(name="banglatts")
# async def bangla_tts(ctx, *, text: str):
#     file_id = str(uuid.uuid4())
#     audio_path = f"/tmp/{file_id}.wav"
    
#     try:
#         # Generate audio and send as a file
#         tts.tts_to_file(text=text, file_path=audio_path)
#         await ctx.send("Here's your audio:", file=discord.File(audio_path))
        
#         # Clean up the file after sending
#         os.remove(audio_path)
#     except Exception as e:
#         await ctx.send(f"An error occurred: {e}")



bot.run(DISCORD_TOKEN)


