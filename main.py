# main.py (FastAPI backend)
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from TTS.api import TTS
import uuid
import os

app = FastAPI()

# Load TTS model once on startup
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

class RecipeRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_recipe(data: RecipeRequest):
    # For now, just echo back the text (replace this with your real LLM logic)
    recipe_text = f"Here's a glamorous Nara Smith recipe for: {data.prompt}"
    return {"recipe": recipe_text}

@app.post("/speak")
async def speak(text: str = Form(...)):
    out_path = f"/tmp/{uuid.uuid4().hex}.wav"
    tts.tts_to_file(
        text=text,
        speaker_wav="/app/narasmithaudio.wav",  # upload your voice sample here
        language="en",
        file_path=out_path
    )
    return FileResponse(out_path, media_type="audio/wav")
