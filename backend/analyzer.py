def analyze_resume(resume: str, job_description: str):
    resume_words = set(resume.lower().split())
    job_words = set(job_description.lower().split())

    matched = resume_words.intersection(job_words)
    missing = job_words - resume_words

    match_percentage = int((len(matched) / max(len(job_words), 1)) * 100)

    suggestions = [
        "Add more skills mentioned in the job description",
        "Highlight relevant projects",
        "Use clear technical keywords"
    ]

    return match_percentage, list(missing)[:10], suggestions
