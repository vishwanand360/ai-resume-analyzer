from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import AnalyzeRequest
from analyzer import analyze_resume

app = FastAPI(title="AI Resume Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "running"}

@app.post("/analyze")
def analyze(data: AnalyzeRequest):
    match, missing, suggestions = analyze_resume(
        data.resume, data.job_description
    )

    return {
        "match_percentage": match,
        "missing_skills": missing,
        "suggestions": suggestions
    }
