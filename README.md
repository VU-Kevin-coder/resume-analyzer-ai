# 📄 Resume Analyzer AI
An AI-powered resume analyzer built with React (frontend) and FastAPI (backend). It extracts text from resumes, compares it with job descriptions, evaluates strengths, highlights missing keywords, and provides AI-based improvement suggestions using Gemini Pro or OpenAI.

## 🚀 Features
Upload resumes in .pdf, .doc, or .docx format
Compare with job descriptions to calculate Fit Score
Extract:
Strengths
Weaknesses
Missing keywords
Metrics found (impact words, quantifiers, etc.)
AI-generated improvement suggestions (via Gemini)
Responsive React frontend
RESTful FastAPI backend
CORS-enabled API

## 🖼️ Demo
⚙️ 
<img width="871" height="603" alt="image" src="https://github.com/user-attachments/assets/391cf96a-7a25-4467-acb2-55533650ef2a" />

<img width="1126" height="648" alt="image" src="https://github.com/user-attachments/assets/e6c021fc-6d83-4b72-9e95-29ee1c2e9a11" />

<img width="907" height="566" alt="image" src="https://github.com/user-attachments/assets/4cbaea4c-f677-4472-9496-1b39f04002ae" />

## 🛠️ Tech Stack
Frontend	Backend	NLP & AI
React (CRA)	FastAPI	spaCy (NLP)
JavaScript	Python 3.10+	Google GenerativeAI or OpenAI
CSS (custom)	Uvicorn (ASGI)	TfidfVectorizer (sklearn)

## 📦 Installation
1. Clone the repository
```
git clone https://github.com/VU-Kevin-coder/resume-analyzer-ai.git
```
cd resume-analyzer-ai
2. ⚙️ Backend Setup (FastAPI)
```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate   # Windows
   .venv/bin/activate   # macOS/Linux
   pip install -r requirements.txt
```
## 🔐 Create a .env file (in /backend)
```
GOOGLE_API_KEY=your_gemini_api_key_here
```
## Run FastAPI backend:
```
uvicorn app:app --reload
```
- Server runs at: http://localhost:8000

- API docs: http://localhost:8000/docs

## 💻 Frontend Setup (React)
```
cd frontend
npm install
npm start
```
- React dev server: http://localhost:3000

- Communicates with backend at http://localhost:8000

- Ensure CORS is enabled in FastAPI.

## 🧪 Test API with cURL
```
curl -X POST http://localhost:8000/analyze \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'resume=@cv.pdf' \
  -F 'job_description=Data Entry Specialist'
```
## 📂 Project Structure
```
resume-analyzer-ai/
├── backend/
│   ├── app.py
│   ├── analyzer.py
│   ├── parser.py
│   ├── openai_suggester.py
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   │   ├── FileUpload.js
│   │   │   └── Results.js
│   └── public/
└── README.md
```
## 🧠 AI Suggestions Handling
This project supports one provider:

- Gemini Pro: Set GOOGLE_API_KEY in .env

Fallback handled gracefully if API key is missing.

## 🛡️ License
MIT License © 2025 kevin
