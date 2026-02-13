import os
import requests
import json
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()

# Serve the frontend HTML file
app.mount("/static", StaticFiles(directory="static"), name="static")

# THE NUCLEAR OPTION - DIRECT HARDCODED KEY
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
genai.configure(api_key=GEMINI_API_KEY)

class AnalyzeRequest(BaseModel):
    username: str

@app.get("/")
async def serve_frontend():
    return FileResponse("static/index.html")

@app.post("/api/analyze")
async def analyze_github_profile(request: AnalyzeRequest):
    username = request.username
    
    # 1. Fetch User Profile
    user_res = requests.get(f"https://api.github.com/users/{username}")
    if user_res.status_code == 404:
        raise HTTPException(status_code=404, detail="GitHub user not found")
    elif user_res.status_code == 403:
        raise HTTPException(status_code=403, detail="GitHub API Rate Limit Exceeded. Try again in an hour.")
        
    user_data = user_res.json()
    
    # 2. Fetch Repositories
    repos_res = requests.get(f"https://api.github.com/users/{username}/repos?sort=updated&per_page=10")
    repos_data = repos_res.json() if repos_res.status_code == 200 else []
    
    simplified_repos = [
        {
            "name": repo.get("name"),
            "description": repo.get("description"),
            "language": repo.get("language"),
            "stars": repo.get("stargazers_count")
        }
        for repo in repos_data
    ]

    # 3. The Recruiter AI Prompt
    prompt = f"""
    You are an expert technical recruiter and Senior Engineering Manager evaluating a GitHub profile for an early-career software engineering role.
    
    Candidate Username: {user_data.get('login')}
    Bio: {user_data.get('bio')}
    Total Public Repos: {user_data.get('public_repos')}
    
    Top Recent Repositories (Analyzed Data): 
    {simplified_repos}
    
    Evaluate this profile based on real-world hiring signals:
    1. Project Clarity & Storytelling (Are descriptions clear? Do they solve real problems?)
    2. Engineering Maturity (Are they just doing tutorials, or building complex, structured applications?)
    3. Documentation (Do these repositories have READMEs? If we can't see the README, assume it needs improvement).
    
    Return EXACTLY this JSON structure. Do not include markdown formatting or backticks. Make sure the score is an integer.
    {{
        "score": 85,
        "strengths": ["Specific green flag from their repos", "Another specific green flag"],
        "red_flags": ["Specific gap, e.g., Missing descriptions on 3 pinned repos", "Another gap"],
        "actionable_steps": ["High-value task, e.g., Add an architecture diagram to [Repo Name]", "Another task"]
    }}
    """

    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        clean_text = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(clean_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Error: {str(e)}")