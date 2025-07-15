from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
import os
from parser import extract_text_from_file
from analyzer import analyze_resume
from openai_suggester import get_ai_suggestions
import shutil
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = 'uploads/'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(default="")
):
    if resume.filename == "":
        raise HTTPException(status_code=400, detail="Empty filename")

    filename = os.path.basename(resume.filename)  # safe filename handling
    filepath = os.path.join(UPLOAD_FOLDER, filename)

    try:
        # Save the uploaded file to disk
        with open(filepath, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        # Extract text and analyze
        resume_text = extract_text_from_file(filepath)
        analysis = analyze_resume(resume_text, job_description)
        analysis['ai_suggestions'] = get_ai_suggestions(analysis)
        return analysis

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

    finally:
        # Optionally delete the uploaded file after processing
        if os.path.exists(filepath):
            os.remove(filepath)

