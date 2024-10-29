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

@app.post("/generate-voice")
async def generate_voice(data: TextToConvert):
    file_id = str(uuid.uuid4())
    audio_path = f"/tmp/{file_id}.wav"
    
    # Generate the audio file from text
    try:
        tts.tts_to_file(text=data.text, file_path=audio_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating audio: {str(e)}")
    
    return {"audio_path": audio_path}


def start_fastapi():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    start_fastapi()

