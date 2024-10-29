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
    await ctx.send("hi i am coleslaw, i looksmaxx everyday and goon to kamala harri's gyat!")


# Example commands
# @bot.command(name="banglatts", help="Converts text to Bangladeshi-accented voice.")
# async def bangla_tts(ctx, *, text: str):
#     await ctx.send(f"Converting text '{text}' to Bangladeshi-accented voice...")

@bot.command(name="hello", help="Greets the user.")
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author}!")

@bot.command(name="info", help="Provides information about the bot.")
async def info(ctx):
    await ctx.send("I'm a bot that converts text to Bangladeshi-accented voice!")

# Custom help command to display an embedded list of commands
@bot.command(name="help")
async def custom_help(ctx):
    embed = discord.Embed(
        title="Bot Commands",
        description="Here are the commands you can use with this bot:",
        color=discord.Color.blue()
    )

    # Add each command with its description
    for command in bot.commands:
        embed.add_field(
            name=f"!{command.name}",
            value=command.help,
            inline=False
        )

    embed.set_footer(text="Type !<command> for more details on each command.")
    
    await ctx.send(embed=embed)


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


