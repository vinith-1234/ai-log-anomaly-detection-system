from fastapi import FastAPI
from pydantic import BaseModel
import requests
import re
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLData(BaseModel):
    url: str

@app.post("/analyze-url")
def analyze_url(data: URLData):
    response = requests.get(data.url, timeout=10)
    logs = response.text.lower()

    error_count = len(re.findall("error", logs))
    warning_count = len(re.findall("warning", logs))
    critical_count = len(re.findall("critical", logs))
    failed_login = len(re.findall("failed", logs))

    risk_score = error_count*2 + warning_count + critical_count*3 + failed_login*2

    if risk_score < 5:
        level = "LOW"
    elif risk_score < 15:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return {
        "url": data.url,
        "errors": error_count,
        "warnings": warning_count,
        "critical": critical_count,
        "failed_logins": failed_login,
        "risk_score": risk_score,
        "risk_level": level,
        "content": logs[:500]
    }