from fastapi import FastAPI, UploadFile, File, HTTPException
import whisper
import os

app = FastAPI()

model = whisper.load_model("base")

def save_file(uploaded_file: UploadFile, path: str) -> str:
    with open(path, "wb") as buffer:
        buffer.write(uploaded_file.file.read())
    return path

def transcribe_audio(file_path: str, language: str = "tr") -> str:

    result = model.transcribe(file_path, language=language,  fp16=False)
    return result["text"]


def generate_srt(transcription: str) -> str:
    # Placeholder for generating SRT. Implement as needed.
    return transcription.replace("\n", "\n1\n")

@app.post("/inferencePath")
async def inference_path(filepath: str):
    
    if not os.path.exists(filepath):
        raise HTTPException(status_code=400, detail="File not found.")
    text = transcribe_audio(filepath)
    srt = generate_srt(text)
    temp_dir = "temp"
    text_file_path = os.path.join(temp_dir, "transcription_"+ filepath + "_.txt") # This is optional path for saving the transcription as a text file,  can be directly name as
    srt_file_path = os.path.join(temp_dir, "transcription_"+ filepath + "_.srt") # os.path.join(temp_dir, "transcription.txt") | os.path.join(temp_dir, "transcription.srt")

    with open(text_file_path, "w",encoding="utf-8") as text_file:
        text_file.write(text)

    with open(srt_file_path, "w", encoding="utf-8") as srt_file:
        srt_file.write(srt)
    
    return {"text": text, "srt": srt}


@app.post("/inferenceRaw")
async def inference_raw(file: UploadFile = File(...)):
    
    temp_dir = "temp"
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    file_path = save_file(file, os.path.join(temp_dir, file.filename))
    text = transcribe_audio(file_path)
    srt = generate_srt(text)
    # os.remove(file_path)  # Clean up the temporary file
    
    # Save text and srt files
    text_file_path = os.path.join(temp_dir, "transcription_"+ file_path + "_.txt") # This is optional path for saving the transcription as a text file,  can be directly name as
    srt_file_path = os.path.join(temp_dir, "transcription_"+ file_path + "_.srt") # os.path.join(temp_dir, "transcription.txt") | os.path.join(temp_dir, "transcription.srt")

    with open(text_file_path, "w",encoding="utf-8") as text_file:
        text_file.write(text)

    with open(srt_file_path, "w", encoding="utf-8") as srt_file:
        srt_file.write(srt)

    return {"text": text, "srt": srt, "text_file_path": text_file_path, "srt_file_path": srt_file_path}

