import os
import uuid
import discord
from discord.ext import commands
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from TTS.api import TTS
import uvicorn
import asyncio

# Initialize TTS model
tts_model_path = "./trained_model/best_model.pth"
tts = TTS(tts_model_path)

# Initialize FastAPI app
app = FastAPI()

# Define input model for FastAPI
class TextToConvert(BaseModel):
    text: str

