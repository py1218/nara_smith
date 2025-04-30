from TTS.api import TTS
import uuid
import os

# Load XTTS model once (global)
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

def generate_voice(text, voice_sample_path="narasmithaudio.wav", output_dir="static/audio"):
    os.makedirs(output_dir, exist_ok=True)
    file_name = f"{uuid.uuid4().hex}.wav"
    file_path = os.path.join(output_dir, file_name)
    tts.tts_to_file(
        text=text,
        speaker_wav=voice_sample_path,
        language="en",
        file_path=file_path
    )
    return f"/static/audio/{file_name}"
